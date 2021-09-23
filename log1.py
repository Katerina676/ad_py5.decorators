from datetime import datetime


def logger_file(func):
    def new_func(*args, **kwargs):
        now = datetime.now()
        res = func(*args, **kwargs)
        with open('logger1.txt', 'w', encoding='utf8') as f:
            f.write(f'Дата: {now}\nИмя функции: {func.__name__}\nАргументы функции: {args, kwargs}\n'
                    f'Результат: {res} ')
        return res
    return new_func


@logger_file
def calculate(a, b):
    return a + b


if __name__ == '__main__':
    print(calculate(1, 10))




