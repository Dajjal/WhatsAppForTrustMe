import re

import pandas as pd

if __name__ == '__main__':
    file_path = 'asd.xlsx'
    df = pd.read_excel(file_path, usecols=[0])
    df = df.astype(str)
    frame = []
    for index, row in df.iterrows():
        number = row.iloc[0]
        frame.append('+' + str(number) + ',')
    df = pd.DataFrame({
        'aaa': frame
    })
    df.to_excel('zxc.xlsx', index=False, engine='openpyxl')


def normalize_phone_number(input: str) -> str:
    # Извлекаем только цифры из входной строки
    digits = re.sub(r'[^0-9]', '', input)

    # Проверяем длину извлеченной строки цифр
    if len(digits) == 11 and digits.startswith("7"):
        return digits[1:]
    elif len(digits) == 11 and digits.startswith("8"):
        return digits[1:]
    elif len(digits) == 10:
        return digits
    elif len(digits) == 9:
        return input
    else:
        return input[-10:]
