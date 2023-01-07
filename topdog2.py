from telebot import types
from flask import Flask, request
import random
import telebot
import requests
import re
from bs4 import BeautifulSoup



#парсим температуру по координатам у яндекса
url = 'https://yandex.com.am/weather/details/10-day-weather?lat=52.28959&lon=104.280608&via=mf#29'

response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")
temp = bs.find('span', 'temp__value temp__value_with-unit')
tempresult = temp.text

token = '5903030879:AAFdIDyjd5y9glJLrGwOKQrW-vAULoX6Vxg'
bot = telebot.TeleBot(token)
app = Flask(__name__)

#получаем url картинок с кошками
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

#отсекаем gif и видео
def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

#получаем url картинок с кошками
def get_cat_url():
	contents = requests.get("http://aws.random.cat/meow").json()
	url = contents["file"]
	return url

# Подключаем модуль случайных чисел
# Подключаем модуль для Телеграма
# Импортируем типы из модуля, чтобы создавать кнопки
# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.", "Оптимальный день для того, чтобы решиться на смелый поступок!", "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.", "Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про", "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на", "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.", "работу и деловые вопросы, которые могут так некстати помешать планам.", "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.", "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.", "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.", "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.", "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


# Метод, который получает сообщения и обрабатывает их


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет" or "привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(
            text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(
            text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(
            text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(
            text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(
            text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(
            text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(
            text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(
            text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(
            text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(
            text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(
            text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(
            text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        
        key_dog = types.InlineKeyboardButton(
            text='Картинки с собачками', callback_data='dog')
        keyboard.add(key_dog)
        key_cat = types.InlineKeyboardButton(
            text='Картинки с кошками', callback_data='cat')
        keyboard.add(key_cat)
        
        key_temp1 = types.InlineKeyboardButton(
            text='Погода', callback_data='temp1')
        keyboard.add(key_temp1)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    
# Обработчик нажатий на кнопки


@bot.callback_query_handler(func=lambda call: True)



@bot.message_handler(content_types=['text'])
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + \
            ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "dog":
        bot.send_photo(call.message.chat.id, photo=get_image_url(), caption='гав')
    elif call.data == "cat":
        bot.send_photo(call.message.chat.id, photo=get_cat_url(), caption='мяу')


    elif call.data == 'temp1' :
        bot.send_message(call.message.chat.id, "сейчас в Иркутске " + tempresult)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


@app.route("/" + token, methods=['POST'])
def getMessage():
  bot.process_new_updates(
      [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
  return "!", 200


bot.remove_webhook()
bot.set_webhook('https://test.com/' + token)
app.run()
