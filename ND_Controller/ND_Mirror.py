import maya.cmds as cmds


def mirror_shapes():
    source_list = mirror_list_dict["source_list"]
    target_list = mirror_list_dict["target_list"]
    x, y, z = 0, 0, 0
    if cmds.checkBox('Axis_X_ID_ND', q=True, v=True):
        x = 180
    if cmds.checkBox('Axis_Y_ID_ND', q=True, v=True):
        y = 180
    if cmds.checkBox('Axis_Z_ID_ND', q=True, v=True):
        z = 180
    index = 0
    for target in target_list:
        if target != 'Self':
            source = source_list[index]
            source_shape = cmds.listRelatives(source, f=True, s=True)
            target_shape = cmds.listRelatives(target, f=True, s=True)
            cmds.duplicateCurve(source_shape[0], name='Source_Curve_ND', ch=False)
            save_color_shape('Source_Curve_NDShape', target_shape)
            set_width = cmds.getAttr(source_shape[0] + ".lineWidth")
            cmds.setAttr("Source_Curve_NDShape.lineWidth", set_width)
            cmds.parent('Source_Curve_NDShape', target, shape=True, relative=True)
            save_selections_sets('Source_Curve_NDShape', target_shape)
            sel_vtx = cmds.ls('{}.controlPoints[:]'.format('Source_Curve_NDShape'), fl=True)
            cmds.select(sel_vtx)
            if cmds.checkBox('Axis_XYZ_World_ID_ND', q=True, v=True):
                cmds.xform(r=True, ro=(x, y, z), p=True, ws=True)
            else:
                cmds.xform(r=True, ro=(x, y, z), p=True, os=True)
            cmds.rename('Source_Curve_NDShape', target + 'Shape')
            cmds.delete(target_shape)
            cmds.delete('Source_Curve_ND')
        index += 1
    cmds.select(None)


def mirror_tool():
    if cmds.window("Mirror_Tool_Standalone_ND_ID", exists=1):
        cmds.deleteUI("Mirror_Tool_Standalone_ND_ID")
    if cmds.windowPref("Mirror_Tool_Standalone_ND_ID", exists=True):
        cmds.windowPref("Mirror_Tool_Standalone_ND_ID", remove=True)
    cmds.window("Mirror_Tool_Standalone_ND_ID", title="ND Mirror Tool", width=330, tlb=False)
    main_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    # renameLayout
    cmds.text("Mirror Markers", bgc=(0.4, 0.4, 0.4), h=20, parent=main_layout)

    mirror_markers_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=0, parent=main_layout)

    mirror_marker_l_layout = cmds.rowLayout(numberOfColumns=2,
                                            parent=mirror_markers_layout,
                                            width=280,
                                            h=25,
                                            columnAttach2=['left', 'left'],
                                            columnOffset2=[12, 2])
    cmds.text("L Marker", parent=mirror_marker_l_layout)
    cmds.textField("L_Marker_ND_ID", parent=mirror_marker_l_layout,  width=250, pht='Prefix_|_mid_|_suffix')

    mirror_marker_r_layout = cmds.rowLayout(numberOfColumns=2,
                                            parent=mirror_markers_layout,
                                            width=280,
                                            h=25,
                                            columnAttach2=['left', 'right'],
                                            columnOffset2=[12, 0])

    cmds.text("R Marker", parent=mirror_marker_r_layout)
    cmds.textField("R_Marker_ND_ID", parent=mirror_marker_r_layout, width=250,  pht='Prefix_|_mid_|_suffix')

    mirror_way_layout = cmds.rowLayout(numberOfColumns=3,
                                       parent=main_layout,
                                       width=280,
                                       h=20,
                                       columnAttach3=['left', 'right', 'right'],
                                       columnOffset3=[5, 0, 0])
    cmds.checkBox('Hierarchy', parent=mirror_way_layout, width=75, height=20, v=True)
    cmds.radioCollection(parent=mirror_way_layout)
    cmds.radioButton('Mirror_L', label='Left >> Right', select=True)
    cmds.radioButton('Mirror_R', label='Right >> Left')
    # Scroll list
    source_target_layout = cmds.columnLayout(parent=main_layout, adjustableColumn=True, rowSpacing=1)
    cmds.text("Source curves >> Target curves", bgc=(0.3, 0.3, 0.3), h=20, parent=source_target_layout)
    source_scroll_layout = cmds.scrollLayout('source_scroll_layout_ND_ID', childResizable=True,
                                             parent=source_target_layout, width=280, h=200)  # List objects
    scroll_source_target(False)
    buttons_layout = cmds.columnLayout(parent=main_layout, rowSpacing=20, adj=True)
    cmds.button(label="Update List", parent=buttons_layout, c=lambda *x: scroll_source_target(delete=True))
    mirror_options_layout = cmds.columnLayout(parent=main_layout, rowSpacing=5, adj=True)
    cmds.text("Mirror Axis", parent=mirror_options_layout, bgc=(0.3, 0.3, 0.3), h=20)
    mirror_axis_layout = cmds.rowLayout(numberOfColumns=4,
                                        parent=mirror_options_layout,
                                        width=280,
                                        h=25,
                                        columnAttach4=['left', 'both', 'right', 'left'],
                                        columnOffset4=[20, 0, 0, 10])
    cmds.checkBox('Axis_X_ID_ND', l='Axis X', parent=mirror_axis_layout, width=60, height=20)
    cmds.checkBox('Axis_Y_ID_ND', l='Axis Y', parent=mirror_axis_layout, width=60, height=20)
    cmds.checkBox('Axis_Z_ID_ND', l='Axis Z', parent=mirror_axis_layout, width=75, height=20)
    cmds.checkBox('Axis_XYZ_World_ID_ND', l='World', parent=mirror_axis_layout, width=75, height=20)

    cmds.button(label="Mirror", parent=mirror_options_layout, h=35, c=lambda *x: mirror_shapes())

    # cmds.button(label="Cancel", parent=buttons_layout, c="cmds.deleteUI(\"Mirror_Tool_Standalone_ND_ID\")")
    cmds.showWindow("Mirror_Tool_Standalone_ND_ID")


def scroll_source_target(delete):
    if delete and cmds.columnLayout('Scroll_Source_Target_ND_ID', exists=True):
        cmds.deleteUI("Scroll_Source_Target_ND_ID")
    source_list = cmds.ls(sl=True)
    target_list = produce_target_list(source_list)
    cmds.columnLayout('Scroll_Source_Target_ND_ID', p='source_scroll_layout_ND_ID',
                      adjustableColumn=True, rowSpacing=1, columnOffset=["both", 0])
    for index in range(len(source_list)):
        cmds.textField(text=source_list[index]+' >> '+target_list[index], w=100, ed=False)
    mirror_list_dict["source_list"] = source_list
    mirror_list_dict["target_list"] = target_list


mirror_list_dict = {
    "source_list": [],
    "target_list": []
}


def produce_target_list(source_list):
    source_list = source_list

    left_prefix_list =  ['L_', 'l_', 'Left_', 'left_']
    right_prefix_list = ['R_', 'r_', 'Right_', 'right_']

    left_mid_list =  ['_L_', '_l_', '_Left_', '_left_']
    right_mid_list = ['_R_', '_r_', '_Right_', '_right_']

    left_suffix_list =  ['_L', '_l', '_Left', '_left']
    right_suffix_list = ['_R', '_r', '_Right', '_right']

    custom_l_marker_list = cmds.textField("L_Marker_ND_ID", q=True, text=True)
    custom_r_marker_list = cmds.textField("R_Marker_ND_ID", q=True, text=True)

    c_m_index = 0
    if custom_l_marker_list and custom_r_marker_list:
        if '|' in custom_l_marker_list and '|' in custom_r_marker_list:
            custom_l_marker_list = custom_l_marker_list.split('|')
            custom_r_marker_list = custom_r_marker_list.split('|')
        else:
            custom_l_marker_list = [custom_l_marker_list]
            custom_r_marker_list = [custom_r_marker_list]

        for custom_l_marker in custom_l_marker_list:
            custom_r_marker = custom_r_marker_list[c_m_index]
            if custom_l_marker[-1] == '_' and custom_r_marker[-1] == '_' and custom_l_marker[0] != '_' and custom_r_marker[0] != '_':
                left_prefix_list.insert(0, custom_l_marker)
                right_prefix_list.insert(0, custom_r_marker)
            elif custom_l_marker[0] == '_' and custom_r_marker[0] == '_' and custom_l_marker[-1] != '_' and custom_r_marker[-1] != '_':
                left_suffix_list.insert(0, custom_l_marker)
                right_suffix_list.insert(0, custom_r_marker)
            elif custom_l_marker[0] == '_' and custom_r_marker[0] == '_' and custom_l_marker[-1] == '_' and custom_r_marker[-1] == '_':
                left_mid_list.insert(0, custom_l_marker)
                right_mid_list.insert(0, custom_r_marker)
            c_m_index += 1

    source_marker_list = []
    target_marker = ''
    target_marker_list = []

    for source in source_list:
        source_marker = ''
        if cmds.radioButton('Mirror_L', q=True, select=True):
            for left_prefix in left_prefix_list:
                if left_prefix.split("_")[0] == source.split("_")[0]:
                    source_marker = left_prefix
                    target_marker = right_prefix_list[left_prefix_list.index(left_prefix)]
                    break
            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            for left_mid in left_mid_list:
                if left_mid in source:
                    source_marker = left_mid
                    target_marker = right_mid_list[left_mid_list.index(left_mid)]
                    break

            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            for left_suffix in left_suffix_list:
                if source.endswith(left_suffix):
                    source_marker = left_suffix
                    target_marker = right_suffix_list[left_suffix_list.index(left_suffix)]
                    break
            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            if source_marker == '':
                source_marker_list.append('')
                target_marker_list.append('')

        else:
            for right_prefix in right_prefix_list:
                if right_prefix.split("_")[0] == source.split("_")[0]:
                    source_marker = right_prefix
                    target_marker = left_prefix_list[right_prefix_list.index(right_prefix)]
                    break
            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            for right_mid in right_mid_list:
                if right_mid in source:
                    source_marker = right_mid
                    target_marker = left_mid_list[right_mid_list.index(right_mid)]
                    break
            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            for right_suffix in right_suffix_list:
                if source.endswith(right_suffix):
                    source_marker = right_suffix
                    target_marker = left_suffix_list[right_suffix_list.index(right_suffix)]
                    break
            if source_marker != '':
                source_marker_list.append(source_marker)
                target_marker_list.append(target_marker)
                continue

            if source_marker == '':
                source_marker_list.append('')
                target_marker_list.append('')

    target_list = []
    index = 0
    target_path = []
    source_path = []
    for target_mark in target_marker_list:
        if target_mark == '':
            target = 'Not_Exist_Element_ND_ID'
        else:
            source = source_list[index]
            target = source.replace(source_marker_list[index], target_mark)
            target_path = cmds.ls(target, o=True, l=True)
            source_path = cmds.ls(source, o=True, l=True)
        index += 1
        if source_path != [] and target_path != []:
            source_path = source_path[0].split('|')
            target_path = target_path[0].split('|')
        if cmds.checkBox('Hierarchy', q=True, v=True):
            if cmds.objExists(target) and len(target_path) == len(source_path):
                target_list.append(target)
            else:
                target_list.append('Self')
        else:
            if cmds.objExists(target):
                target_list.append(target)
            else:
                target_list.append('Self')

    print (left_prefix_list)
    print (right_prefix_list)
    print (left_mid_list)
    print (right_mid_list)
    print (left_suffix_list)
    print (right_suffix_list)
    print (source_list)
    print (target_list)

    return target_list


mirror_tool()
