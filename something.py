import unreal

def saveSelectedassets():
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        unreal.EditorAssetLibrary.save_asset(asset.get_path_name())

def Duplicate (suffix):
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        assetPath = asset.get_path_name()
        newPath = assetPath.replace(asset.get_name(), f"{asset.get_name()}{suffix}")
        unreal.EditorAssetLibrary.duplicate_asset(assetPath, newPath)

Duplicate("lol")

def batchRenameAssets(prefix, suffix):
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        assetName = asset.get_name()
        newAssetName = f"{prefix}{assetName}{suffix}"
        assetPath = asset.get_path_name()
        newPath = assetPath.repalce(assetName, newAssetName)
        unreal.EditorAssetLibrary.rename_asset(assetPath, newPath)

def importAssetFromDir(dir):
    importTask = unreal.AssetImportTask()
    importTask.filename = dir
    importTask.destination_path = "/game/ImportedAssets"
    importTask.replace_existing = True
    importTask.automated = True

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([importTask])


#something random
import unreal
import random

def SpawnCubeAt(x,y,z):
    EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    #convert to unreal vector
    location = unreal.Vector(x,y,z)
    #create static mesh actor + static mesh
    actorClass = unreal.StaticMeshActor
    componentClass = unreal.StaticMeshComponent
    staticMeshActor = EAS.spawn_actor_from_class(actorClass, location)
    staticMesh = unreal.EditorAssetLibrary.load_asset('/Engine/BasicShapes/Cube.Cube')
    #set statuc mesh on actor
    staticMeshActor.get_component_by_class(componentClass).set_static_mesh(staticMesh)

def SpawnInBox (x,y,z, radius, num):
    for i in range(num):
        rx = random.uniform(-radius, radius)
        ry = random.uniform(-radius, radius)
        rz = random.uniform(-radius, radius)
        SpawnCubeAt(x+rx, y+ry, z+rz)

SpawnInBox(0,0,0,500,150)