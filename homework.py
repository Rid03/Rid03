class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
# Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} 
# км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.

    def get_message(self) -> str:
        message: str = (f'Тип тренировки: {self.training_type}; '
                        f'Длительность: {self.duration:.3f} ч.; '
                        f'Дистанция: {self.distance:.3f} км; '
                        f'Ср. скорость: {self.speed:.3f} км/ч; '
                        f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км.""" # action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения.""" # преодоленная_дистанция_за_тренировку/время_тренировки
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий.""" # не трогаем
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        return (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration * 60
        # (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return (0.035 * self.weight + (
                self.get_mean_speed() ** 2 // self.height) * 0.029 * self.weight) * self.duration * 60
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration
         # длина_бассейна * count_pool / M_IN_KM / время_тренировки

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight
         # (средняя_скорость + 1.1) * 2 * вес


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info().get_message()
    print(info)


if __name__ == '__main__':
    packages = [('SWM', [720, 1, 80, 25, 40]), ('RUN', [15000, 1, 75]), ('WLK', [9000, 1, 75, 180]), ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

