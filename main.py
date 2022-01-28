from ctypes import resize
import PySimpleGUI as sg
from src.layouts import qrLayouts,mainProgram

def main():
    sg.theme("DarkAmber")

    layout = [
        qrLayouts()
    ]

    mainProgram("QR Generate", layout)


if __name__ == "__main__":
    main()

