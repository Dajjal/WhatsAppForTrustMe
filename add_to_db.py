import re
import pandas as pd

from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.db', echo=True)
Base = declarative_base()


class PhonesTable(Base):
    __tablename__ = 'phones'

    id = Column(Integer, Sequence('phone_id_seq'), primary_key=True)
    name = Column(String(500))
    phone = Column(String(500))
    status = Column(String(500))

    def __repr__(self):
        return f"<Phone(name={self.name})>"


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


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Загрузка Excel файла
    file_path = 'phones.xlsx'
    df = pd.read_excel(file_path, usecols=[36, 39])

    for index, row in df.iterrows():
        value_ak = row.iloc[0]
        value_an = row.iloc[1]

        if str(value_ak) != 'nan' and str(value_an) != 'nan' and value_ak and value_an:
            if (str(value_ak).lower() == 'частное лицо'
                    or str(value_ak).lower() == 'без имени'
                    or str(value_ak).lower() == 'номер'):
                value_ak = None
            value_an = normalize_phone_number(str(value_an))
            phone = PhonesTable(name=value_ak, phone=value_an, status='waiting')
            session.add(phone)
            session.commit()
