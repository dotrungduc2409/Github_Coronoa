import requests
from win10toast import ToastNotifier
import json
import time
def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'Ca nhiễm: {data["cases"]} \nNgười chết: {data["deaths"]} \nCứu chữa: {data["recovered"]}'

    while True:
        t=ToastNotifier()
        t.show_toast("Covid 19 Update -- Giám đốc ĐỨC ĐỖ ",text,duration=20)
        time.sleep(60)
update()
