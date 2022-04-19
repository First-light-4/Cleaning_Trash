# программа, чистящая весь мусор из дат, которые заранее прочитала сетка
# входные данные типа URY_FED_PASSPORT_2015_HORIZONTAL;28 MAR/MAR 198AS;03281984;28 MAR 1984, где 28 MAR/MAR 198AS - прочитала сетка
# сравнение происдит по году, месяцу и дню отдельно, всё что не ошибка переносится в новую папку, остальное остаётся как мусор
class All_clean:

    # на вход подаётся отдельная строка из файла
    def __init__(self, text):
        self.text = text

    #сравнение на правильность чтения года (сравниваются только последние 2 цифры так как есть много дат фармата 01.01.99)
    def clean_years(text):
        if text[3][-3] == text[1][-2] and text[3][-2] == text[1][-1] and text[1][-1].isdigit() == True:
            return True
        elif text[3][-3] == text[1][-3] and text[3][-2] == text[1][-2] and text[1][-1].isdigit() == False: # если  в конце стоит точка или случайный символ, убрать его
            return True
        else:
            return False

    #сравнение на правильность чтения месяца( дата может разделяться ' ', '/', '.' )
    def clean_month(text):
        if '/' in text[3]:
            if text[3].split('/')[1] in text[1] or text[2][0:2] in text[1]:
                return True
            else:
                return False
        elif ' ' in text[3]:
            if text[3].split()[1]  in text[1] or text[2][0:2]  in text[1]:
                return True
            else:
                return False
        elif '.' in text[3] or text[2][0:2]  in text[1]:
            if text[3].split('.')[1] in text[1] or text[2][0:2]  in text[1]:
                return True
            else:
                return False
        else:
            return False

    #сравнение на правильность чтения дня ( дата может разделяться ' ', '/', '.' так же имя файла может содержать 0, который надо подставить для соблюдения ревенства)
    def clean_date(text):
        if '/' in text[3]:
            if text[3].split('/')[0] in text[1] or text[1][0] + text[1][2] == text[3].split('/')[0] or '0' + text[1][0] == \
                    text[3].split('/')[0]:
                return True
            else:
                return False
        elif ' ' in text[3]:
            if text[3].split(' ')[0] in text[1] or text[1][0] + text[1][2] == text[3].split(' ')[0] or '0' + text[1][0] == \
                    text[3].split(' ')[0]:
                return True
            else:
                return False
        elif '.' in text[3]:
            if text[3].split('.')[0] in text[1] or text[1][0] + text[1][2] == text[3].split('.')[0] or '0' + text[1][0] == \
                    text[3].split('.')[0]:
                return True
            else:
                return False
        else:
            return False

# на вход  подаётся csv файл, содержащий строки
with open(rf'C:.....Date_Input.csv') as file_input:
    # то что не является мусором будет сохранятся в отдельный финальный файл
    with open(rf'C:.....Date_Final.csv', 'a') as file_output:
        f = file_input.readlines()
        tr = []
        count = 0
        trash = []
        # запись всего хорошего
        for i in range(len(f)):
            text = f[i].split(';')
            if len(text[1]) >= 4:
                # запись всего хорошего
                if All_clean.clean_date(text) == True and All_clean.clean_month(text) == True and All_clean.clean_years(text) == True:
                    print(f[i])
                    count+=1
                    file_output.write(i)
                # запись всего мусора tr - trash
                if All_clean.clean_date(text) == False or All_clean.clean_month(text) == False or All_clean.clean_years(text) == False:
                    tr.append(i)
            count += 1
        # запись всего мусора
        for i in range(0, 21072):
            if i not in tr:
                trash.append(f[i])
                print(f[i])
        # запись всего мусора в отдельный файл
        with open(rf'C:......Date_Trash.csv', 'a') as file_trash:
            file_trash.writelines(trash)
        print(count)