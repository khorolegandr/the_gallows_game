import random


def start_game():
    secret_word = get_word()
    gallows = [' _________', ' |/      ', ' |      ', ' |       ', ' |      ', '/|\     ']
    wrong = 0
    return secret_word, gallows, wrong


def get_word():
    word_list = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр',  'Башня',
                 'Кондитер', 'Омар', 'Чан', 'Пламя', 'Банк', 'Тетерев', 'Муж',  'Камбала',  'Груз',  'Кино',
                 'Лаваш',  'Калач',  'Геолог', 'Бальзам',  'Бревно', 'Жердь',   'Борец', 'Самовар',  'Карабин',
                 'Подлокотник', 'Барак', 'Мотор',  'Шарж', 'Сустав',  'Амфитеатр', 'Скворечник', 'Подлодка',
                 'Затычка',  'Ресница', 'Спичка', 'Кабан',  'Муфта',  'Синоптик',  'Характер',  'Мафиози',
                 'Фундамент',  'Бумажник',  'Библиофил',  'Дрожжи',   'Казино', 'Конечность', 'Пробор', 'Дуст',
                 'Комбинация',  'Мешковина',  'Процессор',  'Крышка', 'Сфинкс',   'Пассатижи', 'Фунт',  'Кружево',
                 'Агитатор']
    return word_list[random.randint(0, len(word_list) - 1)]


def is_correct(letter):
    flag = False
    correct_symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    correct_symbols += correct_symbols.upper()
    while flag is False:
        if letter in correct_symbols:
            return True
        else:
            print('Некорректный символ!')
            letter = input('Введи букву: ')


def is_right(letter):
    if letter in secret_word:
        right_letter(letter)
    else:
        wrong_letter()


def right_letter(letter):
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            word[i] = letter.upper()


def wrong_letter():
    global wrong
    wrong += 1
    if wrong == 1:
        gallows[1] += '|'
    elif wrong == 2:
        gallows[2] += '( )'
    elif wrong == 3:
        gallows[3] += '|'
    elif wrong == 4:
        gallows[4] += '/^\ '
    elif wrong == 5:
        gallows[3] = gallows[3][:-2]
        gallows[3] += '/|\ '


def output(gallows, wrong):
    print(*gallows, sep='\n')
    print('\n', *word)


print('В И С Е Л И Ц А')
secret_word, gallows, wrong = start_game()
word = ['__' for i in range(len(secret_word))]
output(gallows, wrong)

game_end = False
while game_end is False:
    letter = input('Введи букву: ')
    is_correct(letter)
    is_right(letter)
    output(gallows, wrong)
    if '__' not in word:
        game_end = True
    elif wrong == 5:
        game_end = True
        print('GAME OVER')
