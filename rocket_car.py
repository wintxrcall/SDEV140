from car import Car

class RocketCar(Car):

######## Private Methods
    def __init__(
        self, 
        heading: str = 'N', 
        x: float = 0.0, 
        y: float = 0.0, 
        fuel: float = 2.0
    ) -> None:


        super().__init__(
            heading=heading,
            x=x,
            y=y,
        )

        self._BASE_VELOCITY = 2.0
        self._ROCKET_VELOCITY = 10.0
        self._use_rocket_fuel = False
        self._minutes_of_fuel = fuel

        self._velocity = self._BASE_VELOCITY


###### Public Methods
    def toggle_rocket_fuel(self):
        self._use_rocket_fuel = not self._use_rocket_fuel
        if self._use_rocket_fuel:
            print('Rocket fuel is now on.')
            self._velocity = self._ROCKET_VELOCITY
        else:
            print('Rocket fuel is now off.')
            self._velocity = self._BASE_VELOCITY


##### OVERRIDES
    def move(self, time: float = 1.0) -> None:
        
        if self._use_rocket_fuel:
            # determine if we have enough fuel for request
            fueled_move = min(self._minutes_of_fuel, time)
            unfueled_move = time - fueled_move

            #update the fuel level
            self._minutes_of_fuel -= fueled_move

            # move(with the rocket fuel)
            super().move(fueled_move)

            if fueled_move < time:
                print('Out of fuel!')
                self.toggle_rocket_fuel()
                super().move(unfueled_move)
        else:
            super().move(time) 