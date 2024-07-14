# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def execute_counter(function):
    counter: int = 0

    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f'\nIt was running {counter} times')
        return function(*args, **kwargs)

    return inner


# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати
# два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

def todo():
    todo_list: list[str] = []

    def add_todo(task: str) -> None:
        nonlocal todo_list
        todo_list.append(task)

    @execute_counter
    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add_todo, get_all = todo()

add_todo('1. watch lesson')
add_todo('2. make hw')
add_todo('3. try not to die')

print('TODO list:\n', get_all())

add_todo('4. make one more hw')

print('TODO list:\n', get_all())


#
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

@execute_counter
def expanded_form(number: int) -> str:
    digits: list[str] = []
    length: int = len(str(number))

    for i, num in enumerate(str(number)):
        if num != '0':
            digits.append(num + '0' * (length - i - 1))

    return '+'.join(digits)

expanded_form(5)
print(expanded_form(2))
print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
