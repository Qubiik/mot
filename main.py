import telebot
from telebot import types

bot = telebot.TeleBot("7019249353:AAHdX958MFtTopZbeoUaYcUw2J-h2L7uLPw")
users = []
tasks = {}


def create_task(message):
  task = message.text
  id = message.chat.id
  if id not in users:
    users.append(id)
    tasks[id] = []
  tasks[id].append(task)
  bot.reply_to(message, "Задача добавлена")


def tasks12(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn3 = types.KeyboardButton("Создать задачу")
  btn4 = types.KeyboardButton("Просмотреть задачи")
  markup.add(btn3, btn4)
  bot.reply_to(message, "Задачи", reply_markup=markup)


def show_tasks(message):
  if tasks[message.chat.id]:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in tasks[message.chat.id]:
      btn = types.KeyboardButton(str(tasks[message.chat.id].index(i))  + " задача")
      markup.add(btn)
    for i in tasks[message.chat.id]:
      bot.reply_to(message, i, reply_markup=markup)
  else:
    bot.reply_to(message, "You haven't created any tasks yet.")


def taska(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn8 = types.KeyboardButton("Удалить задачу " + message.text[:7])
  btn9 = types.KeyboardButton("Выполнить задачу " + message.text[:7])
  markup.add(btn8, btn9)
  bot.reply_to(
      message,
      f'Задача \n"{tasks[message.chat.id][int(message.text.split()[0])]}" \n',
      reply_markup=markup)

def del_task(message):
  tasks[message.chat.id].pop(int(message.text.split()[-2]))
  bot.reply_to(message, "Задача удалена")



def do_task(message):
  tasks[message.chat.id].pop(int(message.text.split()[-1]))
  bot.reply_to(message, "Задача выполнена")


@bot.message_handler(commands=['start', 'menu'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Задачи")
  btn2 = types.KeyboardButton("Разработчики")
  markup.add(btn1, btn2)
  bot.reply_to(message, "Hello world!", reply_markup=markup)


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
  elif message.text == "Выполнить задачу":
    do_task(message)


bot.polling(none_stop=True)
