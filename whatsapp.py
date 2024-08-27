from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class WhatsApp:

    # Конструктор
    def __init__(self):
        # Настройка локальной папки, в которой будет храниться авторизация
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=user_data')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://web.whatsapp.com/')

    # Помошник - применяется для того, чтобы узнать есть ли элемент html в отображении (загрузился или нет)
    def element_presence(self, by, xpath, time):
        element_present = ec.presence_of_element_located((by, xpath))
        WebDriverWait(self.driver, time).until(element_present)

    # Основной метод для отправки сообщения
    # параметры: номер телефона и текст который хотите передать
    def send_message_to_number(self, phone_no, text):
        try:
            self.driver.get('https://web.whatsapp.com/send?phone={}&source=&data=#'.format(phone_no))
            sleep(5)
            text_input = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            self.element_presence(by=By.XPATH, xpath=text_input, time=30)
            txt_box = self.driver.find_element(By.XPATH, text_input)
            txt_box.send_keys(text)
            txt_box.send_keys(Keys.ENTER)

            # Интервал отправки следуещего сообщения в секундах (можно менять)
            sleep(60)

        except:
            print('invalid phone no :' + str(phone_no))

