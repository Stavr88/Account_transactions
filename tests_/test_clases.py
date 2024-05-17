from Account_transactions.utilit.clases import Operation


def test_date_format():
    operation_1 = Operation(pk=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            amount="31957.58",
                            currency_name="руб.",
                            description="Перевод организации",
                            from_="Maestro 1596837868705199",
                            to="Счет 64686473678894779589"
                            )
    assert operation_1.date_format() == "26.08.2019"


def test_date_format():
    operation_1 = Operation(pk=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            amount="31957.58",
                            currency_name="руб.",
                            description="Перевод организации",
                            from_="Maestro 1596837868705199",
                            to="Счет 64686473678894779589"
                            )
    assert operation_1.convert_from_to("Maestro 1596837868705199") == "Maestro 159683******5199"


def test_date_format():
    operation_1 = Operation(pk=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            amount="31957.58",
                            currency_name="руб.",
                            description="Перевод организации",
                            from_="Maestro 1596837868705199",
                            to="Счет 64686473678894779589"
                            )
    assert operation_1.convert_from_to("Счет 64686473678894779589") == "Счет ** 9589"


def test_from_to():
    operation_1 = Operation(pk=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            amount="31957.58",
                            currency_name="руб.",
                            description="Перевод организации",
                            from_="Maestro 1596837868705199",
                            to="Счет 64686473678894779589"
                            )
    assert operation_1.from_ == 'Maestro 159683******5199'
    assert operation_1.to == "Счет ** 9589"


def test_str():
    operation_1 = Operation(pk=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            amount="31957.58",
                            currency_name="руб.",
                            description="Перевод организации",
                            from_="Maestro 1596837868705199",
                            to="Счет 64686473678894779589"
                            )
    assert str(operation_1) == (
        "26.08.2019 Перевод организации\n" 
        "Maestro 159683******5199 -> Счет ** 9589\n"
        "31957.58 руб."
    )






