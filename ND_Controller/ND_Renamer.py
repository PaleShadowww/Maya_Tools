import maya.cmds as cmds


def add_to_all():
    # Take text (new_name) from variable (expField) of other function (main())
    # if global_stuff["mylist"]:
    #     selected_obj = global_stuff["mylist"]
    # else:
    #     selected_obj = cmds.ls(sl=True)   # Make list selected objects
    # global_stuff["mylist"] = []
    add_text = cmds.textField("NewName_ND_ID", query=True, text=True)
    selected_obj = cmds.ls(sl=True)
    if "*" in add_text:
        for i in selected_obj:
            new_name = add_text.replace("*", str(i))
            cmds.rename(i, new_name)  # Change name of selected Object in list
            # global_stuff["mylist"].append(new_name)
        cmds.textField("NewName_ND_ID", edit=True, text="")  # Clear expField


def remove_from_all():
    # if global_stuff["mylist"]:
    #     selected_obj = global_stuff["mylist"]
    # else:
    #     selected_obj = cmds.ls(sl=True)
    # global_stuff["mylist"] = []
    remove_text = cmds.textField("NewName_ND_ID", query=True, text=True)
    selected_obj = cmds.ls(sl=True)
    for i in selected_obj:
        obj_name = i.split("|")[-1]  # Get name objects
        if remove_text in obj_name:  # Check remove_text in name of selected objects
            new_name = obj_name.replace(remove_text, '')  # Replace remove_text on '' in name of object
            cmds.rename(i, new_name)  # Change name of selected Object in list
        #     global_stuff["mylist"].append(new_name)
        # else:
        #     global_stuff["mylist"].append(obj_name)
    cmds.textField("NewName_ND_ID", edit=True, text="")  # Clear expField


def renamer():
    if cmds.window("Renamer_SA_ND_ID", exists=1):
        cmds.deleteUI("Renamer_SA_ND_ID")
    if cmds.windowPref("Renamer_SA_ND_ID", exists=True):
        cmds.windowPref("Renamer_SA_ND_ID", remove=True)
    cmds.window("Renamer_SA_ND_ID", title="ND Renamer", width=250, tlb=True)
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
    cmds.button(label="Cancel", parent=buttons_layout, c="cmds.deleteUI(\"Renamer_SA_ND_ID\")")
    cmds.showWindow("Renamer_SA_ND_ID")


renamer()
