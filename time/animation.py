'''
This file is responsible for helping in animating properties until
https://developer.blender.org/T66392
is resolved.
'''
from ..core import *
from ..core import l
from ..errors.bvtk_errors import assert_bvtk
import bpy
import numpy as np

invalid_frame = int(-1e6)
invalid_vtk_time = -4.37e6

class AnimationHelper():

    current_frame = invalid_frame
    vtk_time = invalid_vtk_time
    def setup(self):
        self.current_frame = int(-1e6)
        self.animated_properties = None

    def get_animated_property_list(self):
        '''Fetches the animated properties in a presentable way'''
        self.f_curves = bpy.data.actions["NodeTreeAction"].fcurves

        animated_properties = {}
        for node_group in bpy.data.node_groups.values():
            node_tree_name = node_group.name
            for key, val in bpy.data.actions.items():

                #Skip unrelated node trees
                if node_tree_name + "Action" in key:
                    for f_curve in self.f_curves:
                        prop_path = f_curve.data_path
                        delimiter_index = prop_path.rindex(".")
                        node_name = prop_path[7:delimiter_index-2]
                        attribute_name = prop_path[delimiter_index+1:]
                        arr_ind = f_curve.array_index
                        interpolation_modes = [kf.interpolation for kf in f_curve.keyframe_points]
                        keyframes = [int(kf.co[0]) for kf in f_curve.keyframe_points]
                        keyframe_values = [kf.co[1] for kf in f_curve.keyframe_points]
                        first_interpolation_mode = interpolation_modes[0]
                        single_mode = all(x == first_interpolation_mode for x in interpolation_modes)
                        if not single_mode:
                            l.warning("Global Time Keeper: Mixed interpolation type encountered. This should not happen")

                        interpolation_mode = (first_interpolation_mode if single_mode else "Mixed")

                        #Load current value of the property
                        try:
                            try:
                                current_val = eval(f_curve.data_path + "[{}]".format(arr_ind), 
                                        {"nodes": node_group.nodes})
                            except TypeError as err:
                                if arr_ind == 0: #May be a scalar
                                    current_val = eval(f_curve.data_path, {"nodes": node_group.nodes})
                                else:
                                    l.error("Could not load property " + prop_path 
                                                + ". Error: " + str(err))
                                    continue

                        except Exception as ex:
                            l.error("Could not load property " + prop_path + ". Error: " + str(ex))
                            continue

                        key = prop_path
                        #Array structures
                        if key in animated_properties:
                            old_props = animated_properties[key]
                            old_keyframes, old_keyframe_values, old_current_val = [old_props[i] for i in [2, 3, 4]]

                            if np.any(np.array(old_keyframes) != np.array(keyframes)) or arr_ind !=len(old_keyframe_values):
                                l.warning("Global Time Keeper: Keyframe times of property " 
                                            + str(prop_path) 
                                            + " do not match up for different array indices. Skipping")
                                continue

                            animated_properties[key] = (node_name, attribute_name, keyframes, old_keyframe_values + (keyframe_values,), old_current_val + (current_val,), interpolation_mode)

                        else:
                            animated_properties[key] = (node_name, attribute_name, keyframes, (keyframe_values,), (current_val,), interpolation_mode)

        animated_properties = {k: (v[0], v[1], v[2], [tmp for tmp in zip(*v[3])], v[4], v[5]) for k, v in animated_properties.items()}
        return animated_properties

    def update_animated_properties(self, scene):
        current_frame = scene.frame_current
        AnimationHelper.current_frame = current_frame

        self.animated_properties = []
        self.animated_properties_info = []
        self.interpolation_modes = []

        self.animated_values = {}
        for node_group in bpy.data.node_groups.values():
            node_tree_name = node_group.name
            for key, val in bpy.data.actions.items():

                #Skip unrelated node trees
                if node_tree_name + "Action" in key:
                    self.f_curves = bpy.data.actions["NodeTreeAction"].fcurves
                    updated_nodes = set()

                    for f_curve in self.f_curves:
                        prop_path = f_curve.data_path
                        delimiter_index = prop_path.rindex(".")
                        node_name = prop_path[7:delimiter_index-2]
                        attribute_name = prop_path[delimiter_index+1:]
                        arr_ind = f_curve.array_index
                        try:
                            try:
                                current_val = eval(f_curve.data_path + "[{}]".format(arr_ind), 
                                        {"nodes": node_group.nodes})
                            except TypeError as err:
                                if arr_ind == 0: #May be a scalar
                                    current_val = eval(f_curve.data_path, {"nodes": node_group.nodes})
                                else:
                                    l.error("Could not load property " + prop_path 
                                                + ". Error: " + str(err))
                                    continue

                        except Exception as ex:
                            l.error("Could not load property " + prop_path + ". Error: " + str(ex))
                            continue

                        interpolation_modes = [kf.interpolation for kf in f_curve.keyframe_points]
                        first_mode = interpolation_modes[0]
                        single_mode = all(x == first_mode for x in interpolation_modes)
                        self.interpolation_modes.append(first_mode if single_mode else "Mixed")

                        #TODO: Make other interpolation modes available
                        #All interpolation modes will be set to linear in all cases
                        for mode_i, mode in enumerate(interpolation_modes):
                            if mode != "LINEAR":
                                f_curve.keyframe_points[mode_i].interpolation = "LINEAR"

                        interpolation_modes = ["LINEAR" for _ in interpolation_modes]
                        new_val = f_curve.evaluate(current_frame)

                        if prop_path not in self.animated_properties:
                            self.animated_properties.append(prop_path)
                            old_vals = (self.animated_values[prop_path] if prop_path in self.animated_values else ())
                            self.animated_values[prop_path] = old_vals + (new_val,)

                        #No update necessary if the value hasn't changed
                        if np.isclose(current_val, new_val):
                            continue

                        #Update the property with the new value
                        try:
                            try:
                                exec(f_curve.data_path + "[{}] = {}".format(arr_ind, new_val), 
                                        {"nodes": node_group.nodes})
                            except TypeError as err:
                                if arr_ind == 0: #May be a scalar update
                                    exec(f_curve.data_path + " = {}".format(new_val), 
                                        {"nodes": node_group.nodes})
                                else:
                                    l.error("Could not update property " + prop_path 
                                                + ". Error: " + str(err))

                            updated_node = eval(prop_path[:delimiter_index], {"nodes": node_group.nodes})
                            updated_nodes = updated_nodes.union(set([updated_node]))
                        except Exception as ex:
                            l.error("Could not update property " + prop_path + ". Error: " + str(ex))

                    #This helps in better displaying vectors by concatenating into a list of tuples
                    self.animated_properties = self.get_animated_property_list()
                    return updated_nodes
