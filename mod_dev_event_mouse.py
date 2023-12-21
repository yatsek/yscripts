#!/usr/bin/python3

# Script stitched together from several sources on the web
# It fixes mouse wheel jumping too much on Ubuntu 18.4
# Licens GPL 3.0

import evdev
from evdev import ecodes
import subprocess
import sys

#key=ecodes.KEY_LEFTSHIFT
#kb=evdev.InputDevice('/dev/input/event1')   # keybord
mouse_device = '/dev/input/event' +sys.argv[1]
#print(mouse_device)

mouse=evdev.InputDevice(mouse_device)   # mouse
dummy=evdev.UInput.from_device(mouse)
hwheel=evdev.UInput({ecodes.EV_REL:[ecodes.REL_HWHEEL]})
mouse.grab()
for event in mouse.read_loop():
  if event.type==ecodes.EV_REL and event.code==ecodes.REL_WHEEL: # and key in kb.active_keys():
    #print(event)
    event.value =  int(event.value>0)*2-1
    #subprocess.run(["xdotool", "click", str(5 - int(event.value>0))])
    #hwheel.write(ecodes.EV_REL, ecodes.REL_HWHEEL, int(event.value>0)*2-1)
    #hwheel.write(ecodes.EV_SYN, ecodes.SYN_REPORT, 0)
    #ummy.write_event(hwheel)
  dummy.write_event(event)
