from random import*
from time import*
def triangle(n):
    for i in range(1, n + 1):
        print(i * ' ')

def square(n):
    for i in range(n):
        print (n * ' ')

def rect(m, n):
    for i in range(n):
        print (m * ' *')

#ресурс 1 - меч
#ресурс 1.1 - топор
#ресурс 1 - нож
#ресурс 1.1 - лук и стрелы
#баф 1 - +2 силы
#ресурс 2 - +4 армора
#Расса - Викинги
#Расса - рыцари

#фразы:
#твои силы слишком слабы для меня
#Ты мог лучше, я же не такой сильный
#Ха-ха настолько слабого создания я ещё не видел

#Ладно, ты смог меня одалеть, отправляйся к моему боссу
#Как это возможно, как ты смог меня одалеть
#Хорошо, ты меня победил в этой достойной схватке, ты встанешь на мой путь главы всех дедов
#
#


'''from random import*
список = ['у вашего персонажа меч, лук со стрелами, +2 силы и расса Викинги, ваш уровень 0.']
random.choices(список)
print(список)'''
'''from random import choice
from random import *
resurs = 'меч', 'топор'
resurs2 = 'нож', 'лук со стрелами'
Baf = '+60', '+80'
Rassa = ['Викинги', 'Рыцари']'''



словарь = {
    'name': '',
    'хп': 740,
    'хп2': 50,
    'хп3': 90,
    'хп4': 160,
}








бой = 20
game = ''
lvl = 0
name = str(input('Как звать тебя?'))
resurs = randint(1,2)
resurs2 = randint(1,2)
Baf = randint(1,2)
Rassa = randint(1,2)
if resurs == 1 and resurs2 == 2 and Baf == 1 and Rassa == 1:
    print(f"{name} у вашего персонажа меч, лук со стрелами, +2 силы и расса Викинги, ваш уровень 0.")
elif resurs == 1 and resurs2 == 2 and Baf == 2 and Rassa == 1:
    print(f"{name} у вашего персонажа меч, лук со стрелами, +4 силы и расса Рыцари, ваш уровень 0.")
elif resurs == 1 and resurs2 == 2 and Baf == 2 and Rassa == 2:
    print(f"{name} у вашего персонажа меч, лук со стрелами, +4 силы и расса Викинги, ваш уровень 0.")
elif resurs == 1 and resurs2 == 2 and Baf == 1 and Rassa == 2:
    print(f"{name} у вашего персонажа меч, лук со стрелами, +2 силы и расса Викинги, ваш уровень 0.")
elif resurs == 1 and resurs2 == 1 and Baf == 2 and Rassa == 1:
    print(f"{name} у вашего персонажа меч, нож, +4 силы и расса Рыцари, ваш уровень 0.")
if resurs == 1 and resurs2 == 1 and Baf == 1 and Rassa == 2:
    print(f"{name} у вашего персонажа меч, нож, +2 силы и расса Викинги, ваш уровень 0.")
if resurs == 2 and resurs2 == 1 and Baf == 2 and Rassa == 2:
    print(f"{name} у вашего персонажа топор, нож, +4 силы и расса Викинги, ваш уровень 0.")
if resurs == 2 and resurs2 == 1 and Baf == 1 and Rassa == 2:
    print(f"{name} у вашего персонажа топор, нож, +2 силы и расса Викинги, ваш уровень 0.")
if resurs == 2 and resurs2 == 1 and Baf == 1 and Rassa == 1:
    print(f"{name} у вашего персонажа топор, нож, +2 силы и расса Рыцари, ваш уровень 0.")
if resurs == 2 and resurs2 == 1 and Baf == 2 and Rassa == 1:
    print(f"{name} у вашего персонажа топор, нож, +4 силы и расса Рыцари, ваш уровень 0.")
if resurs == 2 and resurs2 == 2 and Baf == 1 and Rassa == 2:
    print(f"{name} у вашего персонажа топор, лук со стрелами, +2 силы и расса Викинги, ваш уровень 0.")
if resurs == 2 and resurs2 == 2 and Baf == 2 and Rassa == 1:
    print(f"{name} у вашего персонажа топор, лук со стрелами, +4 силы и расса Рыцари, ваш уровень 0.")
if resurs == 2 and resurs2 == 2 and Baf == 2 and Rassa == 2:
    print(f"{name} у вашего персонажа топор, лук со стрелами, +4 силы и расса Рыцари, ваш уровень 0.")
if resurs == 1 and resurs2 == 1 and Baf == 1 and Rassa == 1:
    print(f"{name} у вашего персонажа меч, нож, +2 силы и расса Викинги, ваш уровень 0.")

while словарь ['хп'] > 0 and словарь ['хп2'] > 0 and словарь ['хп3'] > 0 and словарь ['хп4'] > 0:
            if round == 1 and lvl == 0:
                print(f'остлаось {словарь["хп2"]}')
                словарь['хп2'] -= (бой + Baf)
            elif round == 1 and lvl == 1:
                print(f'остлаось {словарь["хп3"]}')
                словарь['хп3'] -= (бой + Baf)
            elif round == 1 and lvl == 2:
                print(f'остлаось {словарь["хп4"]}')
                словарь['хп4'] -= (бой + Baf)
            elif round == 2 and lvl == 0:
                print(f'остлаось {словарь["хп"]}')
                словарь['хп'] -= 50
            elif round == 2 and lvl == 1:
                print(f'остлаось {словарь["хп"]}') 
                словарь['хп'] -= 70
            elif round == 2 and lvl == 2:
                print(f'остлаось {словарь["хп"]}')
                словарь['хп'] -= 100
if словарь["хп2"] <= 0 or словарь["хп3"] <= 0 or словарь["хп4"] <= 0:
            print('Ты победил')
elif словарь["хп"] <= 0 or словарь["хп"] <= 0 or словарь["хп"] <= 0:
            print('Ты проиграл')

if словарь['хп'] == 0:
     game == 'loss'
elif словарь['хп2'] == 0:
    game == 'win'
elif словарь['хп3'] == 0:
    game == 'win'
elif словарь['хп4'] == 0:
    game == 'win'
from time import*
def tren():
    что_делать = input('Будем тренировать атаку? ') 
    while что_делать != 'нет':
        if что_делать == 'да' or что_делать == 'Да':
            print(+1) and бой + 1
            sleep(1)
            print (+1) and бой + 1
            sleep(1)
            print (+1) and бой + 1
            sleep(1)
            print (+1) and бой + 1
            sleep(1)
            print (+1) and бой + 1
            что_делать = input('Будем тренировать атаку? ')