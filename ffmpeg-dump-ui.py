#! /bin/env python3
import tkinter as tk
import os
import sys

# path to the file which will contain the last run's settings, if set.
fileName=os.path.expanduser("~") + "/.xwdui"
# these vars are global because the script's too small for me to want to care
# otherwise.
targetPath=''
targetName=''
if(not os.path.exists(fileName)):
    f=open(fileName,'w')
else:
    f=open(fileName,'r+')

class MyApp(tk.Tk):
    def __init__(self):
        global f
        global targetPath
        global targetName
        tk.Tk.__init__(self)
        self.label=tk.Label(self,text="Directory to save image in:").grid(row=0, column=0, sticky=tk.W)
        self.dirEntry = tk.Entry(self)
        self.dirEntry.config(width=30)
        self.dirEntry.grid(row=0, column=1)
        self.label2=tk.Label(self,text="Filename (if empty, use timestamp):").grid(row=1,column=0, sticky=tk.W)
        self.fNameEntry = tk.Entry(self)
        self.fNameEntry.grid(row=1, column=1)
        self.fNameEntry.config(width=30)
        f.seek(0)
        targetPath=f.readline()
        targetName=f.readline()
        if targetPath=='' or targetPath=='\n':
            # the file contains no useful info (could be corrupt). Erase it and re-open
            print("I think your 'previous session' file might be corrupt; erasing contents.")
            f.close()
            f=open(fileName,'w')
            targetpath=''
            targetName=''
        else:
            # Remove trailing newlines if present.
            # Yeah, I went a little overboard.
            targetPath=targetPath.rstrip("\r\n")
            targetPath=targetPath.rstrip("\n\r")
            targetPath=targetPath.rstrip("\n")
            targetPath=targetPath.rstrip("\r")

            targetName=targetName.rstrip("\r\n")
            targetName=targetName.rstrip("\n\r")
            targetName=targetName.rstrip("\n")
            targetName=targetName.rstrip("\r")
        print("read path:     "+targetPath+" from file.")
        print("read filename: "+targetName+" from file.")
        self.dirEntry.insert(0,targetPath)
        self.fNameEntry.insert(0,targetName)
        targetPath=f.readline()
        self.button2=tk.Button(self, text="Cancel", command=self.destroy)
        self.button2.grid(row=2, column=0, columnspan=1)
        self.button=tk.Button(self, text="Take Screenshot", command=self.close)
        self.button.grid(row=2, column=1, columnspan=2)
    def closeEnter(self,event):
        self.close()
    def close(self):
        global result
        global f
        self.string = self.dirEntry.get()
        self.string2 = self.fNameEntry.get()
        # Write the entered path into our storage file
        if self.string != '' and self.string != '\n':
            f.close()
            f=open(fileName, 'w')
            f.write(self.string+'\n')
        if self.string2 != '' and self.string2 != '\n':
            f.write(self.string2+'\n')
        # close the file
        f.close()
        self.destroy()

    def mainloop(self):
        mainWin=tk.Tk.mainloop(self)
        try:
            self.string
        except AttributeError:
            return
        else:
            return [self.string, self.string2]

# Run the thing
app = MyApp()
app.title("Screenshot a Window")
# Allow pressing the enter/return key instead of clicking "Take a Screenshot!"
app.bind('<Return>',app.closeEnter)
# 'Result' is a list of strings.
result = app.mainloop()
# result[0] is the directory path
# result[1] is the filename (if empty, ignored).
try:
    result[0]
except:
    pass
else:
    print("you entered: "+result[0]+" "+result[1])

    # -b used to show window decorations
    # -m would show cursor if added
    params = [ 'ffmpeg-dump', '-b', result[0] ]
    if result[1]:
        params.append(result[1])

    os.execvp('ffmpeg-dump', params)

# prevent injections by not using system()
# if not result[1]: # if the filename string is empty
# #    os.system("ffmpeg-dump "+'"'+result[0]+'"')
#     os.system("ffmpeg-dump -b "+'"'+result[0]+'"')
# else: # if the filename string is not empty
# #    os.system("ffmpeg-dump "+'"'+result[0]+'"'+" "+'"'+result[1]+'"')
#     os.system("ffmpeg-dump -b "+'"'+result[0]+'"'+" "+'"'+result[1]+'"')
