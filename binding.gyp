{
  "targets": [
    {
      "target_name": 'addon',

      'include_dirs': [
          './recastnavigation/DebugUtils/Include',
          './recastnavigation/Detour/Include',
          './recastnavigation/DetourCrowd/Include',
          './recastnavigation/DetourTileCache/Include',
          './recastnavigation/Recast/Include/',
          './recastnavigation/RecastDemo/Include',
          './SDL',
          './recastnavigation/RecastDemo/Contrib/fastlz',
          "<!(node -e \"require('nan')\")"
      ],

      'conditions': [
        ['OS=="linux"', {
          'include_dirs!': [
            './SDL'
          ],
          'include_dirs': [
            '/usr/include/SDL2'
          ]
        }]
      ],

      "sources": [ 
      './recastnavigation/DebugUtils/Source/DebugDraw.cpp',
      './recastnavigation/DebugUtils/Source/DetourDebugDraw.cpp',
      './recastnavigation/DebugUtils/Source/RecastDebugDraw.cpp',
      './recastnavigation/DebugUtils/Source/RecastDump.cpp',
      './recastnavigation/Detour/Source/DetourAlloc.cpp',
      './recastnavigation/Detour/Source/DetourAssert.cpp',
      './recastnavigation/Detour/Source/DetourCommon.cpp',
      './recastnavigation/Detour/Source/DetourNavMesh.cpp',
      './recastnavigation/Detour/Source/DetourNavMeshBuilder.cpp',
      './recastnavigation/Detour/Source/DetourNavMeshQuery.cpp',
      './recastnavigation/Detour/Source/DetourNode.cpp',
      './recastnavigation/DetourCrowd/Source/DetourCrowd.cpp',
      './recastnavigation/DetourCrowd/Source/DetourLocalBoundary.cpp',
      './recastnavigation/DetourCrowd/Source/DetourObstacleAvoidance.cpp',
      './recastnavigation/DetourCrowd/Source/DetourPathCorridor.cpp',
      './recastnavigation/DetourCrowd/Source/DetourPathQueue.cpp',
      './recastnavigation/DetourCrowd/Source/DetourProximityGrid.cpp',
      './recastnavigation/DetourTileCache/Source/DetourTileCache.cpp',
      './recastnavigation/DetourTileCache/Source/DetourTileCacheBuilder.cpp',
      './recastnavigation/Recast/Source/Recast.cpp',
      './recastnavigation/Recast/Source/RecastAlloc.cpp',
      './recastnavigation/Recast/Source/RecastArea.cpp',
      './recastnavigation/Recast/Source/RecastAssert.cpp',
      './recastnavigation/Recast/Source/RecastContour.cpp',
      './recastnavigation/Recast/Source/RecastFilter.cpp',
      './recastnavigation/Recast/Source/RecastLayers.cpp',
      './recastnavigation/Recast/Source/RecastMesh.cpp',
      './recastnavigation/Recast/Source/RecastMeshDetail.cpp',
      './recastnavigation/Recast/Source/RecastRasterization.cpp',
      './recastnavigation/Recast/Source/RecastRegion.cpp',
      './recastnavigation/RecastDemo/Source/ChunkyTriMesh.cpp',
      './recastnavigation/RecastDemo/Source/Filelist.cpp',
      './recastnavigation/RecastDemo/Source/InputGeom.cpp',
      './recastnavigation/RecastDemo/Source/MeshLoaderObj.cpp',
      './recastnavigation/RecastDemo/Source/PerfTimer.cpp',
      './recastnavigation/RecastDemo/Source/ValueHistory.cpp',
      './recastnavigation/RecastDemo/Source/Sample.cpp',
      './recastnavigation/RecastDemo/Source/Sample_Debug.cpp',
      './recastnavigation/RecastDemo/Source/Sample_SoloMesh.cpp',
      './recastnavigation/RecastDemo/Source/Sample_TempObstacles.cpp',
      './recastnavigation/RecastDemo/Source/Sample_TileMesh.cpp',
      './recastnavigation/RecastDemo/Source/SampleInterfaces.cpp',
      './recastnavigation/RecastDemo/Contrib/fastlz/fastlz.c',
      './src/addon.cc',
      './src/dtCrowdWrap.cpp',
      './src/dtNavMeshQueryWrap.cpp',
      './src/dtNavMeshWrap.cpp',
      './src/InputGeomWrap.cpp',
      './src/BuildContextWrap.cpp',
      './src/Sample_TempObstaclesWrap.cpp',
      './src/Sample_TempObstaclesExt.cpp',
    ]
    }
  ]
}
