import json
import os.path
from random import uniform
from argparse import ArgumentParser

CONFIG_FILENAME = 'config.json'
CONFIG_TMP_FILENAME = 'relevant_config.json'


def read_file_config(CONFIG_TMP_FILENAME):
    """Читання файлу конфігурації json з заданим ім'ям"""
    with open(CONFIG_TMP_FILENAME, 'r') as json_file:
        info = json.load(json_file)
    return info


def recording_tmp_config(data_config):
    """збереження в файл конфігурацій json з заданим ім'ям """
    with open(CONFIG_TMP_FILENAME, 'w') as json_file:
        json.dump(data_config, json_file)


def get_config():
    """функція створення нового файлу конфігурації """
    if os.path.isfile(CONFIG_TMP_FILENAME):
        info = read_file_config(CONFIG_TMP_FILENAME)
    else:
        info = restart()
    return info


def rate(info):
    """Поточний курс валютної пари, в нашому випадку UAH до USD"""
    print(info['exchange_rate'])


def available(info):
    """Поточний стан на рахунку у валютах"""
    print(f"USD {info['USD']} UAH {info['UAH']}")


def buy_xxx(usd_amount, info):
    """Купівля валюти(USD) вказаної кількості"""
    recount = round(usd_amount * info['exchange_rate'], 2)
    if (info['UAH'] - recount) > 0:
        info['UAH'] = round(info['UAH'] - recount, 2)
        info['USD'] = round(info['USD'] + usd_amount, 2)
        recording_tmp_config(info)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {recount}, AVAILABLE {info['UAH']}")


def sell_xxx(usd_amount, info):
    """Продаж валюти(USD) вказаної кількості"""
    if usd_amount <= info['USD']:
        info['UAH'] = round(info['UAH'] + usd_amount * info['exchange_rate'], 2)
        info['USD'] = round(info['USD'] - usd_amount, 2)
        recording_tmp_config(info)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {info['USD']}")


def buy_all(info):
    """Купівля валюти (USD) на всі кошти на рахунку (UAH)"""
    if info['UAH'] > 0.01 * info['exchange_rate']:
        currency_quantity = round(info['UAH'] / info['exchange_rate'], 2)
        info['USD'] = round(info['USD'] + currency_quantity, 2)
        info['UAH'] = round(info['UAH'] - currency_quantity * info['exchange_rate'], 2)
        if info['UAH'] < 0:
            info['UAH'] = info['UAH'] + 0.01 * info['exchange_rate']
            info['USD'] = info['USD'] - 0.01
        recording_tmp_config(info)


def sell_all(info):
    """Продаж всієї валюти (USD) і конвертація у валюту (UAH)"""
    if info['USD'] > 0:
        info['UAH'] = round(info['UAH'] + info['USD'] * info['exchange_rate'], 2)
        info['USD'] -= info['USD']
        recording_tmp_config(info)


def next(info):
    """Зміна поточного курсу в межах діапазону за рахунок 'delta' """
    info['exchange_rate'] = round(uniform(info['exchange_rate'] - info['delta'],
                                          info['exchange_rate'] + info['delta']), 2)
    recording_tmp_config(info)


def restart():
    """Створення нового файлу з початковими конфігураціями"""
    info = read_file_config(CONFIG_FILENAME)
    recording_tmp_config(info)
    return info


args = ArgumentParser()
args.add_argument('command')
args.add_argument('second_argument', type=str, nargs='?', default=0)  # створив другий аргумент типу "універсальній"
args = vars(args.parse_args())
command = args['command']
second_argument = args['second_argument']

info = get_config()

if command == 'RATE':
    rate(info)
elif command == 'AVAILABLE':
    available(info)
elif command == 'BUY':
    if second_argument == 'ALL':
        buy_all(info)
    else:
        buy_xxx(float(second_argument), info)
elif command == 'SELL':
    if second_argument == 'ALL':
        sell_all(info)
    else:
        sell_xxx(float(second_argument), info)
elif command == 'NEXT':
    next(info)
elif command == 'RESTART':
    restart()
