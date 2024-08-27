from whatsapp import WhatsApp

mobile_numbers_list = [
    # тут писать номера в формате чисел - пример: 77071234567, 7701...
]

if __name__ == '__main__':
    whatsapp = WhatsApp()
    for mobile_number in mobile_numbers_list:
        whatsapp.send_message_to_number(mobile_number, 'Тут писать текст который хотите чтобы был отправлен...')
