import telebot
from directions import *
from keyboards import keyboard_hello, keyboard_direction, keyboard_course, keyboard_week, day_of_week, keyboard_fac
from parserWords import parserWord
from week import weeker

bot = telebot.TeleBot('1272730146:AAHExswns-QVmiLF7Y2ysVwtrfU8lw7PGmc')

direction = ''
course = 0
result = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я помогу тебе с расписанием', reply_markup=keyboard_hello)
    bot.send_message(message.chat.id, 'Вот что я умею:\r\n'
                                      '    /start - перезагрузить бот \r\n'
                                      '    /help - помощь \r\n'
                                      '    <Бвт1801 понедельник> - пример ввода группы, чтобы узнать расписание\r\n'
                                      '    или нажимай на кнопки в интерактивном меню'
                     )


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'Вот что я умею:\r\n'
                                      '    /start - перезагрузить бот \r\n'
                                      '    /help - помощь \r\n'
                                      '    <Бвт1801 понедельник> - пример ввода группы, чтобы узнать расписание\r\n'
                                      '    или нажимай на кнопки в интерактивном меню'
                     )


@bot.message_handler(content_types=['text'])
def send_text(message):
    messageText = parserWord(message.text.lower())
    global result
    global direction
    global course
    # len(messageText) == 3 and
    # print(len(messageText))

    if message.text.lower() == 'узнать расписание':
        bot.send_message(message.chat.id, 'Выбери свое направление', reply_markup=keyboard_direction)

    elif message.text.lower() == 'бвт' or message.text.lower() == 'бст' or message.text.lower() == 'бфи':

        direction = message.text.lower()
        bot.send_message(message.chat.id, 'На каком курсе ты учишься?', reply_markup=keyboard_course)




    elif message.text == '1' or message.text == '2' or message.text == '3' or message.text == '4':

        course = int(message.text)
        now = datetime.now()
        year = now.year
        keyboard_group = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        butns = list()
        for i in range(courses[direction][course]):
            butns.append(direction.upper() + str(year - 1999 - course) + "0" + str(i+1))
        for i in range(5):
            butns.append('')

        keyboard_group.row(butns[0],butns[1],butns[2],butns[3],butns[4] )
        keyboard_group.row('Начать сначала')
        bot.send_message(message.chat.id, 'Выбери свою группу', reply_markup=keyboard_group)




    elif message.text.lower() in directionBVT or message.text.lower() in directionBST or message.text.lower() in directionBFI:
        result = message.text.lower()
        try:
            bot.send_message(message.chat.id, 'На какой день недели?', reply_markup=keyboard_week)
        except:
            bot.send_message(message.chat.id, 'Видимо такой группы не существует', reply_markup=keyboard_hello)
            bot.send_message(message.chat.id, 'Попробуй еще')




    elif message.text.lower() in day_of_week:

        if len(direction) > 0 and len(result) > 0 and course > 0:
            try:
                bot.send_message(message.chat.id, '________________________')
                bot.send_message(message.chat.id, 'Сейчас ' + weeker())
                if day_of_week[message.text.lower()] == 6:
                    bot.send_message(message.chat.id, 'Для группы ' + result.upper(), reply_markup=keyboard_hello)
                    for i in range(5):
                        img = open('/Users/arshegor/PycharmProjects/MtuciBot/groups/' + result.upper() + '-' + str(
                            i + 1) + '.png', 'rb')
                        bot.send_photo(message.chat.id, img)
                    bot.send_message(message.chat.id, '________________________')
                    bot.send_message(message.chat.id, 'Жду тебя снова)))', reply_markup=keyboard_hello)
                else:
                    bot.send_message(message.chat.id, 'Для группы ' + result.upper(), reply_markup=keyboard_hello)
                    img = open('/Users/arshegor/PycharmProjects/MtuciBot/groups/' + result.upper() + '-' + str(
                        day_of_week[message.text.lower()]) + '.png', 'rb')
                    bot.send_photo(message.chat.id, img)
                    bot.send_message(message.chat.id, '________________________')
                    bot.send_message(message.chat.id, 'Жду тебя снова)))', reply_markup=keyboard_hello)
            except:
                bot.send_message(message.chat.id, 'Видимо такой группы не существует', reply_markup=keyboard_hello)
                bot.send_message(message.chat.id, 'Попробуй еще')
        else:
            bot.send_message(message.chat.id, 'Что-то пошло не так...', reply_markup=keyboard_hello)
            bot.send_message(message.chat.id, 'Попробуй еще')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай)')




    elif message.text.lower() == 'начать сначала':
        bot.send_message(message.chat.id, 'Начнем сначала', reply_markup=keyboard_hello)





    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

    elif messageText[0] in directionBVT:

        try:
            if len(messageText) == 4 and messageText[1] + ' ' + messageText[2] in day_of_week:
                bot.send_message(message.chat.id, '________________________')
                bot.send_message(message.chat.id, 'Сейчас ' + weeker())
                bot.send_message(message.chat.id, 'Для группы ' + messageText[0].upper(), reply_markup=keyboard_hello)
                for i in range(5):
                    img = open('/Users/arshegor/PycharmProjects/MtuciBot/groups/' + messageText[0].upper() + '-' + str(
                        i + 1) + '.png', 'rb')
                    bot.send_photo(message.chat.id, img)
                bot.send_message(message.chat.id, '________________________')
                bot.send_message(message.chat.id, 'Жду тебя снова)))', reply_markup=keyboard_hello)
            elif messageText[1] in day_of_week:
                bot.send_message(message.chat.id, 'Сейчас ' + weeker())
                bot.send_message(message.chat.id, 'Для группы ' + messageText[0].upper(), reply_markup=keyboard_hello)
                img = open('/Users/arshegor/PycharmProjects/MtuciBot/groups/' + messageText[0].upper() + '-' + str(
                    day_of_week[messageText[1]]) + '.png', 'rb')
                bot.send_photo(message.chat.id, img)
                bot.send_message(message.chat.id, '________________________')
                bot.send_message(message.chat.id, 'Жду тебя снова)))', reply_markup=keyboard_hello)
            elif not messageText[1] + ' ' + messageText[2] in day_of_week or not messageText[1] in day_of_week:
                bot.send_message(message.chat.id, 'Что-то непонятное...', reply_markup=keyboard_hello)
                bot.send_message(message.chat.id, 'Попробуй еще')
        except:
            bot.send_message(message.chat.id, 'Что-то непонятное...', reply_markup=keyboard_hello)
            bot.send_message(message.chat.id, 'Попробуй еще')


    else:
        bot.send_message(message.chat.id, 'Введите название группы или пройдите по интерактиному меню)',
                         reply_markup=keyboard_hello)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
