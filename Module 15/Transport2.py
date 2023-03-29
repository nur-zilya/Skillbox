from abc import ABC, abstractmethod

class MusicMixin:

    def play_music(self):
       print("""На теплоходе музыка играет,
                    а я стою на берегу""")



class Transport(ABC):

    def __init__(self, color, speed, sign):
        self.color = color
        self.speed = speed
        self.move = move
        self.sign = sign

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, val):
        self.color = val

    @abstractmethod
    def move_on_earth(self):
        pass


    @abstractmethod
    def move_on_water(self):
        pass


class Bus(Transport):

    def __init__(self, color, speed, sign):
        super().__init__(color, speed, sign)

    def move_on_earth(self):
        print("ride on earth")


class Boat(Transport):

    def __init__(self, color, speed, sign):
        super().__init__(color, speed, sign)

    def move_on_water(self):
        print("ride on water")


class Amphibian(Bus, Boat, MusicMixin):
    pass




