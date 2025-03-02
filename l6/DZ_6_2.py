# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

user_num = int(input('Введіть число менше або яке дорівнює 8640000: '))

if user_num < 0 or user_num >= 8640000:
    print('Число має бути більше або дорівнювати 0 і менше 8640000')
else:
    seconds_tpl = divmod(user_num, 60)
    minutes_tpl = divmod(seconds_tpl[0], 60)
    hours_tpl = divmod(minutes_tpl[0], 24)

    seconds = str(seconds_tpl[1]).zfill(2)
    minutes = str(minutes_tpl[1]).zfill(2)
    hours = str(hours_tpl[1]).zfill(2)
    days = str(hours_tpl[0])

    if days[-1] not in ('1', '2', '3', '4') or (len(days) > 1 and days[-2] == '1'):
        word_days = 'днів'
    elif days[-1] == '1':
        word_days = 'день'
    else:
        word_days = 'дні'

    print(days, word_days + ",", hours + ":" + minutes + ":" + seconds)