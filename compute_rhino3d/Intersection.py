from . import Util


def CurvePlane(curve, plane, tolerance, multiple=False):
    """
    Intersects a curve with an (infinite) plane.

    Args:
        curve (Curve): Curve to intersect.
        plane (Plane): Plane to intersect with.
        tolerance (double): Tolerance to use during intersection.

    Returns:
        CurveIntersections: A list of intersection events or None if no intersections were recorded.
    """
    url = "rhino/geometry/intersect/intersection/curveplane-curve_plane_double"
    if multiple: url += "?multiple=true"
    args = [curve, plane, tolerance]
    if multiple: args = zip(curve, plane, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def MeshPlane(mesh, plane, multiple=False):
    """
    Intersects a mesh with an (infinite) plane.

    Args:
        mesh (Mesh): Mesh to intersect.
        plane (Plane): Plane to intersect with.

    Returns:
        Polyline[]: An array of polylines describing the intersection loops or None (Nothing in Visual Basic) if no intersections could be found.
    """
    url = "rhino/geometry/intersect/intersection/meshplane-mesh_plane"
    if multiple: url += "?multiple=true"
    args = [mesh, plane]
    if multiple: args = zip(mesh, plane)
    response = Util.ComputeFetch(url, args)
    return response


def MeshPlane1(mesh, planes, multiple=False):
    """
    Intersects a mesh with a collection of (infinite) planes.

    Args:
        mesh (Mesh): Mesh to intersect.
        planes (IEnumerable<Plane>): Planes to intersect with.

    Returns:
        Polyline[]: An array of polylines describing the intersection loops or None (Nothing in Visual Basic) if no intersections could be found.
    """
    url = "rhino/geometry/intersect/intersection/meshplane-mesh_planearray"
    if multiple: url += "?multiple=true"
    args = [mesh, planes]
    if multiple: args = zip(mesh, planes)
    response = Util.ComputeFetch(url, args)
    return response


def BrepPlane(brep, plane, tolerance, multiple=False):
    """
    Intersects a Brep with an (infinite) plane.

    Args:
        brep (Brep): Brep to intersect.
        plane (Plane): Plane to intersect with.
        tolerance (double): Tolerance to use for intersections.

    Returns:
        bool: True on success, False on failure.
        intersectionCurves (Curve[]): The intersection curves will be returned here.
        intersectionPoints (Point3d[]): The intersection points will be returned here.
    """
    url = "rhino/geometry/intersect/intersection/brepplane-brep_plane_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [brep, plane, tolerance]
    if multiple: args = zip(brep, plane, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveSelf(curve, tolerance, multiple=False):
    """
    Finds the places where a curve intersects itself.

    Args:
        curve (Curve): Curve for self-intersections.
        tolerance (double): Intersection tolerance. If the curve approaches itself to within tolerance,
            an intersection is assumed.

    Returns:
        CurveIntersections: A collection of intersection events.
    """
    url = "rhino/geometry/intersect/intersection/curveself-curve_double"
    if multiple: url += "?multiple=true"
    args = [curve, tolerance]
    if multiple: args = zip(curve, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveCurve(curveA, curveB, tolerance, overlapTolerance, multiple=False):
    """
    Finds the intersections between two curves.

    Args:
        curveA (Curve): First curve for intersection.
        curveB (Curve): Second curve for intersection.
        tolerance (double): Intersection tolerance. If the curves approach each other to within tolerance,
            an intersection is assumed.
        overlapTolerance (double): The tolerance with which the curves are tested.

    Returns:
        CurveIntersections: A collection of intersection events.
    """
    url = "rhino/geometry/intersect/intersection/curvecurve-curve_curve_double_double"
    if multiple: url += "?multiple=true"
    args = [curveA, curveB, tolerance, overlapTolerance]
    if multiple: args = zip(curveA, curveB, tolerance, overlapTolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveLine(curve, line, tolerance, overlapTolerance, multiple=False):
    """
    Intersects a curve and an infinite line.

    Args:
        curve (Curve): Curve for intersection.
        line (Line): Infinite line to intesect.
        tolerance (double): Intersection tolerance. If the curves approach each other to within tolerance,
            an intersection is assumed.
        overlapTolerance (double): The tolerance with which the curves are tested.

    Returns:
        CurveIntersections: A collection of intersection events.
    """
    url = "rhino/geometry/intersect/intersection/curveline-curve_line_double_double"
    if multiple: url += "?multiple=true"
    args = [curve, line, tolerance, overlapTolerance]
    if multiple: args = zip(curve, line, tolerance, overlapTolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveSurface(curve, surface, tolerance, overlapTolerance, multiple=False):
    """
    Intersects a curve and a surface.

    Args:
        curve (Curve): Curve for intersection.
        surface (Surface): Surface for intersection.
        tolerance (double): Intersection tolerance. If the curve approaches the surface to within tolerance,
            an intersection is assumed.
        overlapTolerance (double): The tolerance with which the curves are tested.

    Returns:
        CurveIntersections: A collection of intersection events.
    """
    url = "rhino/geometry/intersect/intersection/curvesurface-curve_surface_double_double"
    if multiple: url += "?multiple=true"
    args = [curve, surface, tolerance, overlapTolerance]
    if multiple: args = zip(curve, surface, tolerance, overlapTolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveSurface1(curve, curveDomain, surface, tolerance, overlapTolerance, multiple=False):
    """
    Intersects a (sub)curve and a surface.

    Args:
        curve (Curve): Curve for intersection.
        curveDomain (Interval): Domain of surbcurve to take into consideration for Intersections.
        surface (Surface): Surface for intersection.
        tolerance (double): Intersection tolerance. If the curve approaches the surface to within tolerance,
            an intersection is assumed.
        overlapTolerance (double): The tolerance with which the curves are tested.

    Returns:
        CurveIntersections: A collection of intersection events.
    """
    url = "rhino/geometry/intersect/intersection/curvesurface-curve_interval_surface_double_double"
    if multiple: url += "?multiple=true"
    args = [curve, curveDomain, surface, tolerance, overlapTolerance]
    if multiple: args = zip(curve, curveDomain, surface, tolerance, overlapTolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveBrep(curve, brep, tolerance, multiple=False):
    """
    Intersects a curve with a Brep. This function returns the 3D points of intersection
    and 3D overlap curves. If an error occurs while processing overlap curves, this function
    will return false, but it will still provide partial results.

    Args:
        curve (Curve): Curve for intersection.
        brep (Brep): Brep for intersection.
        tolerance (double): Fitting and near miss tolerance.

    Returns:
        bool: True on success, False on failure.
        overlapCurves (Curve[]): The overlap curves will be returned here.
        intersectionPoints (Point3d[]): The intersection points will be returned here.
    """
    url = "rhino/geometry/intersect/intersection/curvebrep-curve_brep_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [curve, brep, tolerance]
    if multiple: args = zip(curve, brep, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveBrep1(curve, brep, tolerance, angleTolerance, multiple=False):
    """
    Intersect a curve with a Brep. This function returns the intersection parameters on the curve.

    Args:
        curve (Curve): Curve.
        brep (Brep): Brep.
        tolerance (double): Absolute tolerance for intersections.
        angleTolerance (double): Angle tolerance in radians.

    Returns:
        bool: True on success, False on failure.
        t (double[]): Curve parameters at intersections.
    """
    url = "rhino/geometry/intersect/intersection/curvebrep-curve_brep_double_double_doublearray"
    if multiple: url += "?multiple=true"
    args = [curve, brep, tolerance, angleTolerance]
    if multiple: args = zip(curve, brep, tolerance, angleTolerance)
    response = Util.ComputeFetch(url, args)
    return response


def CurveBrepFace(curve, face, tolerance, multiple=False):
    """
    Intersects a curve with a Brep face.

    Args:
        curve (Curve): A curve.
        face (BrepFace): A brep face.
        tolerance (double): Fitting and near miss tolerance.

    Returns:
        bool: True on success, False on failure.
        overlapCurves (Curve[]): A overlap curves array argument. This out reference is assigned during the call.
        intersectionPoints (Point3d[]): A points array argument. This out reference is assigned during the call.
    """
    url = "rhino/geometry/intersect/intersection/curvebrepface-curve_brepface_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [curve, face, tolerance]
    if multiple: args = zip(curve, face, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def SurfaceSurface(surfaceA, surfaceB, tolerance, multiple=False):
    """
    Intersects two Surfaces.

    Args:
        surfaceA (Surface): First Surface for intersection.
        surfaceB (Surface): Second Surface for intersection.
        tolerance (double): Intersection tolerance.

    Returns:
        bool: True on success, False on failure.
        intersectionCurves (Curve[]): The intersection curves will be returned here.
        intersectionPoints (Point3d[]): The intersection points will be returned here.
    """
    url = "rhino/geometry/intersect/intersection/surfacesurface-surface_surface_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [surfaceA, surfaceB, tolerance]
    if multiple: args = zip(surfaceA, surfaceB, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def BrepBrep(brepA, brepB, tolerance, multiple=False):
    """
    Intersects two Breps.

    Args:
        brepA (Brep): First Brep for intersection.
        brepB (Brep): Second Brep for intersection.
        tolerance (double): Intersection tolerance.

    Returns:
        bool: True on success; False on failure.
        intersectionCurves (Curve[]): The intersection curves will be returned here.
        intersectionPoints (Point3d[]): The intersection points will be returned here.
    """
    url = "rhino/geometry/intersect/intersection/brepbrep-brep_brep_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [brepA, brepB, tolerance]
    if multiple: args = zip(brepA, brepB, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def BrepSurface(brep, surface, tolerance, multiple=False):
    """
    Intersects a Brep and a Surface.

    Args:
        brep (Brep): A brep to be intersected.
        surface (Surface): A surface to be intersected.
        tolerance (double): A tolerance value.

    Returns:
        bool: True on success; False on failure.
        intersectionCurves (Curve[]): The intersection curves array argument. This out reference is assigned during the call.
        intersectionPoints (Point3d[]): The intersection points array argument. This out reference is assigned during the call.
    """
    url = "rhino/geometry/intersect/intersection/brepsurface-brep_surface_double_curvearray_point3darray"
    if multiple: url += "?multiple=true"
    args = [brep, surface, tolerance]
    if multiple: args = zip(brep, surface, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def MeshMeshFast(meshA, meshB, multiple=False):
    """
    This is an old overload kept for compatibility. Overlaps and near misses are ignored.

    Args:
        meshA (Mesh): First mesh for intersection.
        meshB (Mesh): Second mesh for intersection.

    Returns:
        Line[]: An array of intersection line segments, or null.
    """
    url = "rhino/geometry/intersect/intersection/meshmeshfast-mesh_mesh"
    if multiple: url += "?multiple=true"
    args = [meshA, meshB]
    if multiple: args = zip(meshA, meshB)
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToLine(response)
    return response


def MeshMesh(meshes, tolerance, preprocessing, sets, overlaps, textLog, cancel, progress, multiple=False):
    """
    Intersects meshes. Overlaps and perforations are provided in the output list.

    Args:
        meshes (IEnumerable<Mesh>): The mesh input list. This cannot be null. Null entries are tolerated.
        tolerance (double): A tolerance value. If negative, the positive value will be used.
            WARNING! Good tolerance values are in the magnitude of 10^-7, or RhinoMath.SqrtEpsilon*10.
        preprocessing (bool): Indicates if a preprocessing step can be executed.
            Some groups of meshes have distances between vertices and edges that are below the tolerance indicated. In this case, this parameter allows the function
            to improve the mesh in order to increase likelihood of intersection success. The mesh topology might change slightly, but not the overall shape.If meshes have no distances between vertices and edges laying below the tolerance that is indicated, this parameter will do nothing.
        sets (SetsCombinations): Determines which sets of intersections are considered. See SetsCombinations for definitions.
        overlaps (bool): If true, overlaps are computed and returned.
        textLog (FileIO.TextLog): A text log, or null.
        cancel (System.Threading.CancellationToken): A cancellation token to stop the computation at a given point.
        progress (IProgress<double>): A progress reporter to inform the user about progress. The reported value is indicative.

    Returns:
        bool: True, if the operation succeeded, otherwise false.
        intersections (Polyline[]): If true, overlaps are computed and returned.
        overlapsResult (Polyline[]): If requested, overlaps are returned here.
    """
    url = "rhino/geometry/intersect/intersection/meshmesh-mesharray_double_bool_setscombinations_polylinearray_bool_polylinearray_fileio.textlog_system.threading.cancellationtoken_doublearray"
    if multiple: url += "?multiple=true"
    args = [meshes, tolerance, preprocessing, sets, overlaps, textLog, cancel, progress]
    if multiple: args = zip(meshes, tolerance, preprocessing, sets, overlaps, textLog, cancel, progress)
    response = Util.ComputeFetch(url, args)
    return response


def MeshMesh1(meshes, tolerance, preprocessing, sets, textLog, cancel, progress, multiple=False):
    """
    Intersects meshes. Overlaps and perforations are provided in the output list.

    Args:
        meshes (IEnumerable<Mesh>): The mesh input list. This cannot be null. Null entries are tolerated.
        tolerance (double): A tolerance value. If negative, the positive value will be used.
            WARNING! Good tolerance values are in the magnitude of 10^-7, or RhinoMath.SqrtEpsilon*10.
        preprocessing (bool): Indicates if a preprocessing step can be executed.
            Some groups of meshes have distances between vertices and edges that are below the tolerance indicated. In this case, this parameter allows the function
            to improve the mesh in order to increase likelihood of intersection success. The mesh topology might change slightly, but not the overall shape.If meshes have no distances between vertices and edges laying below the tolerance that is indicated, this parameter will do nothing.
        sets (SetsCombinations): Determines which sets of intersections are considered. See SetsCombinations for definitions.
        textLog (FileIO.TextLog): A text log, or null.
        cancel (System.Threading.CancellationToken): A cancellation token to stop the computation at a given point.
        progress (IProgress<double>): A progress reporter to inform the user about progress. The reported value is indicative.

    Returns:
        bool: True, if the operation succeeded, otherwise false.
        intersections (Polyline[]): If true, overlaps are computed and returned.
        overlapsResult (Mesh): If requested, overlaps are returned here.
    """
    url = "rhino/geometry/intersect/intersection/meshmesh-mesharray_double_bool_setscombinations_polylinearray_mesh_fileio.textlog_system.threading.cancellationtoken_doublearray"
    if multiple: url += "?multiple=true"
    args = [meshes, tolerance, preprocessing, sets, textLog, cancel, progress]
    if multiple: args = zip(meshes, tolerance, preprocessing, sets, textLog, cancel, progress)
    response = Util.ComputeFetch(url, args)
    return response


def MeshMeshAccurate(meshA, meshB, tolerance, multiple=False):
    """
    Intersects two meshes. Overlaps and near misses are handled. This is an old method kept for compatibility.

    Args:
        meshA (Mesh): First mesh for intersection.
        meshB (Mesh): Second mesh for intersection.
        tolerance (double): A tolerance value. If negative, the positive value will be used.
            WARNING! Good tolerance values are in the magnitude of 10^-7, or RhinoMath.SqrtEpsilon*10.

    Returns:
        Polyline[]: An array of intersection and overlaps polylines.
    """
    url = "rhino/geometry/intersect/intersection/meshmeshaccurate-mesh_mesh_double"
    if multiple: url += "?multiple=true"
    args = [meshA, meshB, tolerance]
    if multiple: args = zip(meshA, meshB, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def MeshRay(mesh, ray, multiple=False):
    """
    Finds the first intersection of a ray with a mesh.

    Args:
        mesh (Mesh): A mesh to intersect.
        ray (Ray3d): A ray to be casted.

    Returns:
        double: >= 0.0 parameter along ray if successful.
        < 0.0 if no intersection found.
    """
    url = "rhino/geometry/intersect/intersection/meshray-mesh_ray3d"
    if multiple: url += "?multiple=true"
    args = [mesh, ray]
    if multiple: args = zip(mesh, ray)
    response = Util.ComputeFetch(url, args)
    return response


def MeshRay1(mesh, ray, multiple=False):
    """
    Finds the first intersection of a ray with a mesh.

    Args:
        mesh (Mesh): A mesh to intersect.
        ray (Ray3d): A ray to be casted.

    Returns:
        double: >= 0.0 parameter along ray if successful.
        < 0.0 if no intersection found.
        meshFaceIndices (int[]): faces on mesh that ray intersects.
    """
    url = "rhino/geometry/intersect/intersection/meshray-mesh_ray3d_intarray"
    if multiple: url += "?multiple=true"
    args = [mesh, ray]
    if multiple: args = zip(mesh, ray)
    response = Util.ComputeFetch(url, args)
    return response


def MeshPolyline(mesh, curve, multiple=False):
    """
    Finds the intersection of a mesh and a polyline.

    Args:
        mesh (Mesh): A mesh to intersect.
        curve (PolylineCurve): A polyline curves to intersect.

    Returns:
        Point3d[]: An array of points: one for each face that was passed by the faceIds out reference.
        faceIds (int[]): The indices of the intersecting faces. This out reference is assigned during the call.
    """
    url = "rhino/geometry/intersect/intersection/meshpolyline-mesh_polylinecurve_intarray"
    if multiple: url += "?multiple=true"
    args = [mesh, curve]
    if multiple: args = zip(mesh, curve)
    response = Util.ComputeFetch(url, args)
    return response


def MeshLine(mesh, line, multiple=False):
    """
    Finds the intersection of a mesh and a line

    Args:
        mesh (Mesh): A mesh to intersect
        line (Line): The line to intersect with the mesh

    Returns:
        Point3d[]: An array of points: one for each face that was passed by the faceIds out reference.
        faceIds (int[]): The indices of the intersecting faces. This out reference is assigned during the call.
    """
    url = "rhino/geometry/intersect/intersection/meshline-mesh_line_intarray"
    if multiple: url += "?multiple=true"
    args = [mesh, line]
    if multiple: args = zip(mesh, line)
    response = Util.ComputeFetch(url, args)
    return response


def RayShoot(ray, geometry, maxReflections, multiple=False):
    """
    Computes point intersections that occur when shooting a ray to a collection of surfaces.

    Args:
        ray (Ray3d): A ray used in intersection.
        geometry (IEnumerable<GeometryBase>): Only Surface and Brep objects are currently supported. Trims are ignored on Breps.
        maxReflections (int): The maximum number of reflections. This value should be any value between 1 and 1000, inclusive.

    Returns:
        Point3d[]: An array of points: one for each face that was passed by the faceIds out reference.
    """
    url = "rhino/geometry/intersect/intersection/rayshoot-ray3d_geometrybasearray_int"
    if multiple: url += "?multiple=true"
    args = [ray, geometry, maxReflections]
    if multiple: args = zip(ray, geometry, maxReflections)
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToPoint3d(response)
    return response


def ProjectPointsToMeshes(meshes, points, direction, tolerance, multiple=False):
    """
    Projects points onto meshes.

    Args:
        meshes (IEnumerable<Mesh>): the meshes to project on to.
        points (IEnumerable<Point3d>): the points to project.
        direction (Vector3d): the direction to project.
        tolerance (double): Projection tolerances used for culling close points and for line-mesh intersection.

    Returns:
        Point3d[]: Array of projected points, or None in case of any error or invalid input.
    """
    url = "rhino/geometry/intersect/intersection/projectpointstomeshes-mesharray_point3darray_vector3d_double"
    if multiple: url += "?multiple=true"
    args = [meshes, points, direction, tolerance]
    if multiple: args = zip(meshes, points, direction, tolerance)
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToPoint3d(response)
    return response


def ProjectPointsToMeshesEx(meshes, points, direction, tolerance, multiple=False):
    """
    Projects points onto meshes.

    Args:
        meshes (IEnumerable<Mesh>): the meshes to project on to.
        points (IEnumerable<Point3d>): the points to project.
        direction (Vector3d): the direction to project.
        tolerance (double): Projection tolerances used for culling close points and for line-mesh intersection.

    Returns:
        Point3d[]: Array of projected points, or None in case of any error or invalid input.
        indices (int[]): Return points[i] is a projection of points[indices[i]]
    """
    url = "rhino/geometry/intersect/intersection/projectpointstomeshesex-mesharray_point3darray_vector3d_double_intarray"
    if multiple: url += "?multiple=true"
    args = [meshes, points, direction, tolerance]
    if multiple: args = zip(meshes, points, direction, tolerance)
    response = Util.ComputeFetch(url, args)
    return response


def ProjectPointsToBreps(breps, points, direction, tolerance, multiple=False):
    """
    Projects points onto breps.

    Args:
        breps (IEnumerable<Brep>): The breps projection targets.
        points (IEnumerable<Point3d>): The points to project.
        direction (Vector3d): The direction to project.
        tolerance (double): The tolerance used for intersections.

    Returns:
        Point3d[]: Array of projected points, or None in case of any error or invalid input.
    """
    url = "rhino/geometry/intersect/intersection/projectpointstobreps-breparray_point3darray_vector3d_double"
    if multiple: url += "?multiple=true"
    args = [breps, points, direction, tolerance]
    if multiple: args = zip(breps, points, direction, tolerance)
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToPoint3d(response)
    return response


def ProjectPointsToBrepsEx(breps, points, direction, tolerance, multiple=False):
    """
    Projects points onto breps.

    Args:
        breps (IEnumerable<Brep>): The breps projection targets.
        points (IEnumerable<Point3d>): The points to project.
        direction (Vector3d): The direction to project.
        tolerance (double): The tolerance used for intersections.

    Returns:
        Point3d[]: Array of projected points, or None in case of any error or invalid input.
        indices (int[]): Return points[i] is a projection of points[indices[i]]
    """
    url = "rhino/geometry/intersect/intersection/projectpointstobrepsex-breparray_point3darray_vector3d_double_intarray"
    if multiple: url += "?multiple=true"
    args = [breps, points, direction, tolerance]
    if multiple: args = zip(breps, points, direction, tolerance)
    response = Util.ComputeFetch(url, args)
    return response

