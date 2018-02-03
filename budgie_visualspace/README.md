This is the test version of the dynamic workspaces backgrounder and the visualizer.

# To run
The backgrounder (dynamic_spaces) needs to run in the background separately. Subsequently, edit the shortcuts Control_L + Alt + left/right to run the space_switcher with the arguments next or prev (= next/previous).

# Comments
When space_switcher is called a single time, it calls visualspace, which terminates after 0.8 (I believe) seconds, unless within .8 second space_switcher is called a second time. It then assumes user is "on tour" through the workspaces and then waits for key release (Ctrl/Alt).

After termination, the visualspace sets a time out for new calls of .2 seconds (creating a trigger file for space_switcher), to prevent mutter to crash.

Seems a complicated setup, but it seems to work as a workaround for what seems to be a mutter bug.

