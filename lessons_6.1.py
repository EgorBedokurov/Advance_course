class Robots:

    def __init__(self, model, date_dev, modification):
        self.model = model
        self.date_dev = date_dev
        self.modification = modification

    def creat_robots(self):
        print('create robot ' + self.model + self.date_dev + self.modification)

class SpotMini(Robots):
    """колличество прыжков"""
    def __init__(self, model, date_dev, modification, amount):
        Robots.__init__(self, model, date_dev, modification)
        self.amount = amount

    """приказ прыгнуть"""
    def robot_jump(self):
        print('SpotMini jump ' + self.amount + '\n')

class Atlas(Robots):
    """скорость бега"""
    def __init__(self, model, date_dev, modification, run):
        Robots.__init__(self, model, date_dev, modification)
        self.run = run

    """приказать роботу бежать"""
    def robot_run(self):
        print('Atlas run ' + self.run + '\n')

class Handle(Robots):
    """скорость бега"""
    def __init__(self, model, date_dev, modification, hello):
        Robots.__init__(self, model, date_dev, modification)
        self.hello = hello

    """приказать роботу говорить"""
    def robot_hello(self):
        print('Handle says - ' + self.hello + '\n')

robots = Robots('SpotMini, Atlas, Handle ', '2015e. ', 'demo_1 ')
robots.creat_robots()

robots1 = SpotMini('SpotMini ', '2016y. ', 'demo_2.0', '4 times')
robots1.creat_robots()
robots1.robot_jump()

robots2 = Atlas('Atlas ', '2016y. ', 'demo_2.1', '15 km/h')
robots2.creat_robots()
robots2.robot_run()

robots3 = Handle('Handle ', '2016y. ', 'demo_1.1', 'kill all leather bags')
robots3.creat_robots()
robots3.robot_hello()

print(issubclass(SpotMini, Robots))
print(issubclass(Atlas, Robots))
print(issubclass(Handle, Robots))
