site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result


user = input('Какой ключ ищем?')
value = find_key(site, user)
if value:
    print(value)
else:
    print('Такого ключа нет')