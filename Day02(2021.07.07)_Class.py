###类的基础学习
###书上的例子
###属性：类中的形参和实参 方法：类中的具体函数

###将一个类作为另一个类的属性
class Wheel():
    def __init__(self, maker, size):
        self.maker = maker
        self.size = size

    def wheel_description(self):
        print("This wheel is " + str(self.size) + " maked by " + self.maker)


class Car():
    '''模拟汽车的简单尝试'''

    def __init__(self, make, model, year, maker, size):
        self.make = make
        self.model = model
        self.year = year
        self.maker = maker
        self.size = size
        self.odometer_reading = 0
        self.gas_tank = 50
        self.wheel = Wheel(self.maker, self.size)  ###将Wheel类作为Car类的一个属性

    def get_descriptive(self):
        long_name = self.make + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()

    '''修改属性的值'''

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        print('当前里程数为' + str(self.odometer_reading))

    def increment_odometer(self, miles):
        self.odometer_reading += miles  ###mileage和miles为外部形参
        print('当前里程数为' + str(self.odometer_reading))

    def fill_gas_tank(self):
        print("This car's gas tank is " + str(self.gas_tank))


###类的继承
###子类继承父类的所有属性和方法，同时可以定义自己的属性和方法
###父类必须包含在当前文件中，且位于子类的前面
class ElectricCar(Car):
    '''对Car类的继承'''

    def __init__(self, make, model, year, maker, size):  ###初始化父类的属性
        super().__init__(make, model, year, maker, size)  ###super()是一个特殊函数，帮助父类和子类关联起来
        self.battery_size = 100

    '''给子类定义属性和方法'''

    def describe_battery(self):
        print('Battery size is ' + str(self.battery_size))

    '''重写父类的方法'''

    def fill_gas_tank(self):
        print("This car has no gas tank")  ###改写父类中的函数，调用时忽略父类的同名函数


my_car = Car('audi', 'a4', 2021, "maker1", 20)
print(my_car.get_descriptive())
my_car.update_odometer(1000)
my_car.increment_odometer(100)
my_car.fill_gas_tank()
my_car.wheel.wheel_description()
my_byd_car = ElectricCar('BYD', "秦", 2021, "maker2", 30)
print(my_byd_car.get_descriptive())
my_byd_car.describe_battery()
my_byd_car.fill_gas_tank()
my_byd_car.wheel.wheel_description()