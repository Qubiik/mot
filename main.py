import telebot
from telebot import types
from key import Token

bot = telebot.TeleBot(Token)
users = []
tasks = {}
items = {}

start_button = types.KeyboardButton("Меню")

def create_task(message):
  task = message.text
  id = message.chat.id
  tasks[id]['tasksous'] = []
  tasks[id]['tasksous'].append(task)
  bot.reply_to(message, "Задача добавлена")

def buy(price, message, what_is_pokemon):
  try:
    if tasks[message.chat.id]['point'] >= price:
      tasks[message.chat.id]['point'] -= price
      tasks[message.chat.id]['skin'] = what_is_pokemon
      bot.reply_to(message, f"Вы купили {what_is_pokemon}")
    elif tasks[message.chat.id]['point'] < price:
      bot.reply_to(message, "Нехватает денег")
  except:
    bot.reply_to(message, "Напиши /start")

def tasks12(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn3 = types.KeyboardButton("Создать задачу")
  btn4 = types.KeyboardButton("Просмотреть задачи")
  markup.add(btn3, btn4, start_button)
  bot.reply_to(message, "Задачи", reply_markup=markup)


def show_tasks(message):
  try:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in tasks[message.chat.id]['tasksous']:
      btn = types.KeyboardButton(
          str(tasks[message.chat.id]['tasksous'].index(i)) + " задача")
      markup.add(btn)
    markup.add(start_button)
    for i in tasks[message.chat.id]['tasksous']:
      bot.reply_to(message, i, reply_markup=markup)
  except:
    bot.reply_to(message, "You haven't created any tasks yet.")


def taska(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn8 = types.KeyboardButton("Удалить задачу " + message.text[:7])
  btn9 = types.KeyboardButton("Выполнить задачу " + message.text[:7])
  markup.add(btn8, btn9, start_button)
  bot.reply_to(
      message,
      f'Задача \n"{tasks[message.chat.id]["tasksous"][int(message.text.split()[0])]}" \n',
      reply_markup=markup)


def del_task(message):
  tasks[message.chat.id]['tasksous'].pop(int(message.text.split()[-2]))
  tasks12(message)
  bot.reply_to(message, "Задача удалена")


def do_task(message):
  tasks[message.chat.id]['tasksous'].pop(int(message.text.split()[-2]))
  tasks12(message)
  tasks[message.chat.id]['point'] += 1
  bot.reply_to(message, "Задача выполнена")


def items_skins(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn10 = types.KeyboardButton("Скины")
  btn11 = types.KeyboardButton("Предметы")
  markup.add(btn10, btn11, start_button)
  bot.reply_to(message, "Выберите категорию", reply_markup=markup)


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
    tasks12(message)
  elif message.text == "Разработчики":
    bot.send_message(
        message.chat.id,
        "Программист: @neko18 \nФаундер: @Offchick \nХудожник: @Mydak4")
  elif message.text == "Создать задачу":
    bot.send_message(message.chat.id, "Введите задачу")
    bot.register_next_step_handler(message, create_task)
  elif message.text == "Просмотреть задачи":
    show_tasks(message)
  elif "задача" in message.text:
    taska(message)
  elif "Удалить задачу" in message.text:
    del_task(message)
  elif "Выполнить задачу" in message.text:
    do_task(message)
  elif "Меню" in message.text:
    start(message)
  elif "Скины и предметы" == message.text:
    items_skins(message)
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
    buy(10, message, 'dog')
  elif "Взять cat" == message.text:
    buy(10, message, 'cat')
  elif "qwqefg43t3df" == message.text:
    tasks[message.chat.id]['point'] += 1000000
    

bot.polling(none_stop=True)