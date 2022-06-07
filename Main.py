import telebot, requests, time
from datetime import date
from bs4 import BeautifulSoup

start_day=date(day=2, month=5, year=2022)
token='5148310056:AAGLl8CZVxL5FVqUQiiWgYfDXpbt1R6byac'
bot1 = telebot.TeleBot(token)

classes_up=["Практика"]

classes_up_links=['https://us04web.zoom.us/j/6195582246?pwd=RXJ5QUdpVlZGcnlpWUVBd2R0eE5uQT09']

classes_down=["Практика"]

classes_down_links=['https://us04web.zoom.us/j/6195582246?pwd=RXJ5QUdpVlZGcnlpWUVBd2R0eE5uQT09']

def schedule_today_func():
    if week_counter(start_day)=='_верхній_' and date.weekday(date.today())!=6 and date.weekday(date.today())!=5:
        return classes_up[0]#date.weekday(date.today())]
    elif week_counter(start_day)=='_нижній_' and date.weekday(date.today())!=6 and date.weekday(date.today())!=5:
        return classes_down[0]#date.weekday(date.today())]
    elif date.weekday(date.today())==6:
        return "Сьогодні неділя, практики немає"
    elif date.weekday(date.today())==5:
        return "Сьогодні субота, практики немає"

def schedule_today_func_links():
    if week_counter(start_day)=='_верхній_':
        return classes_up_links[0]#date.weekday(date.today())]
    if week_counter(start_day)=='_нижній_':
        return classes_down_links[0]#date.weekday(date.today())]

def check():
    url = 'https://kopiyka.org/sirens'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all(attrs={'data-raion': "Черкаський район"})
    path = str(quotes[0])
    opacity = float(path[14127:14130])
    print(opacity, path)
    if opacity != 0.9:
        return True
    else:
        return False

def week_counter(start):
    date_today = date.today()
    days = date_today-start
    weeks = days.days//7
    if weeks%2==0:
        return '_верхній_'
    else:
        return '_нижній_'

def schedule_otweek_func():
    if week_counter(start_day)=='_верхній_':
        return pary_up
    if week_counter(start_day)=='_нижній_':
        return pary_down

@bot1.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Добрий день, я розклад-бот, я стану вам у пригоді, якщо вам потрібно дізнатися розклад на сьогодні, та швидко підключитися до пари онлайн. \nВивести список команд - /help\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot1.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - запуск бота;\n/week - який тиждень(верхній/нижній);\n/sheduletoday - розклад на сьогодні;\n/sheduleotweek - розклад на цей тиждень;\n/scheduleofcalls - розклад дзвінків;\n/allertstatus - статус повітряної тривоги.\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

#@bot1.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, ("Зараз "+ week_counter(start_day)+" тиждень.\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

@bot1.message_handler(commands=['sheduletoday'])
def help(message):
    if schedule_today_func()=="Сьогодні неділя, пар немає":
        bot.send_message(message.chat.id, (schedule_today_func()+"\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, ("Розклад на сьогодні:\n\n["+ schedule_today_func()+']('+ schedule_today_func_links()+')'+"\n\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')#("Розклад на сьогодні:\n1. "+'['+schedule_today_func()[0]+']('+schedule_today_func_links()[0]+')'+"\n2. "
                                       #+'['+schedule_today_func()[1]+']('+schedule_today_func_links()[1]+')'+"\n3. "
                                       #+'['+schedule_today_func()[2]+']('+schedule_today_func_links()[2]+')'+"\n4. "
                                       #+'['+schedule_today_func()[3]+']('+schedule_today_func_links()[3]+')'+"\n5. "
                                       #+'['+schedule_today_func()[4]+']('+schedule_today_func_links()[4]+')'+"\n6. "
                                       #+'['+schedule_today_func()[5]+']('+schedule_today_func_links()[5]+')'+"\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

#@bot1.message_handler(commands=['sheduleotweek'])
def help(message):
    bot.send_message(message.chat.id, ("Розклад на тиждень:\n\n*Понеділок:* \n1. " + schedule_otweek_func()[0][0] + "\n2. "
                                       + schedule_otweek_func()[0][1] + "\n3. "
                                       + schedule_otweek_func()[0][2] + "\n4. "
                                       + schedule_otweek_func()[0][3] + "\n5. "
                                       + schedule_otweek_func()[0][4] + "\n6. "
                                       + schedule_otweek_func()[0][5] + "\n\n*Вівторок:*\n1. "
                                       + schedule_otweek_func()[1][0] + "\n2. "
                                       + schedule_otweek_func()[1][1] + "\n3. "
                                       + schedule_otweek_func()[1][2] + "\n4. "
                                       + schedule_otweek_func()[1][3] + "\n5. "
                                       + schedule_otweek_func()[1][4] + "\n6. "
                                       + schedule_otweek_func()[1][5] + "\n\n*Середа:*\n1. "
                                       + schedule_otweek_func()[2][0] + "\n2. "
                                       + schedule_otweek_func()[2][1] + "\n3. "
                                       + schedule_otweek_func()[2][2] + "\n4. "
                                       + schedule_otweek_func()[2][3] + "\n5. "
                                       + schedule_otweek_func()[2][4] + "\n6. "
                                       + schedule_otweek_func()[2][5] + "\n\n*Четвер:*\n1. "
                                       + schedule_otweek_func()[3][0] + "\n2. "
                                       + schedule_otweek_func()[3][1] + "\n3. "
                                       + schedule_otweek_func()[3][2] + "\n4. "
                                       + schedule_otweek_func()[3][3] + "\n5. "
                                       + schedule_otweek_func()[3][4] + "\n6. "
                                       + schedule_otweek_func()[3][5] + "\n\n*П'ятниця:*\n1. "
                                       + schedule_otweek_func()[4][0] + "\n2. "
                                       + schedule_otweek_func()[4][1] + "\n3. "
                                       + schedule_otweek_func()[4][2] + "\n4. "
                                       + schedule_otweek_func()[4][3] + "\n5. "
                                       + schedule_otweek_func()[4][4] + "\n6. "
                                       + schedule_otweek_func()[4][5] + "\n\n*Субота:*\n1. "
                                       + schedule_otweek_func()[5][0] + "\n2. "
                                       + schedule_otweek_func()[5][1] + "\n3. "
                                       + schedule_otweek_func()[5][2] + "\n4. "
                                       + schedule_otweek_func()[5][3] + "\n5. "
                                       + schedule_otweek_func()[5][4] + "\n6. "
                                       + schedule_otweek_func()[5][5] + "\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

@bot1.message_handler(commands=['scheduleofcalls'])
def week(message):
    bot.send_message(message.chat.id, "Розклад дзвінків:\n1. 8:30-9:30\n2. 9:40-10:40\n3. 10:50-11:50\n4. 12:10-13:10\n5. 13:20-14:20\n6. 14:30-15:30\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

#@bot1.message_handler(commands=['al'])
def al(message):
    stick = open('D:\\Study\\Projects_PyCharm\\Timetable\\al.webp', 'rb')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, stick)
    stick = None
    allerts[0] = 1

#@bot1.message_handler(commands=['ac'])
def ac(message):
    stick = open('D:\\Study\\Projects_PyCharm\\Timetable\\ac.webp', 'rb')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, stick)
    stick = None
    allerts[0] = 0

@bot1.message_handler(commands=['cid'])
def chat_id(message):
    chat_id = message.chat.id
    file = open(r"D:\Study\Projects_PyCharm\Timetable\schedules\_" + file_name() +".txt", mode="r+", encoding="UTF-8")
    for lines in file:
        id = []
        for i in lines:
            if i !="^":
                id.append(i)
            else:
                break
        if ("".join(id)) == str(chat_id):
            index = lines.index("^")
            index_l = lines.index("~")
            data = []
            link = []
            symbols = len(lines)
            for i in range(index+1, symbols):
                if lines[i] == "~":
                    break
                data.append(lines[i])
            for i in range(index_l+1, symbols):
                link.append(lines[i])
            bot.send_message(message.chat.id, "["+"".join(data)+"]("+"".join(link)+")", parse_mode="Markdown")
    file.close()

def file_name():
    mon = "Monday"
    tue = "Tuesday"
    wed = "Wednesday"
    thu = "Thursday"
    fri = "Friday"
    if date.weekday(date.today()) == 0:
        return "Monday"
    if date.weekday(date.today()) == 1:
        return "Tuesday"
    if date.weekday(date.today()) == 2:
        return "Wednesday"
    if date.weekday(date.today()) == 3:
        return "Thursday"
    if date.weekday(date.today()) == 4:
        return "Friday"

#import logging
#from aiogram import types, executor, Bot, Dispatcher

#button_bot = Bot(token=token)
#dp = Dispatcher(button_bot)
#logging.basicConfig(level=logging.INFO)

#@dp.message_handler(commands="add")
#async def adding(message: types.Message):
    #file = open(r"D:\Study\Projects_PyCharm\Timetable\schedules\Тестовий_файл.txt", mode="a+", encoding="UTF-8")
    #keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #buttons = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
    #keyboard.add(*buttons)
    #await message.answer("Оберіть день", reply_markup=keyboard)
    #file.close()

#executor.start_polling(button_bot, skip_updates=True)

#@bot1.message_handler(commands=['allertstatus'])
def al_status(message):
    if check()==False:
        bot.send_message(message.chat.id, "Повітряної тривоги немає\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Наразі є повітряна тривога\nВсі в укриття!\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

bot1.infinity_polling()