# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)

# if you run code more than 1 time you will not get doubles in new_emails.txt
try:
    existed_emails = set()
    try:
        with open('new_emails.txt', 'r') as file:
            for line in file:
                existed_emails.add(line.strip())
    except Exception:
        pass

    with open('emails.txt', 'r') as file:
        for line in file:
            try:
                email = line.split()[1]
                if email.endswith('@gmail.com') and email not in existed_emails:
                    with open('new_emails.txt', 'a') as new_file:
                        new_file.write(email + '\n')
                        existed_emails.add(email)
            except Exception as e:
                print(e)
except Exception as error:
    print(error)




# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
# * вивід всіх покупок
# * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
#
# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
# data = [
#     [
# {"id": 1110, "field": {}},
# {"id": 1111, "field": {}},
# {"id": 1112, "field": {}},
# {"id": 1113, "field": {}},
# {"id": 1114, "field": {}},
# {"id": 1115, "field": {}},
# ],
# [
# {"id": 1110, "field": {}},
# {"id": 1120, "field": {}},
# {"id": 1122, "field": {}},
# {"id": 1123, "field": {}},
# {"id": 1124, "field": {}},
# {"id": 1125, "field": {}},
#
# ],
# [
# {"id": 1130, "field": {}},
# {"id": 1131, "field": {}},
# {"id": 1122, "field": {}},
# {"id": 1132, "field": {}},
# {"id": 1133, "field": {}},
#
# ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку
# то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]