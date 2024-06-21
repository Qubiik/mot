import telebot
from telebot import types

def create_task(message, tasks, bot):
  task = message.text
  id = message.chat.id
  tasks[id]['tasksous'] = []
  tasks[id]['tasksous'].append(task)
  bot.reply_to(message, "Задача добавлена")

def buy(price, message, what_is_pokemon, tasks, bot):
  try:
    if tasks[message.chat.id]['point'] >= price:
      tasks[message.chat.id]['point'] -= price
      tasks[message.chat.id]['skin'] = what_is_pokemon
      bot.reply_to(message, f"Вы купили {what_is_pokemon}")
    elif tasks[message.chat.id]['point'] < price:
      bot.reply_to(message, "Нехватает денег")
  except:
    bot.reply_to(message, "Напиши /start")

def tasks12(message, bot, start_button):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn3 = types.KeyboardButton("Создать задачу")
  btn4 = types.KeyboardButton("Просмотреть задачи")
  markup.add(btn3, btn4, start_button)
  bot.reply_to(message, "Задачи", reply_markup=markup)


def show_tasks(message, start_button, bot, tasks):
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


def taska(message, start_button, bot, tasks):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn8 = types.KeyboardButton("Удалить задачу " + message.text[:7])
  btn9 = types.KeyboardButton("Выполнить задачу " + message.text[:7])
  markup.add(btn8, btn9, start_button)
  bot.reply_to(
      message,
      f'Задача \n"{tasks[message.chat.id]["tasksous"][int(message.text.split()[0])]}" \n',
      reply_markup=markup)


def del_task(message, tasks, bot, start_button):
  tasks[message.chat.id]['tasksous'].pop(int(message.text.split()[-2]))
  tasks12(message, bot, start_button)
  bot.reply_to(message, "Задача удалена")


def do_task(message, tasks, bot, start_button):
  tasks[message.chat.id]['tasksous'].pop(int(message.text.split()[-2]))
  tasks12(message, bot, start_button)
  tasks[message.chat.id]['point'] += 1
  bot.reply_to(message, "Задача выполнена")


def items_skins(message, start_button, bot):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn10 = types.KeyboardButton("Скины")
  btn11 = types.KeyboardButton("Предметы")
  markup.add(btn10, btn11, start_button)
  bot.reply_to(message, "Выберите категорию", reply_markup=markup)