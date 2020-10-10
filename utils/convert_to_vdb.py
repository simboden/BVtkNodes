#------------------------------------------------------------------------------
# convert_to_vdb.py - Create OpenVDB (.vdb) volume data file from
# image data in argument JSON file. JSON file is generated using
# "VTK To OpenVDB Exporter" node in BVTKNodes (Blender add-on).
#
# Run example: python3 convert_to_vdb.py volume_00001.json
#
# Requirement: pyopenvdb module must be available to Python
#
# If you get error like:
#     "libjemalloc.so.2: cannot allocate memory in static TLS block"
# then prepend command with LD_PRELOAD:
#     LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2 python3 convert_to_vdb.py volume_00001.json
#------------------------------------------------------------------------------

import sys
import json

try:
    import pyopenvdb
    vdb = pyopenvdb
except ImportError:
    print("ERROR: Python can't import pyopenvdb. Please see "
    + "VTK To OpenVDB Exporter node documentation for more information.")
    raise


def create_grid(background_value, dims, array, grid_name, atype):
    """
    Return an OpenVDB grid with dimensions dims containing data from array.
    """

    if array == None:
        return None

    if atype == 'scalar':
        grid = vdb.FloatGrid(background_value)
    elif atype == 'vector':
        grid = vdb.Vec3SGrid()
    else:
        raise TypeError("Unknown type %s" % str(atype))

    grid.gridClass = vdb.GridClass.FOG_VOLUME
    grid.name = grid_name

    # Create grid by looping over points with accessor
    acc = grid.getAccessor()
    for i in range(dims[0]):
        for j in range(dims[1]):
            for k in range(dims[2]):
                idx = i + j*dims[0] + k*dims[0]*dims[1]
                value = array[idx]
                if atype == 'scalar':
                    if value == None:
                        continue
                    if value > background_value:
                        acc.setValueOn((i, j, k), value)

                elif atype == 'vector':
                    if value[0] == None:
                        continue
                    acc.setValueOn((i, j, k), value)
    return grid


def count_active_voxels(grids):
    """
    Counts the number of active voxels in list of OpenVDB grids
    """

    n = 0
    for grid in grids:
        n += grid.activeVoxelCount()
    return n


def create_vdb(vdb_filename, background_value, dims, density_data,
               color_data, flame_data, temperature_data):
    """
    Create vdb file from argument data.
    """

    density_grid = create_grid(background_value, dims, density_data, 'density', 'scalar')
    color_grid = create_grid(background_value, dims, color_data, 'color', 'vector')
    flame_grid = create_grid(background_value, dims, flame_data, 'flame', 'scalar')
    temperature_grid = create_grid(background_value, dims, temperature_data, 'temperature', 'scalar')

    grids = [density_grid, color_grid, flame_grid, temperature_grid]
    grids = [g for g in grids if g is not None]
    nvoxels = count_active_voxels(grids)
    vdb.write(vdb_filename, grids=grids)
    print("%s: %d grids, %d active voxels exported." % (vdb_filename, len(grids), nvoxels))


# Main program: Process all arguments

for filename in sys.argv[1:]:
    with open(filename, "r") as read_file:
        background_value, dims, density_data, color_data, flame_data, \
            temperature_data = json.load(read_file)
        vdb_filename = filename.replace('.json', '.vdb')
        create_vdb(vdb_filename, background_value, dims, density_data,
                   color_data, flame_data, temperature_data)
