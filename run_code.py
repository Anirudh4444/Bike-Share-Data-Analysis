import pyttsx3
import os
import pathlib
from file_read_backwards import FileReadBackwards
from subprocess import call
import tkinter as tk
from tkinter import filedialog

engine = pyttsx3.init('sapi5')
print(engine)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def choose_file():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
   # print(files,type(files),len(files))
    if not files:
        speak("Sorry , you haven't chosen any valid file ,Aborting ,run code "
              "command")
        print("You haven't chosen any valid file ,aborting run code "
              "command")
    if len(files) > 0:
        for file in files:
            # run_code(os.path.abspath(file))
            print(type(file))
            file=file.replace('/','\\\\')
            print(file)
            print(os.path.abspath(file))
choose_file()
# def run_code(filename):
#     # print(os.path.basename(filename).split(".")[0])
#     # print(os.path.basename(filename))
#     logfilename=os.path.basename(filename).split(".")[0]+"_log.txt"
#     with open(logfilename, 'w') as f:
#         speak("Running your code...")
#         print("Running your code...")
#         call(['python', filename], stdout=f,stderr=f)
#     strfile = open(logfilename, 'r').read()
#
#     if (('Error' in strfile) and ('line' in strfile) and ('File' in strfile)) or (strfile.find('Traceback') == 1):
#         with open(logfilename, 'r') as f:
#             file1=""
#             lastline = f.read().splitlines()[-1]
#             speak("The error or exception in your code is " + lastline.split(":")[0])
#             print("The error or exception in your code is " + lastline.split(":")[0])
#             speak("And the cause of your error is " + lastline.split(":", 1)[1])
#             print("And the cause of your error is " + lastline.split(":", 1)[1])
#             with FileReadBackwards(logfilename) as frb:
#                 flag = False
#                 for l in frb:
#                     if not flag:
#                         if 'line' and 'File' in l:
#                             flag = True
#                             trace = l.split(" ")
#                             file_name = trace[trace.index('File') + 1]
#                             file1=os.path.basename(filename)
#                             line_number = trace[trace.index('line') + 1]
#             speak("You might want to check line number " + line_number+" in module "+file1)
#             print("You might want to check line number " + line_number + " in module " + file1)
#         speak("for your reference I have saved the error information in " + logfilename + " file")
#     else:
#         print(strfile)
#         if strfile is None:
#             speak("The code ran without errors or exceptions "
#               "but has no output")
#             speak(strfile)
#         else:
#             speak("The code ran without errors or exceptions "
#               "and the output is ")
#             speak(strfile)
#             speak("for your reference I have save the output in "+logfilename+" file")