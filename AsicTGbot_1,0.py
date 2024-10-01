import asyncio
import time
import requests
import datetime
from aiogram import Bot
from bs4 import BeautifulSoup
def get_btc_course(btc_link = 'https://kursolog.com/rub/btc/1'):
    response = requests.get(btc_link).text
    soup = BeautifulSoup(response, 'lxml')
    soup = soup.find_all("span", class_="pretty-sum")
    course_btc = soup[1].text.split()
    course_btc = course_btc[0]
    return float(course_btc[0] + "." + course_btc[2:])

asic_link = 'https://trustpool.ru/res/saas/observer/home?access_key=25e2c98bebdc10ec04d4fa8d6a8b1ad5&user_id=555914&coin=BTC'
asic_bot = Bot(token='7442779646:AAG0LyU_t4hrOTmVBxonsDtx_U-fYhXOYUg')
while True:
    asic_answer = {}
    current_time = datetime.datetime.now().time()
    current_hour = current_time.hour
    current_minute = current_time.minute
    asic_answer = requests.get(asic_link).json()
    if float(asic_answer['data']['hashrate_10min'][0:-1]) < 120:
        asyncio.get_event_loop().run_until_complete(
            asic_bot.send_message(-4511001816, text=f"Тревога! Маленький хэшрейт: {asic_answer['data']['hashrate_10min']}"))
    if current_hour == 12 and current_minute < 5:
        asyncio.get_event_loop().run_until_complete(
               asic_bot.send_message(-4511001816, text=f"Прибыль за 24 часа: {float(asic_answer['data']['profit_24hour'])//get_btc_course()} Rub"))
    time.sleep(300)
