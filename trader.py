import json
from os import path
from random import uniform
from argparse import ArgumentParser


def open_file_config(file_name):
    """Відкривання файлу конфігурації json для читання з заданим ім'ям"""
    if path.isfile(f'{file_name}.json') == False:
        with open('config.json', 'r') as json_file:
            info = json.load(json_file)
            return info
    with open(f'{file_name}.json', 'r') as json_file:
        info = json.load(json_file)
    return info


def recording_file_config(file_name, something):
    """збереження в файл конфігурацій json з заданим ім'ям """
    with open(f'{file_name}.json', 'w') as json_file:
        json.dump(something, json_file)

def create_config_file():
    """функція створення нового файлу конфігурації """
    open_file_config(file_name)
    recording_file_config(file_name, something=open_file_config(file_name))

def rate():
    '''Повертає поточний курс валютної пари, в нашому випадку UAH до USD'''
    return open_file_config(file_name)['exchange_rate']


def available():
    """Повертає поточний стан на рахунку у валютах"""
    return f"USD {open_file_config(file_name)['USD']} UAH {open_file_config(file_name)['UAH']}"


def buy_xxx(xxx):
    """Купівля валюти(USD) вказаної кількості"""
    info = open_file_config(file_name)
    recount = round(xxx*info['exchange_rate'], 2)
    if (info['UAH'] - recount) > 0:
        info['UAH'] = round((info['UAH'] - recount), 2)
        info['USD'] = round((info['USD'] + xxx), 2)
        recording_file_config(file_name, info)
    else:
        return f"UNAVAILABLE, REQUIRED BALANCE UAH {recount}, AVAILABLE {info['UAH']}"


def sell_xxx(xxx):
    """Продаж валюти(USD) вказаної кількості"""
    info = open_file_config(file_name)
    if xxx <= info['USD']:
        recount = xxx * info['exchange_rate']
        info['UAH'] = round((info['UAH'] + recount), 2)
        info['USD'] = round((info['USD'] - xxx), 2)
        recording_file_config(file_name, info)
    else:
        return f"UNAVAILABLE, REQUIRED BALANCE USD {xxx}, AVAILABLE {info['USD']}"

def buy_all():
    """Купівля валюти (USD) на всі кошти на рахунку (UAH)"""
    info = open_file_config(file_name)
    if info['UAH'] > 0.01*info['exchange_rate']:
        currency_quantity = round(info['UAH']/info['exchange_rate'], 2)
        info['USD'] = round(info['USD'] + currency_quantity, 2)
        info['UAH'] = round(info['UAH'] - currency_quantity*info['exchange_rate'], 2)
        if info['UAH'] < 0:
            info['UAH'] = round((info['UAH'] + 0.01*info['exchange_rate']), 2)
            info['USD'] = round(info['USD'] - 0.01, 2)
        recording_file_config(file_name, info)
    else:
        return f"UNAVAILABLE, AVAILABLE UAH {info['UAH']}"

def sell_all():
    """Продаж всієї валюти (USD) і конвертація у валюту (UAH)"""
    info = open_file_config(file_name)
    if info['USD'] > 0:
        currency_quantity = info['USD']*info['exchange_rate']
        info['USD'] -= info['USD']
        info['UAH'] = round(info['UAH'] + currency_quantity, 2)
        recording_file_config(file_name, info)
    else:
        return f"UNAVAILABLE, AVAILABLE  USD {info['USD']}"


def next():
    """Зміна поточного курсу в межах діапазону за рахунок 'delta' """
    # existence_check()
    info = open_file_config(file_name)
    info['exchange_rate'] = round(uniform(info['exchange_rate']-info['delta'],
                                          info['exchange_rate']+info['delta']), 2)
    recording_file_config(file_name, info)

def restart():
    """Скидання всіх налаштувань, створення нового файлу з початковими конфігураціями"""
    open_file_config('config')
    recording_file_config(file_name, something=open_file_config('config'))



file_name = 'relevant_config'
create_config_file()

args = ArgumentParser()
args.add_argument('command')
args.add_argument('second_argument', type=str, nargs='?', default=0)    # створив другий аргумент типу "універсальній"
args = vars(args.parse_args())                                          # (не знаю наскільки це дозволено)
command = args['command']
# command = args['command'].upper()                          # написав, бо чомусь не працює верхній регістр у терміналі
second_argument = args['second_argument']
# second_argument = args['second_argument'].upper()          # написав, бо чомусь не працює верхній регістр у терміналі
if command == 'RATE':
    variable = rate()
    print(variable)
elif command == 'AVAILABLE':
    variable = available()
    print(variable)
elif command == 'BUY':
    if second_argument == 'ALL':
        variable = buy_all()
        print(variable) if variable != None else None       # якщо без тернарного оператора прінтує None
    else:
        second_argument = float(second_argument)            # відбувається перетворення, якщо ввели число а не "ALL"
        variable = buy_xxx(second_argument)
        print(variable) if variable != None else None
elif command == 'SELL':
    if second_argument == 'ALL':
        variable = sell_all()
        print(variable) if variable != None else None
    else:
        second_argument = float(second_argument)            # відбувається перетворення, якщо ввели число а не "ALL"
        variable = sell_xxx(second_argument)
        print(variable) if variable != None else None
elif command == 'NEXT':
    next()
elif command == 'RESTART':
    restart()





