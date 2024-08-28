from add_to_db import engine, PhonesTable
from whatsapp import WhatsApp

from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()

    phones_list = session.query(PhonesTable).filter(PhonesTable.status == 'error').all()

    whatsapp = WhatsApp()
    for item in phones_list:
        whatsapp.send_message_to_number(phone_no='7' + item.phone, record=item)
        session.commit()
