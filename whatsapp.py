import random
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
    def send_message_to_number(self, phone_no, text, record=None):
        try:
            self.driver.get('https://web.whatsapp.com/send?phone={}&source=&data=#'.format(phone_no))
            sleep(5)
            text_input = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'
            self.element_presence(by=By.XPATH, xpath=text_input, time=30)
            txt_box = self.driver.find_element(By.XPATH, text_input)
            txt_box.click()

            txt_box.send_keys('200 тыс. вместо 3 млн.тг.')
            p = txt_box.find_elements(By.TAG_NAME, 'p')[0].find_element(By.TAG_NAME, 'span')
            self.driver.execute_script("arguments[0].innerHTML += arguments[1];", p, '🚀')
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys('29 августа в TrustMe пройдет "День продаж" с Бейбитом Алибековым!')
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys('Оплати за сервис подписания договоров онлайн TrustContract от 200 тыс и получи возможность рассказать о своем бизнесе в сторис у Алибеков!')
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys('Позвоните по номеру: +77078701904')
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys('или оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
            txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
            txt_box.send_keys('(нужно ответить на сообщение, чтобы нажать на ссылку)')


            txt_box.send_keys(Keys.ENTER)

            # Интервал отправки следуещего сообщения в секундах (можно менять)
            random_number = random.randint(20, 30)
            sleep(random_number)

        except Exception as ex:
            print(ex)
            print('invalid phone no :' + str(phone_no))
