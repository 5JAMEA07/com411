class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0):
        self.name = name,
        self.age = age,
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")


if __name__ == "__main__":
    robot = Robot()
    robot.display()
