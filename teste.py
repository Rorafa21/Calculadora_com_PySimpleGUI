from re import S
import PySimpleGUI as sg      

layout = [[sg.Text('Teste')],      
                 [sg.Button("7", font=("Consolas", 20), key="-SEVEN-"),      
                  sg.Button("8"),
                  sg.Button("9")],

                 [sg.Button("4"),
                  sg.Button("5"),
                  sg.Button("6")]]    


window = sg.Window('Calculadora', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)