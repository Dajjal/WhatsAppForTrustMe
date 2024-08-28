from add_to_db import engine, PhonesTable
from whatsapp import WhatsApp

from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()

    phones_list = session.query(PhonesTable).all()

    whatsapp = WhatsApp()
    for index, item in enumerate(phones_list):
        if index < 1000 and item.status == 'waiting':
            whatsapp.send_message_to_number(phone_no='7' + item.phone, record=item)
            session.commit()
