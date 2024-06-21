import telebot
from telebot import types
from key import Token
from func import create_task, buy, tasks12, show_tasks, taska, del_task, do_task, items_skins

bot = telebot.TeleBot(Token)
users = []
tasks = {}
items = {}

start_button = types.KeyboardButton("Меню")

@bot.message_handler(commands=['start', 'menu'])
def start(message):
  if message.chat.id not in users:
    users.append(message.chat.id)
    tasks[message.chat.id] = {}
    tasks[message.chat.id]['point'] = 0
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Задачи")
  btn2 = types.KeyboardButton("Разработчики")
  btn12 = types.KeyboardButton("Скины и предметы")
  markup.add(btn1, btn2, btn12)
  if message.from_user.first_name:
    name = message.from_user.first_name
  else:
    name = message.chat.id
  try:
    if tasks[message.chat.id]['skin'] == "cat":
      with open("cat.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"{name} \nPoint: {tasks[message.chat.id]['point']}", reply_markup=markup)
    elif tasks[message.chat.id]['skin'] == "dog":
      with open("dog.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"{name} \nPoint: {tasks[message.chat.id]['point']}", reply_markup=markup)
  except:
    with open("defualt.png", "rb") as photo:
      bot.send_photo(message.chat.id, photo, caption=f"{name} \nPoint: {tasks[message.chat.id]['point']}", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def text(message):
  if message.text == "Задачи":
    tasks12(message, bot, start_button)
  elif message.text == "Разработчики":
    bot.send_message(
        message.chat.id,
        "Программист: @neko18 \nФаундер: @Offchick \nХудожник: @Mydak4")
  elif message.text == "Создать задачу":
    bot.send_message(message.chat.id, "Введите задачу")
    bot.register_next_step_handler(message, create_task, tasks, bot)
  elif message.text == "Просмотреть задачи":
    show_tasks(message, start_button, bot, tasks)
  elif "задача" in message.text:
    taska(message, start_button, bot, tasks)
  elif "Удалить задачу" in message.text:
    del_task(message, tasks, bot, start_button)
  elif "Выполнить задачу" in message.text:
    do_task(message, tasks, bot, start_button)
  elif "Меню" in message.text:
    start(message)
  elif "Скины и предметы" == message.text:
    items_skins(message, start_button, bot)
  elif "Скины" == message.text:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnDOG = types.KeyboardButton('dog')
    btnCAT = types.KeyboardButton('cat')
    markup.add(start_button, btnDOG, btnCAT)
    bot.reply_to(message, "Выберите скин", reply_markup=markup)
  elif 'dog' == message.text:
    btnY = types.KeyboardButton("Взять dog")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btnY, start_button)
    with open("dog.png", "rb") as photo:
      bot.send_photo(message.chat.id, photo, caption="Price: 10", reply_markup=markup)
  elif 'cat' == message.text:
    btnY = types.KeyboardButton("Взять cat")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btnY, start_button)
    with open("cat.png", "rb") as photo:
      bot.send_photo(message.chat.id, photo,caption="Price: 10", reply_markup=markup)
  elif "Взять dog" == message.text:
    buy(10, message, "dog", tasks, bot)
  elif "Взять cat" == message.text:
    buy(10, message, "cat", tasks, bot)
  elif "qwqefg43t3df" == message.text:
    tasks[message.chat.id]['point'] += 1000000
  elif "Предметы" == message.text:
    bot.reply_to(message, "soon...")
    

bot.polling(none_stop=True)