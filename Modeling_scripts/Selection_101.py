import maya.cmds as cmds


def main_window():
    if cmds.window("Select_Edges_ID", exists=1):
        cmds.deleteUI("Select_Edges_ID")
    if cmds.windowPref("Select_Edges_ID", exists=True):
        cmds.windowPref("Select_Edges_ID", remove=True)
    cmds.window('Select_Edges_ID', title='Select_Edges', width=150, height=40, toolbox=True, sizeable=False)
    main_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    cmds.text("Step:", parent=main_layout)
    cmds.textField("Step_ID", parent=main_layout, width=150)
    cmds.checkBox('Horizontal_edges_ID', l='Horizontal', p=main_layout, w=176, h=20, vis=False)
    button_layout = cmds.columnLayout(parent=main_layout, adj=True)
    cmds.button(label="Select", parent=button_layout, c=lambda *x: select_edges_step())
    cmds.showWindow("Select_Edges_ID")


def select_edges_step():
    if cmds.checkBox('Horizontal_edges_ID', q=True, v=True):
        pos = 0
    else:
        pos = -1
    sel_edges = [cmds.ls(sl=True)[pos]]
    print (sel_edges)
    obj_name = sel_edges[0].split(".")[0]
    print (obj_name)
    list_edges = []
    step = int(cmds.textField("Step_ID", q=True, text=True))
    for edges in sel_edges:


        # start_end_edges = edges.split("[")[-1].split("]")
        # print (start_end_edges)
        # start_edge = start_end_edges[0].split(":")[0]
        # end_edge = start_end_edges[0].split(":")[-1]
        # print(start_edge, end_edge)
        # edge_numb = int(start_edge)
        # while edge_numb <= int(end_edge):
        #     edge_name = (obj_name + ".e[" + str(edge_numb) + "]")
        #     list_edges.append(edge_name)
        #     edge_numb += step
    print (list_edges)
    cmds.select(list_edges)


main_window()
