class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, users: int):
        """

        :param users: Количество пользователей. Защищен, доступен вне класса только для чтения
        """
        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть типом integer")
        self._users = users

    @property   # Атрибут доступен только для чтения
    def users(self):
        return self._users

    def __str__(self):
        return f"Некая социальная сеть {self.__class__.__name__} имеет {self._users} пользователей."

    def __repr__(self):
        return f"SocialNetwork({self._users})"

    def increase_users(self, n: int):
        """
        Метод, увеличивающий количество пользователей
        :param n: Количество новых пользователей
        :return: None
        """
        self._users += n


class VK(SocialNetwork):
    """Дочерний класс для социальной сети ВКонтакте."""

    def __init__(self, users, groups):
        """

        :param users: Количество пользователей
        :param groups: Количество групп
        """
        super().__init__(users)
        self.groups = groups

    def __str__(self):
        return f"Социальная сеть {self.__class__.__name__} имеет {self._users} пользователей и {self.groups} групп."

    def __repr__(self):
        return f"VK({self.name}, {self._users}, {self.groups})"

    def increase_groups(self, n):
        """
        Метод увеличивающий количество групп
        :param n: Количество новых групп
        :return: None
        """
        self.groups += n


class Facebook(SocialNetwork):
    """Дочерний класс для социальной сети Facebook."""

    def __init__(self, users, pages):
        """

        :param users: Количество пользователей
        :param pages: Количество страниц
        """
        super().__init__(users)
        self.pages = pages

    def __str__(self):
        return f"Социальная сеть {self.__class__.__name__} имеет {self._users} пользователей и {self.pages} страниц."

    def __repr__(self):
        return f"Facebook({self.name}, {self._users}, {self.pages})"

    def increase_pages(self, n):
        """
        Метод увеличивает количество страниц
        :param n: Колдичество новых страниц
        :return: None
        """
        self.pages += n

    def increase_users(self, n):
        """
        Метод увеличивает количество страниц и выводит сообщение о факте увеличения
        :param n:
        :return:
        """
        self._users += n
        print(f"Number of users increased by {n}")
