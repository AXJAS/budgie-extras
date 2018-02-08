This is the test version of the dynamic workspaces backgrounder and the visualizer. All files should be in one and the same directory.

Edit the shortcuts Control_L + Alt + left/right to run the space_switcher with the arguments next or prev (= next/previous).

# Behaviour
When space_switcher is called with a keypress, immediately released, the navigator shows on the new workspace and immediately terminates itself (within 0.4 sec) (more or less similar to how Unity behaves)

If called, keeping Ctrl + Alt pressed, the navigator terminates on key release Ctrl/Alt event. While keeping pressed left/right arrow will browse through the workspaces. While doing so, on moving to the left will clean up unused workspaces.

![screenshot-1](https://github.com/UbuntuBudgie/budgie-extras/blob/development/budgie_visualspace/visualspace.png)

