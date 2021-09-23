from datetime import datetime


def log_path(path):
    def logger_file(func):
        def new_func(*args, **kwargs):
            now = datetime.now()
            res = func(*args, **kwargs)
            with open(path, 'w', encoding='utf8') as f:
                f.write(f'Дата: {now}\nИмя функции: {func.__name__}\nАргументы функции: {args, kwargs}\n'
                        f'Результат: {res} ')
            return res
        return new_func
    return logger_file


@log_path('logger2.txt')
def calculate(a, b):
    return a + b


if __name__ == '__main__':
    print(calculate(1, 10))


