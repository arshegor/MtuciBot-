import telebot
from telebot import *


from facults import facs

keyboard_hello = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_hello.row('Узнать расписание', 'Пока')

keyboard_fac = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_fac.row('ИТ', 'ФЦИИНК', 'РИД')
keyboard_fac.row('СИС', 'КИП')
keyboard_fac.row('Начать сначала')

keyboard_direction = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_direction.row('БВТ', 'БСТ', 'БФИ')
keyboard_direction.row('Начать сначала')

keyboard_course = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_course.row('1', '2', '3', '4')
keyboard_course.row('Начать сначала')

day_of_week = {'понедельник' : 1, 'вторник' : 2,'среда' : 3,'четверг' : 4, 'пятница' : 5, 'вся неделя' : 6}


keyboard_week = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_week.row('Понедельник', 'Вторник', 'Среда')
keyboard_week.row('Четверг', 'Пятница', 'Вся неделя' )
keyboard_week.row('Начать сначала')

