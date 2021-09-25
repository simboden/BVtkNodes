import bpy
import argparse
import sys
import os
import json

# Import the addon to be able to import the node tree
from BVtkNodes.tree import insert_into_node_tree


def assert_quit(condition, message):
    if not condition:
        print("Testscript failed with the message '" + message + "'", file=sys.stderr)
        sys.exit(1)


def parse_standard_test_args():
    """Parses special parameters for the python file after the '--'.
    For more details see the background job template in the blender python scripting UI
    """
    # get the args passed to blender after "--", all of which are ignored by
    # blender so scripts may receive their own arguments
    argv = sys.argv

    if "--" not in argv:
        argv = []  # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1 :]  # get all args after "--"

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-j",
        "--json",
        dest="json",
        type=str,
        required=True,
        help="The json testcase to be executed",
    )

    args = parser.parse_args(argv)
    json_fname = args.json
    json_fname = bpy.path.abspath(
        json_fname
    )  # Replace blender relative paths with absolute paths

    assert_quit(os.path.isfile(json_fname), "File %s not found" % (json_fname))

    return json_fname


def import_json_node_tree(json_fname):
    try:
        # Note: The below modifications to the areas work when the Blender GUI is available, but will NOT work for the headless testing environment.
        #      This is the reason insert_into_node_tree is called directly
        # Search for the Node Editor in the areas
        # node_editor_ind = next(area_i for area_i, area in enumerate(bpy.context.screen.areas) if area.type == "NODE_EDITOR")
        # print("Ind: " + str(node_editor_ind))
        # print(*[area.type for area in bpy.context.screen.areas])
        # area = bpy.context.screen.areas[node_editor_ind]
        # area.type = "NODE_EDITOR"
        # area.ui_type = 'BVTK_NodeTreeType' #Switch to BVTK Node tree view
        # override = bpy.context.copy()
        # override['area'] = area
        # bpy.context.area = area
        # bpy.context.area.type = "NODE_EDITOR" #Change the UI to node editor type
        # bpy.context.area.ui_type = 'BVTK_NodeTreeType' #And switch to BVTK Node tree view
        # bpy.ops.node.new_node_tree() #Create a new node tree (this assumes there is none present in the .blend file)
        # bpy.ops.node.bvtk_node_tree_import(filepath=json_fname, confirm=False)
        with open(json_fname, "r") as json_file:
            json_data = json.load(json_file)

        node_tree_name = "NodeTree"
        assert_quit(node_tree_name in bpy.data.node_groups, "Found no BVTK NodeTree")
        node_tree = bpy.data.node_groups[node_tree_name]
        insert_into_node_tree(node_tree, json_data["nodes"], json_data["links"])

    except Exception as ex:
        assert_quit(False, "Importing the json node tree failed with %s" % (ex))


def import_cli_tree():
    import_json_node_tree(parse_standard_test_args())


def check_node_statuses():
    """Check that status of all nodes is up-to-date"""
    from BVtkNodes.core import get_all_bvtk_nodes

    nodes = get_all_bvtk_nodes()
    for node in nodes:
        if node.vtk_status != "up-to-date":
            assert_quit(False, "Test failed with %s" % node.name)


if __name__ == "__main__":
    try:
        import_cli_tree()
        check_node_statuses()
        print("Success")
    except Exception as ex:
        assert_quit(False, "Test failed with %s" % (ex))
    # Success - Quit
    # sys.exit(0)
