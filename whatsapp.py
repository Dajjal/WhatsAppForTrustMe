import random
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class WhatsApp:
    counter = 1

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
    def send_message_to_number(self, phone_no, record):
        try:
            self.driver.get('https://web.whatsapp.com/send?phone={}&source=&data=#'.format(phone_no))
            sleep(5)
            text_input = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'
            self.element_presence(by=By.XPATH, xpath=text_input, time=30)
            txt_box = self.driver.find_element(By.XPATH, text_input)
            txt_box.click()

            if self.counter == 1:
                txt_box.send_keys('200 тыс. вместо 3 млн.тг.')
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
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 2:
                txt_box.send_keys(f'Здравствуйте!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(
                    'Команда TrustMe рада сообщить вам, что в этот четверг (29авг) у нас особенное событие — «День продаж» с известным блогером- Алибековым!  Не упустите возможность стать известным и кратно увеличить прибыль!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 3:
                txt_box.send_keys('29 августа в TrustMe пройдет "День продаж" с Бейбитом Алибековым!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('200 тыс. вместо 3 млн.тг.')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(
                    'Оплати за сервис подписания договоров онлайн TrustContract от 200 тыс и получи возможность рассказать о своем бизнесе в сторис у Алибеков!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 4:
                txt_box.send_keys(f'Здравствуйте!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(
                    'Команда TrustMe рада сообщить вам, что в этот четверг (29авг) у нас особенное событие — «День продаж» с известным блогером- Алибековым!  Не упустите возможность стать известным и кратно увеличить прибыль!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 5:
                txt_box.send_keys('200 тыс. вместо 3 млн.тг.')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('29 августа в TrustMe пройдет "День продаж" с Бейбитом Алибековым!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(
                    'Оплати за сервис подписания договоров онлайн TrustContract от 200 тыс и получи возможность рассказать о своем бизнесе в сторис у Алибеков!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 6:
                txt_box.send_keys(
                    'Команда TrustMe рада сообщить вам, что в этот четверг (29авг) у нас особенное событие — «День продаж» с известным блогером- Алибековым!  Не упустите возможность стать известным и кратно увеличить прибыль!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
            elif self.counter == 7:
                txt_box.send_keys('29 августа в TrustMe пройдет "День продаж" с Бейбитом Алибековым!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('200 тыс. вместо 3 млн.тг. Успей приобрести.')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(
                    'Оплати за сервис подписания договоров онлайн TrustContract от 200 тыс и получи возможность рассказать о своем бизнесе в сторис у Алибеков!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
            elif self.counter == 8:
                txt_box.send_keys(
                    'Команда TrustMe рада сообщить вам, что в этот четверг (29авг) у нас особенное событие — «День продаж» с известным блогером- Алибековым!  Не упустите возможность стать известным и кратно увеличить прибыль!')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('Оставьте заявку по ссылке: https://trustmekz.bitrix24.site/mail/')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('или позвоните по номеру: +77078701904')
                txt_box.send_keys(Keys.CONTROL + Keys.ENTER)
                txt_box.send_keys('(если вы ознакомились с данной информацией, напишите в ответ любой текст)')

            if self.counter < 8:
                self.counter += 1
            elif self.counter == 8:
                self.counter = 1

            txt_box.send_keys(Keys.ENTER)
            record.status = 'sended'

            # Интервал отправки следуещего сообщения в секундах (можно менять)
            random_number = random.randint(30, 90)
            sleep(random_number)

            return True

        except Exception as ex:
            print(ex)
            print('invalid phone no :' + str(phone_no))

            return False
