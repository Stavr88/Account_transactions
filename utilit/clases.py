
class Operation:
    def __init__(self, pk: str, date: str, state: str, amount: str, currency_name: str, description: str, from_: str, to: str):
        self.pk = pk
        self.date = date
        self.amount = amount
        self.state = state
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

    def __str__(self):
        return f'{__dict__}'
    pass

