import telebot
from telebot import types
import random

TOKEN = '6089466461:AAFtYdjnPwNPp88FyXHxius4U9YRcJkc_og' \

bot = telebot.TeleBot(TOKEN)

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
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                       перейти по ссылке или скопировать значение купона с 
                                                       данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, f"""Название: Яндекс Маркет
                                                       Скидка: В зависимости от выбранного промокода/акции
                                                       Описание: Актуальная подборка выгодных акций и промокодов от @skidkikochanovabot доступна по ссылке \n
                                                       Действует до: В зависимости от выбранного промокода/акции
                                                       Регион: Россия
                                                       Ссылка: https://clck.ru/33FSyM
                                                       Промокод ниже👇
                                                       """, parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())

            elif call.data == 'ozon':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")

                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'sbermegamarket':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Сбермегамаркет
                                                          Скидка: 300₽
                                                          Описание: Скидка 300 рублей при первом заказе от 1500 рублей. Напиши в чате ТГ или директ инсты "Хочу промокод Сбермегамаркет"
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://t.me/+jxOVO4k0w-s5OTli
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id, "Промокод запросить у менеджера ТГ чата по ссылке или в директ инсты")
                bot.send_message(call.message.chat.id, """Название: Сбермегамаркет
                                                          Скидка: 1 000₽
                                                          Описание: Скидка 1000₽ на первый заказ от 5000₽. Действует на все категории товаров кроме категорий Красота и Уход, Бренд Rieker, Алкогольная продукция, Шины , Наушники Apple
                                                          Действует до: 08.03.23
                                                          Регион: Россия
                                                          Ссылка: https://sbermegamarket.prfl.me/skidkinezagorami/f06401afe17a
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "pffe17636")
                bot.send_message(call.message.chat.id, """Скидка: 700₽
                                                          Описание: Скидка 700₽ на первый заказ от 3500₽. Не действует на товары брендов Apple и Rieker, на товары категории «Шины», «Смартфоны», «Портативная акустика», на товары по акции «Гарантия лучших цен».
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://sbermegamarket.prfl.me/skidkinezagorami/f06401afe17a
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "pfd91835")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mvideo':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: МВидео
                                                          Скидка: В зависимости от выбранного промокода/акции
                                                          Описание: Актуальная подборка выгодных акций и промокодов от @skidkikochanovabot доступна по ссылке 
                                                          Действует до: В зависимости от выбранного промокода/акции
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/bAogd
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Список промокодов и акций доступен по ссылке")

                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'aldorado':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Эльдорадо
                                                          Скидка: В зависимости от выбранного промокода/акции
                                                          Описание: Актуальная подборка выгодных акций и промокодов от @skidkikochanovabot доступна по ссылке 
                                                          Действует до: В зависимости от выбранного промокода/акции
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/bAogd
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Список промокодов и акций доступен по ссылке")

                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'mtc':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: МТС
                                                          Скидка: В зависимости от выбранного промокода/акции
                                                          Описание: Актуальная подборка выгодных акций и промокодов от @skidkikochanovabot доступна по ссылке 
                                                          Действует до: В зависимости от выбранного промокода/акции
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/dt3w3
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Список промокодов и акций доступен по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'wildberries':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Wildberries
                                                          Скидка: В зависимости от выбранного товара
                                                          Описание: Наш бренд джинсов высокого качества Amorenezagorami на WB
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка:  https://www.wildberries.ru/brands/amorenezagoram
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Доступ по ссылке")
                bot.send_message(call.message.chat.id, """Название: Wildberries
                                                          Скидка: Курс "Как покорить Вайлдберриз"
                                                          Описание: Пройдите наш курс "Как покорить Вайлдберриз" и узнайте как выйти на доход от 200 тыс. после 1 месяца. Обязательно посмотрите наши бесплатные вебинары
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка:  https://skidkinezagorami.ru/
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Доступ по ссылке")
                bot.send_message(call.message.chat.id, """Название: Wildberries
                                                          Скидка: 30 дней бесплатной работы в сервисе аналитики Market Guru
                                                          Описание: Зарегистрируйся по ссылки и получи 30 дней бесплатного доступа к сервису аналитики Market Guru (для WB и Ozon)
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://my.marketguru.io/?r=yam0ix
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Доступ по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'utkonos':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Утконос
                                                          Скидка: 300₽
                                                          Описание: Скидка 300р на любой заказ от 3000р (суммируется с акциями в приложении)
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://my.marketguru.io/?r=yam0ix
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "300UT18")
                bot.send_message(call.message.chat.id, """Название: Утконос
                                                          Скидка: 500₽ и бесплатная доставка
                                                          Описание: Скидка 500₽ на первый заказ от 1800₽ и бесплатная доставка, суммируется с акциями
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://utkonos.prfl.me/skidkinezagorami/fafedab3f683?marker=2VtzqxUdEux
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "UT0604")
                bot.send_message(call.message.chat.id, """Название: Утконос
                                                          Скидка: 25% и бесплатная доставка
                                                          Описание: Скидка 25% на 2 любых заказа от 3000р и бесплатная доставка 
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://utkonos.prfl.me/skidkinezagorami/fafedab3f683?marker=2VtzqxUdEux
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "25UT10625")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'zoozavr':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Зоозавр ТГ
                                                          Скидка: 15%
                                                          Описание: Скидка 15% на первый заказ от 1500р. Суммируется с акциями
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://zoozavr-detmir.prfl.me/skidkinezagorami/b765d5b51e06?marker=2VtzqwtZsoY
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "PFDM8649")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'obi':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: OBI
                                                          Скидка: 10%
                                                          Описание: Скидка 10% при покупке от 7000₽ по штрих-коду
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33TAxb
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Штрих-код по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'galamart':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Galamart 
                                                          Скидка: 22%
                                                          Описание: Скидка 22% на первый заказ и бесплатная доставка от 1500₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка: https://galamart.prfl.me/skidkinezagorami/97f0db0a8d8d
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GLMRT22-UWF")
                bot.send_message(call.message.chat.id, """Название: Galamart 
                                                          Скидка: 19%
                                                          Описание: Скидка 19% на повторный заказ и бесплатная доставка от 1500₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка: https://galamart.prfl.me/skidkinezagorami/97f0db0a8d8d
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GLMRT19-0K5")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshemarket())
            elif call.data == 'alpha':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Альфа Банк
                                                          Скидка: 500₽ по дебетовой карте
                                                          Описание: Бесплатная дебетовая карта, получи кешбек 500₽после любой первой покупки, кешбек 5% на 3 или 4 категории, до 100% кэшбека на одну категорию в течение месяца в барабане суперкешбека
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/cR0ck
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id, """Название: Альфа Банк
                                                          Скидка: 500₽ по дебетовой карте
                                                          Описание: В Альфе дают 500 ₽ после первой покупки, если оформишь бесплатную дебетовую Альфа-Карту по ссылке ниже
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка:  https://alfa.me/RPlBnQ
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id, """Название: Альфа Банк
                                                          Скидка: 365 дней без % плюс год бесплатного обслуживания по кредитной карте
                                                          Описание: 365 дней без % на покупки плюс год бесплатного обслуживания по кредитной карте
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/QGXMc
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'gaz':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Газпромбанк
                                                          Скидка: 1000₽ кэшбек по кредитной карте
                                                          Описание: Кредитная карта, получи кешбэк 1000₽ за любую первую покупку, 10 дней без%, бесплатное обслуживание 
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка:  https://gtblg.ru/61yZq
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Штрих-код по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoffinst':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Tinkoff инст
                                                          Скидка: 1000₽ кэшбек по дебетовой карте
                                                          Описание: Дебетовая карта, получи кешбэк 1000₽ за траты от 3000₽ в первый месяц
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33TAwQ
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Tinkoff
                                                          Скидка: Бонусы до 2000 рублей по дебетовым и кредитным картам
                                                          Описание: Бонусы по дебетовым, кредитным картам и другим продуктам банка на ваш выбор
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: tinkoff.ru/sl/eED4yuGGT1
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'akbars':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Ак барс банк
                                                          Скидка: Кешбэк 10% на всё + 10% годовых на остаток, 3000₽ за перевод пенсии на карту 
                                                          Описание: Получай кешбек 10% на всё до 28.02(но не более 2000₽/мес)+ бесплатное обслуживание, а также до 10% годовых на остаток( 10% годовых начисляется на остаток от 30 000 ₽ до 100 000 ₽, 3% — при остатке ниже 30 000 ₽, 2% — на остаток выше 100 000). 3000₽ единоразово если перевести получение пенсии на эту карту, через Пенсионный фонд.
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/7iJyx
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'home':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Home Сredit
                                                          Скидка: 500 р по дебетовой, кредитной карте или карте рассрочки
                                                          Описание: Бонус 500 руб при оформлении карты
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: hcrd.ru/ekM3tM
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'open':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Открытие банк
                                                          Скидка: 500 бонусных рублей по дебетовой карте
                                                          Описание: Потрать  1500₽ в течение 30 дней после получения карты и получи 500₽
                                                          Действует до: бессрочно
                                                          Ссылка:  https://mgm.open.ru/friend/zhtbij
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'renesans':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Ренессанс кредит
                                                          Скидка: 2.000₽ кешбэк по кредитной карте "Разумная"
                                                          Описание: Кешбэк 2000₽ за покупки от 2000₽ до 28.02.23; льготный период 145 дней без % на все операции, бесплатное обслуживание навсегда, кешбэк у партнёров при оплате картой
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка:  https://gtblg.ru/TB0AI
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'rosbank':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Росбанк
                                                          Скидка: 500₽ по дебетовой карте Можно Все
                                                          Описание: Дебетовая карта, 500₽ приветственный кэшбэк за покупки от 300₽. 3% кэшбэк на выбранные категории
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка:  https://clck.ru/33Rfe6
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tochkabank':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Точка банк
                                                          Скидка: Бесплатная регистрация  ип
                                                          Описание: Зарегистрируй ИП по ссылке бесплатно без похода в МФЦ и налоговую
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка:  https://clck.ru/giEat
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'ubrir':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: УБРиР ТГ
                                                          Скидка: 1000₽ бонусных рублей на дебетовую карту
                                                          Описание: Потрать 1000₽ в течение 2 месяцев и получи кешбек 1000₽.  Бесплатная дебетовая карта, 5% кешбек на оплату ЖКХ и покупки в интернете, до 1% на остальные покупки
                                                          Действует до: 31.03.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/KeP9A?token=CR8ZwR5Q4npkOFnbP50Ncjtg
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'uralsib':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Уралсиб
                                                          Скидка: 18% на остаток плюс кешбек 3% по дебетовой карте
                                                          Описание: Кешбек до 3% на все покупки, до 20% годовых на ежедневный остаток, бесплатное обслуживание при тратах от 10 тыс.руб, бесплатное снятие наличных в любых банкоматах от 3 тыс.руб
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://usnd.to/UzVN
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshebank())
            elif call.data == 'tinkoff_investments':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Тинькофф Инвестиции
                                                          Скидка: Акция стоимостью до 20000₽
                                                          Описание: Откройте брокерский счет по ссылке и получите в подарок акцию стоимостью до 20000₽
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: tinkoff.ru/sl/9bLZobj3dBs
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'freedome_finance':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Freedom Finance
                                                          Скидка: Вход на крупную инвестиционную площадку
                                                          Описание: Откройте брокерский счет по ссылке и начни инвестировать на крупной инвестиционной площадке
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/32fq7Q
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует только по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinvest())
            elif call.data == 'vkusvill':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: ВкусВилл
                                                          Скидка: 200₽
                                                          Описание: Скидка на первый онлайн заказ от 1000₽ (не распространяется на товары из категории "Аптека")
                                                          Действует до: Бессрочно
                                                          Регион: Зону доставки и магазины для самовывоза проверяйте в приложении
                                                          Ссылка: https://vkusvill.ru/
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "VSEC9C")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'vinlab':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Винлаб 
                                                          Скидка: 10%
                                                          Описание: Скидка 10% на любой заказ 
                                                          Действует до: 28.02.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://winelab.prfl.me/skidkinezagorami/840dbc1c5901
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "PRFL8924")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'globus':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Глобус
                                                          Скидка: 10%
                                                          Описание: Скидка 10% на повторный заказ от 5000₽. Не суммируется с акциями на сайте, не распространяется на алкоголь, бытовую технику и электронику
                                                          Действует до: 31.03.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://gtblg.ru/gthET
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "G232B287")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'deliveryclub':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Delivery Club
                                                          Скидка: 27%
                                                          Описание: Скидка 27% на первый заказ в разделе  магазины от любой суммы, скидка не более 2.000₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка: https://delivery.prfl.me/skidkinezagorami/3494235aa51d
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "VP90SGYK")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'sbermarket':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Сбермаркет
                                                          Скидка: 300₽
                                                          Описание: Скидка 300₽ на повторный заказ от 1800₽ + бесплатная доставка
                                                          Действует до: 28.02.23
                                                          Регион: Казань
                                                          Ссылка: https://clck.ru/33PSpz
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "kaz37c")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'lenta':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Лента онлайн
                                                          Скидка: 500₽ и бесплатная доставка
                                                          Описание: Скидка 500₽ на первый заказ от 1.800₽ и три бесплатные доставки. Суммируется со всеми скидками.
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://lentaonline.prfl.me/skidkinezagorami/cca66cbb905e?marker=2VtzqxhrftM
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "ALLA500")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'magnit':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Магнит
                                                          Скидка: 25%
                                                          Описание: Скидка 25% на первый заказ в приложении от 1000₽, не суммируется со скидками
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка: https://magnitdeli.prfl.me/skidkinezagorami/27e8698269ab
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "SNOW557502")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'metro':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Metro
                                                          Скидка: 20%
                                                          Описание: Скидка 20% на первые три покупки, после регистрации выдается специальный купон на скидку
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка:  http://metro-cc.ru/blogger
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "h5h58")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'omolochko':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: ОмолокО (Чистая линия)
                                                          Скидка: 10%
                                                          Описание: Скидка 10% на заказ от 1000 руб + бесплатная доставка
                                                          Действует до: Бессрочно
                                                          Регион: Москва и МО
                                                          Ссылка: Omoloko.ru
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "SML623781")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'pyaterochka':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Пятёрочка
                                                          Скидка: 25%
                                                          Описание: Скидка 25% на первый заказ от 500₽ и бесплатная доставка, не суммируется с акциями
                                                          Действует до: 19.02.23
                                                          Регион: Россия
                                                          Ссылка: https://5kanew.prfl.me/skidkinezagorami/6e5918f88a59
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "qrrdnc53h")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestok':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Перекрёсток 
                                                          Скидка: 500₽
                                                          Описание: Скидка 500₽ на первый заказ от 2000₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: {'<a href=": https://perekrestok-cpa.prfl.me/skidkinezagorami/eccf8f316dc0?marker=2Vtzqwy6XQE
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "JWPR4S")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestokvprok':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Перекресток Впрок
                                                          Скидка: 22%
                                                          Описание: Скидка 22% на первый заказ от 2.500₽ на доставку.  СУММИРУЕТСЯ со скидками, не распространяется на категории овощи, фрукты, ягоды,товары маркетплейса и социально-значимые позиции, не действует на товары-исключения vprok.ru/s-exc
                                                          Действует до: 26.02.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://prod.prfl.me/skidkinezagorami/55cb7c97b9e8
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "22ZA5")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'perekrestokvprok':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Перекресток Впрок
                                                          Скидка: 22%
                                                          Описание: Скидка 22% на первый заказ от 2.500₽ на доставку.  СУММИРУЕТСЯ со скидками, не распространяется на категории овощи, фрукты, ягоды,товары маркетплейса и социально-значимые позиции, не действует на товары-исключения vprok.ru/s-exc
                                                          Действует до: 26.02.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://prod.prfl.me/skidkinezagorami/55cb7c97b9e8
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "22ZA5")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'samokat':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Самокат
                                                          Скидка: 45%
                                                          Описание: Скидка на первый заказ от 700₽
                                                          Действует до: 28.02.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://samokat.prfl.me/skidkinezagorami/0216bf5f4e69?marker=2VtzqvyfSG9
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "PLEX2R")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexlavka':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Яндекс Лавка
                                                          Скидка: 40%
                                                          Описание: Скидка 40% на первый заказ, но не более 600 ₽
                                                          Действует до: Бессрочно
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://clck.ru/32iBgm
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "pou7jswj")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'yandexeda':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Яндекс Еда
                                                          Скидка: 20% в категории рестораны 
                                                          Описание: Скидка 20% на первый заказ в категории рестораны от 900₽, скидка не более 2.000₽
                                                          Действует до: 10.03.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://clck.ru/33Vuzm
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "PXBTEXM5")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshedelivery())
            elif call.data == 'aptekaru':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Аптека.ру
                                                          Скидка: 3%
                                                          Описание: Скидка на любые виды товаров
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://apteka.ru
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "ДЯТЕЛ")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'aptekasklad':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Аптека от склада
                                                          Скидка: 8%
                                                          Описание: Скидка 8% на повторный заказ от 800₽, суммируется с акциями, но не проходит на товары с отметкой стоп-цена, макс скидка 200₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://aptekaotsklada.prfl.me/skidkinezagorami/ffe5edaa1941?marker=2Vtzqwy6SJX
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "15A88B9")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'eapteka':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: ЕАптека Тг
                                                          Скидка: 350₽
                                                          Описание: Скидка 350₽ на первый заказ от 1600₽
                                                          Действует до: 15.03.23
                                                          Регион: Россия
                                                          Ссылка: https://eapteka.prfl.me/skidkinezagorami/9591b15f0c3b?marker=2VtzqucTrXN
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "FM30COTC")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'uteka':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Ютека
                                                          Скидка: 150₽
                                                          Описание: Скидка 150 рублей на первый заказ от 500 рублей в аптеках-партнерах Ютеки. При заказе выбирай аптеку, в которой можно применить промокод и заказывай со скидкой.
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://a.uteka.ru
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "UT3BC1AB9D")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'sberhealth':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Сбер Здоровье
                                                          Скидка: Онлайн-консультации на год
                                                          Описание: Запись на приём к врачу, онлайн-консультации и другие медицинские сервисы для здоровья вашей семьи
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33BPRS
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshehealth())
            elif call.data == 'burgerking':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Бургер Кинг
                                                          Скидка: 400 корон на еду
                                                          Описание: Вводи промокод при регистрации и активируй свой аккаунт в программе лояльности, бонусы придут за первый заказ от 699 руб. на твой счет 
                                                          Действует до: Бессрочно 
                                                          Регион: Россия 
                                                          Ссылка: http://burgerking.ru/dapp?coupon=LXXWLA
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                     "LXXWLA")
                bot.send_message(call.message.chat.id,
                     "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'kfc':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: KFC
                                                          Скидка: 15%
                                                          Описание: Скидка 15% на первую доставку при заказе от 799₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия 
                                                          Ссылка: https://kfcmobile.prfl.me/skidkinezagorami/fc7eb62a66a6?marker=2VtzqxmHBa3
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "PERF232095")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'foodband':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: FoodBand
                                                          Скидка: подарок на выбор
                                                          Описание: Подарок на выбор в день рождения. Акция действует за семь дней до, в сам день рождения и семь дней после него. Минимальная сумма заказа 650р.
                                                          Действует до: Бессрочно
                                                          Регион: Москва
                                                          Ссылка: https://ad.admitad.com/g/c5ie7eiipzc295601c6b2e77510c9d/?i=3
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "yourday")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'mnogolososya':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Много лосося
                                                          Скидка: 400₽
                                                          Описание: Скидка 400₽ на первый заказ от 600₽
                                                          Действует до: 28.02.23
                                                          Регион: Мск и Спб
                                                          Ссылка: https://clck.ru/33TAzx
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "ZT9R8")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'niyama':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Нияма 
                                                          Скидка: вок Удон с курицей 
                                                          Описание: Вок Удон с курицей в кисло-сладком соусе в подарок при заказе от 1999₽
                                                          Действует до: 30.04.23
                                                          Регион: Москва и МО
                                                          Ссылка: https://gtblg.ru/bNMpF
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GETU1325")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'tanuki':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Тануки
                                                          Скидка: роллы орандж краб и курай
                                                          Описание: Скачай приложение и получи  роллы орандж краб и курай на заказ от 1490₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33TB29
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "17TPF177")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'yakitoria':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Якитория
                                                          Скидка: пицца пепперони
                                                          Описание: Пицца пепперони в подарок от 1.700₽
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://yaki.prfl.me/skidkinezagorami/7cc3af2e5723
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "4CHHQB2N")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshcafe())
            elif call.data == 'flor2u':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Flor2U
                                                          Скидка: 40%
                                                          Описание: Скидка 40% на первый заказ 
                                                          Действует до: 
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/h9yvW
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "CDDJH77Q56")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'cvetryad':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Цветочный ряд
                                                          Скидка: 20%
                                                          Описание: Скидка 20% на покупку от 3.000₽
                                                          Действует до: 31.03.23
                                                          Регион: Россия
                                                          Ссылка: https://tsvet-ryad.prfl.me/skidkinezagorami/543c0a5730d7
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "BP106")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshflowers())
            elif call.data == 'vkmusic':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Vk музыка
                                                          Скидка: Бесплатно/ 30 дней 
                                                          Описание: Месяц бесплатной подписки vk музыка для новых пользователей 
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/ITfAH
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GETL91HC")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'paket':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Пакет
                                                          Скидка: 1мес/ 1₽ +1.000 бонусов
                                                          Описание: Подключай сервис Пакет х5 и поручай повышенный кешбэк и бесплатные доставки, 5% кешбэк на чеки в Пятерочке и Перекрёстке; 50% кешбэк на кофе; 20% кешбэк на выпечку и дополнительные бонусы от партнеров
                                                          Действует до: 22.02.23
                                                          Регион: Россия
                                                          Ссылка: https://x5paket.prfl.me/skidkinezagorami/f537daaebf9b?marker=2VtzqwbEt7L
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GETL91HC")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'ogon':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Огонь
                                                          Скидка: 1 месяц/ 1₽
                                                          Описание: Подписка на сервис предоставляющий огромный выбор скидок.Скидки в Ленту, Ленту онлайн, ситилинк, АСНА, РИВ ГОШ, Fun/sun 6% и др (всех партнероы смотри по ссылке)
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://ogon.prfl.me/skidkinezagorami/844c2f5a3e31
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "6PFE3VOR81")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'kinopoisk':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Кинопоиск 
                                                          Скидка: 60 дней бесплатно
                                                          Описание: Введи промокод и получи 60 дней подписки 
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/32YuXy
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "EFQZW3X2V3")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'okko':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Okko
                                                          Скидка: 35 дней за 1 рубль 
                                                          Описание: Подписка "Оптимум" за 1 рубль на 35 дней. Здесь собрано 90 000 фильмов, сериалов, образовательных программ и мультфильмов без рекламы; более 700 фильмов в качестве Ultra HD 4K и в 8К
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/eNlXg?token=CR9JDk7O0Ip0u0aLUlnWllCw
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "45077560")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexplusmulti':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Яндекс плюс мульти
                                                          Скидка: 60 дней / бесплатно
                                                          Описание: Бесплатный доступ на Яндекс плюс мульти на 60 дней по промокоду
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33RfUg
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "J3XTLLPBYL")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'yandexafisha':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Яндекс Афиша
                                                          Скидка: 400₽
                                                          Описание: Скидка 400₽ на первую покупку билетов от 3.000₽ (не действует на покупку билетов в кино)
                                                          Действует до: 25.04.23
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33SBuw
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "P74044")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshepodpiska())
            elif call.data == 'tamaris':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Tamaris 
                                                          Скидка: 23%
                                                          Описание: Скидка 23% на товары сезона осень-зима 22/23, не суммируется с другими действующими промокодами, суммируется со скидками в разделе sale
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://tamaris.ru/
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "skidkinezagorami23")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'befree':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Befree
                                                          Скидка: 25%
                                                          Описание: Скидка 25% на новинки + 10% за онлайн оплату
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/PFjQW
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "U8FHGB")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'sportmaster':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Спортмастер
                                                          Скидка: 20%
                                                          Описание: Скидка 20% на одежду и обувь и 10% на спортивный инвентарь. Бренды исключения: Nike, PUMA, Adidas Reebok, Columbia u Solomon. Промокод суммируется до максимальной скидки 50%.
                                                          Скидки не суммируются с бонусами и другими промо акциями.
                                                          Действует до: 21.02.23
                                                          Регион: Россия
                                                          Ссылка: https://sportmaster.prfl.me/skidkinezagorami/e9daa386c638
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "OMN8888")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheclothes())
            elif call.data == 'letual':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Летуаль
                                                          Скидка: 25%
                                                          Описание: Скидка 25% по бриллиантовой карте. Суммируется с другими акциями. 
                                                          Действует до: Бессрочно 
                                                          Регион: Россия
                                                          Ссылка: https://www.letu.ru/
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "0411651433")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'goldapple':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Золотое Яблоко
                                                          Скидка: 15%
                                                          Описание: Скидка 15% первый онлайн заказ от 1000₽, не применяется к брендам-исключениям, применяется на товары со скидкой до 40% включительно 
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://goldapple.prfl.me/skidkinezagorami/4ab70335f491
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "HELLO")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'ulibkaradugi':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Улыбка радуги
                                                          Скидка: 20%
                                                          Описание: Скидка 20% для всех, не суммируется с акциями на сайте
                                                          Действует до: 28.02.23
                                                          Регион: Зону доставки проверяйте в приложении
                                                          Ссылка: https://gtblg.ru/QL9Zd
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "GB514")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'samokatbeatu':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Самокат Бьюти
                                                          Скидка: 20% на первый заказ
                                                          Описание: 20% скидки на первый заказ в категории Бьюти
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33BNx4
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheosmetics())
            elif call.data == 'taximaksim':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Такси Максим
                                                          Скидка: 500₽
                                                          Описание: Введи промокод и получи 500 премиальных рублей на поездки и доставку
                                                          Действует до: Бессрочно
                                                          Регион: На территории действия компании
                                                          Ссылка: https://taximaxim.com/l/clireferral
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "BF38E4E3")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalshetaxi())
            elif call.data == 'tinkoffstrahavto':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Тинькофф Страхование Авто
                                                          Скидка: 10% на КАСКО
                                                          Описание: Получи скидку 10% на КАСКО. Для получения скидки сообщи оператору, что твоя заявка по рекомендации
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://www.tinkoff.ru/sl/4yrMOcQBbVN
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahavto':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Сбер Страхование Авто
                                                          Скидка: выгода до 30% на КАСКО
                                                          Описание: Полис КАСКО с выгодой до 30%
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33BPFc
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'sberstrahdom':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Сбер Страхование Жилье
                                                          Скидка: Защита квартиры и дома
                                                          Описание: Защита квартиры и дома от 332₽ в месяц
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://clck.ru/33BPKH
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheinsurance())
            elif call.data == 'tinkoffput':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Тинькофф Путешествия
                                                          Скидка: Кэшбэк до 10% от суммы бронирования
                                                          Описание: Переходи по ссылке и бронируй отели с кэшбеком до 10%
                                                          Действует до: Бессрочно
                                                          Регион: Россия
                                                          Ссылка: https://www.tinkoff.ru/sl/85v0bBvccfS
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
                bot.send_message(call.message.chat.id,
                                 "Куда отправимся дальше?", reply_markup=kudadalsheairtickets())
            elif call.data == 'yandexput':
                bot.send_message(call.message.chat.id, """Чтобы успешно активировать промокод👌 достаточно: 
                                                          перейти по ссылке или скопировать значение купона с 
                                                          данной страницы и ввести его на сайте компании☺️""")
                bot.send_message(call.message.chat.id, """Название: Яндекс путешествия 
                                                          Скидка: 11% на первое бронирование отеля
                                                          Описание: Скидка 11% на первое бронирование отеля (максимально 1.000₽) + кэшбэк до 3.000₽ баллами плюса
                                                          Действует до: 28.02.23
                                                          Регион: Россия
                                                          Ссылка: https://gtblg.ru/wYp2U
                                                          Промокод ниже👇""", parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 "Действует по ссылке")
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

