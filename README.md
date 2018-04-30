xwdui
-----

A tiny crummy UI for `xwd`, the X Window Dump utility.

(It takes screenshots.)

It needs Imagemagick to work (it uses the `convert` utility to convert a
XWD-format file to a PNG).


I wrote this primarily for use in CDE, the old Unix desktop. With that said,
I think it should work on pretty much any X window manager.

To make this work, if you don't already have a file called ~/.dt/dtwmrc, copy
one from the system installation dir (e.g. `/usr/dt/config/C/sys.dtwmrc` ).

To make it work in CDE, I made my `dtwmrc` (`~/.dt/dtwmrc`) look like this:

    Keys DtKeyBindings
    {
        <key>Print                       root|icon|window        f.exec /home/wyatt/bin/xwdui.py
        [the stuff that was already in this section goes here]
    }

That let me use my "Print Screen" key to take screenshots of windows.

To capture the entire desktop, add the `-root` argument to `xwd` command in the
ksh script (`xwddump`).

To remove the window borders, remove `-frame` from the `xwd` command in the
same script.

