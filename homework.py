from typing import Union

class InfoMessage:
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        #Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.
    def get_message(self) -> str:
        message: Union [str, float] =  (f'Тип тренировки {self.training_type} ;'
                                        f'Длительность тренировки {self.duration} ч.;'
                                        f'Дистанция {self.distance} км;'
                                        f'Средняя скорость {self.speed}км;'
                                        f'Расход калорий {self.calories};')
        return str(message)
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM 
        """Получить дистанцию в км."""


    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
        """Получить среднюю скорость движения."""


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight
    def get_distance(self):
        return self.action * self.LEN_STEP
    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    def get_spent_calories(self) -> float:
        return (18 * self.get_mean_speed() - 20) * self.weight/ self.M_IN_KM * self.duration
        #(18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах

    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self, action, duration, weight, height):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.height = height
    def get_distance(self):
        return self.action * self.LEN_STEP
    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    def get_spent_calories(self) -> float:
        return (0.035 * self.weight + (self.get_mean_speed() ** 2 // self.height) * 0.029 * self.weight) * self.duration
        #(0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
    
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    LEN_STEP = 1.38
    M_IN_KM = 1000
    def __init__(self, action, duration, weight,length_pool, count_pool):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.length_pool = length_pool
        self.count_pool = count_pool
    def get_distance(self):
        return self.action * self.LEN_STEP / self.M_IN_KM
    def get_mean_speed(self) -> float:
       return self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        #длина_бассейна * count_pool / M_IN_KM / время_тренировки
    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() +1.1) * 2 * self.weight
        #(средняя_скорость + 1.1) * 2 * вес 

    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    if workout_type == 'SWM':
        return Swimming(*data)
    if workout_type == 'RUN':
        return Running(*data)
    if workout_type == 'WLK':
        return SportsWalking(*data)
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    info = training.show_training_info()
    print (info)
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

