import maya.cmds as cmds


def make_border_topology():
    mesh = cmds.ls(sl=1)
    cmds.duplicate(mesh, n='Temp_to_Retop_ND_ID')
    cmds.polySeparate('Temp_to_Retop_ND_ID', n='Temp_to_Retop_ND_ID_geo')
    separated_meshes = cmds.ls(sl=1)
    print(separated_meshes)
    for geo in separated_meshes:
        cmds.select(geo)
        cmds.polySelectConstraint(m=3, t=0x8000, w=1)  # to get border vertices
        cmds.polySelectConstraint(dis=True)
        cmds.polyExtrudeEdge(off=-1)
        border_faces = cmds.polyListComponentConversion(fromEdge=True, toFace=True)
        cmds.select(border_faces)
        cmds.polyChipOff(border_faces)
        cmds.polySeparate(geo, n='Border_Retop_ND_ID')
        cmds.delete('Border_Retop_ND_ID')
    cmds.delete('Temp_to_Retop_ND_ID', constructionHistory=True)
    children = cmds.listRelatives('Temp_to_Retop_ND_ID', children=True, fullPath=True, allDescendents=1)
    borders_list = []
    for i in children:
        if cmds.nodeType(i) == "mesh":
            transform = cmds.listRelatives(i, parent=1, fullPath=1)[0]
            borders_list.append(transform)
    print(borders_list)
    for bord in borders_list:
        cmds.parent(bord, w=True)
        cmds.polyNormal(bord.split('|')[-1], normalMode=3)
    cmds.delete('Temp_to_Retop_ND_ID')
    cmds.select(mesh)


make_border_topology()
