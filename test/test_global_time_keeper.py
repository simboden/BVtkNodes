import bpy
import argparse
import sys
import os
import numpy as np
sys.path.append(os.path.dirname(__file__))
from test_blender_script import check_node_statuses, assert_quit

def check_cone_validity(cone_node, cone_mesh):
    vertices = np.zeros(shape=[len(cone_mesh.data.vertices), 3])
    cone_mesh.data.vertices.foreach_get('co', vertices.reshape([-1]))
    center = np.array(cone_node.m_Center)
    direction = np.array(cone_node.m_Direction)
    height = cone_node.m_Height
    radius = cone_node.m_Radius
    circle_center = center - direction / 2
    assert_quit(np.isclose(np.linalg.norm(circle_center - vertices[0]), height, atol=1e-4), 
                        "The cone had not the expected height of %f" % (height))
    assert_quit(np.allclose(np.linalg.norm(vertices[1:] - circle_center[np.newaxis], axis=-1), radius, atol=1e-4), 
                        "The cone had not the expected radius of %f" % (radius))



def test_frame_updates():

    node_tree = bpy.data.node_groups["NodeTree"]
    cone_node = node_tree.nodes["vtkConeSource"]
    cone_mesh = bpy.data.objects['mesh']
    keyframes = np.concatenate([np.linspace(.5, .5, num=4), np.linspace(.5, 2.5, num=6)])

    for frame in range(1, 11):
        print("Testing frame %d" % frame)
        keyframe = keyframes[frame-1]
        bpy.context.scene.frame_current = frame
        bpy.context.view_layer.update()
        check_cone_validity(cone_node, cone_mesh)
        assert_quit(np.isclose(cone_node.m_Radius, keyframe), 
                    "The radius of the cone node was not successfully update after changing to frame %d (expected value %f, actual value %f)" 
                        % (frame, keyframe, cone_node.m_Radius))
    

if __name__ == "__main__":
    try:
        check_node_statuses()
        test_frame_updates()
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(1)

    #Success - Quit
    sys.exit(0)
