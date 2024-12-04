# Задание 3
# -------------------------------------------------------------------------
# Перед оформлением заявки на получение кредита потенциальный заемщик
# проходит ряд автоматических стоп-проверок. Если хотя бы одну из этих
# проверок клиент не прошел, то банк вправе отказать ему в выдаче кредита.
# -------------------------------------------------------------------------
# Напишите функцию, которая выполняет расчет указанных ниже стоп-проверок
# клиента. Функция должна получать входным аргументом JSON, указанный выше, и
# возвращать true, если клиент успешно прошел все проверки (т.е. не получил
# отказ), иначе возвращать false.
# Функцию можно написать на любом языке программирования (JS будет плюсом).
# Сам текст функции необходимо сохранить на сервисе onecompiler.com и прислать
# ее в ответе.
from datetime import datetime
import json

def Check(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    birthDate = datetime.strptime(data["birthDate"], '%Y-%m-%dT%H:%M:%S.%fZ')
    issuedAt = datetime.strptime(data["passport"]["issuedAt"], '%Y-%m-%dT%H:%M:%S.%fZ')

    years = check1(birthDate)
    if years:
        if check2(years, birthDate, issuedAt):
            if check3(data["creditHistory"]):
                return True
    return False

# Проверка 1. Минимальный возраст.
# Если клиент моложе 20 лет – отказ.
def check1(birthDate):
    x = ((datetime.now().month, datetime.now().day) < (birthDate.month, birthDate.day))
    y = datetime.now().year - birthDate.year - x
    if y > 20:
        return y
    else:
        return False

# Проверка 2. Проверка действительности паспорта.
# Если возраст клиента более 20 лет и дата выдачи паспорта ранее, чем дата
# достижения им возраста 20 лет, либо если возраст клиента более 45 лет и дата
# выдачи паспорта ранее, чем дата достижения им возраста 45 лет - отказ.
def check2(years, birthDate, issuedAt):
    if years > 20 and years < 45 and issuedAt > birthDate.replace(year=birthDate.year + 20):
        return True
    elif years > 45 and issuedAt > birthDate.replace(year=birthDate.year + 45):
        return True
    else:
        return False

# Проверка 3. Проверка кредитной истории.
# Наличие в кредитной истории в Банке хотя бы одного из условий приводит к
# отказу.
# Если тип кредита не «Кредитная карта», то проверяется:
# 1. Имеется непогашенная просроченная задолженность.
# 2. Возникала просроченная задолженность протяженностью более 60 дней.
# 3. Есть больше двух кредитов с просроченной задолженностью
# протяженностью более 15 дней.
# Если тип кредита «Кредитная карта», то проверяется:
# 1. Имеется непогашенная просроченная задолженность.
# 2. Возникала просроченная задолженность протяженностью более 30 дней.
def check3(creditHistory):
    n = 0
    for i in range (len(creditHistory)):
        if creditHistory[i]["type"] == "Кредитная карта":
            if (creditHistory[i]["currentOverdueDebt"] != 0 or
                creditHistory[i]["numberOfDaysOnOverdue"] > 30):
                return False
        else:
            if (creditHistory[i]["currentOverdueDebt"] != 0 or
                  creditHistory[i]["numberOfDaysOnOverdue"] > 60):
                return False
            elif creditHistory[i]["numberOfDaysOnOverdue"] > 15:
                n += 1
    if n > 2:
        return False
    else:
        return True

