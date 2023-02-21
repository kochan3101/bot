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
    item1 = types.InlineKeyboardButton('Маркетплейс', callback_data='marketplace')
    item2 = types.InlineKeyboardButton('Бонусы от банков', callback_data='banks')
    item3 = types.InlineKeyboardButton('Инвестиции', callback_data='investments')
    item4 = types.InlineKeyboardButton('Доставка/продукты', callback_data='delivery')
    item5 = types.InlineKeyboardButton('Аптеки/здоровье', callback_data='health')
    item6 = types.InlineKeyboardButton('Кафе/рестораны', callback_data='cafe')
    item7 = types.InlineKeyboardButton('Цветы', callback_data='flowers')
    item8 = types.InlineKeyboardButton('Онлайн сервис/подписка', callback_data='online_service')
    item9 = types.InlineKeyboardButton('Обувь/одежда', callback_data='clothes')
    item10 = types.InlineKeyboardButton('Косметика/парфюмерия', callback_data='cosmetics')
    item11 = types.InlineKeyboardButton('Такси/каршеринг', callback_data='taxi')
    item12 = types.InlineKeyboardButton('Страхование', callback_data='insurance')
    item13 = types.InlineKeyboardButton('Авиабилеты/гостинницы', callback_data='air_tickets')
    item14 = types.InlineKeyboardButton('Таблица со всеми промокодами', callback_data='table', url="https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)
    bot.send_message(message.chat.id, 'Выберите категорию в которой хотите получить скидку', reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def welcome_and_choice_categories(message):
    bot.send_message(message.chat.id, 'Давай лучше пройдемся по скидкам')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'marketplace':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Яндекс Маркет', callback_data='yandexmarket')
                item2 = types.InlineKeyboardButton('OZON', callback_data='ozon')
                item3 = types.InlineKeyboardButton('Сбермегамаркет', callback_data='sbermegamarket')
                item4 = types.InlineKeyboardButton('МВидео', callback_data='mvideo')
                item5 = types.InlineKeyboardButton('Эльдорадо', callback_data='aldorado')
                item6 = types.InlineKeyboardButton('МТС', callback_data='mtc')
                item7 = types.InlineKeyboardButton('Wildberries', callback_data='wildberries')
                item8 = types.InlineKeyboardButton('Утконос', callback_data='utkonos')
                item9 = types.InlineKeyboardButton('Зоозавр ТГ', callback_data='zoozavr')
                item10 = types.InlineKeyboardButton('OBI', callback_data='obi')
                item11 = types.InlineKeyboardButton('Galamart', callback_data='galamart')
                item12 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'banks':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Альфа-банк', callback_data='alpha')
                item2 = types.InlineKeyboardButton('Газпромбанк', callback_data='gaz')
                item3 = types.InlineKeyboardButton('Tinkoff инст', callback_data='tinkoffinst')
                item4 = types.InlineKeyboardButton('Tinkoff', callback_data='tinkoff')
                item5 = types.InlineKeyboardButton('Ак барс банк', callback_data='akbars')
                item6 = types.InlineKeyboardButton('Home credit', callback_data='home')
                item7 = types.InlineKeyboardButton('Открытие банк', callback_data='open')
                item8 = types.InlineKeyboardButton('Ренессанс', callback_data='renesans')
                item9 = types.InlineKeyboardButton('Росбанк', callback_data='rosbank')
                item10 = types.InlineKeyboardButton('Точка банк', callback_data='tochkabank')
                item11 = types.InlineKeyboardButton('УБРиР ТГ', callback_data='ubrir')
                item12 = types.InlineKeyboardButton('Уралсиб', callback_data='uralsib')
                item13 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'investments':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Тинькофф инвестиции', callback_data='tinkoff_investments')
                item2 = types.InlineKeyboardButton('Freedom Finance', callback_data='freedome_finance')
                item3 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'delivery':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('ВкусВилл', callback_data='vkusvill')
                item2 = types.InlineKeyboardButton('Винлаб', callback_data='vinlab')
                item3 = types.InlineKeyboardButton('Глобус', callback_data='globus')
                item4 = types.InlineKeyboardButton('Delivery Club', callback_data='deliveryclub')
                item5 = types.InlineKeyboardButton('Сбермаркет', callback_data='sbermarket')
                item6 = types.InlineKeyboardButton('Лента онлайн', callback_data='lenta')
                item7 = types.InlineKeyboardButton('Магнит', callback_data='magnit')
                item8 = types.InlineKeyboardButton('Metro', callback_data='metro')
                item9 = types.InlineKeyboardButton('ОмолочкО', callback_data='omolochko')
                item10 = types.InlineKeyboardButton('Пятёрочка', callback_data='pyaterochka')
                item11 = types.InlineKeyboardButton('Перекрёсток', callback_data='perekrestok')
                item12 = types.InlineKeyboardButton('Перекрёсток Впрок', callback_data='perekrestokvprok')
                item13 = types.InlineKeyboardButton('Самокат', callback_data='samokat')
                item14 = types.InlineKeyboardButton('Яндекс Лавка', callback_data='yandexlavka')
                item15 = types.InlineKeyboardButton('Яндекс Еда', callback_data='yandexeda')
                item16 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)

            elif call.data == 'health':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Аптека.ру', callback_data='aptekaru')
                item2 = types.InlineKeyboardButton('Аптека от склада', callback_data='aptekasklad')
                item3 = types.InlineKeyboardButton('Еаптека Тг', callback_data='eapteka')
                item4 = types.InlineKeyboardButton('Ютека', callback_data='uteka')
                item5 = types.InlineKeyboardButton('Сберздоровье', callback_data='sberhealth')
                item6 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'cafe':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Бургер Кинг', callback_data='burgerking')
                item2 = types.InlineKeyboardButton('KFC', callback_data='kfc')
                item3 = types.InlineKeyboardButton('FoodBand', callback_data='foodband')
                item4 = types.InlineKeyboardButton('Много лосося', callback_data='mnogolososya')
                item5 = types.InlineKeyboardButton('Нияма', callback_data='niyama')
                item6 = types.InlineKeyboardButton('TVOЯ пицца', callback_data='tvoyapizza')
                item7 = types.InlineKeyboardButton('Тануки', callback_data='tanuki')
                item8 = types.InlineKeyboardButton('Якитория', callback_data='yakitoria')
                item9 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'flowers':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Flor2U', callback_data='flor2u')
                item2 = types.InlineKeyboardButton('Цветочный ряд', callback_data='cvetryad')
                item3 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'online_service':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('VK музыка', callback_data='vkmusic')
                item2 = types.InlineKeyboardButton('Пакет', callback_data='paket')
                item3 = types.InlineKeyboardButton('Огонь', callback_data='ogon')
                item4 = types.InlineKeyboardButton('Кинопоиск', callback_data='kinopoisk')
                item5 = types.InlineKeyboardButton('Okko', callback_data='okko')
                item6 = types.InlineKeyboardButton('Яндекс плюс мульти', callback_data='yandexplusmulti')
                item7 = types.InlineKeyboardButton('Яндекс Афиша', callback_data='yandexafisha')
                item8 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'clothes':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Tamaris', callback_data='tamaris')
                item2 = types.InlineKeyboardButton('Befree', callback_data='befree')
                item3 = types.InlineKeyboardButton('Спортмастер', callback_data='sportmaster')
                item4 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'cosmetics':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Летуаль', callback_data='letual')
                item2 = types.InlineKeyboardButton('Золотое яблоко', callback_data='goldapple')
                item3 = types.InlineKeyboardButton('Улыбка Радуги', callback_data='ulibkaradugi')
                item4 = types.InlineKeyboardButton('Самокат Бьюти', callback_data='samokatbeatu')
                item5 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'taxi':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Такси Максим', callback_data='taximaksim')
                item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'insurance':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Тинькофф Страхование Авто', callback_data='tinkoffstrahavto')
                item2 = types.InlineKeyboardButton('Сбер Страхование Авто', callback_data='sberstrahavto')
                item3 = types.InlineKeyboardButton('Сбер Страхование Жилье', callback_data='sberstrahdom')
                item4 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'air_tickets':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Тинькофф Путешествия', callback_data='tinkoffput')
                item2 = types.InlineKeyboardButton('Яндекс Путешествия', callback_data='yandexput')
                item3 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Пожалуйста',
                                 reply_markup=markup)
            elif call.data == 'menu':
                menu(call)
            elif call.data == 'yandexmarket':
                message(call)
                cell_list = worksheet.findall("Яндекс Маркет")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'ozon':
                message(call)
                cell_list = worksheet.findall("OZON")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'sbermegamarket':
                message(call)
                cell_list = worksheet.findall("Сбермегамаркет")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mvideo':
                message(call)
                cell_list = worksheet.findall("МВидео")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'aldorado':
                message(call)
                cell_list = worksheet.findall("Эльдорадо")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mtc':
                message(call)
                cell_list = worksheet.findall("МТС")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'wildberries':
                message(call)
                cell_list = worksheet.findall("Wildberries")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'utkonos':
                message(call)
                cell_list = worksheet.findall("Утконос")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'zoozavr':
                message(call)
                cell_list = worksheet.findall("Зоозавр ТГ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'obi':
                message(call)
                cell_list = worksheet.findall("OBI")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'galamart':
                message(call)
                cell_list = worksheet.findall("Galamart ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'alpha':
                message(call)
                cell_list = worksheet.findall("Альфа Банк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'gaz':
                message(call)
                cell_list = worksheet.findall("Газпромбанк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoffinst':
                message(call)
                cell_list = worksheet.findall("Tinkoff инст")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff':
                message(call)
                cell_list = worksheet.findall("Tinkoff")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'akbars':
                message(call)
                cell_list = worksheet.findall("Ак барс банк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'home':
                message(call)
                cell_list = worksheet.findall("Home Сredit")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'open':
                message(call)
                cell_list = worksheet.findall("Открытие банк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'renesans':
                message(call)
                cell_list = worksheet.findall("Ренессанс кредит")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'rosbank':
                message(call)
                cell_list = worksheet.findall("Росбанк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tochkabank':
                message(call)
                cell_list = worksheet.findall("Точка банк")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'ubrir':
                message(call)
                cell_list = worksheet.findall("УБРиР ТГ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'uralsib':
                message(call)
                cell_list = worksheet.findall("Уралсиб")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff_investments':
                message(call)
                cell_list = worksheet.findall("Тинькофф Инвестиции")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'freedome_finance':
                message(call)
                cell_list = worksheet.findall("Freedom Finance")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'vkusvill':
                message(call)
                cell_list = worksheet.findall("ВкусВилл")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'vinlab':
                message(call)
                cell_list = worksheet.findall("Винлаб")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'globus':
                message(call)
                cell_list = worksheet.findall("Глобус")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'deliveryclub':
                message(call)
                cell_list = worksheet.findall("Delivery Club")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'sbermarket':
                message(call)
                cell_list = worksheet.findall("Сбермаркет")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'lenta':
                message(call)
                cell_list = worksheet.findall("Лента онлайн")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'magnit':
                message(call)
                cell_list = worksheet.findall("Магнит")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'metro':
                message(call)
                cell_list = worksheet.findall("Metro")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'omolochko':
                message(call)
                cell_list = worksheet.findall("ОмолокО (Чистая линия)")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'pyaterochka':
                message(call)
                cell_list = worksheet.findall("Пятёрочка")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestok':
                message(call)
                cell_list = worksheet.findall("Перекрёсток ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestokvprok':
                message(call)
                cell_list = worksheet.findall("Перекресток Впрок")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'samokat':
                message(call)
                cell_list = worksheet.findall("Самокат")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexlavka':
                message(call)
                cell_list = worksheet.findall("Яндекс Лавка")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexeda':
                message(call)
                cell_list = worksheet.findall("Яндекс Еда")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'aptekaru':
                message(call)
                cell_list = worksheet.findall("Аптека.ру")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'aptekasklad':
                message(call)
                cell_list = worksheet.findall("Аптека от склада")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'eapteka':
                message(call)
                cell_list = worksheet.findall("ЕАптека Тг")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'uteka':
                message(call)
                cell_list = worksheet.findall("Ютека")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'sberhealth':
                message(call)
                cell_list = worksheet.findall("Сбер Здоровье")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'burgerking':
                message(call)
                cell_list = worksheet.findall("Бургер Кинг")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                     "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'kfc':
                message(call)
                cell_list = worksheet.findall("KFC")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'foodband':
                message(call)
                cell_list = worksheet.findall("FoodBand")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'mnogolososya':
                message(call)
                cell_list = worksheet.findall("Много лосося")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'niyama':
                message(call)
                cell_list = worksheet.findall("Нияма ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'tvoyapizza':
                message(call)
                cell_list = worksheet.findall("TVOЯ пицца")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'tanuki':
                message(call)
                cell_list = worksheet.findall("Тануки")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'yakitoria':
                message(call)
                cell_list = worksheet.findall("Якитория")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'flor2u':
                message(call)
                cell_list = worksheet.findall("Flor2U")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'cvetryad':
                message(call)
                cell_list = worksheet.findall("Цветочный ряд")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'vkmusic':
                message(call)
                cell_list = worksheet.findall("Vk музыка")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'paket':
                message(call)
                cell_list = worksheet.findall("Пакет")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'ogon':
                message(call)
                cell_list = worksheet.findall("Огонь")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'kinopoisk':
                message(call)
                cell_list = worksheet.findall("Кинопоиск ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'okko':
                message(call)
                cell_list = worksheet.findall("Okko")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexplusmulti':
                message(call)
                cell_list = worksheet.findall("Яндекс плюс мульти")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexafisha':
                message(call)
                cell_list = worksheet.findall("Яндекс Афиша")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'tamaris':
                message(call)
                cell_list = worksheet.findall("Tamaris ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'befree':
                message(call)
                cell_list = worksheet.findall("Befree")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'sportmaster':
                message(call)
                cell_list = worksheet.findall("Спортмастер")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'letual':
                message(call)
                cell_list = worksheet.findall("Летуаль")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'goldapple':
                message(call)
                cell_list = worksheet.findall("Золотое Яблоко")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'ulibkaradugi':
                message(call)
                cell_list = worksheet.findall("Улыбка радуги")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'samokatbeatu':
                message(call)
                cell_list = worksheet.findall("Самокат Бьюти")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'taximaksim':
                message(call)
                cell_list = worksheet.findall("Такси Максим")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshetaxi())
            elif call.data == 'tinkoffstrahavto':
                message(call)
                cell_list = worksheet.findall("Тинькофф Страхование Авто")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahavto':
                message(call)
                cell_list = worksheet.findall("Сбер Страхование Авто")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahdom':
                message(call)
                cell_list = worksheet.findall("Сбер Страхование Жилье")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'tinkoffput':
                message(call)
                cell_list = worksheet.findall("Тинькофф Путешествия")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheairtickets())
            elif call.data == 'yandexput':
                message(call)
                cell_list = worksheet.findall("Яндекс путешествия ")
                for i in cell_list:
                    formattext(call, int(i.row))
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheairtickets())
            else:
                menu(call)


    except Exception as e:
        print(repr(e))

def kudadalshemarket():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Маркетплейс', callback_data='marketplace')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshebank():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Бонусы от банков', callback_data='banks')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalsheinvest():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Инвестиции', callback_data='investments')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshedelivery():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Доставка/продукты', callback_data='delivery')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshehealth():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Аптеки/здоровье', callback_data='health')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshcafe():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Кафе/рестораны', callback_data='cafe')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshflowers():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Цветы', callback_data='flowers')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshepodpiska():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Онлайн сервис/подписка', callback_data='online_service')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalsheclothes():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Обувь/одежда', callback_data='clothes')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalsheosmetics():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Косметика/парфюмерия', callback_data='cosmetics')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalshetaxi():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Такси/каршеринг', callback_data='taxi')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalsheinsurance():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Страхование', callback_data='insurance')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def kudadalsheairtickets():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Авиабилеты/гостинницы', callback_data='air_tickets')
    item2 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.add(item1, item2)
    return markup

def message(call):
    bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
перейти по ссылке или скопировать значение купона с 
данной страницы и ввести его на сайте компании☺️""")

def formattext(call, n):
    worksheet = sh.sheet1
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
    item1 = types.InlineKeyboardButton('Маркетплейс', callback_data='marketplace')
    item2 = types.InlineKeyboardButton('Бонусы от банков', callback_data='banks')
    item3 = types.InlineKeyboardButton('Инвестиции', callback_data='investments')
    item4 = types.InlineKeyboardButton('Доставка/продукты', callback_data='delivery')
    item5 = types.InlineKeyboardButton('Аптеки/здоровье', callback_data='health')
    item6 = types.InlineKeyboardButton('Кафе/рестораны', callback_data='cafe')
    item7 = types.InlineKeyboardButton('Цветы', callback_data='flowers')
    item8 = types.InlineKeyboardButton('Онлайн сервис/подписка', callback_data='online_service')
    item9 = types.InlineKeyboardButton('Обувь/одежда', callback_data='clothes')
    item10 = types.InlineKeyboardButton('Косметика/парфюмерия', callback_data='cosmetics')
    item11 = types.InlineKeyboardButton('Такси/каршеринг', callback_data='taxi')
    item12 = types.InlineKeyboardButton('Страхование', callback_data='insurance')
    item13 = types.InlineKeyboardButton('Авиабилеты/гостинницы', callback_data='air_tickets')
    item14 = types.InlineKeyboardButton('Таблица со всеми промокодами', callback_data='table', url="https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)
    bot.send_message(call.message.chat.id, 'Выберите категорию в которой хотите получить скидку', reply_markup=markup, parse_mode='html')



bot.polling(none_stop=True)

