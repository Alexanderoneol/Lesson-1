class Car:
    """Автомобиль"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машин поехала.")

    def stop(self):
        print(f"{self.name}: Машина остановилась.")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}.")

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    """Городской автомобиль"""

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!" \
             if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    """Грузовой автомобиль"""

    def show_speed(self):
        return f"{self.name}: Скороcть автомобиля: {self.speed}. Превышение скорости!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    """Спортивный автомобиль"""

    def show_speed(self):
        return f"{self.name}: Скороcть автомобиля: {self.speed}. Превышение скорости!" \
            if self.speed > 110 else f"{self.name}: Скорость автомобиля {self.speed}"




class PoliceCar(Car):
    """Полицейский автомобиль"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

        
police_car = PoliceCar('Полицейская', 'белый', 80)