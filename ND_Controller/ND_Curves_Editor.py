import maya.cmds as cmds


def run():
    if cmds.window("ND_Curve_Editor_ID_ND", exists=1):
        cmds.deleteUI("ND_Curve_Editor_ID_ND")
    if cmds.windowPref("ND_Curve_Editor_ID_ND", exists=True):
        cmds.windowPref("ND_Curve_Editor_ID_ND", remove=True)

    cmds.window('ND_Curve_Editor_ID_ND', title='ND Curve Editor', width=300, height=250, toolbox=True, sizeable=False)
    main_layout = cmds.columnLayout(rowSpacing=0)

    flip_xyz_layout = cmds.rowLayout(numberOfColumns=5,
                                     parent=main_layout,
                                     width=300,
                                     height=40,
                                     columnAttach5=['left', 'both', 'right', 'right', 'left'],
                                     columnOffset5=[12, 4, 4, 4, 1])

    cmds.button(label="All VTX", parent=flip_xyz_layout, width=50, height=30, c=lambda *x: select_all_vtx(),
                statusBarMessage="Select all vertexes")
    cmds.button(label="X", parent=flip_xyz_layout, width=50, height=30, c=lambda *x: turn_curve(90, 0, 0))
    cmds.button(label="Y", parent=flip_xyz_layout, width=50, height=30, c=lambda *x: turn_curve(0, 90, 0))
    cmds.button(label="Z", parent=flip_xyz_layout, width=50, height=30, c=lambda *x: turn_curve(0, 0, 90))
    cmds.button(l="Color", p=flip_xyz_layout, w=50, h=30, vis=True, c=lambda *x: change_color(),
                statusBarMessage="Choose color")

    move_opt_row_layout = cmds.rowLayout(numberOfColumns=4, parent=main_layout,
                                         width=300, height=30,
                                         columnAttach4=['left', 'left', 'left', 'left'],
                                         columnOffset4=[10, 0, 0, 0])

    cmds.checkBox('World', l='World', p=move_opt_row_layout, w=156, h=20,
                  statusBarMessage="Move shape in world orientation")
    cmds.radioCollection(parent=move_opt_row_layout)
    cmds.radioButton('move_X', label='X', select=True)
    cmds.radioButton('move_Y', label='Y')
    cmds.radioButton('move_Z', label='Z')

    move_curve_layout = cmds.columnLayout(parent=main_layout,
                                          width=300,
                                          height=65,
                                          columnAlign="center",
                                          columnOffset=["left", 10],
                                          rowSpacing=3)

    move_x_buttons = cmds.rowLayout(numberOfColumns=3,
                                    parent=move_curve_layout,
                                    width=300,
                                    height=25,
                                    columnAttach3=['right', 'left', 'left'],
                                    columnOffset3=[15, 30, 50])

    cmds.text("Move Shape XYZ", parent=move_x_buttons)
    cmds.button(label='-', parent=move_x_buttons, width=30, height=25, c=lambda *x: move_shape(-1))
    cmds.button(label='+', parent=move_x_buttons, width=30, height=25, c=lambda *x: move_shape(1))

    cmds.floatSliderGrp('move_curve_ID_ND', parent=move_curve_layout,
                        min=0,
                        max=20,
                        value=2,
                        field=True,
                        enableKeyboardFocus=True,
                        width=280,
                        height=25)

    change_size_layout = cmds.columnLayout(parent=main_layout,
                                           width=300,
                                           height=65,
                                           columnAlign="center",
                                           columnOffset=["both", 10],
                                           rowSpacing=0)

    size_opt_layout = cmds.rowLayout(numberOfColumns=6,
                                     parent=change_size_layout,
                                     width=300,
                                     height=25,
                                     columnAttach6=['right', 'right', 'right', 'right', 'right', 'right'],
                                     columnOffset6=[10, 0, 0, 25, 0, 0])

    cmds.text("Change Size:", parent=size_opt_layout)

    cmds.radioCollection(parent=size_opt_layout)
    cmds.radioButton('size_x1', label='x1')
    cmds.radioButton('size_x2', label='x2')
    cmds.radioButton('size_x4', label='x4')

    cmds.button(label="Scale", parent=size_opt_layout, width=35, height=20, c=lambda *x: change_size())

    cmds.floatSliderGrp('Change_Size_ID', parent=change_size_layout,
                        min=0.0,
                        max=3.0,
                        value=1,
                        field=True,
                        enableKeyboardFocus=True,
                        width=280,
                        height=30, )

    change_thickness_layout = cmds.columnLayout(parent=main_layout,
                                                width=300,
                                                height=60,
                                                columnAlign="center",
                                                columnOffset=["both", 10],
                                                rowSpacing=3)

    cmds.text("Change Thickness:", parent=change_thickness_layout)

    cmds.floatSliderGrp('Change_Thickness_ID', parent=change_thickness_layout,
                        changeCommand=lambda *x: change_thickness(),
                        field=True,
                        min=0.0,
                        max=10.0,
                        width=280,
                        height=30)

    cmds.showWindow('ND_Curve_Editor_ID_ND')


def change_thickness():
    set_width = cmds.floatSliderGrp("Change_Thickness_ID", query=True, value=True)
    controls = cmds.ls(sl=True)
    control_shape = cmds.listRelatives(controls, shapes=True)
    if controls:
        for shape in control_shape:
            cmds.setAttr(shape + ".lineWidth", set_width)


def change_size():
    sel_curves = cmds.ls(sl=True, o=True)
    quotient = 1.0
    if cmds.radioButton('size_x2', query=True, select=True): quotient = 2.0
    elif cmds.radioButton('size_x4', query=True, select=True): quotient = 4.0
    if sel_curves:
        for sel in sel_curves:
            if (cmds.floatSliderGrp('Change_Size_ID', query=True, value=True) < 1) and (quotient > 1):
                quotient = quotient / 10
            size = float(cmds.floatSliderGrp('Change_Size_ID', query=True, value=True) * float(quotient))
            if size == 0:
                size = 1
            cmds.select(sel)
            select_all_vtx()
            cmds.xform(r=True, s=(size, size, size), os=True)
        cmds.select(sel_curves)


def turn_curve(x, y, z):
    sel_curves = cmds.ls(sl=True, o=True)
    if sel_curves:
        select_all_vtx()
        cmds.xform(r=True, ro=(x, y, z), p=True, os=True)
    cmds.select(sel_curves)


def move_shape(q):
    sel_curves = cmds.ls(sl=True, o=True)
    if cmds.radioButton('move_X', query=True, select=True): x, y, z = 1, 0, 0
    elif cmds.radioButton('move_Y', query=True, select=True): x, y, z = 0, 1, 0
    elif cmds.radioButton('move_Z', query=True, select=True): x, y, z = 0, 0, 1
    move_x = q * x * (cmds.floatSliderGrp("move_curve_ID_ND", query=True, value=True))
    move_y = q * y * (cmds.floatSliderGrp("move_curve_ID_ND", query=True, value=True))
    move_z = q * z * (cmds.floatSliderGrp("move_curve_ID_ND", query=True, value=True))
    if sel_curves:
        select_all_vtx()
        if cmds.checkBox('World', q=True, v=True):
            cmds.xform(r=True, t=(move_x, move_y, move_z), p=True, ws=True)
        else:
            cmds.xform(r=True, t=(move_x, move_y, move_z), p=True, os=True)
    cmds.select(sel_curves)


def select_all_vtx():
    sel_curves = cmds.ls(sl=True, o=True)
    if sel_curves:
        shapes_ls = cmds.listRelatives(sel_curves, children=True)
        vtx_ls = []
        for shape in shapes_ls:
            sel_vtx = cmds.ls('{}.controlPoints[:]'.format(shape), fl=True)
            for vtx in sel_vtx:
                vtx_ls.append(vtx)
        cmds.select(vtx_ls)


def override_color(color_index):
    control = cmds.ls(sl=True)
    control_shape = cmds.listRelatives(control, shapes=True)
    if control:
        for color in control_shape:
            cmds.setAttr(color + ".overrideEnabled", True)
            cmds.setAttr(color + ".overrideColor", color_index)


def change_color():
    if cmds.window("ND_Color_ID_ND", exists=1):
        cmds.deleteUI("ND_Color_ID_ND")
    if cmds.windowPref("ND_Color_ID_ND", exists=True):
        cmds.windowPref("ND_Color_ID_ND", remove=True)

    cmds.window('ND_Color_ID_ND', title='ND Curve Editor Colors', w=200, h=180, toolbox=True, sizeable=False)

    main_layout = cmds.columnLayout(rowSpacing=0)

    colorise_layout = cmds.columnLayout(parent=main_layout,
                                        width=205,
                                        height=175,
                                        columnAlign="center",
                                        columnOffset=["right", 5],
                                        rowSpacing=0)

    change_color_layout = cmds.rowLayout(parent=colorise_layout,
                                         numberOfColumns=6,
                                         width=340,
                                         height=180,
                                         columnAttach6=['left', 'right', 'both', 'both', 'both', 'both'],
                                         columnOffset6=[5, 0, 0, 0, 0, 0])

    color_button_layout_1 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_1, w=30, h=30, bgc=[0.0, 0.0, 0.0], c=lambda *x: override_color(1))
    cmds.button(label="", p=color_button_layout_1, w=30, h=30, bgc=[0.5, 0.5, 0.5], c=lambda *x: override_color(3))
    cmds.button(label="", p=color_button_layout_1, w=30, h=30, bgc=[0.6, 0.0, 0.0], c=lambda *x: override_color(4))
    cmds.button(label="", p=color_button_layout_1, w=30, h=30, bgc=[0.0, 0.0, 0.5], c=lambda *x: override_color(5))
    cmds.button(label="", p=color_button_layout_1, w=30, h=30, bgc=[0.0, 0.0, 0.9], c=lambda *x: override_color(6))

    color_button_layout_2 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_2, w=30, h=30, bgc=[0.0, 0.3, 0.0], c=lambda *x: override_color(7))
    cmds.button(label="", p=color_button_layout_2, w=30, h=30, bgc=[0.1, 0.0, 0.3], c=lambda *x: override_color(8))
    cmds.button(label="", p=color_button_layout_2, w=30, h=30, bgc=[0.8, 0.2, 0.7], c=lambda *x: override_color(9))
    cmds.button(label="", p=color_button_layout_2, w=30, h=30, bgc=[0.6, 0.3, 0.2], c=lambda *x: override_color(10))
    cmds.button(label="", p=color_button_layout_2, w=30, h=30, bgc=[0.4, 0.2, 0.2], c=lambda *x: override_color(11))

    color_button_layout_3 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_3, w=30, h=30, bgc=[0.8, 0.2, 0.0], c=lambda *x: override_color(12))
    cmds.button(label="", p=color_button_layout_3, w=30, h=30, bgc=[1.0, 0.0, 0.0], c=lambda *x: override_color(13))
    cmds.button(label="", p=color_button_layout_3, w=30, h=30, bgc=[0.0, 1.0, 0.0], c=lambda *x: override_color(14))
    cmds.button(label="", p=color_button_layout_3, w=30, h=30, bgc=[0.2, 0.2, 0.7], c=lambda *x: override_color(15))
    cmds.button(label="", p=color_button_layout_3, w=30, h=30, bgc=[1.0, 1.0, 1.0], c=lambda *x: override_color(16))

    color_button_layout_4 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_4, w=30, h=30, bgc=[1.0, 1.0, 0.0], c=lambda *x: override_color(17))
    cmds.button(label="", p=color_button_layout_4, w=30, h=30, bgc=[0.0, 0.9, 0.9], c=lambda *x: override_color(18))
    cmds.button(label="", p=color_button_layout_4, w=30, h=30, bgc=[0.3, 1.0, 0.6], c=lambda *x: override_color(19))
    cmds.button(label="", p=color_button_layout_4, w=30, h=30, bgc=[1.0, 0.7, 0.7], c=lambda *x: override_color(20))
    cmds.button(label="", p=color_button_layout_4, w=30, h=30, bgc=[1.0, 0.7, 0.4], c=lambda *x: override_color(21))

    color_button_layout_5 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_5, w=30, h=30, bgc=[1.0, 1.0, 0.3], c=lambda *x: override_color(22))
    cmds.button(label="", p=color_button_layout_5, w=30, h=30, bgc=[0.7, 0.2, 0.4], c=lambda *x: override_color(31))
    cmds.button(label="", p=color_button_layout_5, w=30, h=30, bgc=[0.8, 0.5, 0.3], c=lambda *x: override_color(24))
    cmds.button(label="", p=color_button_layout_5, w=30, h=30, bgc=[0.6, 0.6, 0.2], c=lambda *x: override_color(25))
    cmds.button(label="", p=color_button_layout_5, w=30, h=30, bgc=[0.5, 0.7, 0.0], c=lambda *x: override_color(26))

    color_button_layout_6 = cmds.columnLayout(parent=change_color_layout,
                                              width=30,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=3)

    cmds.button(label="", p=color_button_layout_6, w=30, h=30, bgc=[0.0, 0.8, 0.4], c=lambda *x: override_color(27))
    cmds.button(label="", p=color_button_layout_6, w=30, h=30, bgc=[0.0, 0.7, 0.7], c=lambda *x: override_color(28))
    cmds.button(label="", p=color_button_layout_6, w=30, h=30, bgc=[0.0, 0.5, 0.6], c=lambda *x: override_color(29))
    cmds.button(label="", p=color_button_layout_6, w=30, h=30, bgc=[0.5, 0.2, 0.6], c=lambda *x: override_color(30))
    cmds.button(label="R", p=color_button_layout_6, w=30, h=30, c=lambda *x: override_color(0))

    cmds.showWindow("ND_Color_ID_ND")
