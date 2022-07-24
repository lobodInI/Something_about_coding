import os
import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1
from lesson_14 import Quote

# load_dotenv()
#
# KEY = os.getenv("KEY")
# SECRET = os.getenv("SECRET")
#
# auth = OAuth1(KEY, SECRET)
# endpoint = "http://api.thenounproject.com/icon/1"
#
# response = requests.get(endpoint, auth=auth)
# print(response.json())

print("Hello fom lesson 15!!!")
print(__name__)

quote_new = Quote(10, 'result_new.json')
quote_new.get_quotes()
quote_new.save_results()