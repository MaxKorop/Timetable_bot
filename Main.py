import telebot, scheduleFromTables, config
from datetime import date

#03/05/2022

start_day=date(day=6, month=2, year=2023)
bot = telebot.TeleBot(config.BOT_TOKEN)

def week_counter(start):
    date_today = date.today()
    days = date_today-start
    weeks = days.days//7
    if weeks%2==0:
        return '_верхній_'
    else:
        return '_нижній_'

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
    #bot.send_message(message.chat.id, "Розклад дзвінків:\n\n1. 8:30-9:30\n2. 9:40-10:40\n3. 10:50-11:50\n4. 12:00-13:00\n5. 13:10-14:10\n6. 14:20-15:20\n7. 15:30-16:30\n8. 16:40-17:40\n9. 17:50-18:50\n\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')
    bot.send_message(message.chat.id, "Розклад дзвінків:\n\n"+scheduleFromTables.getScheduleOfCalls()+"\n\n_Слава Україні!!!_🇺🇦", parse_mode='Markdown')

@bot.message_handler(commands=['scheduletoday'])
def scheduleToday(message):
    schedule = scheduleFromTables.getScheduleForDay(week_counter(start_day), date.weekday(date.today())+1)
    bot.send_message(message.chat.id, "Розклад на сьогодні:\n\n"+schedule+"\n_Слава Україні!!!_🇺🇦", parse_mode="Markdown")

@bot.message_handler(commands=['scheduleotweek'])
def scheduleOTWeek(message):
    schedule = scheduleFromTables.getScheduleForWeek(week_counter(start_day))
    bot.send_message(message.chat.id, "Розклад на тиждень:\n\n"+schedule+"\n_Слава Україні!!!_🇺🇦", parse_mode="Markdown")

bot.infinity_polling()