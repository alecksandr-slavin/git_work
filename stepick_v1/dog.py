class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'{name} говорит: "Привет!"')


class RollOveMixin:
    def roll_over(self):
        print('Сделка кувырок!')


class Dog(SpeakMixin, RollOveMixin):
    pass


dog = Dog()
dog.speak()
dog.roll_over()
