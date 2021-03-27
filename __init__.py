# -*- coding: utf-8 -*-

"""Take screenshots or snips using Gnome screenshot utiliy directly from the launcher.\
Select between a snip, a fullscreen or window only screenshot, to save or to keep on clipboard.

Auto saved screenshots are located in XDG_PICTURES_DIR ('Pictures' folder).

Icon by icons8.com"""

import os
import subprocess
import tempfile
from shutil import which

from albert import FuncAction, Item

__title__ = "Snip"
__version__ = "0.4.0"
__triggers__ = "ss "
__authors__ = "Fabián Pérez"
__exec_deps__ = ["gnome-screenshot"]

iconPath = os.path.dirname(__file__)+"/icon.png"


def handleQuery(query):
  if query.isTriggered:
    return [
      Item(
        id = "%s-area-of-screen" % __title__,
        icon = iconPath,
        text = "Snip screen",
        subtext = "Capture a rectacle drawed with your mouse",
        actions = [
          FuncAction(
            "Capture to clipboard",
            lambda: doScreenshot(["-a -c"])
          ),
          FuncAction(
            "Capture and save in Pictures",
            lambda: doScreenshot(["-a"])
          ),
        ]
      ),
      Item(
        id = "%s-whole-screen" % __title__,
        icon = iconPath,
        text = "Take screenshot",
        subtext = "Save a screenshot in Pictures",
        actions = [
          FuncAction(
            "Take full screenshot",
            lambda: doScreenshot(["-p"])
          ),
          FuncAction(
            "Take screenshot without showing the pointer",
            lambda: doScreenshot([])
          ),
          FuncAction(
            "Take screenshot of actual window only",
            lambda: doScreenshot(["-w --border-effect=shadow"])
          ),
        ]
      ),
    ]

def getScreenshotDirectory():
  if which("xdg-user-dir") is None:
    return tempfile.gettempdir()

  proc = subprocess.run(["xdg-user-dir", "PICTURES"], stdout=subprocess.PIPE)
  pictureDirectory = proc.stdout.decode("utf-8")

  if pictureDirectory:
    return pictureDirectory.strip()
  return tempfile.gettempdir()

def doScreenshot(args):
  path = getScreenshotDirectory()
  command = "sleep 0.1 && gnome-screenshot %s " % path
  subprocess.Popen(command + " ".join(args), shell=True)

