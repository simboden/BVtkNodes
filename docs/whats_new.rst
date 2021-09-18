.. _whats_new:

What's New
==========

This information applies to the
`tkeskita/bvtknodes <https://github.com/tkeskita/BVtkNodes>`_ version.

Version 0.7 (2021-09-18)
------------------------

- New node update system, where VTK updates are independent of node
  editing actions. User has now option to change **Update Mode** in
  the Inspect Panel, which determines when changes in nodes are
  updated to VTK objects. Most useful options include *No Automatic
  Updates* and *Update All Automatically*.

- Nodes have now :ref:`node_status` information, which is shown by node colors.

- Values of dynamic enumeration lists are stored in string properties,
  so that it is possible to pre-define whole node trees without need to
  run updates on nodes. This allows full pre-definition of node trees
  e.g. for JSON imports.

- Development for this release was made in 
  `pull request #46 <https://github.com/tkeskita/BVtkNodes/pull/46>`_.


Previous versions
-----------------

- TBA

