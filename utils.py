import re
from datetime import datetime

def validate_input(prompt, validation_regex=None, error_message="Entrada inválida."):
    while True:
        user_input = input(prompt).strip() # .strip() remove espaços em branco no início e fim
        if not user_input:
            print("O campo não pode ficar vazio. Tente novamente.")
            continue
        if validation_regex:
            # fullmatch verifica se a entrada inteira corresponde ao padrão
            if not re.fullmatch(validation_regex, user_input):
                print(error_message)
                continue
        return user_input

def validate_int_input(prompt, min_val=None, max_val=None, error_message="Entrada inválida. Digite um número inteiro."):
    while True:
        try:
            user_input = int(input(prompt).strip())
            if min_val is not None and user_input < min_val:
                print(f"O número deve ser no mínimo {min_val}.")
                continue
            if max_val is not None and user_input > max_val:
                print(f"O número não pode ser maior que {max_val}.")
                continue
            return user_input
        except ValueError:
            print(error_message)

def validate_float_input(prompt, min_val=None, error_message="Entrada inválida. Digite um número (ex: 10.50)."):
    while True:
        try:
            user_input = float(input(prompt).strip())
            if min_val is not None and user_input < min_val:
                print(f"O valor deve ser no mínimo {min_val}.")
                continue
            return user_input
        except ValueError:
            print(error_message)

def validate_date_input(prompt, date_format="%Y-%m-%d", error_message="Formato de data inválido. Use AAAA-MM-DD."):
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            print(error_message)

def validate_datetime_input(prompt, datetime_format="%Y-%m-%d %H:%M:%S", error_message="Formato de data e hora inválido. Use AAAA-MM-DD HH:MM:SS."):
    while True:
        datetime_str = input(prompt).strip()
        try:
            return datetime.strptime(datetime_str, datetime_format)
        except ValueError:
            print(error_message)