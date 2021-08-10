

class GameLostException(Exception):

    def __init__(self, msg='Вы проиграли. Жизней больше нет.', *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class GameWonException(Exception):

    def __init__(self, msg='Вы выйграли. Трудно быть героем?', *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)
