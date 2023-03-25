class Robot:

    def __init__(self, model):
        self.model = model

    def info(self):
        print("I am a robot")


class Flying:

    def __init__(self, model, height, speed):
        self.model = model
        self.height = height
        self.speed = speed

    def take_of(self):
        print("Пристегнитесь, мы взлетаем")

    def fly(self):
        print("Лечу")

    def land(self):
        print("Сажусь")


class ReconnaissanceDrone(Robot, Flying):

    def __init__(self, model, coordinate=0):
        super().__init__(model=model)
        self.coordinate = coordinate

    def operate(self, coordinate):
        self.coordinate += 1
        print("Веду разведку с воздуха")


class MilitaryRobot(Robot, Flying):

    def __init(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self, gun):
        print(f"Защищаю военный объект с помощью {gun}")


my_warrior = MilitaryRobot('M1')
drone = ReconnaissanceDrone('M2')

my_warrior.operate('gun')
drone.operate(1)