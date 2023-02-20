import telebot
from telebot import types
import gspread

TOKEN = '6089466461:AAFtYdjnPwNPp88FyXHxius4U9YRcJkc_og' \

bot = telebot.TeleBot(TOKEN)

gc = gspread.service_account(filename="json\my-test-378416-ed0f5f5170ee.json")
sh = gc.open("Копия Промокоды")


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
                item9 = types.InlineKeyboardButton('Зоозавр', callback_data='zoozavr')
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
                formattext(call,2)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())

            elif call.data == 'ozon':
                message(call)
                formattext(call, 3)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'sbermegamarket':
                message(call)
                formattext(call, 4)
                formattext(call, 5)
                formattext(call, 6)
                formattext(call, 7)
                formattext(call, 8)
                formattext(call, 9)
                formattext(call, 10)
                formattext(call, 11)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mvideo':
                message(call)
                formattext(call, 12)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'aldorado':
                message(call)
                formattext(call, 13)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mtc':
                message(call)
                formattext(call, 14)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'wildberries':
                message(call)
                formattext(call, 15)
                formattext(call, 16)
                formattext(call, 17)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'utkonos':
                message(call)
                formattext(call, 18)
                formattext(call, 19)
                formattext(call, 20)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'zoozavr':
                message(call)
                formattext(call, 21)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'obi':
                message(call)
                formattext(call, 22)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'galamart':
                message(call)
                formattext(call, 23)
                formattext(call, 24)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'alpha':
                message(call)
                formattext(call, 25)
                formattext(call, 26)
                formattext(call, 27)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'gaz':
                message(call)
                formattext(call, 28)
                formattext(call, 29)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoffinst':
                message(call)
                formattext(call, 30)
                formattext(call, 32)
                formattext(call, 35)
                formattext(call, 36)
                formattext(call, 37)
                formattext(call, 38)
                formattext(call, 39)
                formattext(call, 40)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff':
                message(call)
                formattext(call, 31)
                formattext(call, 33)
                formattext(call, 34)
                formattext(call, 41)
                formattext(call, 42)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'akbars':
                message(call)
                formattext(call, 43)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'home':
                message(call)
                formattext(call, 44)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'open':
                message(call)
                formattext(call, 45)
                formattext(call, 46)
                formattext(call, 47)
                formattext(call, 48)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'renesans':
                message(call)
                formattext(call, 49)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'rosbank':
                message(call)
                formattext(call, 50)
                formattext(call, 51)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tochkabank':
                message(call)
                formattext(call, 52)
                formattext(call, 53)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'ubrir':
                message(call)
                formattext(call, 54)
                formattext(call, 55)
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'uralsib':
                message(call)
                formattext(call, 56)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff_investments':
                message(call)
                formattext(call, 57)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'freedome_finance':
                message(call)
                formattext(call, 58)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'vkusvill':
                message(call)
                formattext(call, 59)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'vinlab':
                message(call)
                formattext(call, 60)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'globus':
                message(call)
                formattext(call, 61)
                formattext(call, 62)
                formattext(call, 63)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'deliveryclub':
                message(call)
                formattext(call, 64)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'sbermarket':
                message(call)
                formattext(call, 65)
                formattext(call, 66)
                formattext(call, 67)
                formattext(call, 68)
                formattext(call, 69)
                formattext(call, 70)
                formattext(call, 71)
                formattext(call, 72)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'lenta':
                message(call)
                formattext(call, 73)
                formattext(call, 74)
                formattext(call, 75)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'magnit':
                message(call)
                formattext(call, 75)
                formattext(call, 76)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'metro':
                message(call)
                formattext(call, 77)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'omolochko':
                message(call)
                formattext(call, 78)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'pyaterochka':
                message(call)
                formattext(call, 79)
                formattext(call, 81)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestok':
                message(call)
                formattext(call, 82)
                formattext(call, 83)
                formattext(call, 84)
                formattext(call, 85)
                formattext(call, 86)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestokvprok':
                message(call)
                formattext(call, 87)
                formattext(call, 88)
                formattext(call, 89)
                formattext(call, 90)
                formattext(call, 91)
                formattext(call, 92)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'samokat':
                message(call)
                formattext(call, 93)
                formattext(call, 94)
                formattext(call, 95)
                formattext(call, 96)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexlavka':
                message(call)
                formattext(call, 97)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexeda':
                message(call)
                formattext(call, 98)
                formattext(call, 99)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'aptekaru':
                message(call)
                formattext(call, 100)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'aptekasklad':
                message(call)
                formattext(call, 101)
                formattext(call, 102)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'eapteka':
                message(call)
                formattext(call, 103)
                formattext(call, 104)
                formattext(call, 105)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'uteka':
                message(call)
                formattext(call, 106)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'sberhealth':
                message(call)
                formattext(call, 107)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'burgerking':
                message(call)
                formattext(call, 108)
                bot.send_message(call.message.chat.id,
                     "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'kfc':
                message(call)
                formattext(call, 109)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'foodband':
                message(call)
                formattext(call, 110)
                formattext(call, 111)
                formattext(call, 112)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'mnogolososya':
                message(call)
                formattext(call, 113)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'niyama':
                message(call)
                formattext(call, 114)
                formattext(call, 115)
                formattext(call, 116)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'tvoyapizza':
                message(call)
                formattext(call, 117)
                formattext(call, 118)
                formattext(call, 119)
                formattext(call, 120)
                formattext(call, 121)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'tanuki':
                message(call)
                formattext(call, 122)
                formattext(call, 123)
                formattext(call, 124)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'yakitoria':
                message(call)
                formattext(call, 125)
                formattext(call, 126)
                formattext(call, 127)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'flor2u':
                message(call)
                formattext(call, 128)
                formattext(call, 129)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'cvetryad':
                message(call)
                formattext(call, 130)
                formattext(call, 131)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'vkmusic':
                message(call)
                formattext(call, 132)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'paket':
                message(call)
                formattext(call, 133)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'ogon':
                message(call)
                formattext(call, 134)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'kinopoisk':
                message(call)
                formattext(call, 135)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'okko':
                message(call)
                formattext(call, 136)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexplusmulti':
                message(call)
                formattext(call, 137)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexafisha':
                message(call)
                formattext(call, 138)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'tamaris':
                message(call)
                formattext(call, 139)
                formattext(call, 140)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'befree':
                message(call)
                formattext(call, 141)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'sportmaster':
                message(call)
                formattext(call, 142)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'letual':
                message(call)
                formattext(call, 143)
                formattext(call, 144)
                formattext(call, 145)
                formattext(call, 146)
                formattext(call, 147)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'goldapple':
                message(call)
                formattext(call, 148)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'ulibkaradugi':
                message(call)
                formattext(call, 149)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'samokatbeatu':
                message(call)
                formattext(call, 150)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'taximaksim':
                message(call)
                formattext(call, 151)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshetaxi())
            elif call.data == 'tinkoffstrahavto':
                message(call)
                formattext(call, 152)
                formattext(call, 153)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahavto':
                message(call)
                formattext(call, 154)
                formattext(call, 155)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahdom':
                message(call)
                formattext(call, 156)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'tinkoffput':
                message(call)
                formattext(call, 157)
                formattext(call, 158)
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheairtickets())
            elif call.data == 'yandexput':
                message(call)
                formattext(call, 159)
                formattext(call, 160)
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
    item1 = types.InlineKeyboardButton('Кафе/рестораны', callback_data='cafe')
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

def formattext(call,n):
    worksheet = sh.sheet1
    values_list = worksheet.row_values(n)
    print(values_list)
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

