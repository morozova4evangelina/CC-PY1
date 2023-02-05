class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Общий класс - книга.
        :param name: str - название книги
        :param author: str - автор книги
        """

        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Название книги должно быть типа str")

        if isinstance(author, str):
            self._author = author
        else:
            raise ValueError("Автор книги должен быть типа str")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

class PaperBook(Book):
    """ Конкретизированный тип книги - бумажная книга. """
    def __init__(self, name: str, author: str, pages: int):
        """
        Вид книги - бумажная книга.
        :param name: str - название книги
        :param author: str - автор книги
        :param pages: int, gt = 0 - количество страниц книги
        """

        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("Количество страниц книги должно быть типа int")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """ Конкретизированный тип книги - аудиокнига. """
    def __init__(self, name: str, author: str, duration: float):
        """
        Вид книги - аудоикнига.
        :param name: str - название книги
        :param author: str - автор книги
        :param duration: float, gt=0 - продолжительность аудиокниги
        """

        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if isinstance(duration, float) and duration > 0:
            self._duration = duration
        else:
            raise ValueError("Продолжительность аудиокниги должно быть типа float")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"
