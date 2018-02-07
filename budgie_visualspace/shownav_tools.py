#!/usr/bin/env python3
import subprocess
import os
import gi
from gi.repository import Gio


navpath = os.path.dirname(os.path.abspath(__file__))
navigator = os.path.join(navpath, "shownav")
shownav_busy = "/tmp/shownav_busy"
shownav_right = "/tmp/shownav_right"
shownav_left = "/tmp/shownav_left"


path = "org.gnome.desktop.wm.preferences"
key = "num-workspaces"
settings = Gio.Settings.new(path)
dynamic = True


def get(cmd):
    try:
        return subprocess.check_output(cmd).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        pass


def get_wsdata():
    # get current workspace, n- workspaces
    data = get(["wmctrl", "-d"]).splitlines()
    return [int([l.split()[0] for l in data if "*" in l][0]) + 1, len(data)]
