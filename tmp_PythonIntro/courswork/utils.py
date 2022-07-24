from tools import read_json_file, write_json_file


class BalanceData:
    def __init__(self, base_config_filename: str, config_filename: str):
        self._base_config_filename = base_config_filename
        self._config_filename = config_filename
        data = read_json_file(self._config_filename)
        self.rate = data["exchange_rate"]
        self.usd = data['USD']
        self.uah = data['UAH']
        self.delta = data['delta']

    def _build_data(self):
        data = {
            "delta": self.delta,
            "exchange_rate": self.rate,
            "UAH": self.uah,
            "USD": self.usd
        }
        return data

    def save(self):
        write_json_file(filename=self._config_filename, data=self._build_data())

    def reset(self):
        data = read_json_file(self._base_config_filename)
        write_json_file(self._config_filename, data)


class Trader:
    def __init__(self, base_config_filename: str, config_filename: str):
        self.wallet = BalanceData(base_config_filename, config_filename)

    def restart(self):
        self.wallet.reset()

    def current_exchange(self):
        print(self.wallet.rate)

    def available(self):
        print(f"USD {self.wallet.usd} UAH {self.wallet.uah}")

    def next_rate(self):
        self.wallet.rate = 36.6
        self.wallet.save()

    def buy(self, count: str):
        pass

    def sell(self, count: str):
        pass