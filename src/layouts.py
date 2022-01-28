import imp
import PySimpleGUI as sg
import os
from .qr import createQR


def qrLayouts():
    layouts = [
        [sg.Push(), sg.Text("QR GENERATE"), sg.Push()],
        [sg.Text("Enter the URL or Message", size=(25,1)),sg.InputText(key="-INP-", do_not_clear=False)],
        [sg.Text("Enter the file name", size=(25,1)),sg.InputText(key="-FILE-", do_not_clear=False)],
        [sg.Text("Output Path", size=(25,1)),sg.InputText(key="-PATH-", do_not_clear=False), sg.FolderBrowse()],
        [sg.Text("Picture type", size=(25,1)),sg.Combo(["png","jpeg","jpg"], key="-TYPE-")],
        [sg.Button("Ok"), sg.Button("cancle")],
    ]

    return layouts

def mainProgram(title : str, layouts : list):
    windows = sg.Window(title, layouts, resizable=True)

    while True:
        event, values = windows.read()

        if event in (sg.WINDOW_CLOSED, "cancle"):
            break

        if event == "Ok":
            try:
                s = values["-INP-"]
                fileName = values["-FILE-"]
                path = values["-PATH-"]
                type = values["-TYPE-"]

                createQR(s,fileName,path, type)
                os.system(f"explorer {path}")
                sg.Popup("Success")

            except Exception as e:
                sg.Popup(f"{e}")