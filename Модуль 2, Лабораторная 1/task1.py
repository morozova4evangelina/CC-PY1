# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class RiverCrossing:
    def __init__(self, width_river: int, trajectory: int):
        """
        Создание и подготовка к работе объекта "Речная переправа"
        :param width_river: Ширина реки
        :param trajectory: Длина пути
        Примеры:
        >>> ferryboat = RiverCrossing(150, 0) # инициализация экземпляра класса
        """

        if not isinstance(width_river, int):
            raise TypeError("Введенная переменная не является целым числом")
        if width_river < 50:
            raise ValueError("Ширина реки для паромной переправы не может быть меньше 50м")
        self.width_rivers = width_river

        if not isinstance(trajectory, int):
            raise TypeError("Введенная переменная не является целым числом")
        if trajectory < 0:
            raise ValueError("Длина пути не моожет быть отрицательной")
        self.trajectory = trajectory

    def at_the_pier(self) -> bool:
        """
        Функция, которая проверяет находится ли паром у пристани
        :return: Паром стоит у пристани
        Примеры:
        >>> ferryboat = RiverCrossing(150, 0)
        >>> ferryboat.at_the_pier()
        """
        ...

    def crosses_the_river(self, way: int) -> None:
        """
        Функция, показывающая пройденный паромо путь
        :param way: Путь парома
        :raise ValueError: Если длина пройденного пути больше длины всего пути, то вызываем ошибку
        Примеры:
        >>> ferryboat = RiverCrossing(150, 0)
        >>> ferryboat.crosses_the_river(80)
        """
        if not isinstance(way, int):
            raise TypeError("Введенная переменная не является целым числом")
        if way <= 0:
            raise ValueError("Длина пройденного пути должна быть больше 0")



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
