import FreeSimpleGUI as sg


# Проверяем корректны ли введённые данные
def is_valid(input_str):
    if not input_str.isalnum():
        print(
            f"В выбранной системе счисления используются только следующие символы:\n{alnum[:int(values["from"])]}"
        )
        return False
    elif input_str.isalnum():
        for c in input_str:
            if c.islower():
                c = c.upper()
            if c in alnum[: int(values["from"])]:
                continue
            else:
                print(
                    f"В выбранной системе счисления используются только следующие символы:\n{alnum[:int(values["from"])]}"
                )
                return False
        return True


# Функция переводит из десятичной системы счисления в любую другую
def from_10_to(num, rank):
    res = []
    rank = int(rank)
    while num >= rank:
        res.append(num % rank)
        num //= rank
    res.append(num)
    res.reverse()
    return res


def output(num):
    for i in num:
        if int(i) >= 10:
            i = alphabet[int(i) - 10]
        print(i, end="")


bit_nums = [str(i) for i in range(2, 37)]  # Здесь список всех разрядностей
digits = [str(i) for i in range(10)]  # Все цифры
alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]  # Английский алфавит
alnum = digits + alphabet

# Макет окна
layout = [
    [
        sg.Text("Перевести число из"),
        sg.Combo(
            bit_nums,
            key="from",
            default_value="10",
            readonly=True,
            tooltip="Выберите из какой системы счисления переводить",
        ),
        sg.Text("в"),
        sg.Combo(
            bit_nums,
            key="to",
            default_value="2",
            readonly=True,
            tooltip="Выберите в какую систему счисления переводить",
        ),
    ],
    [sg.Text("Введите число"), sg.InputText(key="number", size=(19, 1))],
    [sg.Output(key="output_text", size=(40, 5))],
    [sg.Button("Ввод"), sg.Button("Отмена")],
]


# Создаем окно
window = sg.Window("Калькулятор систем счисления", layout, size=(350, 200))
# Цикл для обработки "событий" и получения "значений" входных данных
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Отмена":
        break
    if event == "Ввод":
        window["output_text"].update("")  # Очищаем окно от прошлих выводов
        if is_valid(values["number"]):
            num_in_10 = int(values["number"], int(values["from"]))
            converted_num = from_10_to(num_in_10, values["to"])
            output(converted_num)

window.close()
