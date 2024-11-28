class Car:
    def __init__(self,modele,year,engine_capacity,price,mileage,*,wheels=4):
        self.modele=modele
        self.year=year
        self.engine_capacity=engine_capacity
        self.price=price
        self.mileage=mileage
        self.wheels=wheels


    def car_description(self):
        car_info=f"Модель:{self.modele},год:{self.year},V:{self.engine_capacity},цена:{self.price},пробег:{self.mileage},колёса:{self.wheels}"
        return car_info


class Track(Car):
    def __init__(self,modele,year,engine_capacity,price,mileage,*,wheels=8):
        super().__init__(modele,year,engine_capacity,price,mileage,wheels=8)
        self.chassis=wheels


    def car_description(self):
        car_info=f"Модель:{self.modele},год:{self.year},V:{self.engine_capacity},цена:{self.price},пробег:{self.mileage},колёса:{self.wheels}"
        return car_info

cargo_car=Car("ваз",2000,1500,50000,20000,wheels=4)
print(cargo_car.car_description())
cargo_track=Track("маз",2010,14500,2000000,100000,wheels=8)
print(cargo_track.car_description())