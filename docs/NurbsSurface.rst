NurbsSurface
============

.. py:module:: compute_rhino3d.NurbsSurface

.. py:function:: CreateCurveOnSurfacePoints(surface, fixedPoints, tolerance, periodic, initCount, levels, multiple=False)

   Computes a discrete spline curve on the surface. In other words, computes a sequence
   of points on the surface, each with a corresponding parameter value.

   :param rhino3dm.Surface surface: The surface on which the curve is constructed. The surface should be G1 continuous. \
      If the surface is closed in the u or v direction and is G1 at the seam, the \
      function will construct point sequences that cross over the seam.
   :param list[rhino3dm.Point2d] fixedPoints: Surface points to interpolate given by parameters. These must be distinct.
   :param float tolerance: Relative tolerance used by the solver. When in doubt, use a tolerance of 0.0.
   :param bool periodic: When True constructs a smoothly closed curve.
   :param int initCount: Maximum number of points to insert beteween fixed points on the first level.
   :param int levels: The number of levels (between 1 and 3) to be used in multi-level solver. Use 1 for single level solve.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A sequence of surface points, given by surface parameters, if successful. \
      The number of output points is approximatelely: 2 ^ (level-1) * initCount * fixedPoints.Count.
   :rtype: rhino3dm.Point2d[]
.. py:function:: CreateCurveOnSurface(surface, points, tolerance, periodic, multiple=False)

   Fit a sequence of 2d points on a surface to make a curve on the surface.

   :param rhino3dm.Surface surface: Surface on which to construct curve.
   :param list[rhino3dm.Point2d] points: Parameter space coodinates of the points to interpolate.
   :param float tolerance: Curve should be within tolerance of surface and points.
   :param bool periodic: When True make a periodic curve.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A curve interpolating the points if successful, None on error.
   :rtype: rhino3dm.NurbsCurve
.. py:function:: MakeCompatible(surface0, surface1, multiple=False)

   For expert use only. Makes a pair of compatible NURBS surfaces based on two input surfaces.

   :param rhino3dm.Surface surface0: The first surface.
   :param rhino3dm.Surface surface1: The second surface.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: True if successsful, False on failure.
   :rtype: bool
.. py:function:: CreateFromPoints(points, uCount, vCount, uDegree, vDegree, multiple=False)

   Constructs a NURBS surface from a 2D grid of control points.

   :param list[rhino3dm.Point3d] points: Control point locations.
   :param int uCount: Number of points in U direction.
   :param int vCount: Number of points in V direction.
   :param int uDegree: Degree of surface in U direction.
   :param int vDegree: Degree of surface in V direction.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A NurbsSurface on success or None on failure.
   :rtype: NurbsSurface
.. py:function:: CreateThroughPoints(points, uCount, vCount, uDegree, vDegree, uClosed, vClosed, multiple=False)

   Constructs a NURBS surface from a 2D grid of points.

   :param list[rhino3dm.Point3d] points: Control point locations.
   :param int uCount: Number of points in U direction.
   :param int vCount: Number of points in V direction.
   :param int uDegree: Degree of surface in U direction.
   :param int vDegree: Degree of surface in V direction.
   :param bool uClosed: True if the surface should be closed in the U direction.
   :param bool vClosed: True if the surface should be closed in the V direction.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A NurbsSurface on success or None on failure.
   :rtype: NurbsSurface
.. py:function:: CreateFromCorners(corner1, corner2, corner3, corner4, multiple=False)

   Makes a surface from 4 corner points.
   This is the same as calling  with tolerance 0.

   :param rhino3dm.Point3d corner1: The first corner.
   :param rhino3dm.Point3d corner2: The second corner.
   :param rhino3dm.Point3d corner3: The third corner.
   :param rhino3dm.Point3d corner4: The fourth corner.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: the resulting surface or None on error.
   :rtype: NurbsSurface
.. py:function:: CreateFromCorners1(corner1, corner2, corner3, corner4, tolerance, multiple=False)

   Makes a surface from 4 corner points.

   :param rhino3dm.Point3d corner1: The first corner.
   :param rhino3dm.Point3d corner2: The second corner.
   :param rhino3dm.Point3d corner3: The third corner.
   :param rhino3dm.Point3d corner4: The fourth corner.
   :param float tolerance: Minimum edge length without collapsing to a singularity.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: The resulting surface or None on error.
   :rtype: NurbsSurface
.. py:function:: CreateFromCorners2(corner1, corner2, corner3, multiple=False)

   Makes a surface from 3 corner points.

   :param rhino3dm.Point3d corner1: The first corner.
   :param rhino3dm.Point3d corner2: The second corner.
   :param rhino3dm.Point3d corner3: The third corner.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: The resulting surface or None on error.
   :rtype: NurbsSurface
.. py:function:: CreateRailRevolvedSurface(profile, rail, axis, scaleHeight, multiple=False)

   Constructs a railed Surface-of-Revolution.

   :param rhino3dm.Curve profile: Profile curve for revolution.
   :param rhino3dm.Curve rail: Rail curve for revolution.
   :param Line axis: Axis of revolution.
   :param bool scaleHeight: If true, surface will be locally scaled.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A NurbsSurface or None on failure.
   :rtype: NurbsSurface
.. py:function:: CreateNetworkSurface(uCurves, uContinuityStart, uContinuityEnd, vCurves, vContinuityStart, vContinuityEnd, edgeTolerance, interiorTolerance, angleTolerance, multiple=False)

   Builds a surface from an ordered network of curves/edges.

   :param list[rhino3dm.Curve] uCurves: An array, a list or any enumerable set of U curves.
   :param int uContinuityStart: continuity at first U segment, 0 = loose, 1 = pos, 2 = tan, 3 = curvature.
   :param int uContinuityEnd: continuity at last U segment, 0 = loose, 1 = pos, 2 = tan, 3 = curvature.
   :param list[rhino3dm.Curve] vCurves: An array, a list or any enumerable set of V curves.
   :param int vContinuityStart: continuity at first V segment, 0 = loose, 1 = pos, 2 = tan, 3 = curvature.
   :param int vContinuityEnd: continuity at last V segment, 0 = loose, 1 = pos, 2 = tan, 3 = curvature.
   :param float edgeTolerance: tolerance to use along network surface edge.
   :param float interiorTolerance: tolerance to use for the interior curves.
   :param float angleTolerance: angle tolerance to use.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A NurbsSurface or None on failure.
   :rtype: NurbsSurface
.. py:function:: CreateNetworkSurface1(curves, continuity, edgeTolerance, interiorTolerance, angleTolerance, multiple=False)

   Builds a surface from an autosorted network of curves/edges.

   :param list[rhino3dm.Curve] curves: An array, a list or any enumerable set of curves/edges, sorted automatically into U and V curves.
   :param int continuity: continuity along edges, 0 = loose, 1 = pos, 2 = tan, 3 = curvature.
   :param float edgeTolerance: tolerance to use along network surface edge.
   :param float interiorTolerance: tolerance to use for the interior curves.
   :param float angleTolerance: angle tolerance to use.
   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :return: A NurbsSurface or None on failure.
   :rtype: NurbsSurface
