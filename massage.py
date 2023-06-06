def read_message(file):
    with open(file, 'r', encoding='utf-8') as file:
        message = file.read()
    return message