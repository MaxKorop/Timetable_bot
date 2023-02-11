import telebot
from datetime import date

#03/05/2022

start_day=date(day=6, month=2, year=2023)
token='5148310056:AAGLl8CZVxL5FVqUQiiWgYfDXpbt1R6byac'
bot = telebot.TeleBot(token)

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
        return classes_up
    if week_counter(start_day)=='_нижній_':
        return classes_down

@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id,"Добрий день, я розклад-бот, я стану вам у пригоді, якщо вам потрібно дізнатися розклад на сьогодні, та швидко підключитися до пари онлайн. \nВивести список команд - /help\n\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - запуск бота;\n/help - список команд\n/week - який тиждень(верхній/нижній);\n/scheduletoday - розклад на сьогодні;\n/scheduleotweek - розклад на цей тиждень;\n/scheduleofcalls - розклад дзвінків;\n\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, ("Зараз "+ week_counter(start_day)+" тиждень.\n\n_Слава Україні!!!_🇺🇦"), parse_mode='Markdown')

@bot.message_handler(commands=['scheduleofcalls'])
def scheduleOfCalls(message):
    bot.send_message(message.chat.id, "Розклад дзвінків:\n\n1. 8:30-9:30\n2. 9:40-10:40\n3. 10:50-11:50\n4. 12:00-13:00\n5. 13:10-14:10\n6. 14:20-15:20\n7. 15:30-16:30\n8. 16:40-17:40\n9. 17:50-18:50\n\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['scheduletoday'])
def scheduleToday(message):
    file = open(r'Schedules\Schedule_2P-20.txt', mode="r", encoding="UTF-8")
    lines = []
    for line in file:
        lines.append(line)
    lines[-1] = lines[-1]+'\n'
    schedule_on_day = []
    indexes_days = []
    for i in range(len(lines)):
        if lines[i] == '^\n':
            indexes_days.append(i)
    for a in lines[indexes_days[date.weekday(date.today())*2]+1:indexes_days[date.weekday(date.today())*2+1]]:
        schedule_on_day.append(a)
    #print(str(message.from_user))
    bot.send_message(message.chat.id, "Розклад на сьогодні:\n"+"".join(schedule_on_day)+"\n_Слава Україні!!!_🇺🇦", parse_mode="Markdown")
    file.close()

@bot.message_handler(commands=['scheduleotweek'])
def scheduleOTWeek(message):
    file = open(r'Schedules\Schedule_2P-20.txt', mode="r", encoding="UTF-8")
    lines = []
    for line in file:
        lines.append(line)
    lines[-1] = lines[-1]+'\n'
    schedule = []
    indexes_days = []
    for i in range(len(lines)):
        if lines[i] == '^\n':
            indexes_days.append(i)
    i = 0
    for a in range(13):
        schedule.append(lines[indexes_days[i]+1:indexes_days[i+1]])
        i+=1
    schedule_on_week = []
    for i in schedule:
        if len(i)>0:
            for a in i:
                schedule_on_week.append(a)
            schedule_on_week.append('\n')
    #print(str(message.from_user))
    bot.send_message(message.chat.id, "Розклад на тиждень:\n"+"".join(schedule_on_week)+"\n_Слава Україні!!!_🇺🇦", parse_mode="Markdown")
    file.close()

bot.infinity_polling()
