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

from typing import TypedDict
import json
import uuid


class BuyList:
    class Item(TypedDict):
        id: str
        name: str
        price: int

    def __init__(self):
        self.list: list[BuyList.Item] = []
        self.read_from_file()

    def get_all(self):
        return self.list if self.list else 'no records...'

    def add_to_list(self, name: str, price: int):
        item_id = uuid.uuid4().hex
        item: BuyList.Item = {'id': item_id, 'name': name, 'price': price}
        if not any(existed_item['id'] == item_id for existed_item in self.list):
            item['id'] = item_id
            self.list.append(item)
            self.save_to_file()

    def search_by(self, field_name: str, value: (str, int)):
        match field_name:
            case 'id':
                return [item for item in self.list if item['id'] == value] or 'no matches'
            case 'name':
                return [item for item in self.list if item['name'] == value] or 'no matches'
            case 'price':
                return [item for item in self.list if item['price'] == value] or 'no matches'
            case _:
                return 'field not exist'

    def max_price(self):
        return max(self.list, key=lambda item: item['price']) if len(self.list) else 'no records...'

    def delete_by_id(self, item_id: str):
        self.list = [item for item in self.list if item['id'] != item_id]
        self.save_to_file()

    def read_from_file(self):
        try:
            with open('buylist.json', 'r') as file:
                self.list = json.load(file)
        except Exception:
            self.list = []
            print('no file found')

    def save_to_file(self):
        with open('buylist.json', 'w') as file:
            json.dump(self.list, file, indent=4)


while True:
    blist = BuyList()

    print('1 - show all items')
    print('2 - add new item')
    print('3 - search item')
    print('4 - search the mot expensive item')
    print('5 - delete item by id')
    print('6 - exit')

    choice = input('enter your choice: ')

    match choice:
        case '1':
            print(blist.get_all())
        case '2':
            item_name = input('enter name: ')
            item_price = input('enter price: ')
            blist.add_to_list(item_name, int(item_price))
        case '3':
            field = input('enter field to search by name or price or id: ')
            value = input('enter value: ')
            print(blist.search_by(field, value))
        case '4':
            print(blist.max_price())
        case '5':
            del_id = input('enter id to delete: ')
            blist.delete_by_id(del_id)
            print(blist.get_all())
        case '6':
            break


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
