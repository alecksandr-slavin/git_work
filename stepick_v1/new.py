from datetime import datetime


class Greeter:
    def __init__(self, name):
        self.name = name

    def day():
        return datetime.now().strftime('%A')

    def part_of_day():  # Определяет часть, дня основываясь на текущем часе
        current_hour = datetime.now().hour

        if current_hour < 12:
            part_of_day = "утра"
        elif 12 <= current_hour < 17:
            part_of_day = 'дня'
        else:
            part_of_day = 'вечера'

        return part_of_day

    def greet(self, store): # Выводит приветствие, используя все расчетные составляющие
        print(f'Здраствуйте, меня зовут  {self.name}, и добро пожаловать'
              f'в {store}!')
        print(f'Желаем вам  приятного {day()} {part_of_day()}')
        print('Дарим вам купон на скидку 20%!')
