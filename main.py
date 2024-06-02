import PySimpleGUI as sg
import random



layout = [[sg.Button('Новое число',enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
        [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

def update():
    # получаем новое случайное число
    r = random.randint(1,100)
    # получаем доступ к текстовому элементу
    text_elem = window['-text-']
    # выводим в него текст с новым числом
    text_elem.update("Результат: {}".format(r))


window = sg.Window('Генератор случайных чисел', layout, size=(350,100))


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-FUNCTION-':
        update()

window.close()