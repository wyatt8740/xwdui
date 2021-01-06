xwdui
-----

A tiny crummy UI for `xwd`, the X Window Dump utility (It takes screenshots).

There's also a newer version which uses `ffmpeg` instead, which appears
to be more suited to taking screenshots on systems using compositors.

You will have to change the path to the file to save the last run's settings
in from within the .py scripts. Other than that it shouldn't be too difficult
to set up. Ask if you have problems. I mostly wrote this for myself so it's
definitely a bit strange to set up. Once set up it should work fine though.

If you are having it just not start up properly, try forging a 'last run'
file. That's the file name set in the poorly-named 'fileName' variable in the
.py scripts.

The file should have the format of:
````
[line 1] /path/to/directory/to/save/screenshots/in/ [newline]
[line 2] [empty by default; causes the screenshot program to give screenshots
         timestamps for file names. Alternatively, can be 'filename.png']
         [ newline, only if line 2 is non-empty ]
````
with a unix-style newline (`\n`) separating the two fields.

It needs Imagemagick to work (it uses the `convert` utility to convert a
XWD-format file to a PNG image).

I wrote this primarily for use in CDE, the old commercial Unix desktop. With
that said, I think it should work on pretty much any X window manager. I have
personally been using it in FVWM without issues recently.

To make this work in CDE, if you don't already have a file called ~/.dt/dtwmrc,
copy one from the system installation dir (e.g. `/usr/dt/config/C/sys.dtwmrc`).


#### Key bindings in a selection of window managers
##### CDE (Common Desktop Environment)
To make it work in CDE, I made part of my `dtwmrc` (`~/.dt/dtwmrc`) look like
this:
````
Keys DtKeyBindings
{
    <key>Print         root|icon|window        f.exec /home/wyatt/bin/xwdui.py
    Alt<key>Print      root|icon|window        f.exec /home/wyatt/bin/xwdui-root.py
    [the stuff that was already in this section goes here]
}
````
That let me use my "Print Screen" key to take screenshots of windows.

For full-screen screenshots, I set a separate keybinding for `xwdui-root.py`,
which mapped to alt-PrintScreen. This went in the same `DtKeyBindings` section,
as seen in the example above.

##### FVWM (FVWM2)
For FVWM, I edited my `~/.fvwm2rc` file to include the following lines:
````
# Print Screen
Silent Key Print A A Exec exec /home/wyatt/bin/xwdui.py
# Alt-Print Screen (fullscreen screenshot)
Silent Key Print A M Exec exec /home/wyatt/bin/xwdui-root.py
````

The keyword `Silent` is not strictly necessary, but suppresses errors on
keyboards which don't have a Print Screen key.

##### MATE
This can be done multiple ways in MATE, but the easiest is probably to run
`mate-keybinding-properties` and set it to run your script there via the GUI
interface.

Other options would include setting it up manually using `dconf` (CLI) or
`dconf-editor` (GUI).

Alternatively, MATE already has a screenshot tool
built-in, which is what my cheap little tool is meant to be a partial clone of.
It was the inspiration for my design. It's better than my tool in most ways,
so using that instead would be a viable option.

---

Those are all of the desktop environments I have used in recent times. If you
can't figure out how to do it in yours, ask me in a bug report and I'll
try to figure it out for you if I can.

