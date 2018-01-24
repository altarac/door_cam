# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# import time
# import pandas as pd
# from bs4 import BeautifulSoup as bs
import requests

#
# chromedriver = '/Users/samuelaltarac/Desktop/python programs/chromedriver'
# browser = webdriver.Chrome(chromedriver)

input('Hit enter to send a DM on Twitter...')

r = requests.post('https://maker.ifttt.com/trigger/python/with/key/cItpPn7ldNurH9b0mx5-yN', json={"value1": "This is cool!"})

print(r.status_code)
