import PySimpleGUI as sg

layout = [[sg.Button('Listen', key='Listen')],
          [sg.Text('ここに受信内容が表示されます', key='-DATA-')],]

def init_window():
    sg.theme('LightGreen3')
    window = sg.Window('app', layout)
    return window