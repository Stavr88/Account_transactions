
import datetime


class Operation:
    """
    Создает класс с атрибутами из файла .json
    """
    def __init__(self, pk: int,
                 date: str,
                 state: str,
                 amount: str,
                 currency_name: str,
                 description: str,
                 from_: str,
                 to: str):
        self.pk = pk
        self.date = date
        self.amount = amount
        self.state = state
        self.currency_name = currency_name
        self.description = description
        self.from_ = self.convert_from_to(from_) if from_ is not None else ''
        self.to = self.convert_from_to(to)

    def date_format(self) -> str:
        """
        Форматирует дату
        :return: str
        """
        time_operate = (datetime.datetime.fromisoformat(self.date))
        return time_operate.strftime('%d.%m.%Y')

    def convert_from_to(self, description_: str) -> str:
        """
        Маскирует номер счета/карты
        :param description_: str
        :return: str
        """
        if description_.startswith("Счет"):
            return f'Счет **{description_[-4:]}'
        else:
            str_desc = ''
            str_desc1 = ''
            for i in description_[-10:-8]:
                str_desc += "*"
            for i in description_[-8:-4]:
                str_desc1 += "*"
            return (f"{description_[0:-16]}{description_[-16:-12]} "
                    f"{description_[-12:-10]}"
                    f"{str_desc} "
                    f"{str_desc1} "
                    f"{description_[-4:]}")

    # return f"{description_[0:-10]}{str_desc}{description_[-4:]}"
    def __lt__(self, other):
        """
        Сравнивает два экземпляра по дате, определяет наименьший из них и возращает bool значения
        :param other:
        :return: True or False
        """
        return self.date < other.date

    def __gt__(self, other):
        """
        Сравнивает два экземпляра по дате, определяет наибольшее из них и возращает bool значения
        :param other:
        :return: True or False
        """
        return self.date > other.date

    def __str__(self):
        date = self.date_format()
        return (f'{date} {self.description}\n' 
                f'{self.from_} -> {self.to}\n'
                f'{self.amount} {self.currency_name}')



