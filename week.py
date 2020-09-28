import datetime
def weeker():
    today = datetime.datetime.today().strftime("%W")

    if int(today) % 2 == 0:
         return 'нижняя неделя'
    else:
         return 'верхняя неделя'
