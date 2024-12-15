import asyncio
import time
import requests
import datetime
from aiogram import Bot
from bs4 import BeautifulSoup
cookies = {
    'ak_bmsc': '4C67861D923E5D5D161DB69C5F938BB9~000000000000000000000000000000~YAAQm3zRFxYJ3JqTAQAA6mwqyRpvrbD2GiXAf5v49Sxp0MZY4RW1wxwxBb4a10rJbSJ6Leq72hvI0usSAgyXwz1hliRk66b/HXO479BCu1MR8V8Ng+kl97k0CQSmRbSgu/ZTfZ+NDscY+DBa9RxQya8Y1RljH/wR7te3LKDjxOEAfrLUidTGyDPuqAgzYOv1CYPdjiATtjeX7hpFZAE9QlsCTGGabDmQ5HTcSWa3YmYRdwUT1mcEN9u+Um7tf42a2CfMDoJQza//sO94NYNh+vmEsqw7aLYb0KBTpz+shonSVK1njUjxMhRI3AQNHkmlS4MlfPl26dfKyMz1ciaXoXMpLtiYrOwSg/0NbnrF7cCYQXl0cmkdVbuD1+5A9ONPuGIlXMMNl8M=',
    '_by_l_g_d': '68a90a51-c26e-ae08-73a9-60b8b9c04285',
    'BYBIT_REG_REF_prod': '{"lang":"ru-RU","g":"68a90a51-c26e-ae08-73a9-60b8b9c04285","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/convert/rub-to-btc/","last_refresh_time":"Sun, 15 Dec 2024 07:13:43 GMT","ext_json":{"dtpid":null}}',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22193c92a75e454b-050d342eea703b8-26011851-2073600-193c92a75e59cf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22_a_u_v%22%3A%220.0.6%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYzkyYTc1ZTQ1NGItMDUwZDM0MmVlYTcwM2I4LTI2MDExODUxLTIwNzM2MDAtMTkzYzkyYTc1ZTU5Y2YifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
    'builderSessionId': 'd137dd644644464ab71218c635d82b07',
    'deviceId': 'd275a00c-554b-158b-98c3-3e39ae49bda1',
    '_abck': '0ABD8A06471AF238FF82C188C6F6791B~0~YAAQn/1zPgt5HcmTAQAAZ3IqyQ3vhMsHJLEo31qBZp3Bxfif17Pqe6mc/jZ6+JWJSNLzMd7vUQP4+/YVXbTUl44Hr+wsKmLW8dt3KxWUCK2Q/Artfkels2ZDhZwNwe2yID+8v+aogk8nbSJSlitjXLDeuFWYIOHUpoy4p4n7xTp8yogHtcRtF4kZ2UEexPlZjxK2LZg5Cu7rcSHGeFSXLCHmaTPuHIE2+FaU6Cf4Tt659YwPHfsdr8oBwc+xyOtp+XNV3kzD8OhCMdxlX86BjzgWpAM4jC47tfVXC4zt3l0hlkgdJt7wz1/UfGlIg9Au5m6nKQFwJ2uKfgzlb/vt4DhKZRwG5Cqnw49/pJ16FlyEn/fZstJScktzmJSxx7byTV1r8i1U2LaFbd5FVZlHyAFyVVDzFtt7GbFUlIBAY7Tz7aMpPVoCpnXXt2lhi67/yUY8gbyZ1O3vk3xa0Vvlxcch7iNjhNOLLLT3nJ64eU+vHIVrwmllWmj4~-1~||0||~-1',
    '_gcl_au': '1.1.2065287917.1734246830',
    '_ga_SPS4ND2MGC': 'GS1.1.1734246830.1.0.1734246830.60.0.0',
    '_ga': 'GA1.1.977120183.1734246830',
    '_ym_uid': '173424683039359886',
    '_ym_d': '1734246830',
    'tmr_lvid': '652da4667509ee56c2ea4d0b0a75b649',
    'tmr_lvidTS': '1734246830221',
    '_ym_isad': '2',
    '_fbp': 'fb.1.1734246830401.65285875513516373',
    '_tt_enable_cookie': '1',
    '_ttp': 'mhZk_RfQzCtzyGrm4OVh7Gxux95.tt.1',
    'domain_sid': 'K3OZakWOqKeZvttdHB9Lb%3A1734246830949',
    'tmr_detect': '0%7C1734246832955',
    'bm_mi': 'E33AE4C57F0AC65B43C020D5A67A3325~YAAQdP1zPkUInciTAQAAMXEryRrTIqM78Ta9BS2ungiaZZMf8HXSyh0jitvVk0wSnMmPabds27eG6ZwzuEMkhVMqercWAsLi6iMgNIpa/AlPHxvrCP1LS3c7WR7/HJhWCVZFf9+fOEyL0efZX07pmt2jxzCv50bfJpV7OiilMukQxGnO97+nzzsp3VWc9Ud6E3mmaCAGGNCEt4zekaibXan5Zt1RV7QAHZ684I/Rxo8U4B/QgAg82WEZMVU/MX4cYcxqzeW9lBlG6myXs1xtiYeQSoXjI3CftctdfeNmCheGS85DJi71VyP+JH4oi1VWExX6h/cc8+RXqT1PkuBB2hOQO6Yq~1',
    'bm_sz': '3671B308F2509977E32F729D9DB163B2~YAAQdP1zPkcInciTAQAAMXEryRqlYlEk6fi1gDGPuTm1h2l3LMTu1QC+FtHB2JChCauvccs2ktiAYGA18ttQ/Lex4BkV7AGOedvz5UA3c9l8R3hjlD7hd+9EXlc5bQWLV/0QuGe4meO3xHY6WU5X/6wcZN1yjlNGWIw+bIugX8LNNo1i1ts7VGmaKNMO69KRQeXQFzHLJTimH8KjuiALkwHGK91JbGiTl6V2PRh2J1GzRxECynN6ZTspPHY/JlfEw+vVhfBBVbbOa7s0J7NbfRDuObyb342ZtF7yI5h7thROrVojaIxTI1HpEgme8pYyFm6RPpxK+Y7eTxQiBedjynRjSAcLUwD//XV75JIq0/tjafj36uP8S+1ES6A+9uCbIeQXW9UyqHkyrOUqzEY2jrZLMA==~4408632~4604741',
    'bm_sv': '8D609C2820E362F5F3F538B66D4DF42B~YAAQdP1zPmoLnciTAQAALI8ryRrox/1wAoqTQ9nzCE+Ass1nfgIiGaFFBmAjdTopPgDaV1oF9+xLlZyKctUQBfRzMV7fWZ+vYUUXPJm70TVvxe46WMQwQhbUzFEv/mo+fbWaYFpa79EeRmZ5lTkNJzFXRdhm1kEJoczUrQxKwI/3+mlNFjVGGOgPmaDxjImoSyiOp4ryKyEWK3JjA0Mw0E0slgrGfbrIj8asw02efgEdlRMjquGOMnlz+l+tizr2~1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ak_bmsc=4C67861D923E5D5D161DB69C5F938BB9~000000000000000000000000000000~YAAQm3zRFxYJ3JqTAQAA6mwqyRpvrbD2GiXAf5v49Sxp0MZY4RW1wxwxBb4a10rJbSJ6Leq72hvI0usSAgyXwz1hliRk66b/HXO479BCu1MR8V8Ng+kl97k0CQSmRbSgu/ZTfZ+NDscY+DBa9RxQya8Y1RljH/wR7te3LKDjxOEAfrLUidTGyDPuqAgzYOv1CYPdjiATtjeX7hpFZAE9QlsCTGGabDmQ5HTcSWa3YmYRdwUT1mcEN9u+Um7tf42a2CfMDoJQza//sO94NYNh+vmEsqw7aLYb0KBTpz+shonSVK1njUjxMhRI3AQNHkmlS4MlfPl26dfKyMz1ciaXoXMpLtiYrOwSg/0NbnrF7cCYQXl0cmkdVbuD1+5A9ONPuGIlXMMNl8M=; _by_l_g_d=68a90a51-c26e-ae08-73a9-60b8b9c04285; BYBIT_REG_REF_prod={"lang":"ru-RU","g":"68a90a51-c26e-ae08-73a9-60b8b9c04285","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/convert/rub-to-btc/","last_refresh_time":"Sun, 15 Dec 2024 07:13:43 GMT","ext_json":{"dtpid":null}}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193c92a75e454b-050d342eea703b8-26011851-2073600-193c92a75e59cf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22_a_u_v%22%3A%220.0.6%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYzkyYTc1ZTQ1NGItMDUwZDM0MmVlYTcwM2I4LTI2MDExODUxLTIwNzM2MDAtMTkzYzkyYTc1ZTU5Y2YifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; builderSessionId=d137dd644644464ab71218c635d82b07; deviceId=d275a00c-554b-158b-98c3-3e39ae49bda1; _abck=0ABD8A06471AF238FF82C188C6F6791B~0~YAAQn/1zPgt5HcmTAQAAZ3IqyQ3vhMsHJLEo31qBZp3Bxfif17Pqe6mc/jZ6+JWJSNLzMd7vUQP4+/YVXbTUl44Hr+wsKmLW8dt3KxWUCK2Q/Artfkels2ZDhZwNwe2yID+8v+aogk8nbSJSlitjXLDeuFWYIOHUpoy4p4n7xTp8yogHtcRtF4kZ2UEexPlZjxK2LZg5Cu7rcSHGeFSXLCHmaTPuHIE2+FaU6Cf4Tt659YwPHfsdr8oBwc+xyOtp+XNV3kzD8OhCMdxlX86BjzgWpAM4jC47tfVXC4zt3l0hlkgdJt7wz1/UfGlIg9Au5m6nKQFwJ2uKfgzlb/vt4DhKZRwG5Cqnw49/pJ16FlyEn/fZstJScktzmJSxx7byTV1r8i1U2LaFbd5FVZlHyAFyVVDzFtt7GbFUlIBAY7Tz7aMpPVoCpnXXt2lhi67/yUY8gbyZ1O3vk3xa0Vvlxcch7iNjhNOLLLT3nJ64eU+vHIVrwmllWmj4~-1~||0||~-1; _gcl_au=1.1.2065287917.1734246830; _ga_SPS4ND2MGC=GS1.1.1734246830.1.0.1734246830.60.0.0; _ga=GA1.1.977120183.1734246830; _ym_uid=173424683039359886; _ym_d=1734246830; tmr_lvid=652da4667509ee56c2ea4d0b0a75b649; tmr_lvidTS=1734246830221; _ym_isad=2; _fbp=fb.1.1734246830401.65285875513516373; _tt_enable_cookie=1; _ttp=mhZk_RfQzCtzyGrm4OVh7Gxux95.tt.1; domain_sid=K3OZakWOqKeZvttdHB9Lb%3A1734246830949; tmr_detect=0%7C1734246832955; bm_mi=E33AE4C57F0AC65B43C020D5A67A3325~YAAQdP1zPkUInciTAQAAMXEryRrTIqM78Ta9BS2ungiaZZMf8HXSyh0jitvVk0wSnMmPabds27eG6ZwzuEMkhVMqercWAsLi6iMgNIpa/AlPHxvrCP1LS3c7WR7/HJhWCVZFf9+fOEyL0efZX07pmt2jxzCv50bfJpV7OiilMukQxGnO97+nzzsp3VWc9Ud6E3mmaCAGGNCEt4zekaibXan5Zt1RV7QAHZ684I/Rxo8U4B/QgAg82WEZMVU/MX4cYcxqzeW9lBlG6myXs1xtiYeQSoXjI3CftctdfeNmCheGS85DJi71VyP+JH4oi1VWExX6h/cc8+RXqT1PkuBB2hOQO6Yq~1; bm_sz=3671B308F2509977E32F729D9DB163B2~YAAQdP1zPkcInciTAQAAMXEryRqlYlEk6fi1gDGPuTm1h2l3LMTu1QC+FtHB2JChCauvccs2ktiAYGA18ttQ/Lex4BkV7AGOedvz5UA3c9l8R3hjlD7hd+9EXlc5bQWLV/0QuGe4meO3xHY6WU5X/6wcZN1yjlNGWIw+bIugX8LNNo1i1ts7VGmaKNMO69KRQeXQFzHLJTimH8KjuiALkwHGK91JbGiTl6V2PRh2J1GzRxECynN6ZTspPHY/JlfEw+vVhfBBVbbOa7s0J7NbfRDuObyb342ZtF7yI5h7thROrVojaIxTI1HpEgme8pYyFm6RPpxK+Y7eTxQiBedjynRjSAcLUwD//XV75JIq0/tjafj36uP8S+1ES6A+9uCbIeQXW9UyqHkyrOUqzEY2jrZLMA==~4408632~4604741; bm_sv=8D609C2820E362F5F3F538B66D4DF42B~YAAQdP1zPmoLnciTAQAALI8ryRrox/1wAoqTQ9nzCE+Ass1nfgIiGaFFBmAjdTopPgDaV1oF9+xLlZyKctUQBfRzMV7fWZ+vYUUXPJm70TVvxe46WMQwQhbUzFEv/mo+fbWaYFpa79EeRmZ5lTkNJzFXRdhm1kEJoczUrQxKwI/3+mlNFjVGGOgPmaDxjImoSyiOp4ryKyEWK3JjA0Mw0E0slgrGfbrIj8asw02efgEdlRMjquGOMnlz+l+tizr2~1',
    'if-none-match': '"4a245-OvZRfQIpT4ETej9L4wlbqaOk280"',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
def get_btc_course(btc_link = 'https://www.bybit.com/ru-RU/convert/rub-to-btc/'):
    answer = ''
    response = requests.get(btc_link, cookies=cookies, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    soup1 = soup.find('h2', class_='card-info-price-box')
    for i in soup1.text:
        if i in ['-', '+']:
            break
        elif i.isdigit() or i == '.':
            answer += i
    return float(answer)

asic_link = 'https://trustpool.ru/res/saas/observer/home?access_key=25e2c98bebdc10ec04d4fa8d6a8b1ad5&user_id=555914&coin=BTC'
asic_bot = Bot(token='7442779646:AAG0LyU_t4hrOTmVBxonsDtx_U-fYhXOYUg')
while True:
    current_time = datetime.datetime.now().time()
    current_hour = current_time.hour
    current_minute = current_time.minute
    asic_answer = requests.get(asic_link).json()
    if float(asic_answer['data']['hashrate_10min'][0:-1]) < 120:
        asyncio.get_event_loop().run_until_complete(
            asic_bot.send_message(-4511001816, text=f"Тревога! Маленький хэшрейт: {asic_answer['data']['hashrate_10min']}"))
    if current_hour == 12 and current_minute < 21:
        asyncio.get_event_loop().run_until_complete(
               asic_bot.send_message(-4511001816, text=f"Прибыль за 24 часа: {float(asic_answer['data']['profit_24hour'])//get_btc_course()} Rub"))
    time.sleep(1200)
