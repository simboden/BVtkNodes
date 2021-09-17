import os
import unittest
import subprocess
import numpy as np
try:
    import pyvista as pv
    pv_enabled = True
except ImportError as err:
    pv_enabled = False

class BVTKBaseTest(unittest.TestCase):
    
    def __init__(self, test_name = None):
        super(BVTKBaseTest, self).__init__(test_name)

        self.test_dir = os.path.dirname(__file__) + "/"
        self.blender_files_dir = self.test_dir + "/blend_files/"
        self.base_script = self.test_dir + "test_blender_script.py"
        self.test_output_dir = self.test_dir + "/output/"
        self.blender_path = os.environ["BLENDER_PATH"]
        if not os.path.isdir(self.test_output_dir):
            os.mkdir(self.test_output_dir)

    def emptyOutputDir(self):
        #Empty the output directory
        for root, dirs, files in os.walk(self.test_output_dir):
            for f in files:
                os.unlink(os.path.join(root, f))

    def setUp(self):
        self.emptyOutputDir()

    def tearDown(self):
        self.emptyOutputDir()
        
    def runTestCase(self, blend_file, python_script=None, python_params=None):
        """Standard 

        Parameters
        ----------
        blend_file : str
            name of the blend file inside blend_files
        python_script : str, optional
            The script that will be executed inside blender, by default self.base_script
        """
        if python_script is None:
            python_script = self.base_script
        else:
            python_script = self.test_dir + python_script

        self.assertTrue(os.path.exists(python_script), "The provided python script %s was not found" % (python_script))

        proc = subprocess.Popen([self.blender_path, self.blender_files_dir + blend_file, "--background", 
                            "--python-exit-code", "1", #Exit with failure if the python script fails
                            "--python", python_script,
                            ] + ([] if python_params is None else ["--"] + python_params), 
                            shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # wait for the process to terminate
        proc_output, proc_err = proc.communicate()
        returncode = proc.returncode
        stdout_msg = proc_output.decode('utf-8') #Stdout and Stderr will be displayed if the test fails
        stderr_msg = proc_err.decode('utf-8')
        self.assertTrue(returncode == 0, "Blender STDOUT:%s%s--------------%sSTDERR:%s%s--------------" 
                                                % (os.linesep, stdout_msg, os.linesep, os.linesep, stderr_msg))

    
    def compareWrittenFile(self, produced_file, reference_file, pv_type=None):
        if not pv_enabled:
            self.skipTest("Import of pyvista failed. File comparison will not be performed")

        self.assertFalse(produced_file.endswith("vtk") and pv_type is None, "Unknown vtk type")

        if pv_type is None:
            file_ending_map = {"vtp": pv.PolyData, "vtu": pv.UnstructuredGrid, "vti": pv.UniformGrid}
            self.assertTrue(produced_file[-3:] in file_ending_map, "Unknown vtk type")
            pv_type = file_ending_map[produced_file[-3:]]

        test_dir = os.path.dirname(__file__)
        output_mesh = pv_type(test_dir + "/output/" + produced_file)
        ref_mesh = pv_type(test_dir + "/test_data/" + reference_file)

        self.assertTrue(np.allclose(output_mesh.points, ref_mesh.points, atol=1e-4), "The points of the two meshes differ")

        return output_mesh, ref_mesh #For further processing


class BVTKMainExamples(BVTKBaseTest):
    def test_append(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_append_triangle.json"])

    def test_clip(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_clip.json"])

    def test_cone(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_cone.json"])

    def test_fin(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_fin.json"])

    def test_head(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_head.json"])

    def test_kitchen(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_kitchen.json"])

    def test_global_time_keeper(self):
        self.runTestCase("test_global_time_keeper.blend", "test_global_time_keeper.py")

    def test_glyphs_and_writers(self):
        self.runTestCase("test_template.blend", python_params=["-j", "//../json_files/test_glyphs_and_writers.json"])
        self.compareWrittenFile("test_glyphs_and_writers.vtp", "test_glyphs_and_writers.vtp")

if __name__ == "__main__":
    unittest.main()


