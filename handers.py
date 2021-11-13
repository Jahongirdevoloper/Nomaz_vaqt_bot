from aiogram.types.message import Message
import requests
from config import dp
from aiogram import types
from keyboards import main_keyboard,asosiy


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply('Namoz vaqti botiga hush kelibsiz', reply_markup=asosiy)


@dp.message_handler(regexp='Namoz vaqti')
async def pray_time(message:types.Message):
    await message.answer("👳🏻‍♂️ Namoz vaqti uchun Viloyat tanlang!", reply_markup=main_keyboard)

@dp.message_handler(regexp="Go back")
async def go_back(mes:types.Message):
    await mes.reply("Namoz vaqti", reply_markup=asosiy)


@dp.message_handler(regexp='Tashkent')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")

@dp.message_handler(regexp='Samarkand')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Andijan')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Urgench')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Navoi')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Bukhara')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Termez')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Qarshi')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Gulistan')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Jizzakh')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Fergana')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")


@dp.message_handler(regexp='Namangan')
async def region(message:types.Message):
    city = message.text
    res = requests.api.get(f"https://api.pray.zone/v2/times/today.json?city={city}")
    d = res.json()
    q = d["results"]["datetime"][0]["times"]
    print(d["results"]["datetime"][0]["times"])
    await message.reply(f"Davlat : O'zbekiston 🇺🇿\nViloyat : {city.title()}\n\nBomdod  {q['Fajr']}\n\nQiyosh  {q['Sunrise']}\n\nPeshin  {q['Dhuhr']}\n\nAsr  {q['Asr']}\n\nShom  {q['Sunset']}\n\nXufton  {q['Isha']}")

@dp.message_handler(regexp="Suralar")
async def Suralar(message:types.Message):
    res = requests.api.get('https://api.quran.sutanlab.id/surah/18')
    res = res.json()
    ap = res['data']["verses"][0]["audio"]["secondary"][0]
    print(ap)
    await message.reply(f"{ap}")