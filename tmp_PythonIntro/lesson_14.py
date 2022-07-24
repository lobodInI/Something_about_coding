import requests
import json
from random import randint


# url = "http://api.forismatic.com/api/1.0/"
#
# params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "ru"}
#
# response = requests.post(url, params=params)
# print(response.json())


class Quote:
    def __init__(self, quote_nuber: int, filename_save_result: str, author_exists: bool = True):
        self.quote_nuber = quote_nuber
        self.filename_save_result = filename_save_result
        self.author_exists = author_exists
        self.quotes = []
        self.url = "http://api.forismatic.com/api/1.0/"
        self.params = {"method": "getQuote",
                       "format": "json",
                       "key": 1,
                       "lang": "en"}

    def _get_quote(self):
        self.params["key"] = randint(1, 10000)
        response = requests.post(self.url, params=self.params)
        return response.json()

    def get_quotes(self):
        while len(self.quotes) < self.quote_nuber:
            try:
                quote = self._get_quote()
                if quote["quoteAuthor"].strip():  # Дополнительное ДЗ (как использовать author_exists)
                    self.quotes.append(quote)
            except requests.exceptions.JSONDecodeError:
                pass

    def save_results(self):
        with open(self.filename_save_result, 'w') as file:
            json.dump(self.quotes, file)


if __name__ == "__main__":
    print("Hello fom lesson 14!!!")
    print(__name__)
    quotes = Quote(10, 'result.json')
    quotes.get_quotes()
    quotes.save_results()