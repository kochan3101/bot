import telebot
from telebot import types
import gspread

TOKEN = '6089466461:AAFtYdjnPwNPp88FyXHxius4U9YRcJkc_og' \

bot = telebot.TeleBot(TOKEN)

gc = gspread.service_account(filename="json\my-test-378416-ed0f5f5170ee.json")
sh = gc.open("Копия Промокоды")
worksheet = sh.sheet1

@bot.message_handler(commands=['start'])
def welcome_and_choice_categories(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.InlineKeyboardMarkup(row_width=1)
    values_list = worksheet.col_values(9)
    values_list = set(values_list)
    for i in values_list:
        item = types.InlineKeyboardButton(f'{i}', callback_data=f'{i}')
        markup.add(item)
    item_table = types.InlineKeyboardButton('Таблица со всеми промокодами', callback_data='table', url="https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0")
    markup.add(item_table)
    bot.send_message(message.chat.id, 'Выберите категорию в которой хотите получить скидку', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def welcome_and_choice_categories(message):
    bot.send_message(message.chat.id, 'Давай лучше пройдемся по скидкам')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            cell_list = worksheet.findall(f"{call.data}")
            values_list = worksheet.col_values(9)
            values_list = set(values_list)
            if call.data == 'menu':
                menu(call)
            elif call.data == cell_list[0].value:
                if cell_list[0].value in  values_list:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    list_of_category = []
                    for i in cell_list:
                        list_of_category.append(worksheet.acell(f'A{i.row}').value)
                    list_of_category = set(list_of_category)
                    for i in list_of_category:
                        item = types.InlineKeyboardButton(f'{i}', callback_data=f'{i}')
                        markup.add(item)
                    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                    markup.add(item2)
                    bot.send_message(call.message.chat.id, 'Выберите категорию в которой хотите получить скидку',
                             reply_markup=markup, parse_mode='html')
                else:
                    message(call)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    cell_list = worksheet.findall(f"{call.data}")
                    for i in cell_list:
                        formattext(call, int(i.row))
                    item1 = types.InlineKeyboardButton(f"{call.data}", callback_data=f"{call.data}")
                    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                    markup.add(item1, item2)
                    bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=markup)
    except Exception as e:
        print(repr(e))


def message(call):
    bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
перейти по ссылке или скопировать значение купона с 
данной страницы и ввести его на сайте компании☺️""")

def formattext(call, n):
    values_list = worksheet.row_values(n)
    bot.send_message(call.message.chat.id, f"""Название: {values_list[0]}
Скидка: {values_list[3]}
Описание: {values_list[7]} 
Действует до: {values_list[5]}
Регион: {values_list[6]}
Ссылка: {values_list[4]}
Промокод ниже👇""",
                     parse_mode='html')
    bot.send_message(call.message.chat.id, f"{values_list[2]}")

def menu(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    values_list = worksheet.col_values(9)
    values_list = set(values_list)
    for i in values_list:
        item = types.InlineKeyboardButton(f'{i}', callback_data=f'{i}')
        markup.add(item)
    item_table = types.InlineKeyboardButton('Таблица со всеми промокодами', callback_data='table',
                                            url="https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0")
    markup.add(item_table)
    bot.send_message(call.message.chat.id, 'Выберите категорию в которой хотите получить скидку', reply_markup=markup,
                     parse_mode='html')



bot.polling(none_stop=True)

