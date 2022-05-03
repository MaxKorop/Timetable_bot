import telebot, schedule
from datetime import date, time

start_day=date(day=2, month=5, year=2022)

token='5095955535:AAGQVJdQqcvjUJPnSBLpxO95feN7YmXMM_A'
bot = telebot.TeleBot(token)

pary_up=[['-', 'Англійська мова(Comunicate)', '-', 'ООП', 'Екононміка', 'Математика'],
         ['-','-','-','Машинне навчання','Історія України','Історія України'],
         ['-','-','Англійська мова', 'WEB-програмування', 'Українська література', 'Математика'],
         ['-','Онлайн інструменти','-','-','Схемотехніка','ФЗВ'],
         ['-','-','-','Економіка','WEB-програмування','Схемотехніка']]

pary_up_links=[['-', 'https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09', '-', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'https://meet.google.com/zvg-uepp-dok', 'Математика'],
         ['-','-','-','https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09','Історія України','Історія України'],
         ['-','-','https://us04web.zoom.us/j/73388415945?pwd=tltb2ilvvczlC21V8cHCNGLNZS6Xen.1', 'https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09', 'Українська література', 'Математика'],
         ['-','https://zoom.us/j/8780854117','-','-','Схемотехніка','https://us04web.zoom.us/j/4796891689?pwd=YUROZzNZbzkyQ0wwdU0rU3NSdDIvQT09'],
         ['-','-','-','https://meet.google.com/zvg-uepp-dok','https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09','Схемотехніка']]

pary_down=[['-', 'Англійська мова(Comunicate)', '-', 'ООП', 'ООП', 'Математика'],
         ['-','-','-','Машинне навчання','Історія України','-'],
         ['-','-','Англійська мова', 'WEB-програмування', 'Українська література', 'Математика'],
         ['-','Онлайн інструменти','-','-','Схемотехніка','ФЗВ'],
         ['-','Англійська мова(Comunicate)','-','-','WEB-програмування','Схемотехніка']]

pary_down=[['-', 'https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09', '-', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09', 'Математика'],
         ['-','-','-','https://us04web.zoom.us/j/4210751889?pwd=SXhxVnhkYUQ4RkdueFN4bUhQV2ZTZz09','Історія України','-'],
         ['-','-','Англійська мова', 'https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09', 'Українська література', 'Математика'],
         ['-','https://zoom.us/j/8780854117','-','-','Схемотехніка','https://us04web.zoom.us/j/4796891689?pwd=YUROZzNZbzkyQ0wwdU0rU3NSdDIvQT09'],
         ['-','https://us04web.zoom.us/j/4365350808?pwd=TVFiZFBvaml2RmhsOEY3TjYzWDdEdz09','-','-','https://us04web.zoom.us/j/6471239726?pwd=VnA2aTJ0aFIxaTgxcW5WVmk2NkppQT09','Схемотехніка']]

def schedule_today_func():
    if week_counter(start_day)=='_верхній_':
        return pary_up[date.weekday(date.today())]
    if week_counter(start_day)=='_нижній_':
        return pary_down[date.weekday(date.today())]

def schedule_today_func_links():
    if week_counter(start_day)=='_верхній_':
        return pary_up_links[date.weekday(date.today())]
    if week_counter(start_day)=='_нижній_':
        return pary_down_links[date.weekday(date.today())]

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
    bot.send_message(message.chat.id,"Добрий день, я розклад-бот, я стану вам у пригоді, якщо вам потрібно дізнатися розклад на сьогодні, та швидко підключитися до пари онлайн. \nВивести список команд - /help")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - запуск бота;\n/week - який тиждень(верхній/нижній);\n/shedule_today - розклад на сьогодні;\n/shedule_otweek - розклад на цей тиждень;")

@bot.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, ("Зараз "+ week_counter(start_day)+" тиждень."), parse_mode='Markdown')

@bot.message_handler(commands=['shedule_today'])
def help(message):
    bot.send_message(message.chat.id, ("Розклад на сьогодні:\n1. "+'['+schedule_today_func()[0]+']('+schedule_today_func_links()[0]+')'+"\n2. "
                                       +'['+schedule_today_func()[1]+']('+schedule_today_func_links()[1]+')'+"\n3. "
                                       +'['+schedule_today_func()[2]+']('+schedule_today_func_links()[2]+')'+"\n4. "
                                       +'['+schedule_today_func()[3]+']('+schedule_today_func_links()[3]+')'+"\n5. "
                                       +'['+schedule_today_func()[4]+']('+schedule_today_func_links()[4]+')'+"\n6. "
                                       +'['+schedule_today_func()[5]+']('+schedule_today_func_links()[5]+')'), parse_mode='Markdown')

@bot.message_handler(commands=['shedule_otweek'])
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
                                       + schedule_otweek_func()[4][5]), parse_mode='Markdown')

bot.infinity_polling()