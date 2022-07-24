from argparse import ArgumentParser
from utils import Trader

config_filename = "base_config.json"
base_config_filename = "config.json"

args = ArgumentParser()
args.add_argument("command", type=str, nargs='?', default=None)
args.add_argument("count", type=str, nargs='?', default=None)
args = vars(args.parse_args())

command = args['command']
count = args['count']

trader = Trader(base_config_filename=base_config_filename,
                config_filename=config_filename)

if command == "RESTART":
    trader.restart()
elif command == "RATE":
    trader.current_exchange()
elif command == "AVAILABLE":
    trader.available()
elif command == "NEXT":
    trader.next_rate()
elif command == "BUY":
    trader.buy(count)
elif command == "SELL":
    trader.sell(count)