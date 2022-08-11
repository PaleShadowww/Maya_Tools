import maya.cmds as cmds
import os
import sys
import json


def get_image(name):
    dn = os.path.dirname(os.path.realpath(__file__))  # script's path
    return os.path.join(dn, 'icons', 'DN_Controller_%s.png' % name)  # take imagine in icon folder


def run():
    if cmds.window("ND_Controller_ID", exists=1):
        cmds.deleteUI("ND_Controller_ID")
    if cmds.windowPref("ND_Controller_ID", exists=True):
        cmds.windowPref("ND_Controller_ID", remove=True)
    # main window
    cmds.window('ND_Controller_ID', title='ND_Controller', width=600, height=500, toolbox=False, sizeable=False)
    main_layout = cmds.columnLayout(rowSpacing=0)

    all_curve_layout = cmds.rowLayout(numberOfColumns=3, width=645, height=280,
                                      columnAttach3=['left', 'right', 'both'],
                                      columnOffset3=[10, 0, 10])

    curve_layout_1 = cmds.rowLayout(numberOfColumns=3,
                                    parent=all_curve_layout,
                                    columnAttach3=['both', 'both', 'both'],
                                    columnOffset3=[0, 0, 0])
    # curves button layout
    button_layout_1 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('Cylinder'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('Cylinder'))
    cmds.symbolButton(i=get_image('Circle'), p=button_layout_1, w=50, h=50, c=lambda *x: create_circle())
    cmds.symbolButton(i=get_image('HalfSphere'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('HalfSphere'))
    cmds.symbolButton(i=get_image('HalfCircle'), p=button_layout_1, w=50, h=50, c=lambda *x: half_circle())
    cmds.symbolButton(i=get_image('Crescent_Moon'), p=button_layout_1, w=50, h=50, c=lambda *x: crescent_moon())

    button_layout_2 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('Locator'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('Locator'))
    cmds.symbolButton(i=get_image('Spiral'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('Spiral'))
    cmds.symbolButton(i=get_image('Cog'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('Cog'))
    cmds.symbolButton(i=get_image('Sphere'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('Sphere'))
    cmds.symbolButton(i=get_image('CirclePlus'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('CirclePlus'))

    button_layout_3 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('ArrowCross'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('ArrowCross'))
    cmds.symbolButton(i=get_image('PlusCircle'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('PlusCircle'))
    cmds.symbolButton(i=get_image('Plus'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Plus'))
    cmds.symbolButton(i=get_image('StarCircle'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('StarCircle'))
    cmds.symbolButton(i=get_image('StarCross'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('StarCross'))

    curve_layout_2 = cmds.rowLayout(numberOfColumns=4,
                                    parent=all_curve_layout,
                                    columnAttach4=['left', 'both', 'right', 'right'],
                                    columnOffset4=[0, 0, 0, 0])

    button_layout_4 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('Cube'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Cube'))
    cmds.symbolButton(i=get_image('Pyramid'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Pyramid'))
    cmds.symbolButton(i=get_image('Rhombus'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Rhombus'))
    cmds.symbolButton(i=get_image('SquareCircle'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('SquareCircle'))
    cmds.symbolButton(i=get_image('Square'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Square'))

    button_layout_5 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('ArrowArrow'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('ArrowArrow'))
    cmds.symbolButton(i=get_image('Triangle'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Triangle'))
    cmds.symbolButton(i=get_image('Nail'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Nail'))
    cmds.symbolButton(i=get_image('DoubleArrow'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('DoubleArrow'))
    cmds.symbolButton(i=get_image('Arrow'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Arrow'))

    button_layout_6 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('DoubleArrowSphere'), p=button_layout_6, w=50, h=50, c=lambda *x: create_proxy_curve('DoubleArrowSphere'))
    cmds.symbolButton(i=get_image('CrossArrowSphere'), p=button_layout_6, w=50, h=50, c=lambda *x: create_proxy_curve('CrossArrowSphere'))
    cmds.symbolButton(i=get_image('CrossArrowCircle'), p=button_layout_6, w=50, h=50, c=lambda *x: create_proxy_curve('CrossArrowCircle'))
    cmds.symbolButton(i=get_image('CrossArrow'), p=button_layout_6, w=50, h=50, c=lambda *x: create_proxy_curve('CrossArrow'))
    cmds.symbolButton(i=get_image('DoubleNailCross'), p=button_layout_6, w=50, h=50, c=lambda *x: create_proxy_curve('DoubleNailCross'))

    button_layout_7 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('RoundCross'), p=button_layout_7, w=50, h=50, c=lambda *x: create_proxy_curve('RoundCross'))
    cmds.symbolButton(i=get_image('DarkStar'), p=button_layout_7, w=50, h=50, c=lambda *x: create_proxy_curve('DarkStar'))
    cmds.symbolButton(i=get_image('Gear'), p=button_layout_7, w=50, h=50, c=lambda *x: create_proxy_curve('Gear'))
    cmds.symbolButton(i=get_image('GearCircle'), p=button_layout_7, w=50, h=50, c=lambda *x: create_proxy_curve('GearCircle'))
    cmds.button(l="More", p=button_layout_7, w=50, h=50, bgc=[0.0, 0.0, 0.0], c=lambda *x: more_ctrl())

    add_button_layout_3 = cmds.columnLayout(parent=all_curve_layout,
                                            width=350,
                                            height=300,
                                            columnAlign="center",
                                            columnOffset=["right", 5],
                                            rowSpacing=2)

    add_row_layout = cmds.rowLayout(numberOfColumns=6, parent=add_button_layout_3,
                                    width=330, height=30,
                                    columnAttach6=['left', 'left', 'left', 'left', 'left', 'left'],
                                    columnOffset6=[0, 0, 0, 0, 0, 0])
    # additional tools
    cmds.button(l="Loc", p=add_row_layout, w=30, h=30, sbm="Smart Locator", c=lambda *x: smart_locator())
    cmds.button(l="Extra", p=add_row_layout, w=30, h=30, sbm="Create  group above", c=lambda *x: make_extra_gr())
    cmds.button(l="Bot", p=add_row_layout, w=30, h=30, sbm="Create  group under", c=lambda *x: make_bot_gr())
    cmds.button(l="CurveC", p=add_row_layout, w=40, h=30, sbm="Get Curve Command", c=lambda *x: create_curve_command())
    cmds.button(l="Renamer", p=add_row_layout, w=48, h=30, sbm="Renamer", c=lambda *x: renamer())
    # cmds.button(l="Mirror", p=add_row_layout, w=40, h=30, sbm="Select all vertexes", vis=True, c=lambda *x: mirror_tool())
    cmds.button(label="Add", parent=add_row_layout,
                width=30, height=30,
                statusBarMessage="Source + Target_1 + Target_2 ... >> Add Shape",
                c=lambda *x: change_curve(0))

    move_opt_row_layout = cmds.rowLayout(numberOfColumns=2, parent=add_button_layout_3,
                                         width=320, height=30,
                                         columnAttach2=['left', 'left'],
                                         columnOffset2=[0, 0])
    # move tool
    cmds.checkBox('World', l='Move in World orientation', p=move_opt_row_layout, w=176, h=20)
    cmds.button(l="Reset", p=move_opt_row_layout, w=40, h=20, vis=0, sbm="Reset shape position",
                c=lambda *x: reset_shape_position())

    move_curve_layout = cmds.columnLayout(parent=add_button_layout_3,
                                          width=340,
                                          height=175,
                                          columnAlign="center",
                                          columnOffset=["right", 5],
                                          rowSpacing=3)

    move_x_buttons = cmds.rowLayout(numberOfColumns=3,
                                    parent=move_curve_layout,
                                    width=340,
                                    height=25,
                                    columnAttach3=['right', 'left', 'left'],
                                    columnOffset3=[15, 20, 30])

    cmds.text("Move Shape X", parent=move_x_buttons)
    cmds.button(label='-', parent=move_x_buttons, width=30, height=25, c=lambda *x: move_shape(-1, 0, 0))
    cmds.button(label='+', parent=move_x_buttons, width=30, height=25, c=lambda *x: move_shape(1, 0, 0))

    cmds.floatSliderGrp('move_curve_x_ID', parent=move_curve_layout,
                        min=0,
                        max=10,
                        value=2,
                        field=True,
                        enableKeyboardFocus=True,
                        width=220,
                        height=25)

    move_y_buttons = cmds.rowLayout(numberOfColumns=3,
                                    parent=move_curve_layout,
                                    width=340,
                                    height=25,
                                    columnAttach3=['right', 'left', 'left'],
                                    columnOffset3=[15, 20, 30])

    cmds.text("Move Shape Y", parent=move_y_buttons)
    cmds.button(label='-', parent=move_y_buttons, width=30, height=25, c=lambda *x: move_shape(0, -1, 0))
    cmds.button(label='+', parent=move_y_buttons, width=30, height=25, c=lambda *x: move_shape(0, 1, 0))

    cmds.floatSliderGrp('move_curve_y_ID', parent=move_curve_layout,
                        min=0,
                        max=10,
                        value=2,
                        field=True,
                        enableKeyboardFocus=True,
                        width=220,
                        height=25)

    move_z_buttons = cmds.rowLayout(numberOfColumns=3,
                                    parent=move_curve_layout,
                                    width=340,
                                    height=25,
                                    columnAttach3=['right', 'left', 'left'],
                                    columnOffset3=[15, 20, 30])

    cmds.text("Move Shape Z", parent=move_z_buttons)
    cmds.button(label='-', parent=move_z_buttons, width=30, height=25, c=lambda *x: move_shape(0, 0, -1))
    cmds.button(label='+', parent=move_z_buttons, width=30, height=25, c=lambda *x: move_shape(0, 0, 1))

    cmds.floatSliderGrp('move_curve_z_ID', parent=move_curve_layout,
                        min=0,
                        max=10,
                        value=2,
                        field=True,
                        enableKeyboardFocus=True,
                        width=220,
                        height=25)

    text_curve_layout = cmds.rowLayout(numberOfColumns=2,
                                       parent=add_button_layout_3,
                                       width=210,
                                       height=30,
                                       columnAttach2=['right', 'left'],
                                       columnOffset2=[0, 0])
    # Create curve text
    cmds.textField('Create_curve_text_ID', parent=text_curve_layout, placeholderText="Create curve text",
                   width=160,
                   height=30)

    cmds.button(label='Create', parent=text_curve_layout, width=40, height=23, c=lambda *x: create_curve_text())

    # options bot part

    all_options_layout = cmds.rowLayout(numberOfColumns=2,
                                        parent=main_layout,
                                        width=650,
                                        height=215,
                                        columnAttach2=['left', 'right'],
                                        columnOffset2=[0, 0])

    left_options_layout = cmds.columnLayout(parent=all_options_layout,
                                            width=300,
                                            height=215,
                                            columnAlign="center",
                                            columnOffset=["right", 0],
                                            rowSpacing=0)

    name_layout = cmds.rowLayout(numberOfColumns=3,
                                 parent=left_options_layout,
                                 width=720,
                                 height=70,
                                 columnAttach3=['left', 'right', 'right'],
                                 columnOffset3=[3, 5, 5])
    # Set curve's name
    cmds.text("Name:", parent=name_layout)
    cmds.textField("NewName_DN_ID",
                   placeholderText="Name of control",
                   width=175,
                   height=30,
                   parent=name_layout)

    checkbox_layout = cmds.columnLayout(parent=name_layout,
                                        width=90,
                                        height=70,
                                        columnAlign="center",
                                        columnOffset=["right", 15],
                                        rowSpacing=3)
    # curve creation options
    cmds.checkBox('Control', parent=checkbox_layout, width=70, height=20)
    cmds.checkBox('Group', parent=checkbox_layout, width=60, height=20)
    cmds.checkBox('Color', parent=checkbox_layout, width=60, height=20)

    change_thickness_layout = cmds.columnLayout(parent=left_options_layout,
                                                width=720,
                                                height=65,
                                                columnAlign="center",
                                                columnOffset=["both", 3],
                                                rowSpacing=3)
    # Change Thickness
    cmds.text("Change Thickness:", parent=change_thickness_layout)

    cmds.floatSliderGrp('Change_Thickness_ID', parent=change_thickness_layout,
                        changeCommand=lambda *x: change_thickness(),
                        field=True,
                        min=0.0,
                        max=10.0,
                        width=300,
                        height=30)

    change_size_layout = cmds.columnLayout(parent=left_options_layout,
                                           width=720,
                                           height=65,
                                           columnAlign="center",
                                           columnOffset=["both", 3],
                                           rowSpacing=0)

    size_opt_layout = cmds.rowLayout(numberOfColumns=6,
                                     parent=change_size_layout,
                                     width=300,
                                     height=25,
                                     columnAttach6=['right', 'right', 'right', 'right', 'right', 'right'],
                                     columnOffset6=[10, 0, 0, 25, 0, 0])
    # Change Size
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
                        width=300,
                        height=30,)

    right_options_layout = cmds.columnLayout(parent=all_options_layout,
                                             width=350,
                                             height=215,
                                             columnAlign="center",
                                             columnOffset=["right", 15],
                                             rowSpacing=0)

    flip_xyz_layout = cmds.rowLayout(numberOfColumns=5,
                                     parent=right_options_layout,
                                     width=350,
                                     height=32,
                                     columnAttach5=['left', 'both', 'right', 'right', 'left'],
                                     columnOffset5=[12, 4, 4, 4, 1])
    # Main curves edit tools
    cmds.button(label="All VTX", parent=flip_xyz_layout, width=60, height=30, c=lambda *x: select_all_vtx(),
                statusBarMessage="Select all vertexes")
    cmds.button(label="X", parent=flip_xyz_layout, width=60, height=30, c=lambda *x: turn_curve(90, 0, 0))
    cmds.button(label="Y", parent=flip_xyz_layout, width=60, height=30, c=lambda *x: turn_curve(0, 90, 0))
    cmds.button(label="Z", parent=flip_xyz_layout, width=60, height=30, c=lambda *x: turn_curve(0, 0, 90))
    cmds.button(l="Mirror", p=flip_xyz_layout, w=60, h=30, vis=True, c=lambda *x: mirror_tool())

    colorise_layout = cmds.columnLayout(parent=right_options_layout,
                                        width=350,
                                        height=175,
                                        columnAlign="center",
                                        columnOffset=["right", 5],
                                        rowSpacing=0)

    change_color = cmds.rowLayout(parent=colorise_layout,
                                  numberOfColumns=6,
                                  width=340,
                                  height=180,
                                  columnAttach6=['left', 'right', 'both', 'both', 'both', 'both'],
                                  columnOffset6=[10, 0, 0, 0, 0, 0])

    color_button_layout_1 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)
    # color palette
    cmds.button(label="", p=color_button_layout_1, w=50, h=30, bgc=[0.0, 0.0, 0.0], c=lambda *x: override_color(1))
    cmds.button(label="", p=color_button_layout_1, w=50, h=30, bgc=[0.5, 0.5, 0.5], c=lambda *x: override_color(3))
    cmds.button(label="", p=color_button_layout_1, w=50, h=30, bgc=[0.6, 0.0, 0.0], c=lambda *x: override_color(4))
    cmds.button(label="", p=color_button_layout_1, w=50, h=30, bgc=[0.0, 0.0, 0.5], c=lambda *x: override_color(5))
    cmds.button(label="", p=color_button_layout_1, w=50, h=30, bgc=[0.0, 0.0, 0.9], c=lambda *x: override_color(6))

    color_button_layout_2 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)

    cmds.button(label="", p=color_button_layout_2, w=50, h=30, bgc=[0.0, 0.3, 0.0], c=lambda *x: override_color(7))
    cmds.button(label="", p=color_button_layout_2, w=50, h=30, bgc=[0.1, 0.0, 0.3], c=lambda *x: override_color(8))
    cmds.button(label="", p=color_button_layout_2, w=50, h=30, bgc=[0.8, 0.2, 0.7], c=lambda *x: override_color(9))
    cmds.button(label="", p=color_button_layout_2, w=50, h=30, bgc=[0.6, 0.3, 0.2], c=lambda *x: override_color(10))
    cmds.button(label="", p=color_button_layout_2, w=50, h=30, bgc=[0.4, 0.2, 0.2], c=lambda *x: override_color(11))

    color_button_layout_3 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)

    cmds.button(label="", p=color_button_layout_3, w=50, h=30, bgc=[0.8, 0.2, 0.0], c=lambda *x: override_color(12))
    cmds.button(label="", p=color_button_layout_3, w=50, h=30, bgc=[1.0, 0.0, 0.0], c=lambda *x: override_color(13))
    cmds.button(label="", p=color_button_layout_3, w=50, h=30, bgc=[0.0, 1.0, 0.0], c=lambda *x: override_color(14))
    cmds.button(label="", p=color_button_layout_3, w=50, h=30, bgc=[0.2, 0.2, 0.7], c=lambda *x: override_color(15))
    cmds.button(label="", p=color_button_layout_3, w=50, h=30, bgc=[1.0, 1.0, 1.0], c=lambda *x: override_color(16))

    color_button_layout_4 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)

    cmds.button(label="", p=color_button_layout_4, w=50, h=30, bgc=[1.0, 1.0, 0.0], c=lambda *x: override_color(17))
    cmds.button(label="", p=color_button_layout_4, w=50, h=30, bgc=[0.0, 0.9, 0.9], c=lambda *x: override_color(18))
    cmds.button(label="", p=color_button_layout_4, w=50, h=30, bgc=[0.3, 1.0, 0.6], c=lambda *x: override_color(19))
    cmds.button(label="", p=color_button_layout_4, w=50, h=30, bgc=[1.0, 0.7, 0.7], c=lambda *x: override_color(20))
    cmds.button(label="", p=color_button_layout_4, w=50, h=30, bgc=[1.0, 0.7, 0.4], c=lambda *x: override_color(21))

    color_button_layout_5 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)

    cmds.button(label="", p=color_button_layout_5, w=50, h=30, bgc=[1.0, 1.0, 0.3], c=lambda *x: override_color(22))
    cmds.button(label="", p=color_button_layout_5, w=50, h=30, bgc=[0.7, 0.2, 0.4], c=lambda *x: override_color(31))
    cmds.button(label="", p=color_button_layout_5, w=50, h=30, bgc=[0.8, 0.5, 0.3], c=lambda *x: override_color(24))
    cmds.button(label="", p=color_button_layout_5, w=50, h=30, bgc=[0.6, 0.6, 0.2], c=lambda *x: override_color(25))
    cmds.button(label="", p=color_button_layout_5, w=50, h=30, bgc=[0.5, 0.7, 0.0], c=lambda *x: override_color(26))

    color_button_layout_6 = cmds.columnLayout(parent=change_color,
                                              width=53,
                                              height=175,
                                              columnAlign="center",
                                              columnOffset=["right", 0],
                                              rowSpacing=5)

    cmds.button(label="", p=color_button_layout_6, w=50, h=30, bgc=[0.0, 0.8, 0.4], c=lambda *x: override_color(27))
    cmds.button(label="", p=color_button_layout_6, w=50, h=30, bgc=[0.0, 0.7, 0.7], c=lambda *x: override_color(28))
    cmds.button(label="", p=color_button_layout_6, w=50, h=30, bgc=[0.0, 0.5, 0.6], c=lambda *x: override_color(29))
    cmds.button(label="", p=color_button_layout_6, w=50, h=30, bgc=[0.5, 0.2, 0.6], c=lambda *x: override_color(30))
    cmds.button(label="R", p=color_button_layout_6, w=50, h=30, c=lambda *x: override_color(0))

    curve_comm_layout = cmds.columnLayout(parent=main_layout,
                                          width=650,
                                          height=35,
                                          columnAlign="center",
                                          columnOffset=["both", 0],
                                          rowSpacing=3)

    curve_comm_row_layout = cmds.rowLayout(parent=curve_comm_layout,
                                           numberOfColumns=3,
                                           width=650,
                                           height=30,
                                           columnAttach3=['left', 'left', 'both'],
                                           columnOffset3=[7, 0, 0])

    save_curve_layout = cmds.columnLayout(parent=curve_comm_row_layout,
                                          width=210,
                                          height=30,
                                          #bgc=[0.1, 0.7, 0.6],
                                          columnAlign="center",
                                          columnOffset=["both", 0],
                                          rowSpacing=3)
    # Curve saver
    cmds.button(label="Save Curve", parent=save_curve_layout,
                width=205, height=30, c=lambda *x: save_curve())

    change_curve_layout = cmds.columnLayout(parent=curve_comm_row_layout,
                                            width=210,
                                            height=30,
                                            #bgc=[0.5, 0.2, 0.6],
                                            columnAlign="center",
                                            columnOffset=["both", 0],
                                            rowSpacing=3)
    # Change Curve
    cmds.button(label="Change Curve", parent=change_curve_layout,
                width=205, height=30,
                statusBarMessage="Source + Target_1 + Target_2 ... >> Change",
                c=lambda *x: change_curve(1))
    combine_curve_layout = cmds.columnLayout(parent=curve_comm_row_layout,
                                             width=210,
                                             height=30,
                                             columnAlign="center",
                                             columnOffset=["both", 0],
                                             rowSpacing=3)
    # Combine Curve
    cmds.button(label="Combine Curve", parent=combine_curve_layout,
                width=205, height=30, statusBarMessage="Source_1 + Source_2 ... + Target >> Combine",
                c=lambda *x: combine_curve())

    cmds.showWindow("ND_Controller_ID")


def more_ctrl():
    if cmds.window("ND_Controller_More_ID", exists=1):
        cmds.deleteUI("ND_Controller_More_ID")
    if cmds.windowPref("ND_Controller_More_ID", exists=True):
        cmds.windowPref("ND_Controller_More_ID", remove=True)
    # extra controls window
    cmds.window('ND_Controller_More_ID', title='ND_Controller_More_Controls', w=250, h=250, toolbox=True, sizeable=False)

    main_layout = cmds.columnLayout(rowSpacing=0)

    all_curve_layout = cmds.rowLayout(numberOfColumns=3, width=295, height=280,
                                      columnAttach3=['left', 'right', 'both'],
                                      columnOffset3=[0, 0, 10])

    curve_layout_1 = cmds.rowLayout(numberOfColumns=3,
                                    parent=all_curve_layout,
                                    columnAttach3=['both', 'both', 'both'],
                                    columnOffset3=[0, 0, 0])

    button_layout_1 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('BrightStar'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('BrightStar'))
    cmds.symbolButton(i=get_image('Flower'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('Flower'))
    cmds.symbolButton(i=get_image('Arc'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('Arc'))
    cmds.symbolButton(i=get_image('DoubleNail'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('DoubleNail'))
    cmds.symbolButton(i=get_image('GearMech'), p=button_layout_1, w=50, h=50, c=lambda *x: create_proxy_curve('GearMech'))

    button_layout_2 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('Ring'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('Ring'))
    cmds.symbolButton(i=get_image('CircleArrow'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('CircleArrow'))
    cmds.symbolButton(i=get_image('HalfCircleArrow'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('HalfCircleArrow'))
    cmds.symbolButton(i=get_image('QuarterArrow'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('QuarterArrow'))
    cmds.symbolButton(i=get_image('TArrow'), p=button_layout_2, w=50, h=50, c=lambda *x: create_proxy_curve('TArrow'))

    button_layout_3 = cmds.columnLayout(parent=curve_layout_1,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('Star'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Star'))
    cmds.symbolButton(i=get_image('Frame'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Frame'))
    cmds.symbolButton(i=get_image('Corner'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Corner'))
    cmds.symbolButton(i=get_image('Heart'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Heart'))
    cmds.symbolButton(i=get_image('Spring'), p=button_layout_3, w=50, h=50, c=lambda *x: create_proxy_curve('Spring'))

    curve_layout_2 = cmds.rowLayout(numberOfColumns=4,
                                    parent=all_curve_layout,
                                    columnAttach4=['left', 'both', 'right', 'right'],
                                    columnOffset4=[0, 0, 0, 0])

    button_layout_4 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('NailCross'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('NailCross'))
    cmds.symbolButton(i=get_image('ArrowHead'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('ArrowHead'))
    cmds.symbolButton(i=get_image('ArrowDot'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('ArrowDot'))
    cmds.symbolButton(i=get_image('Arrow3'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Arrow3'))
    cmds.symbolButton(i=get_image('Platonic'), p=button_layout_4, w=50, h=50, c=lambda *x: create_proxy_curve('Platonic'))

    button_layout_5 = cmds.columnLayout(parent=curve_layout_2,
                                        width=55,
                                        height=300,
                                        columnAlign="center",
                                        columnOffset=["both", 5],
                                        rowSpacing=5)

    cmds.symbolButton(i=get_image('GearTech'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('GearTech'))
    cmds.symbolButton(i=get_image('Cone'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Cone'))
    cmds.symbolButton(i=get_image('CircleCube'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('CircleCube'))
    cmds.symbolButton(i=get_image('Pow'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Pow'))
    cmds.symbolButton(i=get_image('Snowflake'), p=button_layout_5, w=50, h=50, c=lambda *x: create_proxy_curve('Snowflake'))

    cmds.showWindow("ND_Controller_More_ID")


def add_to_all():
    add_text = cmds.textField("NewName_ND_ID", query=True, text=True)
    selected_obj = cmds.ls(sl=True)
    if "*" in add_text:
        for i in selected_obj:
            new_name = add_text.replace("*", str(i))
            cmds.rename(i, new_name)  # Change name of selected Object in list
        cmds.textField("NewName_ND_ID", edit=True, text="")  # Clear expField


def remove_from_all():
    remove_text = cmds.textField("NewName_ND_ID", query=True, text=True)
    selected_obj = cmds.ls(sl=True)
    for i in selected_obj:
        obj_name = i.split("|")[-1]  # Get name objects
        if remove_text in obj_name:  # Check remove_text in name of selected objects
            new_name = obj_name.replace(remove_text, '')  # Replace remove_text on '' in name of object
            cmds.rename(i, new_name)  # Change name of selected Object in list
    cmds.textField("NewName_ND_ID", edit=True, text="")  # Clear expField


def renamer():
    if cmds.window("Renamer_ND_ID", exists=1):
        cmds.deleteUI("Renamer_ND_ID")
    if cmds.windowPref("Renamer_ND_ID", exists=True):
        cmds.windowPref("Renamer_ND_ID", remove=True)
    cmds.window("Renamer_ND_ID", title="ND_Renamer", width=250, tlb=True)
    main_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=15)
    # renameLayout
    rename_layout = cmds.columnLayout(adjustableColumn=True,  # Able to change size
                                      columnAlign="left",  # Align to left side
                                      columnOffset=["both", 10],  # Offset by borders
                                      rowSpacing=5,  # Space between elements
                                      statusBarMessage="New name",  # Translucent words in bar
                                      parent=main_layout)

    cmds.text("Rename:", parent=rename_layout)  # Name  function
    cmds.textField("NewName_ND_ID", placeholderText="Use '*' as an original name", parent=rename_layout)
    # Scroll list
    scroll_layout = cmds.scrollLayout(childResizable=1, parent=main_layout)  # List objects
    #  Layout for list objects
    cmds.columnLayout(parent=scroll_layout, adjustableColumn=True, rowSpacing=1, columnOffset=["both", 10])
    selected_obj = cmds.ls(sl=True)

    for i in selected_obj:
        cmds.nameField(o=i)  # Change name from list
    buttons_layout = cmds.columnLayout(parent=main_layout, rowSpacing=3, adj=True)  # Layout for buttons
    cmds.button(label="Add", parent=buttons_layout, c=lambda *x: add_to_all())
    cmds.button(label="Remove", parent=buttons_layout, c=lambda *x: remove_from_all())
    cmds.button(label="Cancel", parent=buttons_layout, c="cmds.deleteUI(\"Renamer_ND_ID\")")
    cmds.showWindow("Renamer_ND_ID")


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
    if cmds.window("Mirror_Tool_ND_ID", exists=1):
        cmds.deleteUI("Mirror_Tool_ND_ID")
    if cmds.windowPref("Mirror_Tool_ND_ID", exists=True):
        cmds.windowPref("Mirror_Tool_ND_ID", remove=True)
    cmds.window("Mirror_Tool_ND_ID", title="ND_Mirror_Tool", width=330, tlb=True)
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
    # field to left marker
    cmds.textField("L_Marker_ND_ID", parent=mirror_marker_l_layout,  width=250, pht='Prefix_|_mid_|_suffix')

    mirror_marker_r_layout = cmds.rowLayout(numberOfColumns=2,
                                            parent=mirror_markers_layout,
                                            width=280,
                                            h=25,
                                            columnAttach2=['left', 'right'],
                                            columnOffset2=[12, 0])

    cmds.text("R Marker", parent=mirror_marker_r_layout)
    # field to left marker
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
    scroll_source_target(False)  # create interface targets list as scroll

    buttons_layout = cmds.columnLayout(parent=main_layout, rowSpacing=20, adj=True)
    # Update interface targets list after changes
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

    # cmds.button(label="Cancel", parent=buttons_layout, c="cmds.deleteUI(\"Mirror_Tool_ND_ID\")")
    cmds.showWindow("Mirror_Tool_ND_ID")


def scroll_source_target(delete):  # Create or update interface targets list after changes
    if delete == True and cmds.columnLayout('Scroll_Source_Target_ND_ID', exists=True):
        cmds.deleteUI("Scroll_Source_Target_ND_ID")  # delete scroll targets list before create new interface
    source_list = cmds.ls(sl=True)  # list current objects
    target_list = produce_target_list(source_list)  # create list target objects base on list current objects
    # Create interface
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
    source_list = source_list  # list current objects
    # lists base markers
    left_prefix_list =  ['L_', 'l_', 'Left_', 'left_']
    right_prefix_list = ['R_', 'r_', 'Right_', 'right_']

    left_mid_list =  ['_L_', '_l_', '_Left_', '_left_']
    right_mid_list = ['_R_', '_r_', '_Right_', '_right_']

    left_suffix_list =  ['_L', '_l', '_Left', '_left']
    right_suffix_list = ['_R', '_r', '_Right', '_right']
    # set custom markers
    custom_l_marker_list = cmds.textField("L_Marker_ND_ID", q=True, text=True)
    custom_r_marker_list = cmds.textField("R_Marker_ND_ID", q=True, text=True)

    c_m_index = 0
    # put custom markers in appropriate marker's list
    if custom_l_marker_list and custom_r_marker_list:
        if '|' in custom_l_marker_list and '|' in custom_r_marker_list:  # separate several custom markers
            custom_l_marker_list = custom_l_marker_list.split('|')
            custom_r_marker_list = custom_r_marker_list.split('|')
        else:
            custom_l_marker_list = [custom_l_marker_list]
            custom_r_marker_list = [custom_r_marker_list]

        for custom_l_marker in custom_l_marker_list:  # Find and put marker in appropriate marker's list
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
    # find opposite marker's list
    for source in source_list:
        source_marker = ''
        if cmds.radioButton('Mirror_L', q=True, select=True):  # from left to right
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

        else:  # from right to left
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
    # find object name in scene with opposite marker
    for target_mark in target_marker_list:
        if target_mark == '':
            target = 'Not_Exist_Element_ND_ID'  # if object haven't mirror target
        else:
            source = source_list[index]  # take name source object
            target = source.replace(source_marker_list[index], target_mark)  # create name target object
            target_path = cmds.ls(target, o=True, l=True)  # take path for check
            source_path = cmds.ls(source, o=True, l=True)
        index += 1
        if source_path != [] and target_path != []:  # take list objects to find hierarchy length
            source_path = source_path[0].split('|')
            target_path = target_path[0].split('|')
        if cmds.checkBox('Hierarchy', q=True, v=True):  # obligation or not check of hierarchy length
            # checking existing targets and equal hierarchies
            if cmds.objExists(target) and len(target_path) == len(source_path):
                target_list.append(target)
            else:
                target_list.append('Self')
        else:
            # checking only existing targets
            if cmds.objExists(target):
                target_list.append(target)
            else:
                target_list.append('Self')
    # print finals lists of markers
    print (left_prefix_list)
    print (right_prefix_list)
    print (left_mid_list)
    print (right_mid_list)
    print (left_suffix_list)
    print (right_suffix_list)
    # print finals lists of sources and targets
    print (source_list)
    print (target_list)

    return target_list


def save_curve():
    if cmds.window("ND_Save_Curve_ID_ND", exists=1):
        cmds.deleteUI("ND_Save_Curve_ID_ND")
    if cmds.windowPref("ND_Save_Curve_ID_ND", exists=True):
        cmds.windowPref("ND_Save_Curve_ID_ND", remove=True)
    cmds.window('ND_Save_Curve_ID_ND', title='ND_Curve_Saver', w=300, h=410, toolbox=True, sizeable=False)
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

    cmds.showWindow("ND_Save_Curve_ID_ND")


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
    create_curve(None)


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


# def save_json(file_name, data):
#     print('save: %s' % file_name)
#     with open(file_name, 'w') as file:
#         file.write(json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True))


# def load_json(file_name):
#     with codecs.open(file_name, "r", "utf-8") as file:
#         shapes_json = file.read()
#     result = json.loads(shapes_json)
#     return result


def create_curve_command():
    sel_list = cmds.ls(sl=True, o=True)
    for sel in sel_list:
        sel_shape = cmds.listRelatives(sel, s=True)[0]
        degree = str(cmds.getAttr(sel_shape + ".degree"))
        sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
        cmds.select(sel_vtx)
        i = 0
        all_vtx_list = []
        for vtx in sel_vtx:
            cmds.select(vtx)
            x = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].xValue'))
            y = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].yValue'))
            z = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].zValue'))
            all_vtx_list.append((x, y, z))
            i += 1
        print (all_vtx_list)
        # print (str('cmds.curve(d=' + degree + ', n="' + sel + '", p=' + all_vtx_list + ')'))
        sys.stdout.write(str('cmds.curve(d=' + degree + ', n="' + sel + '", p=' + str(all_vtx_list) + ')'))
    cmds.select(sel_list)


def create_curve_text():
    text = cmds.textField("Create_curve_text_ID", query=True, text=True)
    if text:
        cmds.textCurves(t=text)
    top_gr = cmds.ls(sl=True)[0]
    cmds.xform(top_gr, r=True, s=(5, 5, 5), os=True)
    cmds.makeIdentity(top_gr, apply=True, t=True, r=True, s=True, n=0)
    cmds.select(top_gr, hi=True)
    text_gr = cmds.ls(sl=True)
    curve_text = []
    for curve in text_gr:
        if cmds.nodeType(curve) == 'nurbsCurve':
            curve_tran = cmds.listRelatives(curve, parent=True)[0]
            cmds.parent(curve_tran, w=True)
            cmds.makeIdentity(curve, apply=True, t=True, r=True, s=True, n=0)
            curve_text.append(curve_tran)
    cmds.delete(top_gr)
    cmds.select(curve_text, curve_text[0])
    combine_curve()
    cmds.rename(curve_text[0], text+'_txt')
    cmds.select(text+'_txt')


def combine_curve():
    change_ls = cmds.ls(sl=True)
    if len(change_ls) >= 2:
        new_control = change_ls[-1]
        change_ls.remove(new_control)
        for curve in change_ls:
            base_shape = cmds.listRelatives(curve, s=True)[0]
            cmds.makeIdentity(curve, apply=True, t=True, r=True, s=True, n=0)
            cmds.makeIdentity(new_control, apply=True, t=True, r=True, s=True, n=0)
            cmds.parent(base_shape, new_control, s=True, relative=True)
            cmds.delete(curve)


def change_curve(end):
    targets_ls = cmds.ls(sl=True)
    if len(targets_ls) >= 2:
        source = targets_ls[0]
        targets_ls.remove(source)
        for curve in targets_ls:
            target_shape = cmds.listRelatives(curve, s=True)
            source_shape = cmds.listRelatives(source, s=True)[0]
            set_width = cmds.getAttr(source_shape+".lineWidth")
            cmds.duplicateCurve(source_shape, name='Source_Curve_ND', constructionHistory=False)
            list_sets = cmds.listSets(object=target_shape[0])
            cmds.parent('Source_Curve_NDShape', curve, shape=True, relative=True)
            cmds.delete('Source_Curve_ND')
            save_color_shape('Source_Curve_NDShape', target_shape)
            if end == 1:
                cmds.delete(target_shape)
            cmds.setAttr("Source_Curve_NDShape.lineWidth", set_width)
            cmds.rename('Source_Curve_NDShape', curve + 'Shape')
            new_shape = cmds.ls(sl=True)
            if list_sets:
                for in_set in list_sets:
                    cmds.sets(new_shape, add=in_set)
            cmds.select(curve)


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


def reset_shape_position():
    curve = cmds.ls(sl=True)
    locator = cmds.spaceLocator(n='Locator_Reset_Pos_ND_ID')
    cmds.matchTransform(locator, curve)
    tx = cmds.getAttr('Locator_Reset_Pos_ND_ID.translateX')
    ty = cmds.getAttr('Locator_Reset_Pos_ND_ID.translateY')
    tz = cmds.getAttr('Locator_Reset_Pos_ND_ID.translateZ')
    cmds.select(curve)
    select_all_vtx()
    cmds.xform(r=True, t=(tx, ty, tz), p=True, ws=True)
    cmds.select(curve)


def move_shape(x, y, z):
    sel_curves = cmds.ls(sl=True, o=True)
    move_x = x * (cmds.floatSliderGrp("move_curve_x_ID", query=True, value=True))
    move_y = y * (cmds.floatSliderGrp("move_curve_y_ID", query=True, value=True))
    move_z = z * (cmds.floatSliderGrp("move_curve_z_ID", query=True, value=True))
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
            cmds.setAttr(color + '.overrideRGBColors', False)
            cmds.setAttr(color + ".overrideEnabled", True)
            cmds.setAttr(color + ".overrideColor", color_index)


def set_name():
    control = cmds.ls(sl=True)
    new_name = cmds.textField("NewName_DN_ID", query=True, text=True)
    cmds.rename(control, new_name)


def smart_locator():
    list_objects = cmds.ls(sl=True)
    if list_objects:
        for main_object in list_objects:
            locator = cmds.spaceLocator(n='Locator_ND')
            if cmds.objectType(main_object) != "joint":
                bbox = cmds.exactWorldBoundingBox(main_object)
                loc_size = (bbox[3] - bbox[0]) * 0.77
                cmds.setAttr('Locator_NDShape.localScaleX', loc_size)
                cmds.setAttr('Locator_NDShape.localScaleY', loc_size)
                cmds.setAttr('Locator_NDShape.localScaleZ', loc_size)
            cmds.matchTransform(locator, main_object)
            cmds.select(locator)
            cmds.rename(locator, "locator1")
    else:
        cmds.spaceLocator()


def make_extra_gr():
    obj_list = cmds.ls(sl=True)
    if obj_list:
        for obj in obj_list:
            i = 1
            while cmds.objExists(obj + '_' + str(i) + '_extra'):
                i += 1
            cmds.group(em=True, n=obj + '_' + str(i) + '_extra')
            cmds.matchTransform(obj + '_' + str(i) + '_extra', obj, scl=False)
            up = cmds.listRelatives(obj, parent=1, fullPath=1)[0]
            cmds.parent(obj + '_' + str(i) + '_extra', up)
            cmds.reorder(obj + '_' + str(i) + '_extra', relative=i)
            cmds.parent(obj, obj + '_' + str(i) + '_extra')
    cmds.select(obj_list)


def make_bot_gr():
    obj_list = cmds.ls(sl=True)
    if obj_list:
        for obj in obj_list:
            i = 1
            while cmds.objExists(obj + '_' + str(i) + '_bot'):
                i += 1
            cmds.group(em=True, n=obj + '_' + str(i) + '_bot')
            cmds.matchTransform(obj + '_' + str(i) + '_bot', obj, scl=False)
            cmds.parent(obj + '_' + str(i) + '_bot', obj)
            cmds.reorder(obj + '_' + str(i) + '_bot', relative=i)
    cmds.select(obj_list)


def make_control_group_over(proxy_curve, curve_name):
    cmds.rename(proxy_curve, curve_name + "_over_ctrl")
    cmds.group(em=True, n=curve_name + '_over_gr')
    cmds.group(em=True, n=curve_name + '_over_extra')
    cmds.parent(curve_name + '_over_extra', curve_name + '_over_gr')
    cmds.group(em=True, n=curve_name + '_over_loc')
    cmds.parent(curve_name + '_over_loc', curve_name + "_over_ctrl")
    cmds.matchTransform(curve_name + '_over_gr', curve_name + "_over_ctrl", scl=False)
    cmds.matchTransform(curve_name + '_over_loc', curve_name + "_over_ctrl", scl=False)
    cmds.parent(curve_name + "_over_ctrl", curve_name + '_over_extra')


def make_control_group(new_control, curve_name, new_proxy_shape):
    cmds.rename(new_control, curve_name + "_ctrl")
    cmds.rename(new_proxy_shape, curve_name + "Shape")
    cmds.group(em=True, n=curve_name + '_gr')
    cmds.group(em=True, n=curve_name + '_extra')
    cmds.parent(curve_name + '_extra', curve_name + '_gr')
    cmds.parent(curve_name + '_ctrl', curve_name + '_extra')
    cmds.group(em=True, n=curve_name + '_loc')
    cmds.parent(curve_name + '_loc', curve_name + '_ctrl')
    cmds.select(curve_name + '_ctrl')


def save_selections_sets(proxy_shape, old_shape):
    list_sets = cmds.listSets(object=old_shape[0])
    if list_sets:
        for sel_set in list_sets:
            cmds.sets(proxy_shape, add=sel_set)


def save_color_shape(proxy_shape, old_shape):
    cmds.setAttr(proxy_shape + ".overrideEnabled", True)
    if cmds.getAttr(old_shape[0] + '.overrideRGBColors'):
        color_rgb = cmds.getAttr(old_shape[0] + ".overrideColorRGB")
        cmds.setAttr(proxy_shape + '.overrideRGBColors', True)
        cmds.setAttr(proxy_shape + '.overrideColorR', color_rgb[0][0])
        cmds.setAttr(proxy_shape + '.overrideColorG', color_rgb[0][1])
        cmds.setAttr(proxy_shape + '.overrideColorB', color_rgb[0][2])
    else:
        color_index = cmds.getAttr(old_shape[0] + ".overrideColor")
        cmds.setAttr(proxy_shape + ".overrideColor", color_index)


def create_curve(type_ctrl):
    control_ls = cmds.ls(sl=True)
    if len(control_ls) >= 2:
        new_control = control_ls[-1]
        control_ls.remove(new_control)
        for curve in control_ls:
            old_shape = cmds.listRelatives(curve, s=True)
            cmds.duplicateCurve(new_control, n='Proxy_Curve_Control_IDND', ch=False)
            proxy_curve = cmds.ls(sl=True)
            proxy_shape = cmds.listRelatives('Proxy_Curve_Control_IDND', s=True)[0]
            # set color from target
            if cmds.checkBox('Color', q=True, v=True):
                save_color_shape(proxy_shape, old_shape)
            # check text in text field
            if cmds.textField("NewName_DN_ID", q=True, text=True) and len(control_ls) == 1:
                target_curve_name = cmds.textField("NewName_DN_ID", q=True, text=True)
            else:
                target_curve_name = curve.split("|")[-1]
            # make control in group
            if cmds.checkBox('Group', q=True, v=True) and cmds.checkBox('Control', q=True, v=True):
                cmds.matchTransform(proxy_curve, curve)
                make_control_group_over(proxy_curve, target_curve_name)
            # make only control
            elif cmds.checkBox('Control', q=True, v=True):
                cmds.matchTransform(proxy_curve, curve)
                cmds.rename(proxy_curve, target_curve_name+"_over")
            else:
                curve_name = curve.split("|")[-1]
                save_selections_sets(proxy_shape, old_shape)
                save_color_shape(proxy_shape, old_shape)
                loc_pivot = cmds.xform(curve, q=True, pivots=True, r=True)
                cmds.setAttr('Proxy_Curve_Control_IDND.translateX', loc_pivot[0])
                cmds.setAttr('Proxy_Curve_Control_IDND.translateY', loc_pivot[1])
                cmds.setAttr('Proxy_Curve_Control_IDND.translateZ', loc_pivot[2])
                cmds.makeIdentity('Proxy_Curve_Control_IDND', apply=True, t=True, r=True, s=True, n=0)
                cmds.parent(proxy_shape, curve, shape=True, r=True)
                cmds.delete(old_shape)
                cmds.rename(proxy_shape, curve_name + "Shape")
                cmds.delete(proxy_curve)
                sel_vtx = cmds.ls('{}.controlPoints[:]'.format(curve_name + "Shape"), fl=True)
                cmds.select(sel_vtx)
                # cmds.matchTransform(sel_vtx, curve, scl=False)
        cmds.delete(new_control)
        cmds.select(control_ls)
    elif cmds.checkBox('Group', q=True, v=True) and cmds.checkBox('Control', q=True, v=True):
        new_control = control_ls[-1]
        if cmds.textField("NewName_DN_ID", q=True, text=True):
            curve_name = cmds.textField("NewName_DN_ID", q=True, text=True)
        else:
            curve_name = new_control.split("_")[0]
        new_proxy_shape = cmds.listRelatives(new_control, s=True)[0]
        make_control_group(new_control, curve_name, new_proxy_shape)
    else:
        new_control = control_ls[-1]
        control_shape = cmds.listRelatives(new_control, s=True)[0]
        if cmds.textField("NewName_DN_ID", q=True, text=True):
            curve_name = cmds.textField("NewName_DN_ID", q=True, text=True)
        else:
            curve_name = new_control.split("_")[0]
        cmds.rename(new_control, curve_name)
        if control_shape != 'Demilune_ctrlShape' \
                and control_shape != 'Circle_ctrlShape' \
                and control_shape != 'HalfCircle_ctrlShape':
            cmds.rename(control_shape, curve_name+'Shape')


def create_proxy_curve(curve):
    if curve not in shapes_list:
        print('Name %s not found' % curve)
        return
    control = cmds.ls(sl=True)
    ctrl = cmds.curve(d=shapes_list[curve]['d'], n=curve, p=shapes_list[curve]['p'])
    cmds.select(control, ctrl)
    create_curve(None)


def create_circle():
    control = cmds.ls(sl=True)
    ctrl = cmds.circle(n="Circle_ctrl", r=10, nr=[0, 1, 0])
    ctrl.remove(ctrl[1])
    cmds.select(control, ctrl)
    create_curve(None)


def half_circle():
    control = cmds.ls(sl=True)
    cmds.circle(n="Half_Circle_ctrl_ND_ID", r=10, nr=[0, 1, 0])
    sel = cmds.ls(sl=True, o=True)[0]
    points_x = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    points_y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    points_z = [0.0, 0.0, 0.0, 0.0, -7.8361, -11.0819, -7.8361, 0.0, 0.0, 0.0, 0.0]
    sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
    for index in range(len(sel_vtx)):
        cmds.setAttr('Half_Circle_ctrl_ND_ID.controlPoints[' + str(index) + '].xValue', points_x[index])
        cmds.setAttr('Half_Circle_ctrl_ND_ID.controlPoints[' + str(index) + '].yValue', points_y[index])
        cmds.setAttr('Half_Circle_ctrl_ND_ID.controlPoints[' + str(index) + '].zValue', points_z[index])
    cmds.rename(sel, "HalfCircle_ctrl")
    ctrl = cmds.ls(sl=True, o=True)[0]
    cmds.select(control, ctrl)
    create_curve(None)


def crescent_moon():
    control = cmds.ls(sl=True)
    cmds.circle(n="Demilune_ctrl_ND_ID", r=10, nr=[0, 1, 0])
    sel = cmds.ls(sl=True, o=True)[0]
    points_x = [0.3677, -0.0, -0.3825, -0.5159, -0.4242, -0.0, 0.4132, 0.4989, 0.0, 0.0, 0.0]
    points_y = [3.19, 6.0463, 3.1537, -1.9615, 6.2426, 9.6582, 6.2501, -1.961, 0.0, 0.0, 0.0]
    points_z = [7.8361, 11.0819, 7.8361, 0.0, -7.8361, -11.0819, -7.8361, -0.0, 0.0, 0.0, 0.0]
    sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
    for index in range(len(sel_vtx)):
        cmds.setAttr('Demilune_ctrl_ND_ID.controlPoints[' + str(index) + '].xValue', points_x[index])
        cmds.setAttr('Demilune_ctrl_ND_ID.controlPoints[' + str(index) + '].yValue', points_y[index])
        cmds.setAttr('Demilune_ctrl_ND_ID.controlPoints[' + str(index) + '].zValue', points_z[index])
    cmds.rename(sel, "Demilune_ctrl")
    ctrl = cmds.ls(sl=True, o=True)[0]
    cmds.select(control, ctrl)
    create_curve(None)


def circle_star():
    control = cmds.ls(sl=True)
    cmds.circle(n="Circle_Star_ctrl_ND_ID", r=10, nr=[0, 1, 0])
    sel = cmds.ls(sl=True, o=True)[0]
    points_x = [8.4669, -0.0, -8.4669, -4.1856, -20.441, -5.9193, -20.441, -4.1856, -8.4669, -0.0, 8.4669, 4.1856, 20.441, 5.9193, 20.441, 4.1856, 0.0, 0.0, 0.0]
    points_y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    points_z = [-20.441, -5.9193, -20.441, -4.1856, -8.4669, -0.0, 8.4669, 4.1856, 20.441, 5.9193, 20.441, 4.1856, 8.4669, -0.0, -8.4669, -4.1856, 0.0, 0.0, 0.0]
    sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
    for index in range(len(sel_vtx)):
        cmds.setAttr('Circle_Star_ctrl_ND_ID.controlPoints[' + str(index) + '].xValue', points_x[index])
        cmds.setAttr('Circle_Star_ctrl_ND_ID.controlPoints[' + str(index) + '].yValue', points_y[index])
        cmds.setAttr('Circle_Star_ctrl_ND_ID.controlPoints[' + str(index) + '].zValue', points_z[index])
    cmds.rename(sel, "Circle_Star_ctrl")
    ctrl = cmds.ls(sl=True, o=True)[0]
    cmds.select(control, ctrl)
    create_curve(None)


shapes_list = {
    "Cylinder": {
        'd': 1,
        'p': [(0.0, 9.47, 9.83), (-2.54, 9.47, 9.48), (-4.91, 9.47, 8.5), (-6.95, 9.47, 6.95),
              (-8.5, 9.47, 4.91), (-9.48, 9.47, 2.54), (-9.83, 9.47, 0.0), (-9.83, -9.47, 0.0),
              (-9.48, -9.47, 2.54), (-8.5, -9.47, 4.91), (-6.95, -9.47, 6.95), (-4.91, -9.47, 8.5),
              (-2.54, -9.47, 9.48), (0.0, -9.47, 9.83), (0.0, 9.47, 9.83), (2.54, 9.47, 9.48),
              (4.91, 9.47, 8.5), (6.95, 9.47, 6.95), (8.5, 9.47, 4.91), (9.48, 9.47, 2.54),
              (9.83, 9.47, 0.0), (9.48, 9.47, -2.54), (8.5, 9.47, -4.91), (6.95, 9.47, -6.95),
              (4.91, 9.47, -8.5), (2.54, 9.47, -9.48), (0.0, 9.47, -9.83), (0.0, -9.47, -9.83),
              (-2.54, -9.47, -9.48), (-4.91, -9.47, -8.5), (-6.95, -9.47, -6.95), (-8.5, -9.47, -4.91),
              (-9.48, -9.47, -2.54), (-9.83, -9.47, 0.0), (-9.83, 9.47, 0.0), (-9.48, 9.47, -2.54),
              (-8.5, 9.47, -4.91), (-6.95, 9.47, -6.95), (-4.91, 9.47, -8.5), (-2.54, 9.47, -9.48),
              (0.0, 9.47, -9.83), (0.0, -9.47, -9.83), (2.54, -9.47, -9.48), (4.91, -9.47, -8.5),
              (6.95, -9.47, -6.95), (8.5, -9.47, -4.91), (9.48, -9.47, -2.54), (9.83, -9.47, 0.0),
              (9.83, 9.47, 0.0), (9.83, -9.47, 0.0), (9.48, -9.47, 2.54), (8.5, -9.47, 4.91),
              (6.95, -9.47, 6.95), (4.91, -9.47, 8.5), (2.54, -9.47, 9.48), (0.0, -9.47, 9.83)]
    },
    "HalfSphere": {
        'd': 1,
        'p': [(-0.04, 0.11, 15.32), (-2.49, 0.11, 15.17), (-4.78, 0.11, 14.56),
              (-6.92, 0.11, 13.64), (-9.06, 0.11, 12.42), (-10.89, 0.11, 10.89),
              (-12.42, 0.11, 9.06), (-13.64, 0.11, 6.92), (-14.56, 0.11, 4.78),
              (-15.17, 0.11, 2.49), (-15.32, 0.11, 0.04), (-15.17, 2.56, 0.04),
              (-14.56, 4.85, 0.04), (-13.64, 6.99, 0.04), (-12.42, 9.13, 0.04),
              (-10.89, 10.96, 0.04), (-9.06, 12.49, 0.04), (-6.92, 13.71, 0.04),
              (-4.78, 14.63, 0.04), (-2.49, 15.24, 0.04), (-0.04, 15.39, 0.04),
              (2.4, 15.24, 0.04), (4.69, 14.63, 0.04), (6.83, 13.71, 0.04),
              (8.97, 12.49, 0.04), (10.81, 10.96, 0.04), (12.33, 9.13, 0.04),
              (13.56, 6.99, 0.04), (14.47, 4.85, 0.04), (15.09, 2.56, 0.04),
              (15.24, 0.11, 0.04), (15.09, 0.11, 2.49), (14.47, 0.11, 4.78),
              (13.56, 0.11, 6.92), (12.33, 0.11, 9.06), (10.81, 0.11, 10.89),
              (8.97, 0.11, 12.42), (6.83, 0.11, 13.64), (4.69, 0.11, 14.56),
              (2.4, 0.11, 15.17), (-0.04, 0.11, 15.32), (-0.04, 2.56, 15.17),
              (-0.04, 4.85, 14.56), (-0.04, 6.99, 13.64), (-0.04, 9.13, 12.42),
              (-0.04, 10.96, 10.89), (-0.04, 12.49, 9.06), (-0.04, 13.71, 6.92),
              (-0.04, 14.63, 4.78), (-0.04, 15.24, 2.49), (-0.04, 15.39, 0.04),
              (-0.04, 15.24, -2.4), (-0.04, 14.63, -4.69), (-0.04, 13.71, -6.83),
              (-0.04, 12.49, -8.97), (-0.04, 10.96, -10.81), (-0.04, 9.13, -12.33),
              (-0.04, 6.99, -13.56), (-0.04, 4.85, -14.47), (-0.04, 2.56, -15.09),
              (-0.04, 0.11, -15.24), (2.4, 0.11, -15.09), (4.69, 0.11, -14.47),
              (6.83, 0.11, -13.56), (8.97, 0.11, -12.33), (10.81, 0.11, -10.81),
              (12.33, 0.11, -8.97), (13.56, 0.11, -6.83), (14.47, 0.11, -4.69),
              (15.09, 0.11, -2.4), (15.24, 0.11, 0.04), (15.09, 0.11, -2.4),
              (14.47, 0.11, -4.69), (13.56, 0.11, -6.83), (12.33, 0.11, -8.97),
              (10.81, 0.11, -10.81), (8.97, 0.11, -12.33), (6.83, 0.11, -13.56),
              (4.69, 0.11, -14.47), (2.4, 0.11, -15.09), (-0.04, 0.11, -15.24),
              (-2.49, 0.11, -15.09), (-4.78, 0.11, -14.47), (-6.92, 0.11, -13.56),
              (-9.06, 0.11, -12.33), (-10.89, 0.11, -10.81), (-12.42, 0.11, -8.97),
              (-13.64, 0.11, -6.83), (-14.56, 0.11, -4.69), (-15.17, 0.11, -2.4),
              (-15.32, 0.11, 0.04)]
    },
    "Locator": {
        'd': 1,
        'p': [(0.0, 13.13, 0.0), (0.0, -13.13, 0.0), (0.0, 0.0, 0.0), (13.13, 0.0, 0.0),
              (-13.13, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, -13.13), (0.0, 0.0, 13.13)]
    },
    "Spiral": {
        'd': 3,
        'p': [(6.7, 0.0, -15.25), (0.81, 0.0, -16.25), (-7.7, 0.0, -14.25),
              (-14.46, 0.0, -5.36), (-15.09, 0.0, 3.77), (-10.33, 0.0, 12.66),
              (-0.94, 0.0, 16.29), (10.58, 0.0, 13.79), (15.21, 0.0, 3.4),
              (12.2, 0.0, -5.86), (2.94, 0.0, -10.24), (-6.2, 0.0, -6.24),
              (-8.33, 0.0, 2.52), (-1.44, 0.0, 8.66), (5.19, 0.0, 6.53), (5.57, 0.0, 3.27)]
    },
    "Cog": {
        'd': 3,
        'p': [(-21.09, 0.0, -1.6), (-23.37, 0.0, 0.0), (-21.09, 0.0, 1.6), (-19.49, 0.0, 2.28),
               (-17.66, 0.0, 3.65), (-16.3, 0.0, 5.25), (-16.3, 0.0, 7.53), (-16.98, 0.0, 9.59),
               (-17.89, 0.0, 11.18), (-18.81, 0.0, 13.69), (-16.07, 0.0, 13.69), (-14.24, 0.0, 13.47),
               (-12.19, 0.0, 13.47), (-10.13, 0.0, 13.92), (-8.76, 0.0, 15.75), (-8.08, 0.0, 17.8),
               (-7.85, 0.0, 19.63), (-7.17, 0.0, 22.14), (-4.88, 0.0, 20.77), (-3.52, 0.0, 19.4),
               (-1.92, 0.0, 18.03), (0.14, 0.0, 17.35), (2.19, 0.0, 18.03), (3.79, 0.0, 19.4),
               (5.16, 0.0, 20.77), (7.44, 0.0, 22.14), (8.12, 0.0, 19.63), (8.35, 0.0, 17.8),
               (9.04, 0.0, 15.75), (10.18, 0.0, 13.92), (12.23, 0.0, 13.47), (14.51, 0.0, 13.47),
               (16.34, 0.0, 13.69), (19.08, 0.0, 13.69), (18.16, 0.0, 11.18), (17.25, 0.0, 9.59),
               (16.57, 0.0, 7.53), (16.57, 0.0, 5.25), (17.94, 0.0, 3.65), (19.53, 0.0, 2.51),
               (21.36, 0.0, 1.6), (23.41, 0.0, 0.0), (21.36, 0.0, -1.6), (19.53, 0.0, -2.51),
               (17.94, 0.0, -3.65), (16.57, 0.0, -5.25), (16.57, 0.0, -7.53), (17.25, 0.0, -9.58),
               (18.16, 0.0, -11.18), (19.08, 0.0, -13.69), (16.34, 0.0, -13.69), (14.51, 0.0, -13.46),
               (12.23, 0.0, -13.46), (10.18, 0.0, -13.92), (9.04, 0.0, -15.74), (8.35, 0.0, -17.8),
               (8.12, 0.0, -19.62), (7.44, 0.0, -22.13), (5.16, 0.0, -20.76), (3.79, 0.0, -19.4),
               (2.19, 0.0, -18.03), (0.14, 0.0, -17.34), (-1.92, 0.0, -18.03), (-3.52, 0.0, -19.4),
               (-4.88, 0.0, -20.76), (-7.17, 0.0, -22.13), (-7.85, 0.0, -19.62), (-8.08, 0.0, -17.8),
               (-8.76, 0.0, -15.74), (-10.13, 0.0, -13.92), (-12.19, 0.0, -13.46), (-14.24, 0.0, -13.46),
               (-16.07, 0.0, -13.69), (-18.81, 0.0, -13.69), (-17.89, 0.0, -11.18), (-16.98, 0.0, -9.58),
               (-16.3, 0.0, -7.53), (-16.3, 0.0, -5.25), (-17.66, 0.0, -3.65), (-18.81, 0.0, -2.74),
               (-21.09, 0.0, -1.6), (-21.09, 0.0, -1.6), (-21.09, 0.0, -1.6), (-21.09, 0.0, -1.6)]
    },
    "Sphere": {
        'd': 1,
        'p': [(0.0, 0.0, 8.6), (0.0, 2.67, 8.17), (0.0, 5.08, 6.96), (0.0, 6.97, 5.07),
              (0.0, 8.18, 2.66), (0.0, 8.61, -0.01), (0.0, 8.18, -2.68), (0.0, 6.97, -5.09),
              (0.0, 5.08, -6.99), (0.0, 2.67, -8.19), (0.0, 0.0, -8.62), (0.0, -2.67, -8.19),
              (0.0, -5.08, -6.99), (0.0, -6.97, -5.09), (0.0, -8.18, -2.68), (0.0, -8.61, -0.01),
              (0.0, -8.18, 2.66), (0.0, -6.97, 5.07), (0.0, -5.08, 6.96), (0.0, -2.67, 8.17),
              (0.0, 0.0, 8.6), (2.67, 0.0, 8.17), (5.08, 0.0, 6.96), (6.97, 0.0, 5.07),
              (8.18, 0.0, 2.66), (8.61, 0.0, -0.01), (8.18, 0.0, -2.68), (6.97, 0.0, -5.09),
              (5.08, 0.0, -6.99), (2.67, 0.0, -8.19), (0.0, 0.0, -8.62), (-2.67, 0.0, -8.19),
              (-5.08, 0.0, -6.99), (-6.97, 0.0, -5.09), (-8.18, 0.0, -2.68), (-8.61, 0.0, -0.01),
              (-8.18, 2.67, -0.01), (-6.97, 5.08, -0.01), (-5.08, 6.97, -0.01), (-2.67, 8.18, -0.01),
              (0.0, 8.61, -0.01), (2.67, 8.18, -0.01), (5.08, 6.97, -0.01), (6.97, 5.08, -0.01),
              (8.18, 2.67, -0.01), (8.61, 0.0, -0.01), (8.18, -2.67, -0.01), (6.97, -5.08, -0.01),
              (5.08, -6.97, -0.01), (2.67, -8.18, -0.01), (0.0, -8.61, -0.01), (-2.67, -8.18, -0.01),
              (-5.08, -6.97, -0.01), (-6.97, -5.08, -0.01), (-8.18, -2.67, -0.01), (-8.61, 0.0, -0.01),
              (-8.18, 0.0, 2.66), (-6.97, 0.0, 5.07), (-5.08, 0.0, 6.96), (-2.67, 0.0, 8.17),
              (0.0, 0.0, 8.6)]
    },
    "CirclePlus": {
        'd': 1,
        'p': [(0.0, 0.0, -11.68), (4.44, 0.0, -10.86), (8.29, 0.0, -8.29), (10.86, 0.0, -4.44),
              (11.68, 0.0, 0.0), (10.86, 0.0, 4.44), (8.29, 0.0, 8.29), (4.44, 0.0, 10.86),
              (0.0, 0.0, 11.68), (0.0, 0.0, 0.0), (0.0, 0.0, -11.68), (-4.44, 0.0, -10.86),
              (-8.29, 0.0, -8.29), (-10.86, 0.0, -4.44), (-11.68, 0.0, 0.0), (0.0, 0.0, 0.0),
              (11.68, 0.0, 0.0), (10.86, 0.0, 4.44), (8.29, 0.0, 8.29), (4.44, 0.0, 10.86),
              (0.0, 0.0, 11.68), (-4.44, 0.0, 10.86), (-8.29, 0.0, 8.29), (-10.86, 0.0, 4.44),
              (-11.68, 0.0, 0.0)]
    },
    "ArrowCross": {
        'd': 1,
        'p': [(0.0, 0.0, 17.06), (-7.52, 0.0, 9.37), (-5.64, 0.0, 9.37), (-5.64, 0.0, 5.61),
              (-9.4, 0.0, 5.61), (-9.4, 0.0, 7.49), (-17.09, 0.0, -0.03), (-9.4, 0.0, -7.55),
              (-9.4, 0.0, -5.67), (-5.64, 0.0, -5.67), (-5.64, 0.0, -9.43), (-7.52, 0.0, -9.43),
              (0.0, 0.0, -17.11), (7.52, 0.0, -9.43), (5.64, 0.0, -9.43), (5.64, 0.0, -5.67),
              (9.4, 0.0, -5.67), (9.4, 0.0, -7.55), (17.09, 0.0, -0.03), (9.4, 0.0, 7.49),
              (9.4, 0.0, 5.61), (5.64, 0.0, 5.61), (5.64, 0.0, 9.37), (7.52, 0.0, 9.37),
              (0.0, 0.0, 17.06)]
    },
    "PlusCircle": {
      'd': 3,
      'p': [(-4.42, 0.0, -4.42), (-4.42, 0.0, -4.42), (-4.42, 0.0, -4.42),
              (-4.42, 0.0, -8.73), (-4.42, 0.0, -8.73), (-4.42, 0.0, -10.94),
              (-2.21, 0.0, -10.94), (2.21, 0.0, -10.94), (2.21, 0.0, -10.94),
              (4.42, 0.0, -10.94), (4.42, 0.0, -8.73), (4.42, 0.0, -8.73),
              (4.42, 0.0, -4.42), (4.42, 0.0, -4.42), (4.42, 0.0, -4.42),
              (8.73, 0.0, -4.42), (8.73, 0.0, -4.42), (10.94, 0.0, -4.42),
              (10.94, 0.0, -2.21), (10.94, 0.0, -2.21), (10.94, 0.0, 2.21),
              (10.94, 0.0, 2.21), (10.94, 0.0, 4.42), (8.73, 0.0, 4.42),
              (4.42, 0.0, 4.42), (4.42, 0.0, 4.42), (4.42, 0.0, 4.42),
              (4.42, 0.0, 8.73), (4.42, 0.0, 8.73), (4.42, 0.0, 10.94),
              (2.21, 0.0, 10.94), (-2.21, 0.0, 10.94), (-2.21, 0.0, 10.94),
              (-4.42, 0.0, 10.94), (-4.42, 0.0, 8.73), (-4.42, 0.0, 4.42),
              (-4.42, 0.0, 4.42), (-4.42, 0.0, 4.42), (-8.73, 0.0, 4.42),
              (-8.73, 0.0, 4.42), (-10.94, 0.0, 4.42), (-10.94, 0.0, 2.21),
              (-10.94, 0.0, -2.21), (-10.94, 0.0, -2.21), (-10.94, 0.0, -4.42),
              (-8.73, 0.0, -4.42), (-4.42, 0.0, -4.42), (-4.42, 0.0, -4.42),
              (-4.42, 0.0, -4.42)]
    },
    "Plus": {
        'd': 1,
        'p': [(-15.51, 0.0, -3.88), (-3.84, 0.0, -3.88), (-3.84, 0.0, -15.55), (3.94, 0.0, -15.55),
                (3.94, 0.0, -3.88), (15.61, 0.0, -3.88), (15.61, 0.0, 3.9), (3.94, 0.0, 3.9),
                (3.94, 0.0, 15.57), (-3.84, 0.0, 15.57), (-3.84, 0.0, 3.9), (-15.51, 0.0, 3.9),
                (-15.51, 0.0, -3.88)]
    },
    "StarCircle": {
        'd' : 3,
        'p' : [(-13.77, 0.0, -0.93), (-18.76, 0.0, 0.0), (-13.77, 0.0, 0.94),
                  (-12.36, 0.0, 1.41), (-9.25, 0.0, 2.5), (-7.22, 0.0, 3.59), (-4.88, 0.0, 5.15),
                  (-3.32, 0.0, 7.49), (-2.23, 0.0, 9.67), (-1.14, 0.0, 12.47), (-0.67, 0.0, 14.19),
                  (0.26, 0.0, 18.55), (1.2, 0.0, 14.19), (1.67, 0.0, 12.47), (2.76, 0.0, 9.67),
                  (3.85, 0.0, 7.49), (5.41, 0.0, 5.15), (7.75, 0.0, 3.59), (9.93, 0.0, 2.5),
                  (12.73, 0.0, 1.41), (14.45, 0.0, 0.94), (18.81, 0.0, 0.0), (14.45, 0.0, -0.93),
                  (12.73, 0.0, -1.4), (9.93, 0.0, -2.49), (7.75, 0.0, -3.58), (5.41, 0.0, -5.14),
                  (3.85, 0.0, -7.48), (2.76, 0.0, -9.66), (1.67, 0.0, -12.47), (1.2, 0.0, -14.18),
                  (0.26, 0.0, -18.55), (-0.67, 0.0, -14.18), (-1.14, 0.0, -12.47), (-2.23, 0.0, -9.66),
                  (-3.32, 0.0, -7.48), (-4.88, 0.0, -5.14), (-7.22, 0.0, -3.58), (-9.25, 0.0, -2.49),
                  (-11.74, 0.0, -1.56), (-13.77, 0.0, -0.93), (-13.77, 0.0, -0.93), (-13.77, 0.0, -0.93),
                  (-13.77, 0.0, -0.93)]
    },
    "StarCross": {
        'd': 1,
        'p': [(0.0, 0.0, 16.98), (-4.97, 0.0, 4.9), (-17.05, 0.0, -0.07),
              (-4.97, 0.0, -5.05), (0.0, 0.0, -17.12), (4.97, 0.0, -5.05),
              (17.05, 0.0, -0.07), (4.97, 0.0, 4.9), (0.0, 0.0, 16.98)]
    },
    "Cube": {
        'd': 1,
        'p': [(6.33, 6.33, -6.33), (-6.33, 6.33, -6.33), (-6.33, 6.33, 6.33), (-6.33, -6.33, 6.33),
                (-6.33, -6.33, -6.33), (-6.33, 6.33, -6.33), (-6.33, 6.33, 6.33), (6.33, 6.33, 6.33),
                (6.33, 6.33, -6.33), (6.33, -6.33, -6.33), (-6.33, -6.33, -6.33), (-6.33, -6.33, 6.33),
                (6.33, -6.33, 6.33), (6.33, -6.33, -6.33), (6.33, -6.33, 6.33), (6.33, 6.33, 6.33)]
    },
    "Pyramid": {
        'd': 1,
        'p': [(0.0, 10.13, 0.0), (-9.13, -8.13, -9.13), (-9.13, -8.13, 9.13), (0.0, 10.13, 0.0),
              (9.13, -8.13, 9.13), (9.13, -8.13, -9.13), (0.0, 10.13, 0.0), (-9.13, -8.13, -9.13),
              (9.13, -8.13, -9.13), (9.13, -8.13, 9.13), (-9.13, -8.13, 9.13)]
    },
    "Rhombus": {
        'd': 1,
        'p': [(0.0, 9.57, 0.06), (0.0, -0.06, -9.57), (9.63, -0.06, 0.06), (0.0, -0.06, 9.69),
              (-9.63, -0.06, 0.06), (0.0, 9.57, 0.06), (9.63, -0.06, 0.06), (0.0, -9.69, 0.06),
              (-9.63, -0.06, 0.06), (0.0, -0.06, -9.57), (0.0, 9.57, 0.06), (0.0, -0.06, 9.69),
              (0.0, -9.69, 0.06), (0.0, -0.06, -9.57)]
    },
    "SquareCircle": {
        'd': 3,
        'p': [(-5.05, 0.0, 11.47), (-8.2, 0.0, 11.47), (-11.47, 0.0, 11.47),
              (-11.47, 0.0, 8.73), (-11.47, 0.0, 5.08), (-11.47, 0.0, -4.86),
              (-11.47, 0.0, -8.57), (-11.47, 0.0, -11.47), (-8.2, 0.0, -11.47),
              (-4.89, 0.0, -11.47), (4.86, 0.0, -11.47), (8.39, 0.0, -11.47),
              (11.47, 0.0, -11.47), (11.47, 0.0, -8.57), (11.47, 0.0, -4.55),
              (11.47, 0.0, 4.87), (11.47, 0.0, 8.73), (11.47, 0.0, 11.47),
              (8.39, 0.0, 11.47), (4.59, 0.0, 11.47), (-5.05, 0.0, 11.47)]
    },
    "Square": {
        'd': 1,
        'p': [(-5.05, 0.0, 11.47), (-8.2, 0.0, 11.47), (-11.47, 0.0, 11.47),
              (-11.47, 0.0, 8.73), (-11.47, 0.0, 5.08), (-11.47, 0.0, -4.86),
              (-11.47, 0.0, -8.57), (-11.47, 0.0, -11.47), (-8.2, 0.0, -11.47),
              (-4.89, 0.0, -11.47), (4.86, 0.0, -11.47), (8.39, 0.0, -11.47),
              (11.47, 0.0, -11.47), (11.47, 0.0, -8.57), (11.47, 0.0, -4.55),
              (11.47, 0.0, 4.87), (11.47, 0.0, 8.73), (11.47, 0.0, 11.47),
              (8.39, 0.0, 11.47), (4.59, 0.0, 11.47), (-5.05, 0.0, 11.47)]
    },
    "ArrowArrow": {
        'd': 1,
        'p': [(-13.09, 0.0, 0.0), (1.52, 0.0, -10.96), (1.52, 0.0, -5.84),
              (12.47, 0.0, -5.84), (12.47, 0.0, 5.84), (1.52, 0.0, 5.84),
              (1.52, 0.0, 10.96), (-13.09, 0.0, 0.0), (1.52, -10.96, 0.0),
              (1.52, -5.84, 0.0), (12.47, -5.84, 0.0), (12.47, 5.84, 0.0),
              (1.52, 5.84, 0.0), (1.52, 10.96, 0.0), (-13.09, 0.0, 0.0)]
    },
    "Triangle": {
        'd': 1,
        'p': [(-11.98, 0.0, 7.25), (11.96, 0.0, 7.25), (-0.01, 0.0, -13.47), (-11.98, 0.0, 7.25)]
    },
    "DoubleArrow": {
        'd': 1,
        'p': [(-7.93, 0.0, 7.93), (-3.97, 0.0, 7.93), (-3.97, 0.0, -7.93),
              (-7.93, 0.0, -7.93), (0.0, 0.0, -15.86), (7.93, 0.0, -7.93),
              (3.97, 0.0, -7.93), (3.97, 0.0, 7.93), (7.93, 0.0, 7.93),
              (0.0, 0.0, 15.86), (-7.93, 0.0, 7.93)]
    },
    "Arrow": {
        'd': 1,
        'p': [(-2.6985, 0.0, 8.5233), (2.6985, 0.0, 8.5233), (2.6985, 0.0, -7.668), (8.0956, 0.0, -7.668),
              (0.0, 0.0, -18.4622), (-8.0956, 0.0, -7.668), (-2.6985, 0.0, -7.668), (-2.6985, 0.0, 8.5233)]
    },
    "DoubleArrowSphere": {
        'd': 1,
        'p': [(12.03, -5.21, 0.0), (11.67, -3.02, 2.31), (10.94, -0.82, 4.5),
              (9.72, 1.12, 6.82), (9.72, 1.12, 4.5), (9.72, 1.12, 2.31),
              (8.26, 2.83, 2.31), (6.44, 4.17, 2.31), (4.37, 5.26, 2.31),
              (2.3, 5.87, 2.31), (-0.02, 5.99, 2.31), (-2.33, 5.87, 2.31),
              (-4.4, 5.26, 2.31), (-6.47, 4.17, 2.31), (-8.29, 2.83, 2.31),
              (-9.75, 1.12, 2.31), (-9.75, 1.12, 4.5), (-9.75, 1.12, 6.82),
              (-10.97, -0.82, 4.5), (-11.7, -3.02, 2.31), (-12.07, -5.21, 0.0),
              (-11.7, -3.02, -2.31), (-10.97, -0.82, -4.5), (-9.75, 1.12, -6.82),
              (-9.75, 1.12, -4.5), (-9.75, 1.12, -2.31), (-8.29, 2.83, -2.31),
              (-6.47, 4.17, -2.31), (-4.4, 5.26, -2.31), (-2.33, 5.87, -2.31),
              (-0.02, 5.99, -2.31), (2.3, 5.87, -2.31), (4.37, 5.26, -2.31),
              (6.44, 4.17, -2.31), (8.26, 2.83, -2.31), (9.72, 1.12, -2.31),
              (9.72, 1.12, -4.5), (9.72, 1.12, -6.82), (10.94, -0.82, -4.5),
              (11.67, -3.02, -2.31), (12.03, -5.21, 0.0)]
    },
    "CrossArrowSphere": {
        'd': 1,
        'p': [(16.02, -6.89, 0.0), (15.38, -4.0, 3.05), (14.42, -1.12, 5.93),
                (12.81, 1.45, 8.98), (12.81, 1.45, 5.93), (12.81, 1.45, 3.05),
                (10.89, 3.69, 3.05), (8.49, 5.45, 3.05), (5.92, 6.9, 3.05),
                (3.04, 7.7, 3.05), (3.04, 6.9, 5.93), (3.04, 5.45, 8.49),
                (3.04, 3.69, 10.9), (3.04, 1.45, 12.82), (5.92, 1.45, 12.82),
                (8.97, 1.45, 12.82), (5.92, -1.12, 14.43), (3.04, -4.0, 15.39),
                (-0.01, -6.89, 16.03), (-3.05, -4.0, 15.39), (-5.94, -1.12, 14.43),
                (-8.98, 1.45, 12.82), (-5.94, 1.45, 12.82), (-3.05, 1.45, 12.82),
                (-3.05, 3.69, 10.9), (-3.05, 5.45, 8.49), (-3.05, 6.9, 5.93),
                (-3.05, 7.7, 3.05), (-5.94, 6.9, 3.05), (-8.5, 5.45, 3.05),
                (-10.91, 3.69, 3.05), (-12.83, 1.45, 3.05), (-12.83, 1.45, 5.93),
                (-12.83, 1.45, 8.98), (-14.43, -1.12, 5.93), (-15.4, -4.0, 3.05),
                (-16.04, -6.89, 0.0), (-15.4, -4.0, -3.05), (-14.43, -1.12, -5.93),
                (-12.83, 1.45, -8.98), (-12.83, 1.45, -5.93), (-12.83, 1.45, -3.05),
                (-10.91, 3.69, -3.05), (-8.5, 5.45, -3.05), (-5.94, 6.9, -3.05),
                (-3.05, 7.7, -3.05), (-3.05, 6.9, -5.93), (-3.05, 5.45, -8.49),
                (-3.05, 3.69, -10.9), (-3.05, 1.45, -12.82), (-5.94, 1.45, -12.82),
                (-8.98, 1.45, -12.82), (-5.94, -1.12, -14.43), (-3.05, -4.0, -15.39),
                (-0.01, -6.89, -16.03), (3.04, -4.0, -15.39), (5.92, -1.12, -14.43),
                (8.97, 1.45, -12.82), (5.92, 1.45, -12.82), (3.04, 1.45, -12.82),
                (3.04, 3.69, -10.9), (3.04, 5.45, -8.49), (3.04, 6.9, -5.93),
                (3.04, 7.7, -3.05), (5.92, 6.9, -3.05), (8.49, 5.45, -3.05),
                (10.89, 3.69, -3.05), (12.81, 1.45, -3.05), (12.81, 1.45, -5.93),
                (12.81, 1.45, -8.98), (14.42, -1.12, -5.93), (15.38, -4.0, -3.05),
                (16.02, -6.89, 0.0)]
    },
    "CrossArrowCircle": {
        'd': 1,
        'p': [(2.63, 0.0, 13.4), (3.35, 0.0, 17.0), (6.7, 0.0, 17.0), (0.0, 0.0, 23.94),
                (-6.71, 0.0, 17.0), (-3.35, 0.0, 17.0), (-2.64, 0.0, 13.4), (-5.27, 0.0, 12.45),
                (-7.67, 0.0, 11.25), (-9.58, 0.0, 9.57), (-11.26, 0.0, 7.66), (-12.45, 0.0, 5.26),
                (-13.41, 0.0, 2.63), (-17.0, 0.0, 3.35), (-17.0, 0.0, 6.7), (-23.95, 0.0, -0.01),
                (-17.0, 0.0, -6.71), (-17.0, 0.0, -3.36), (-13.41, 0.0, -2.64), (-12.45, 0.0, -5.28),
                (-11.26, 0.0, -7.67), (-9.58, 0.0, -9.59), (-7.67, 0.0, -11.26), (-5.27, 0.0, -12.46),
                (-2.64, 0.0, -13.42), (-3.35, 0.0, -17.01), (-6.71, 0.0, -17.01), (0.0, 0.0, -23.96),
                (6.7, 0.0, -17.01), (3.35, 0.0, -17.01), (2.63, 0.0, -13.42), (5.27, 0.0, -12.46),
                (7.66, 0.0, -11.26), (9.58, 0.0, -9.59), (11.25, 0.0, -7.67), (12.45, 0.0, -5.28),
                (13.41, 0.0, -2.64), (17.0, 0.0, -3.36), (17.0, 0.0, -6.71), (23.95, 0.0, -0.01),
                (17.0, 0.0, 6.7), (17.0, 0.0, 3.35), (13.41, 0.0, 2.63), (12.45, 0.0, 5.26),
                (11.25, 0.0, 7.66), (9.58, 0.0, 9.57), (7.66, 0.0, 11.25), (5.27, 0.0, 12.45),
                (2.63, 0.0, 13.4)]
    },
    "CrossArrow": {
        'd': 1,
        'p': [(0.0, 0.0, -14.6219), (4.874, 0.0, -9.7479), (2.437, 0.0, -9.7479), (2.437, 0.0, -2.437),
              (9.7479, 0.0, -2.437), (9.7479, 0.0, -4.874), (14.6219, 0.0, 0.0), (9.7479, 0.0, 4.874),
              (9.7479, 0.0, 2.437), (2.437, 0.0, 2.437), (2.437, 0.0, 9.7479), (4.874, 0.0, 9.7479),
              (0.0, 0.0, 14.6219), (-4.874, 0.0, 9.7479), (-2.437, 0.0, 9.7479), (-2.437, 0.0, 2.437),
              (-9.7479, 0.0, 2.437), (-9.7479, 0.0, 4.874), (-14.6219, 0.0, 0.0), (-9.7479, 0.0, -4.874),
              (-9.7479, 0.0, -2.437), (-2.437, 0.0, -2.437), (-2.437, 0.0, -9.7479), (-4.874, 0.0, -9.7479),
              (0.0, 0.0, -14.6219)]
    },
    "DoubleNailCross": {
        'd': 1,
        'p': [(7.37, 0.0, 0.0), (7.42, 0.0, 0.57), (7.57, 0.0, 1.15), (7.76, 0.0, 1.68),
              (8.08, 0.0, 2.18), (8.45, 0.0, 2.61), (11.06, 0.0, 0.0), (8.45, 0.0, 2.61),
              (8.89, 0.0, 2.99), (9.38, 0.0, 3.29), (9.92, 0.0, 3.51), (10.48, 0.0, 3.65),
              (11.06, 0.0, 3.69), (11.64, 0.0, 3.65), (12.2, 0.0, 3.51), (12.74, 0.0, 3.3),
              (13.24, 0.0, 2.98), (13.67, 0.0, 2.61), (11.06, 0.0, 0.0), (13.67, 0.0, 2.61),
              (14.05, 0.0, 2.17), (14.35, 0.0, 1.68), (14.57, 0.0, 1.14), (14.71, 0.0, 0.58),
              (14.75, 0.0, 0.0), (14.71, 0.0, -0.58), (14.57, 0.0, -1.14), (14.35, 0.0, -1.68),
              (14.05, 0.0, -2.17), (13.67, 0.0, -2.61), (11.06, 0.0, 0.0), (13.67, 0.0, -2.61),
              (13.24, 0.0, -2.98), (12.74, 0.0, -3.3), (12.2, 0.0, -3.51), (11.64, 0.0, -3.65),
              (11.06, 0.0, -3.69), (10.48, 0.0, -3.65), (9.92, 0.0, -3.51), (9.38, 0.0, -3.29),
              (8.89, 0.0, -2.99), (8.45, 0.0, -2.61), (11.06, 0.0, 0.0), (8.45, 0.0, -2.61),
              (8.08, 0.0, -2.18), (7.77, 0.0, -1.68), (7.55, 0.0, -1.15), (7.41, 0.0, -0.58),
              (7.37, 0.0, 0.0), (0.0, 0.0, 0.0), (-7.37, 0.0, 0.0), (-7.42, 0.0, -0.57),
              (-7.57, 0.0, -1.15), (-7.76, 0.0, -1.68), (-8.08, 0.0, -2.18), (-8.45, 0.0, -2.61),
              (-11.06, 0.0, 0.0), (-8.45, 0.0, -2.61), (-8.89, 0.0, -2.99), (-9.38, 0.0, -3.29),
              (-9.92, 0.0, -3.51), (-10.48, 0.0, -3.65), (-11.06, 0.0, -3.69), (-11.64, 0.0, -3.65),
              (-12.2, 0.0, -3.51), (-12.74, 0.0, -3.3), (-13.24, 0.0, -2.98), (-13.67, 0.0, -2.61),
              (-11.06, 0.0, 0.0), (-13.67, 0.0, -2.61), (-14.05, 0.0, -2.17), (-14.35, 0.0, -1.68),
              (-14.57, 0.0, -1.14), (-14.71, 0.0, -0.58), (-14.75, 0.0, 0.0), (-14.71, 0.0, 0.58),
              (-14.57, 0.0, 1.14), (-14.35, 0.0, 1.68), (-14.05, 0.0, 2.17), (-13.67, 0.0, 2.61),
              (-11.06, 0.0, 0.0), (-13.67, 0.0, 2.61), (-13.24, 0.0, 2.98), (-12.74, 0.0, 3.3),
              (-12.2, 0.0, 3.51), (-11.64, 0.0, 3.65), (-11.06, 0.0, 3.69), (-10.48, 0.0, 3.65),
              (-9.92, 0.0, 3.51), (-9.38, 0.0, 3.29), (-8.89, 0.0, 2.99), (-8.45, 0.0, 2.61),
              (-11.06, 0.0, 0.0), (-8.45, 0.0, 2.61), (-8.08, 0.0, 2.18), (-7.77, 0.0, 1.68),
              (-7.55, 0.0, 1.15), (-7.41, 0.0, 0.58), (-7.37, 0.0, 0.0)]
    },
    "RoundCross": {
        'd': 3,
        'p': [(-6.34, 0.0, 14.42), (-10.3, 0.0, 14.42), (-5.08, 0.0, 5.08),
              (-14.42, 0.0, 10.97), (-14.42, 0.0, 6.38), (-14.42, 0.0, -6.11),
              (-14.42, 0.0, -10.77), (-5.08, 0.0, -5.08), (-10.3, 0.0, -14.42),
              (-6.15, 0.0, -14.42), (6.1, 0.0, -14.42), (10.54, 0.0, -14.42),
              (5.08, 0.0, -5.08), (14.42, 0.0, -10.77), (14.42, 0.0, -5.72),
              (14.42, 0.0, 6.12), (14.42, 0.0, 10.97), (5.08, 0.0, 5.08),
              (10.54, 0.0, 14.42), (5.76, 0.0, 14.42), (-6.34, 0.0, 14.42)]
    },
    "DarkStar": {
        'd': 1,
        'p': [(2.47, 0.06, 12.43), (2.49, 0.06, 12.46), (2.59, 0.08, 12.46),
                (0.0, 0.06, 17.44), (-2.59, 0.04, 12.46), (-2.49, 0.06, 12.46),
                (-2.47, 0.06, 12.43), (-4.85, 0.06, 11.7), (-7.04, 0.06, 10.53),
                (-12.57, 0.07, 12.28), (-10.53, 0.07, 7.04), (-11.7, 0.07, 4.85),
                (-12.43, 0.07, 2.47), (-12.46, 0.07, 2.49), (-12.46, 0.07, 2.48),
                (-17.44, 0.07, 0.0), (-12.46, 0.07, -2.48), (-12.46, 0.07, -2.49),
                (-12.43, 0.07, -2.47), (-11.7, 0.07, -4.85), (-10.53, 0.07, -7.04),
                (-12.57, 0.07, -12.28), (-7.04, 0.06, -10.53), (-4.85, 0.06, -11.7),
                (-2.47, 0.06, -12.43), (-2.49, 0.06, -12.46), (-2.59, 0.04, -12.46),
                (0.0, 0.06, -17.44), (2.59, 0.08, -12.46), (2.49, 0.06, -12.46),
                (2.47, 0.06, -12.43), (4.85, 0.05, -11.7), (7.04, 0.05, -10.53),
                (12.29, 0.21, -12.2), (10.62, 0.05, -7.04), (11.7, 0.05, -4.85),
                (12.43, 0.05, -2.47), (12.46, 0.05, -2.49), (12.46, 0.05, -2.41),
                (17.44, 0.04, 0.0), (12.46, 0.05, 2.41), (12.46, 0.05, 2.49),
                (12.43, 0.05, 2.47), (11.7, 0.05, 4.85), (10.53, 0.05, 7.04),
                (11.99, 0.05, 12.28), (7.04, 0.05, 10.53), (4.85, 0.05, 11.7),
                (2.47, 0.06, 12.43)]
    },
    "Gear": {
        'd': 1,
        'p': [(-3.76, -0.25, 17.05), (-3.16, -0.19, 12.2), (-6.21, -0.26, 10.96),
              (-8.84, -0.32, 8.98), (-12.69, -0.45, 11.99), (-15.04, -0.48, 8.84),
              (-16.64, -0.49, 5.26), (-12.14, -0.36, 3.36), (-12.6, -0.34, 0.1),
              (-12.2, -0.3, -3.17), (-16.73, -0.41, -5.0), (-15.18, -0.33, -8.61),
              (-12.88, -0.24, -11.79), (-8.98, -0.16, -8.84), (-6.39, -0.08, -10.86),
              (-3.36, 0.02, -12.15), (-4.04, 0.04, -16.99), (-0.14, 0.15, -17.45),
              (3.76, 0.25, -17.05), (3.16, 0.19, -12.2), (6.21, 0.26, -10.96),
              (8.84, 0.32, -8.98), (12.69, 0.45, -11.99), (15.04, 0.48, -8.84),
              (16.64, 0.49, -5.26), (12.14, 0.36, -3.36), (12.6, 0.34, -0.1),
              (12.2, 0.3, 3.17), (16.73, 0.41, 5.0), (15.18, 0.33, 8.61), (12.88, 0.24, 11.79),
              (8.98, 0.16, 8.84), (6.39, 0.08, 10.86), (3.36, -0.02, 12.15), (4.04, -0.04, 16.99),
              (0.14, -0.15, 17.45), (-3.76, -0.25, 17.05)]
    },
    "GearCircle": {
        'd': 1,
        'p': [(-13.93, 0.0, 1.6), (-13.91, 0.0, -1.78), (-12.73, 0.0, -2.18),
              (-11.43, 0.0, -6.01), (-12.21, 0.0, -6.91), (-10.21, 0.0, -9.62),
              (-9.01, 0.0, -9.26), (-5.71, 0.0, -11.59), (-5.82, 0.0, -12.77),
              (-2.6, 0.0, -13.79), (-1.85, 0.0, -12.8), (2.19, 0.0, -12.75),
              (2.8, 0.0, -13.76), (6.01, 0.0, -12.7), (6.03, 0.0, -11.45),
              (9.27, 0.0, -9.03), (10.36, 0.0, -9.49), (12.33, 0.0, -6.75),
              (11.61, 0.0, -5.73), (12.81, 0.0, -1.87), (13.96, 0.0, -1.6),
              (13.94, 0.0, 1.77), (12.76, 0.0, 2.18), (11.46, 0.0, 6.01),
              (12.24, 0.0, 6.9), (10.24, 0.0, 9.62), (9.05, 0.0, 9.25),
              (5.74, 0.0, 11.59), (5.85, 0.0, 12.77), (2.63, 0.0, 13.79),
              (1.88, 0.0, 12.79), (-2.16, 0.0, 12.74), (-2.77, 0.0, 13.76),
              (-5.97, 0.0, 12.69), (-5.99, 0.0, 11.45), (-9.24, 0.0, 9.03),
              (-10.33, 0.0, 9.49), (-12.29, 0.0, 6.75), (-11.57, 0.0, 5.73),
              (-12.78, 0.0, 1.86), (-13.93, 0.0, 1.6)]
    },
    "Nail": {
        'd': 1,
        'p': [(0.0, 9.7872, 0.0), (0.0, 9.911, 0.9155), (0.0, 10.2645, 1.7691), (0.0, 10.8244, 2.504),
              (0.0, 11.5593, 3.0638), (0.0, 12.4128, 3.4174), (0.0, 13.3283, 3.5411), (0.0, 14.2439, 3.4174),
              (0.0, 15.0974, 3.0638), (0.0, 15.8323, 2.504), (0.0, 16.3922, 1.7691), (0.0, 16.7457, 0.9155),
              (0.0, 16.8694, 0.0), (0.0, 16.7457, -0.9155), (0.0, 16.3922, -1.7691), (0.0, 15.8323, -2.504),
              (0.0, 15.0974, -3.0638), (0.0, 14.2439, -3.4174), (0.0, 13.3283, -3.5411), (0.0, 12.4128, -3.4174),
              (0.0, 11.5593, -3.0638), (0.0, 10.8244, -2.504), (0.0, 10.2645, -1.7691), (0.0, 9.911, -0.9155),
              (0.0, 9.7872, 0.0), (0.0, 0.0691, 0.0)]
    },
    "Cone": {
        'd': 1,
        'p': [(0.0, -6.2496, 6.7558), (3.3779, -6.2496, 5.8507), (5.8507, -6.2496, 3.3779), (6.7558, -6.2496, 0.0),
              (5.8507, -6.2496, -3.3779), (3.3779, -6.2496, -5.8507), (0.0, -6.2496, -6.7558),
              (-3.3779, -6.2496, -5.8507), (-5.8507, -6.2496, -3.3779), (-6.7558, -6.2496, 0.0),
              (-5.8507, -6.2496, 3.3779), (-3.3779, -6.2496, 5.8507), (0.0, -6.2496, 6.7558), (0.0, 0.0123, 3.9143),
              (0.0, 9.2809, 0.0), (0.0, 0.0123, -3.9143), (0.0, -6.2496, -6.7558), (-3.3779, -6.2496, -5.8507),
              (-5.8507, -6.2496, -3.3779), (-6.7558, -6.2496, 0.0), (-3.9143, 0.0123, 0.0), (0.0, 9.2809, 0.0),
              (3.9143, 0.0123, 0.0), (6.7558, -6.2496, 0.0), (3.9143, 0.0123, 0.0), (3.3899, 0.0123, -1.9571),
              (1.9571, 0.0123, -3.3899), (0.0, 0.0123, -3.9143), (-1.9571, 0.0123, -3.3899), (-3.3899, 0.0123, -1.9571),
              (-3.9143, 0.0123, 0.0), (-3.3899, 0.0123, 1.9571), (-1.9571, 0.0123, 3.3899), (0.0, 0.0123, 3.9143),
              (1.9571, 0.0123, 3.3899), (3.3899, 0.0123, 1.9571), (3.9143, 0.0123, 0.0)]
    },
    "Corner": {
        'd': 1,
        'p': [(-14.8097, 0.0, 5.755), (-0.0707, 0.0, -8.984), (14.6683, 0.0, 5.755), (8.7727, 0.0, 5.755),
              (-0.0707, 0.0, -3.0884), (-8.9141, 0.0, 5.755), (-14.8097, 0.0, 5.755)]
    },
    "Heart": {
        'd': 3,
        'p': [(0.0, -0.0069, 10.7896), (4.7677, -0.0069, 6.895), (10.6729, -0.0069, -0.0634),
              (11.7609, -0.0069, -5.7015), (9.5611, -0.0069, -9.761), (5.1173, -0.0069, -10.7557),
              (1.6537, -0.0069, -9.1768), (0.0, -0.0069, -7.2623), (-1.6537, -0.0069, -9.1768),
              (-5.1172, -0.0069, -10.7557), (-9.5611, -0.0069, -9.761), (-11.7609, -0.0069, -5.7015),
              (-10.6729, -0.0069, -0.0634), (-4.7677, -0.0069, 6.895), (0.0, -0.0069, 10.7896)]
    },
    "HalfCircleArrow": {
        'd': 1,
        'p': [(-13.522, 0.0, 0.0), (-12.9631, 0.0, 4.1363), (-11.1033, 0.0, 7.8676), (-8.1294, 0.0, 10.9877),
              (-4.4464, 0.0, 12.8815), (0.0, 0.0, 13.4942), (4.2062, 0.0, 12.9343), (8.5266, 0.0, 10.674),
              (11.5972, 0.0, 7.3285), (12.2098, 0.0, 4.9262), (14.4504, 0.0, 4.9262), (10.9305, 0.0, 0.0),
              (7.3408, 0.0, 4.7714), (9.8326, 0.0, 4.7714), (9.2045, 0.0, 6.6875), (6.6875, 0.0, 9.2045),
              (3.5158, 0.0, 10.8206), (0.0, 0.0, 11.3774), (-3.5158, 0.0, 10.8206), (-6.6875, 0.0, 9.2045),
              (-9.2045, 0.0, 6.6875), (-10.8206, 0.0, 3.5158), (-11.3774, 0.0, 0.0), (-13.522, 0.0, 0.0)]
    },
    "TArrow": {
        'd': 1,
        'p': [(-3.2, 0.0, -1.6), (-9.6, 0.0, -1.6), (-9.6, 0.0, 1.6), (-16.0, 0.0, -4.8), (-9.6, 0.0, -11.2),
              (-9.6, 0.0, -8.0), (-3.2, 0.0, -8.0), (3.2, 0.0, -8.0), (9.6, 0.0, -8.0), (9.6, 0.0, -11.2),
              (16.0, 0.0, -4.8), (9.6, 0.0, 1.6), (9.6, 0.0, -1.6), (3.2, 0.0, -1.6), (3.2, 0.0, 4.8), (6.4, 0.0, 4.8),
              (0.0, 0.0, 11.2), (-6.4, 0.0, 4.8), (-3.2, 0.0, 4.8), (-3.2, 0.0, -1.6)]
    },
    "CircleCube": {
        'd': 1,
        'p': [(4.1751, 4.1751, -4.1751), (2.1203, 4.8863, -4.8863), (0.0, 5.1151, -5.1151), (-2.1203, 4.8863, -4.8863),
              (-4.1751, 4.1751, -4.1751), (-4.8863, 4.8863, -2.1203), (-5.1151, 5.1151, 0.0), (-4.8863, 4.8863, 2.1203),
              (-4.1751, 4.1751, 4.1751), (-2.1203, 4.8863, 4.8863), (0.0, 5.1151, 5.1151), (2.1203, 4.8863, 4.8863),
              (4.1751, 4.1751, 4.1751), (4.8863, 4.8863, 2.1203), (5.1151, 5.1151, 0.0), (4.8863, 4.8863, -2.1203),
              (4.1751, 4.1751, -4.1751), (4.8863, 2.1203, -4.8863), (5.1151, 0.0, -5.1151), (4.8863, -2.1203, -4.8863),
              (4.1751, -4.1751, -4.1751), (2.1203, -4.8863, -4.8863), (0.0, -5.1151, -5.1151), (-2.1203, -4.8863, -4.8863),
              (-4.1751, -4.1751, -4.1751), (-4.8863, -2.1203, -4.8863), (-5.1151, 0.0, -5.1151), (-4.8863, 2.1203, -4.8863),
              (-4.1751, 4.1751, -4.1751), (-4.8863, 2.1203, -4.8863), (-5.1151, 0.0, -5.1151), (-4.8863, -2.1203, -4.8863),
              (-4.1751, -4.1751, -4.1751), (-4.8863, -4.8863, -2.1203), (-5.1151, -5.1151, 0.0), (-4.8863, -4.8863, 2.1203),
              (-4.1751, -4.1751, 4.1751), (-4.8863, -2.1203, 4.8863), (-5.1151, 0.0, 5.1151), (-4.8863, 2.1203, 4.8863),
              (-4.1751, 4.1751, 4.1751), (-4.8863, 2.1203, 4.8863), (-5.1151, 0.0, 5.1151), (-4.8863, -2.1203, 4.8863),
              (-4.1751, -4.1751, 4.1751), (-2.1203, -4.8863, 4.8863), (0.0, -5.1151, 5.1151), (2.1203, -4.8863, 4.8863),
              (4.1751, -4.1751, 4.1751), (4.8863, -2.1203, 4.8863), (5.1151, 0.0, 5.1151), (4.8863, 2.1203, 4.8863),
              (4.1751, 4.1751, 4.1751), (4.8863, 2.1203, 4.8863), (5.1151, 0.0, 5.1151), (4.8863, -2.1203, 4.8863),
              (4.1751, -4.1751, 4.1751), (4.8863, -4.8863, 2.1203), (5.1151, -5.1151, 0.0), (4.8863, -4.8863, -2.1203),
              (4.1751, -4.1751, -4.1751)]
    },
    "Frame": {
        'd': 1,
        'p': [(-6.6817, 0.0, -6.6817), (-6.6817, 0.0, 6.6817), (6.6817, 0.0, 6.6817), (6.6817, 0.0, -6.6817),
              (-6.6817, 0.0, -6.6817), (-13.3634, 0.0, -13.3634), (13.3634, 0.0, -13.3634), (6.6817, 0.0, -6.6817),
              (6.6817, 0.0, 6.6817), (13.3634, 0.0, 13.3634), (13.3634, 0.0, -13.3634), (13.3634, 0.0, 13.3634),
              (-13.3634, 0.0, 13.3634), (-6.6817, 0.0, 6.6817), (-13.3634, 0.0, 13.3634), (-13.3634, 0.0, -13.3634)]
    },
    "Pow": {
        'd': 1,
        'p': [(-0.1552, 0.0, -8.1868), (0.9569, 0.0, -8.3193), (3.267, 0.0, -8.878), (4.2775, 0.0, -8.9804),
              (5.2819, 0.0, -8.8163), (6.1862, 0.0, -8.2772), (6.7426, 0.0, -7.6304), (7.1869, 0.0, -6.5409),
              (7.2403, 0.0, -5.6283), (7.0054, 0.0, -4.5689), (6.8119, 0.0, -4.0734), (6.6268, 0.0, -2.9947),
              (6.7816, 0.0, -2.0648), (7.3711, 0.0, -0.9144), (8.1585, 0.0, -0.4259), (8.9032, 0.0, -0.2159),
              (9.6399, 0.0, 0.3149), (10.4334, 0.0, 1.4621), (10.746, 0.0, 2.573), (10.7571, 0.0, 3.3435),
              (10.6088, 0.0, 4.0435), (12.2563, 0.0, 6.5105), (9.6221, 0.0, 5.3087), (9.0167, 0.0, 5.4891),
              (8.5636, 0.0, 5.493), (7.9669, 0.0, 5.3529), (7.3479, 0.0, 5.1919), (6.8426, 0.0, 4.9854),
              (6.4681, 0.0, 4.8129), (6.1029, 0.0, 4.6194), (5.8373, 0.0, 4.4341), (5.5668, 0.0, 4.2232),
              (5.6538, 0.0, 4.431), (5.7562, 0.0, 4.7448), (5.8844, 0.0, 5.1603), (6.0457, 0.0, 5.8298),
              (6.1074, 0.0, 6.6894), (5.9852, 0.0, 7.7216), (5.6546, 0.0, 8.8992), (5.2224, 0.0, 9.5791),
              (4.5666, 0.0, 10.0618), (4.4292, 0.0, 12.5719), (3.0193, 0.0, 10.2018), (2.1376, 0.0, 9.7576),
              (1.3575, 0.0, 8.9338), (0.8116, 0.0, 7.8458), (0.4838, 0.0, 6.9517), (0.3273, 0.0, 6.1932),
              (0.2379, 0.0, 5.6274), (0.1808, 0.0, 5.2276), (0.0814, 0.0, 4.7984), (0.0421, 0.0, 5.1926),
              (-0.0084, 0.0, 5.593), (-0.1735, 0.0, 6.2935), (-0.3125, 0.0, 6.8551), (-0.5155, 0.0, 7.3388),
              (-0.8392, 0.0, 7.936), (-1.2229, 0.0, 8.5378), (-1.4804, 0.0, 8.9549), (-2.2296, 0.0, 9.7403),
              (-2.8357, 0.0, 10.1092), (-3.5706, 0.0, 10.2658), (-4.9503, 0.0, 12.7735), (-4.8965, 0.0, 9.8547),
              (-5.2067, 0.0, 9.601), (-5.6261, 0.0, 9.043), (-5.9288, 0.0, 8.339), (-6.0147, 0.0, 7.9904),
              (-6.0892, 0.0, 7.1147), (-6.0757, 0.0, 6.7638), (-5.9372, 0.0, 5.9104), (-5.7204, 0.0, 5.1696),
              (-5.4821, 0.0, 4.6578), (-5.3579, 0.0, 4.385), (-5.167, 0.0, 4.0738), (-5.3992, 0.0, 4.1842),
              (-5.5282, 0.0, 4.2469), (-5.845, 0.0, 4.4048), (-6.1022, 0.0, 4.5606), (-6.4163, 0.0, 4.7449),
              (-6.7199, 0.0, 4.9509), (-7.0586, 0.0, 5.1761), (-7.6593, 0.0, 5.5292), (-8.3496, 0.0, 5.6832),
              (-9.007, 0.0, 5.6004), (-9.4813, 0.0, 5.3614), (-9.9464, 0.0, 5.0391), (-12.5062, 0.0, 6.3158),
              (-10.5634, 0.0, 4.1126), (-10.7181, 0.0, 3.3958), (-10.5136, 0.0, 2.2785), (-10.1816, 0.0, 1.2599),
              (-9.431, 0.0, 0.2657), (-8.7241, 0.0, -0.1949), (-7.7422, 0.0, -0.5272), (-6.9762, 0.0, -1.0706),
              (-6.5242, 0.0, -2.0189), (-6.6133, 0.0, -3.2121), (-7.123, 0.0, -4.0734), (-7.3165, 0.0, -4.5689),
              (-7.5545, 0.0, -5.6283), (-7.5627, 0.0, -6.0394), (-7.498, 0.0, -6.5409), (-7.053, 0.0, -7.6304),
              (-6.4973, 0.0, -8.2772), (-5.8543, 0.0, -8.7026), (-4.6142, 0.0, -8.9797), (-3.7626, 0.0, -8.9021),
              (-3.5435, 0.0, -8.8697), (-1.7552, 0.0, -8.412), (-0.7447, 0.0, -8.2523), (-0.1552, 0.0, -8.1868)]

    },
    "Ring": {
        'd': 1,
        'p': [(-10.0399, 1.3012, 10.0399), (0.0, 1.3012, 14.1986), (0.0, -1.3012, 14.1986), (-10.0399, -1.3012, 10.0399),
              (-10.0399, 1.3012, 10.0399), (-14.1986, 1.3012, 0.0), (-14.1986, -1.3012, 0.0), (-10.0399, -1.3012, 10.0399),
              (-14.1986, -1.3012, 0.0), (-10.0399, -1.3012, -10.0399), (-10.0399, 1.3012, -10.0399), (-14.1986, 1.3012, 0.0),
              (-10.0399, 1.3012, -10.0399), (0.0, 1.3012, -14.1986), (0.0, -1.3012, -14.1986), (-10.0399, -1.3012, -10.0399),
              (-10.0399, 1.3012, -10.0399), (-10.0399, -1.3012, -10.0399), (0.0, -1.3012, -14.1986), (10.0399, -1.3012, -10.0399),
              (10.0399, 1.3012, -10.0399), (0.0, 1.3012, -14.1986), (10.0399, 1.3012, -10.0399), (14.1986, 1.3012, 0.0),
              (14.1986, -1.3012, 0.0), (10.0399, -1.3012, -10.0399), (14.1986, -1.3012, 0.0), (10.0399, -1.3012, 10.0399),
              (10.0399, 1.3012, 10.0399), (14.1986, 1.3012, 0.0), (10.0399, 1.3012, 10.0399), (0.0, 1.3012, 14.1986),
              (0.0, -1.3012, 14.1986), (10.0399, -1.3012, 10.0399)]
    },
    "QuarterArrow": {
        'd': 1,
        'p': [(5.839, 0.0, 8.6344), (0.4378, 0.0, 9.6843), (2.071, 0.0, 7.2689), (0.724, 0.0, 6.5646),
              (-1.79, 0.0, 4.7788), (-4.6931, 0.0, 1.1919), (-6.5266, 0.0, -3.0449), (-7.1531, 0.0, -7.6186),
              (-5.533, 0.0, -7.6186), (-4.9666, 0.0, -3.4807), (-3.3071, 0.0, 0.3532), (-0.6815, 0.0, 3.5977),
              (1.5941, 0.0, 5.214), (2.8125, 0.0, 5.8512), (4.6445, 0.0, 3.0929), (5.839, 0.0, 8.6344)]
    },
    "GearMech": {
        'd': 1,
        'p': [(-2.7059, 0.0, -11.3043), (-5.6754, 0.0, -13.4715), (-8.916, 0.0, -11.4739), (-8.6791, 0.0, -7.8811),
              (-11.0814, 0.0, -3.3849), (-14.5042, 0.0, -1.8203), (-14.4052, 0.0, 1.985), (-11.0896, 0.0, 3.6668),
              (-8.5323, 0.0, 7.8158), (-8.8384, 0.0, 11.6636), (-5.4807, 0.0, 13.4575), (-2.3529, 0.0, 11.4375),
              (2.489, 0.0, 11.3111), (5.6754, 0.0, 13.4715), (8.916, 0.0, 11.4739), (8.6577, 0.0, 7.9347),
              (11.116, 0.0, 3.3335), (14.5042, 0.0, 1.8203), (14.4049, 0.0, -1.985), (10.9989, 0.0, -3.8239),
              (8.6366, 0.0, -7.6564), (8.8384, 0.0, -11.6636), (5.4807, 0.0, -13.4579), (2.5833, 0.0, -11.4422),
              (-2.7059, 0.0, -11.3043)]
    },
    "Spring": {
        'd': 3,
        'p': [(5.6158, 5.6931, 1.8247), (4.7907, 5.5507, 3.452), (3.5081, 5.4084, 4.7497), (1.8907, 5.2661, 5.5939),
              (0.0927, 5.1237, 5.9041), (-1.7141, 4.9814, 5.6505), (-3.3573, 4.8391, 4.8575), (-4.6799, 4.6968, 3.6007),
              (-5.5557, 4.5544, 2.0001), (-5.9011, 4.4121, 0.2086), (-5.6831, 4.2698, -1.6028), (-4.9225, 4.1275, -3.2613),
              (-3.6919, 3.9851, -4.6083), (-2.1088, 3.8428, -5.5154), (-0.3244, 3.7005, -5.8959), (1.4909, 3.5582, -5.7135),
              (3.164, 3.4158, -4.9856), (4.5349, 3.2735, -3.7817), (5.4729, 3.1312, -2.2167), (5.8884, 2.9889, -0.4401),
              (5.7416, 2.8465, 1.3785), (5.0467, 2.7042, 3.0655), (3.87, 2.5619, 4.4598), (2.3238, 2.4195, 5.4283),
              (0.5557, 2.2772, 5.8786), (-1.2655, 2.1349, 5.7676), (-2.9658, 1.9926, 5.1059), (-4.383, 1.8502, 3.9568),
              (-5.3817, 1.7079, 2.4299), (-5.8666, 1.5656, 0.671), (-5.7913, 1.4233, -1.152), (-5.1632, 1.2809, -2.865),
              (-4.0421, 1.1386, -4.3044), (-2.5351, 0.9963, -5.3329), (-0.786, 0.854, -5.8522), (1.0381, 0.7116, -5.8128),
              (2.7631, 0.5693, -5.2184), (4.2242, 0.427, -4.1258), (5.2821, 0.2847, -2.6393), (5.8357, 0.1423, -0.9008),
              (5.8321, 0.0, 0.9237), (5.2717, -0.1423, 2.6601), (4.208, -0.2847, 4.1424), (2.7425, -0.427, 5.2293),
              (1.0152, -0.5693, 5.8169), (-0.809, -0.7116, 5.8491), (-2.556, -0.854, 5.3229), (-4.059, -0.9963, 4.2885),
              (-5.1744, -1.1386, 2.8446), (-5.7958, -1.2809, 1.1292), (-5.8639, -1.4233, -0.694), (-5.3721, -1.5656, -2.451),
              (-4.3674, -1.7079, -3.974), (-2.9457, -1.8502, -5.1176), (-1.2428, -1.9926, -5.7725), (0.5788, -2.1349, -5.8764),
              (2.3451, -2.2772, -5.4192), (3.8875, -2.4195, -4.4445), (5.0588, -2.5619, -3.0456), (5.747, -2.7042, -1.3559),
              (5.8866, -2.8465, 0.4633), (5.4642, -2.9888, 2.2382), (4.52, -3.1312, 3.7995), (3.1443, -3.2735, 4.998),
              (1.4685, -3.4158, 5.7193), (-0.3476, -3.5582, 5.8946), (-2.1305, -3.7005, 5.507), (-3.71, -3.8428, 4.5937),
              (-4.9353, -3.9851, 3.2419), (-5.6894, -4.1275, 1.5805), (-5.9002, -4.2698, -0.2318), (-5.5478, -4.4121, -2.022),
              (-4.6657, -4.5544, -3.6191), (-3.3381, -4.6968, -4.8707), (-1.6919, -4.8391, -5.6572), (0.1159, -4.9814, -5.9037),
              (1.9127, -5.1237, -5.5864), (3.5268, -5.2661, -4.7359), (4.8042, -5.4084, -3.4331), (5.6229, -5.5507, -1.8026),
              (5.9048, -5.693, 0.0)]
    },
    "DoubleNail": {
        'd': 1,
        'p': [(7.37, 0.0, 0.0), (7.42, 0.0, 0.57), (7.57, 0.0, 1.15), (7.76, 0.0, 1.68), (8.08, 0.0, 2.18),
              (8.45, 0.0, 2.61), (8.45, 0.0, 2.61), (8.89, 0.0, 2.99), (9.38, 0.0, 3.29), (9.92, 0.0, 3.51),
              (10.48, 0.0, 3.65), (11.06, 0.0, 3.69), (11.64, 0.0, 3.65), (12.2, 0.0, 3.51), (12.74, 0.0, 3.3),
              (13.24, 0.0, 2.98), (13.67, 0.0, 2.61), (13.67, 0.0, 2.61), (14.05, 0.0, 2.17), (14.35, 0.0, 1.68),
              (14.57, 0.0, 1.14), (14.71, 0.0, 0.58), (14.75, 0.0, 0.0), (14.71, 0.0, -0.58), (14.57, 0.0, -1.14),
              (14.35, 0.0, -1.68), (14.05, 0.0, -2.17), (13.67, 0.0, -2.61), (13.67, 0.0, -2.61), (13.24, 0.0, -2.98),
              (12.74, 0.0, -3.3), (12.2, 0.0, -3.51), (11.64, 0.0, -3.65), (11.06, 0.0, -3.69), (10.48, 0.0, -3.65),
              (9.92, 0.0, -3.51), (9.38, 0.0, -3.29), (8.89, 0.0, -2.99), (8.45, 0.0, -2.61), (8.45, 0.0, -2.61),
              (8.08, 0.0, -2.18), (7.77, 0.0, -1.68), (7.55, 0.0, -1.15), (7.41, 0.0, -0.58), (7.37, 0.0, 0.0),
              (0.0, 0.0, 0.0), (-7.37, 0.0, 0.0), (-7.42, 0.0, -0.57), (-7.57, 0.0, -1.15), (-7.76, 0.0, -1.68),
              (-8.08, 0.0, -2.18), (-8.45, 0.0, -2.61), (-8.45, 0.0, -2.61), (-8.89, 0.0, -2.99), (-9.38, 0.0, -3.29),
              (-9.92, 0.0, -3.51), (-10.48, 0.0, -3.65), (-11.06, 0.0, -3.69), (-11.64, 0.0, -3.65), (-12.2, 0.0, -3.51),
              (-12.74, 0.0, -3.3), (-13.24, 0.0, -2.98), (-13.67, 0.0, -2.61), (-13.67, 0.0, -2.61), (-14.05, 0.0, -2.17),
              (-14.35, 0.0, -1.68), (-14.57, 0.0, -1.14), (-14.71, 0.0, -0.58), (-14.75, 0.0, 0.0), (-14.71, 0.0, 0.58),
              (-14.57, 0.0, 1.14), (-14.35, 0.0, 1.68), (-14.05, 0.0, 2.17), (-13.67, 0.0, 2.61), (-13.67, 0.0, 2.61),
              (-13.24, 0.0, 2.98), (-12.74, 0.0, 3.3), (-12.2, 0.0, 3.51), (-11.64, 0.0, 3.65), (-11.06, 0.0, 3.69),
              (-10.48, 0.0, 3.65), (-9.92, 0.0, 3.51), (-9.38, 0.0, 3.29), (-8.89, 0.0, 2.99), (-8.45, 0.0, 2.61),
              (-8.45, 0.0, 2.61), (-8.08, 0.0, 2.18), (-7.77, 0.0, 1.68), (-7.55, 0.0, 1.15), (-7.41, 0.0, 0.58),
              (-7.37, 0.0, 0.0)]
    },
    "Platonic": {
        'd': 1,
        'p': [(2.5151, -4.0695, 7.7406), (0.0, -9.0996, 0.0), (8.139, -4.0695, 0.0), (2.5151, -4.0695, 7.7406),
              (-6.5846, -4.0695, 4.784), (0.0, -9.0996, 0.0), (-6.5846, -4.0695, -4.784), (-6.5846, -4.0695, 4.784),
              (-8.139, 4.0695, 0.0), (-6.5846, -4.0695, -4.784), (2.5151, -4.0695, -7.7406), (0.0, -9.0996, 0.0),
              (8.139, -4.0695, 0.0), (2.5151, -4.0695, -7.7406), (6.5846, 4.0695, -4.784), (8.139, -4.0695, 0.0),
              (6.5846, 4.0695, 4.784), (6.5846, 4.0695, -4.784), (0.0, 9.0996, 0.0), (6.5846, 4.0695, 4.784),
              (2.5151, -4.0695, 7.7406), (-2.5151, 4.0695, 7.7406), (6.5846, 4.0695, 4.784), (0.0, 9.0996, 0.0),
              (-2.5151, 4.0695, 7.7406), (-6.5846, -4.0695, 4.784), (-2.5151, 4.0695, 7.7406), (-8.139, 4.0695, 0.0),
              (0.0, 9.0996, 0.0), (-2.5151, 4.0695, -7.7406), (-8.139, 4.0695, 0.0), (-2.5151, 4.0695, -7.7406),
              (6.5846, 4.0695, -4.784), (-2.5151, 4.0695, -7.7406), (2.5151, -4.0695, -7.7406), (-2.5151, 4.0695, -7.7406),
              (-6.5846, -4.0695, -4.784)]
    },
    "GearTech": {
        'd': 1,
        'p': [(-10.8443, 0.0, -11.9754), (-9.4256, 0.0, -11.4616), (-8.3462, 0.0, -10.6084), (-6.6069, 0.0, -11.7705),
              (-6.9821, 0.0, -13.0943), (-6.9139, 0.0, -14.6016), (-5.4361, 0.0, -15.2138), (-4.322, 0.0, -14.1961),
              (-3.6512, 0.0, -12.9948), (-1.5996, 0.0, -13.4029), (-1.4396, 0.0, -14.7695), (-0.7998, 0.0, -16.136),
              (0.7998, 0.0, -16.136), (1.4396, 0.0, -14.7695), (1.5996, 0.0, -13.4029), (3.6512, 0.0, -12.9948),
              (4.322, 0.0, -14.1961), (5.4361, 0.0, -15.2138), (6.9139, 0.0, -14.6017), (6.9821, 0.0, -13.0943),
              (6.6069, 0.0, -11.7705), (8.3462, 0.0, -10.6084), (9.4256, 0.0, -11.4616), (10.8443, 0.0, -11.9754),
              (11.9754, 0.0, -10.8443), (11.4616, 0.0, -9.4256), (10.6084, 0.0, -8.3462), (11.7705, 0.0, -6.6069),
              (13.0943, 0.0, -6.9821), (14.6016, 0.0, -6.9139), (15.2138, 0.0, -5.4361), (14.1961, 0.0, -4.322),
              (12.9948, 0.0, -3.6512), (13.4029, 0.0, -1.5996), (14.7695, 0.0, -1.4396), (16.136, 0.0, -0.7998),
              (16.136, 0.0, 0.7998), (14.7695, 0.0, 1.4396), (13.4029, 0.0, 1.5996), (12.9948, 0.0, 3.6512),
              (14.1961, 0.0, 4.322), (15.2138, 0.0, 5.4361), (14.6016, 0.0, 6.9139), (13.0943, 0.0, 6.9821),
              (11.7705, 0.0, 6.6069), (10.6084, 0.0, 8.3462), (11.4616, 0.0, 9.4256), (11.9754, 0.0, 10.8443),
              (10.8443, 0.0, 11.9754), (9.4256, 0.0, 11.4616), (8.3462, 0.0, 10.6084), (6.6069, 0.0, 11.7705),
              (6.9821, 0.0, 13.0943), (6.9139, 0.0, 14.6016), (5.4361, 0.0, 15.2138), (4.322, 0.0, 14.1961),
              (3.6512, 0.0, 12.9948), (1.5996, 0.0, 13.4029), (1.4396, 0.0, 14.7695), (0.7998, 0.0, 16.136),
              (-0.7998, 0.0, 16.136), (-1.4396, 0.0, 14.7695), (-1.5996, 0.0, 13.4029), (-3.6512, 0.0, 12.9948),
              (-4.322, 0.0, 14.1961), (-5.4361, 0.0, 15.2138), (-6.9139, 0.0, 14.6017), (-6.9821, 0.0, 13.0943),
              (-6.6069, 0.0, 11.7705), (-8.3462, 0.0, 10.6084), (-9.4256, 0.0, 11.4616), (-10.8443, 0.0, 11.9754),
              (-11.9754, 0.0, 10.8443), (-11.4616, 0.0, 9.4256), (-10.6084, 0.0, 8.3462), (-11.7705, 0.0, 6.6069),
              (-13.0943, 0.0, 6.9821), (-14.6016, 0.0, 6.9139), (-15.2138, 0.0, 5.4361), (-14.1961, 0.0, 4.322),
              (-12.9948, 0.0, 3.6512), (-13.4029, 0.0, 1.5996), (-14.7695, 0.0, 1.4396), (-16.136, 0.0, 0.7998),
              (-16.136, 0.0, -0.7998), (-14.7695, 0.0, -1.4396), (-13.4029, 0.0, -1.5996), (-12.9948, 0.0, -3.6512),
              (-14.1961, 0.0, -4.322), (-15.2138, 0.0, -5.4361), (-14.6017, 0.0, -6.9139), (-13.0943, 0.0, -6.9821),
              (-11.7705, 0.0, -6.6069), (-10.6084, 0.0, -8.3462), (-11.4616, 0.0, -9.4256), (-11.9754, 0.0, -10.8443),
              (-10.8443, 0.0, -11.9754)]
    },
    "Flower": {
        'd': 1,
        'p': [(-3.76, -0.25, 17.05), (-1.8709, -0.1125, 7.223), (-1.2893, -0.054, 2.2754), (-5.2337, -0.1895, 5.3166),
              (-12.69, -0.45, 11.99), (-18.3965, -0.5871, 10.8128), (-16.64, -0.49, 5.26), (-7.1874, -0.2131, 1.9893),
              (-2.6159, -0.0706, 0.0208), (-7.223, -0.1776, -1.8768), (-16.73, -0.41, -5.0), (-18.5677, -0.4036, -10.5315),
              (-12.88, -0.24, -11.79), (-5.3166, -0.0947, -5.2337), (-1.3266, -0.0166, -2.2547), (-1.9893, 0.0118, -7.1934),
              (-4.04, 0.04, -16.99), (-0.1712, 0.1835, -21.3443), (3.76, 0.25, -17.05), (1.8709, 0.1125, -7.223),
              (1.2893, 0.054, -2.2754), (5.2337, 0.1895, -5.3166), (12.69, 0.45, -11.99), (18.3965, 0.5871, -10.8128),
              (16.64, 0.49, -5.26), (7.1874, 0.2131, -1.9893), (2.6159, 0.0706, -0.0208), (7.223, 0.1776, 1.8768),
              (16.73, 0.41, 5.0), (18.5677, 0.4036, 10.5315), (12.88, 0.24, 11.79), (5.3166, 0.0947, 5.2337),
              (1.3266, 0.0166, 2.2547), (1.9893, -0.0118, 7.1934), (4.04, -0.04, 16.99), (0.1712, -0.1835, 21.3443),
              (-3.76, -0.25, 17.05)]
    },
    "BrightStar": {
        'd': 1,
        'p': [(2.47, 0.06, 12.43), (2.49, 0.06, 12.46), (2.59, 0.08, 12.46), (0.0, 0.06, 17.44), (-2.59, 0.04, 12.46),
              (-2.49, 0.06, 12.46), (-2.47, 0.06, 12.43), (-6.6793, 0.06, 16.113), (-7.04, 0.06, 10.53),
              (-12.57, 0.07, 12.28), (-10.53, 0.07, 7.04), (-16.113, 0.0738, 6.6793), (-12.43, 0.07, 2.47),
              (-12.46, 0.07, 2.49), (-12.46, 0.07, 2.48), (-17.44, 0.07, 0.0), (-12.46, 0.07, -2.48),
              (-12.46, 0.07, -2.49), (-12.43, 0.07, -2.47), (-16.113, 0.0738, -6.6793), (-10.53, 0.07, -7.04),
              (-12.57, 0.07, -12.28), (-7.04, 0.06, -10.53), (-6.6793, 0.06, -16.113), (-2.47, 0.06, -12.43),
              (-2.49, 0.06, -12.46), (-2.59, 0.04, -12.46), (0.0, 0.06, -17.44), (2.59, 0.08, -12.46),
              (2.49, 0.06, -12.46), (2.47, 0.06, -12.43), (6.6793, 0.0462, -16.113), (7.04, 0.05, -10.53),
              (12.29, 0.21, -12.2), (10.62, 0.05, -7.04), (16.113, 0.0462, -6.6793), (12.43, 0.05, -2.47),
              (12.46, 0.05, -2.49), (12.46, 0.05, -2.41), (17.44, 0.04, 0.0), (12.46, 0.05, 2.41), (12.46, 0.05, 2.49),
              (12.43, 0.05, 2.47), (16.113, 0.0462, 6.6793), (10.53, 0.05, 7.04), (11.99, 0.05, 12.28),
              (7.04, 0.05, 10.53), (6.6793, 0.0462, 16.113), (2.47, 0.06, 12.43)]
    },
    "Arc": {
        'd': 3,
        'p': [(14.1986, -0.0, -0.0), (14.1986, -0.0, -1.8467), (13.4593, -0.0, -5.5804), (10.3013, -0.0, -10.2998),
              (5.575, -0.0, -13.4597), (-0.0, 0.0, -14.568), (-5.575, 0.0, -13.4597), (-10.3013, 0.0, -10.2998),
              (-13.4593, 0.0, -5.5804), (-14.1986, 0.0, -1.8467), (-14.1986, 0.0, 0.0)]
    },
    "NailCross": {
        'd': 1,
        'p': [(0.0, 0.0, 0.0), (0.0, 17.7321, 0.0), (-0.6076, 17.7786, 0.0), (-1.1996, 17.9295, 0.0),
              (-1.7608, 18.1423, 0.0), (-2.2793, 18.4674, 0.0), (-2.736, 18.866, 0.0), (0.0, 21.602, 0.0),
              (-2.736, 18.866, 0.0), (-3.1346, 19.3226, 0.0), (-3.4558, 19.8412, 0.0), (-3.688, 20.4023, 0.0),
              (-3.8273, 20.9944, 0.0), (-3.8698, 21.602, 0.0), (-3.8273, 22.2095, 0.0), (-3.688, 22.8016, 0.0),
              (-3.4558, 23.3627, 0.0), (-3.1346, 23.8813, 0.0), (-2.736, 24.3379, 0.0), (0.0, 21.602, 0.0),
              (-2.736, 24.3379, 0.0), (-2.2793, 24.7365, 0.0), (-1.7608, 25.0577, 0.0), (-1.1996, 25.2899, 0.0),
              (-0.6076, 25.4292, 0.0), (0.0, 25.4718, 0.0), (0.6076, 25.4292, 0.0), (1.1996, 25.2899, 0.0),
              (1.7608, 25.0577, 0.0), (2.2793, 24.7365, 0.0), (2.736, 24.3379, 0.0), (0.0, 21.602, 0.0),
              (2.736, 24.3379, 0.0), (3.1346, 23.8813, 0.0), (3.4558, 23.3627, 0.0), (3.688, 22.8016, 0.0),
              (3.8273, 22.2095, 0.0), (3.8698, 21.602, 0.0), (3.8273, 20.9944, 0.0), (3.688, 20.4023, 0.0),
              (3.4558, 19.8412, 0.0), (3.1346, 19.3226, 0.0), (2.736, 18.866, 0.0), (0.0, 21.602, 0.0),
              (2.736, 18.866, 0.0), (2.2793, 18.4674, 0.0), (1.7608, 18.1462, 0.0), (1.1996, 17.914, 0.0),
              (0.6076, 17.7747, 0.0), (0.0, 17.7321, 0.0)]
    },
    "Arrow3": {
        'd': 1,
        'p': [(-0.0, 0.0, 8.3794), (0.0, 0.0, 8.3794), (0.0, 0.0, -12.0161), (5.6658, 0.0, -8.3794),
              (0.0, 0.0, -19.5518), (-5.6658, 0.0, -8.3794), (-0.0, 0.0, -12.0161), (-0.0, 0.0, 8.3794)]
    },
    "ArrowDot": {
        'd': 1,
        'p': [(0.0, 7.3915, 0.0), (-3.6464, 7.3915, 0.0), (0.0, 0.0, 0.0), (3.6464, 7.3915, 0.0), (0.0, 7.3915, 0.0),
              (0.0, 25.8208, 0.0), (0.9855, 25.9194, 0.0), (1.8725, 26.3136, 0.0), (2.5624, 26.9049, 0.0),
              (3.1537, 27.5948, 0.0), (3.5479, 28.4817, 0.0), (3.6464, 29.4673, 0.0), (3.5479, 30.4528, 0.0),
              (3.1537, 31.3398, 0.0), (2.5624, 32.1282, 0.0), (1.8725, 32.7195, 0.0), (0.9855, 33.0152, 0.0),
              (0.0, 33.2123, 0.0), (-0.9855, 33.0152, 0.0), (-1.8725, 32.7195, 0.0), (-2.5624, 32.1282, 0.0),
              (-3.1537, 31.3398, 0.0), (-3.5479, 30.4528, 0.0), (-3.6464, 29.4673, 0.0), (-3.5479, 28.4817, 0.0),
              (-3.1537, 27.5948, 0.0), (-2.5624, 26.9049, 0.0), (-1.8725, 26.3136, 0.0), (-0.9855, 25.9194, 0.0),
              (0.0, 25.8208, 0.0)]
    },
    "ArrowHead": {
        'd': 1,
        'p': [(0.0, 0.0, -11.1603), (-15.1352, 0.0, 11.1603), (-11.9247, 0.0, 8.5613), (-8.1027, 0.0, 6.5739),
              (-4.1278, 0.0, 5.3508), (0.0, 0.0, 4.8922), (4.1278, 0.0, 5.3508), (8.1027, 0.0, 6.5739),
              (11.9247, 0.0, 8.5613), (15.1352, 0.0, 11.1603), (0.0, 0.0, -11.1603)]
    },
    "Star": {
        'd': 1,
        'p': [(0.0528, 0.0, 7.3472), (-11.2412, 0.0, 15.3417), (-6.8706, 0.0, 2.2976), (-18.0963, 0.0, -5.8887),
              (-4.2076, 0.0, -5.8474), (-0.0234, 0.0, -18.9688), (4.3616, 0.0, -5.8317), (18.0015, 0.0, -5.8224),
              (6.9947, 0.0, 2.323), (11.0685, 0.0, 15.3827), (0.0528, 0.0, 7.3472)]
    },
    "CircleArrow": {
        'd': 1,
        'p': [(-7.8983, 0.0, -10.8711), (-10.8711, 0.0, -7.8983), (-12.7798, 0.0, -4.1524), (-13.4374, 0.0, 0.0),
              (-12.7798, 0.0, 4.1524), (-10.8711, 0.0, 7.8983), (-7.8983, 0.0, 10.8711), (-4.1524, 0.0, 12.7798),
              (0.0, 0.0, 13.4374), (4.1524, 0.0, 12.7798), (7.8983, 0.0, 10.8711), (10.8711, 0.0, 7.8983),
              (12.7798, 0.0, 4.1524), (13.4374, 0.0, 0.0), (12.9712, 0.0, -4.0534), (10.9537, 0.0, -8.1989),
              (7.6549, 0.0, -11.6695), (3.9131, 0.0, -13.1493), (3.8663, 0.0, -15.4447), (-0.0729, 0.0, -11.9341),
              (3.9293, 0.0, -8.3352), (3.921, 0.0, -11.0788), (6.4701, 0.0, -10.0388), (9.323, 0.0, -7.0142),
              (11.0542, 0.0, -3.4306), (11.4218, 0.0, 0.0), (10.8628, 0.0, 3.5295), (9.2404, 0.0, 6.7136),
              (6.7136, 0.0, 9.2404), (3.5295, 0.0, 10.8628), (0.0, 0.0, 11.4218), (-3.5295, 0.0, 10.8628),
              (-6.7136, 0.0, 9.2404), (-9.2404, 0.0, 6.7136), (-10.8628, 0.0, 3.5295), (-11.4218, 0.0, 0.0),
              (-10.8628, 0.0, -3.5295), (-9.2404, 0.0, -6.7136), (-6.7136, 0.0, -9.2404), (-7.8983, 0.0, -10.8711)]
    },
    "Snowflake": {
        'd': 1,
        'p': [(-3.76, -0.25, 17.05), (-1.8333, -0.205, 13.1638), (-9.0984, -0.3811, 16.0571), (-10.2941, -0.3545, 8.4025),
              (-12.69, -0.45, 11.99), (-18.3965, -0.5871, 10.8128), (-16.64, -0.49, 5.26), (-12.3433, -0.3792, 4.9125),
              (-18.46, -0.4982, 0.1468), (-12.4228, -0.2915, -4.7253), (-16.73, -0.41, -5.0), (-18.5677, -0.4036, -10.5315),
              (-12.88, -0.24, -11.79), (-10.4305, -0.2048, -8.2335), (-9.3616, -0.1171, -15.9111), (-1.9493, 0.0215, -13.1099),
              (-4.04, 0.04, -16.99), (-0.1712, 0.1835, -21.3443), (3.76, 0.25, -17.05), (1.8333, 0.205, -13.1638),
              (9.0984, 0.3811, -16.0571), (10.2941, 0.3545, -8.4023), (12.69, 0.45, -11.99), (18.3965, 0.5871, -10.8128),
              (16.64, 0.49, -5.26), (12.3432, 0.3792, -4.9126), (18.46, 0.4982, -0.1468), (12.2479, 0.2838, 5.0333),
              (16.73, 0.41, 5.0), (18.5677, 0.4036, 10.5315), (12.88, 0.24, 11.79), (10.6054, 0.2124, 7.9255),
              (9.3616, 0.1171, 15.9111), (1.9493, -0.0215, 13.1099), (4.04, -0.04, 16.99), (0.1712, -0.1835, 21.3443),
              (-3.76, -0.25, 17.05)]
    },
}
