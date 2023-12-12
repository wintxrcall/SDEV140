#
#
#
from car import Car
from rocket_car import RocketCar

# car = Car(heading='N', x=0, y=0)
# car.move(1.0)
# car.turn_right()
# car.move(1.0)
# car.turn_right()
# car.move(1.rocket_0)
# car.turn_right()

rocket_car = RocketCar(
    heading='N',
    x=0,
    y=0,
    fuel = 2.0)
rocket_car.move(1)
rocket_car.toggle_rocket_fuel()
rocket_car.move(5)


# rocket_car.move(1.0)
# rocket_car.turn_right()
# rocket_car.move(1.0)
# rocket_car.turn_right()
# rocket_car.move(1.0)
# rocket_car.turn_right()
# rocket_car.move(1.0)