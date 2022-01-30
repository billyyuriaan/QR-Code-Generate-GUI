import PySimpleGUI as sg
import os
from src.qr import QRCode

class Window(QRCode):
    title : str
    theme : str
    resizeable : bool

    def __init__(self, title : str, theme : str, resizeable : bool):
        super().__init__()
        self.title = title
        self.theme = theme
        self.resizeable = resizeable

    def qrLayouts(self):
        layouts = [
            [sg.Push(), sg.Text("QR GENERATE"), sg.Push()],
            [sg.Text("Enter the URL or Message", size=(25,1)),sg.InputText(key="-INP-", do_not_clear=False)],
            [sg.Text("Enter the file name", size=(25,1)),sg.InputText(key="-FILE-", do_not_clear=False)],
            [sg.Text("Output Path", size=(25,1)),sg.InputText(key="-PATH-", do_not_clear=False), sg.FolderBrowse()],
            [sg.Text("Picture type", size=(25,1)),sg.Combo(["png","jpeg","jpg"], key="-TYPE-")],
            [sg.Button("Ok"), sg.Button("cancle")],
        ]

        return layouts

    def start(self):
        sg.theme(self.theme)

        layouts = [
            self.qrLayouts()
        ]

        windows = sg.Window(self.title, layouts, resizable=self.resizeable)

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

                    self.createQR(s,fileName,path, type)
                    os.system(f"explorer {path}")
                    sg.Popup("Success")

                except Exception as e:
                    sg.Popup(f"{e}")