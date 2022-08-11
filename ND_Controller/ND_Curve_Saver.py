import maya.cmds as cmds
import os
import sys
import json


def save_curve():
    if cmds.window("ND_Save_Curve_Standalone_ID_ND", exists=1):
        cmds.deleteUI("ND_Save_Curve_Standalone_ID_ND")
    if cmds.windowPref("ND_Save_Curve_Standalone_ID_ND", exists=True):
        cmds.windowPref("ND_Save_Curve_Standalone_ID_ND", remove=True)
    cmds.window('ND_Save_Curve_Standalone_ID_ND', title='ND Curve Saver', w=300, h=410, toolbox=True, sizeable=False)
    main_layout = cmds.columnLayout("Saved_Curves_Main_Layout_ND_ID", rowSpacing=0)
    cmds.text("Curve Name", bgc=(0.3, 0.3, 0.3), w=300, h=20, p=main_layout)
    save_name_layout = cmds.columnLayout(rowSpacing=5, columnOffset=["both", 10], h=70)
    cmds.textField("Curve_Save_Name_ND_ID", p=save_name_layout, width=280, h=25)
    cmds.button(l='Save Current Curve', w=280, h=30, c=lambda *x: save_custom_curve())
    cmds.text("List Saved Curves", bgc=(0.3, 0.3, 0.3), w=300, h=20, p=main_layout)
    cmds.columnLayout('Saved_Curves_List_Layout_ND_ID', rowSpacing=5, p=main_layout, columnOffset=["both", 10])
    curve_list_interface(False)
    delete_button = cmds.columnLayout(rowSpacing=5, p=main_layout, columnOffset=["both", 10])
    cmds.button(l='Delete Saved Curve', p=delete_button, w=280, h=30, c=lambda *x: delete_custom_curve())

    cmds.showWindow("ND_Save_Curve_Standalone_ID_ND")


def saved_dict_path():
    nd = os.path.dirname(os.path.realpath(__file__))  # script's path
    return os.path.join(nd, 'saved_curves', 'saved_curves_dict.json')  # take json file in saved curves folder


def curve_list_interface(delete):
    if delete == True and cmds.columnLayout('Saved_Curves_Layout_ND_ID', exists=True):
        cmds.deleteUI("Saved_Curves_Layout_ND_ID")
    custom_curves = list_custom_curves()
    cmds.columnLayout("Saved_Curves_Layout_ND_ID", rowSpacing=5, p="Saved_Curves_List_Layout_ND_ID")
    cmds.textScrollList("Saved_Curves_ND_ID", p="Saved_Curves_Layout_ND_ID", w=280, h=250, a=custom_curves,
                        doubleClickCommand=lambda *x: create_proxy_custom_curve())


def create_proxy_custom_curve():
    control = cmds.ls(sl=True, o=True)
    curve = cmds.textScrollList('Saved_Curves_ND_ID', q=True, selectItem=True)[0]
    json_path = saved_dict_path()
    list_saved = list_custom_curves()
    index = list_saved.index(curve)
    with open(json_path) as outfile:
        data = json.load(outfile)
    ctrl = cmds.curve(d=data["curves"][index][curve]['d'], n=curve, p=data["curves"][index][curve]['p'])
    cmds.select(control, ctrl)


def write_json_data(data):
    json_path = saved_dict_path()
    with open(json_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def save_custom_curve():
    curve = cmds.ls(sl=True, o=True)
    if not curve:
        return
    d, n, p = get_curve_inf(curve[0])
    curve_dict = {n: {'d': d, 'p': p}}
    json_path = saved_dict_path()

    with open(json_path) as outfile:
        data = json.load(outfile)
        temp = data["curves"]
        temp.append(curve_dict)
    write_json_data(data)
    curve_list_interface(True)


def delete_custom_curve():
    if not cmds.textScrollList('Saved_Curves_ND_ID', q=True, selectItem=True):
        return
    curve = cmds.textScrollList('Saved_Curves_ND_ID', q=True, selectItem=True)[0]
    json_path = saved_dict_path()
    list_saved = list_custom_curves()
    index_del = list_saved.index(curve)
    with open(json_path) as outfile:
        data = json.load(outfile)
        temp = data["curves"]
        temp.remove(data["curves"][index_del])
    write_json_data(data)
    curve_list_interface(True)


def get_curve_inf(curve):
    sel = curve
    sel_shape = cmds.listRelatives(sel, s=True)[0]
    degree = cmds.getAttr(sel_shape + ".degree")
    sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
    cmds.select(sel_vtx)
    i = 0
    all_vtx_ls = []
    for vtx in sel_vtx:
        cmds.select(vtx)
        x = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].xValue'))
        y = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].yValue'))
        z = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].zValue'))
        all_vtx_ls.append((x, y, z))
        i += 1
    cmds.select(sel)
    if cmds.textField("Curve_Save_Name_ND_ID", q=True, text=True):
        name = cmds.textField("Curve_Save_Name_ND_ID", q=True, text=True)
    else:
        name = sel
    return degree, name,  all_vtx_ls


def list_custom_curves():
    json_path = saved_dict_path()
    with open(json_path) as outfile:
        data = json.load(outfile)
    saved_curve_list = []
    for d in data["curves"]:
        for key in d:
            saved_curve_list.append(key)
    return saved_curve_list
