import PySimpleGUI as sg      

layout = [[sg.Text('Teste')],      
                 [sg.Button("7")],      
                 [sg.Button("4")],
                 [sg.Button("1")]]      

window = sg.Window('Calculadora', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)