import telebot, requests, time
from datetime import date
from bs4 import BeautifulSoup

start_day=date(day=2, month=5, year=2022)
token='5095955535:AAGQVJdQqcvjUJPnSBLpxO95feN7YmXMM_A'
bot = telebot.TeleBot(token)

pary_up=[['-', 'Англійська мова(Comunicate)', '-', 'ООП', 'Екононміка', 'Математика'],
         ['-','-','-','Машинне навчання','Історія України','Історія України'],
         ['-','-','Англійська мова', 'WEB-програмування', 'Українська література', 'Математика'],
         ['-','Онлайн інструменти','-','Схемотехніка','ФЗВ','-'],
         ['-','-','Англійська мова','Економіка','WEB-програмування','Схемотехніка'],
         ['-','-','-','Машинне навчання','Історія України','-']]

pary_up_links=[['-', 'https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09', '-', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'https://meet.google.com/zvg-uepp-dok', 'https://zoom.us/j/2957751716?pwd=dEtEU2lXSk8yWUIrVllkNzlLcERwUT09'],
         ['-','-','-','https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09','https://us05web.zoom.us/j/82698146962?pwd=dms0NmxyeWlORzdYVFAyUGNBQUl1Zz09','https://us05web.zoom.us/j/82698146962?pwd=dms0NmxyeWlORzdYVFAyUGNBQUl1Zz09'],
         ['-','-','https://us04web.zoom.us/j/73388415945?pwd=tltb2ilvvczlC21V8cHCNGLNZS6Xen.1', 'https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09', 'https://us04web.zoom.us/j/9989836304?pwd=a1B3Y3cyRy9vTG1jSnNIOVE0V0tHZz09', 'https://zoom.us/j/2957751716?pwd=dEtEU2lXSk8yWUIrVllkNzlLcERwUT09'],
         ['-','https://zoom.us/j/8780854117','-','https://t.me/+oU_FSfiJ_25mNWNi','https://us04web.zoom.us/j/4796891689?pwd=YUROZzNZbzkyQ0wwdU0rU3NSdDIvQT09','-'],
         ['-','-','https://us04web.zoom.us/j/71851942085?pwd=FfhnaEdW4uzMCAq6X0vXV7lwF54mqi.1','https://meet.google.com/zvg-uepp-dok','https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09','https://t.me/+oU_FSfiJ_25mNWNi'],
         ['-','-','-','https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09','https://us05web.zoom.us/j/82698146962?pwd=dms0NmxyeWlORzdYVFAyUGNBQUl1Zz09','-']]

pary_down=[['-', 'Англійська мова(Comunicate)', '-', 'ООП', 'ООП', 'Українська мова'],
           ['-','-','-','Машинне навчання','Історія України','-'],
           ['-','-','Англійська мова', 'WEB-програмування', 'Українська література', 'Математика'],
           ['-','Онлайн інструменти','-','Схемотехніка','ФЗВ','-'],
           ['-','Англійська мова(Comunicate)','-','-','WEB-програмування','Схемотехніка'],
           ['-', '-', 'Англійська мова', 'WEB-програмування', 'Українська література', 'Математика']]

pary_down_links=[['-', 'https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09', '-', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'https://us04web.zoom.us/j/9989836304?pwd=a1B3Y3cyRy9vTG1jSnNIOVE0V0tHZz09'],
         ['-','-','-','https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09','https://us05web.zoom.us/j/82698146962?pwd=dms0NmxyeWlORzdYVFAyUGNBQUl1Zz09','-'],
         ['-','-','Англійська мова', 'https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09', 'https://us04web.zoom.us/j/9989836304?pwd=a1B3Y3cyRy9vTG1jSnNIOVE0V0tHZz09', 'https://zoom.us/j/2957751716?pwd=dEtEU2lXSk8yWUIrVllkNzlLcERwUT09'],
         ['-','https://zoom.us/j/8780854117','-','https://t.me/+oU_FSfiJ_25mNWNi','https://us04web.zoom.us/j/4796891689?pwd=YUROZzNZbzkyQ0wwdU0rU3NSdDIvQT09','-'],
         ['-','https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09','-','-','https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09','https://t.me/+oU_FSfiJ_25mNWNi'],
         ['-','-','Англійська мова', 'https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09', 'https://us04web.zoom.us/j/9989836304?pwd=a1B3Y3cyRy9vTG1jSnNIOVE0V0tHZz09', 'https://zoom.us/j/2957751716?pwd=dEtEU2lXSk8yWUIrVllkNzlLcERwUT09']]

def schedule_today_func():
    if week_counter(start_day)=='_верхній_' and date.weekday(date.today())!=6:
        return pary_up[date.weekday(date.today())]
    elif week_counter(start_day)=='_нижній_' and date.weekday(date.today())!=6:
        return pary_down[date.weekday(date.today())]
    else:
        return "Сьогодні неділя, пар немає"

def schedule_today_func_links():
    if week_counter(start_day)=='_верхній_':
        return pary_up_links[date.weekday(date.today())]
    if week_counter(start_day)=='_нижній_':
        return pary_down_links[date.weekday(date.today())]

def check():
    url = 'https://kopiyka.org/sirens'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all(attrs={'data-raion': "Черкаський район"})
    path = str(quotes[0])
    opacity = float(path[14127:14130])
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

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Добрий день, я розклад-бот, я стану вам у пригоді, якщо вам потрібно дізнатися розклад на сьогодні, та швидко підключитися до пари онлайн. \nВивести список команд - /help\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - запуск бота;\n/week - який тиждень(верхній/нижній);\n/sheduletoday - розклад на сьогодні;\n/sheduleotweek - розклад на цей тиждень;\n/scheduleofcalls - розклад дзвінків;\n/allertstatus - статус повітряної тривоги.\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, ("Зараз "+ week_counter(start_day)+" тиждень.\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

@bot.message_handler(commands=['sheduletoday'])
def help(message):
    if schedule_today_func()=="Сьогодні неділя, пар немає":
        bot.send_message(message.chat.id, (schedule_today_func()+"\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, ("Розклад на сьогодні:\n1. "+'['+schedule_today_func()[0]+']('+schedule_today_func_links()[0]+')'+"\n2. "
                                       +'['+schedule_today_func()[1]+']('+schedule_today_func_links()[1]+')'+"\n3. "
                                       +'['+schedule_today_func()[2]+']('+schedule_today_func_links()[2]+')'+"\n4. "
                                       +'['+schedule_today_func()[3]+']('+schedule_today_func_links()[3]+')'+"\n5. "
                                       +'['+schedule_today_func()[4]+']('+schedule_today_func_links()[4]+')'+"\n6. "
                                       +'['+schedule_today_func()[5]+']('+schedule_today_func_links()[5]+')'+"\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

@bot.message_handler(commands=['sheduleotweek'])
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

@bot.message_handler(commands=['scheduleofcalls'])
def week(message):
    bot.send_message(message.chat.id, "Розклад дзвінків:\n1. 8:30-9:30\n2. 9:40-10:40\n3. 10:50-11:50\n4. 12:10-13:10\n5. 13:20-14:20\n6. 14:30-15:30\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['al'])
def al(message):
    stick = open('D:\\Study\\Projects_PyCharm\\Timetable\\al.webp', 'rb')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, stick)
    stick = None
    allerts[0] = 1

@bot.message_handler(commands=['ac'])
def ac(message):
    stick = open('D:\\Study\\Projects_PyCharm\\Timetable\\ac.webp', 'rb')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, stick)
    stick = None
    allerts[0] = 0

@bot.message_handler(commands=['allertstatus'])
def al_status(message):
    if check()==False:
        bot.send_message(message.chat.id, "Повітряної тривоги немає\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Наразі є повітряна тривога\nВсі в укриття!\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

bot.infinity_polling()