import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import datetime
from config import LOGIN, PASSWORD  #лучше вынести потом в переменные окружения да считывать их, как делал при разработке ботов для тг
import getpass


class ErrorPage:
    def __init__(self,airport_name, devops_name = 'Скрыто в целях конфиденциальности'):
        self.airport_name = airport_name 
        self.devops_name = devops_name

    def open_error_frame(self):
            window = tkinter.Tk()
            window.title('Что-то стало красным')
            window.geometry('300x400')
            text = tkinter.Label(window, text=f'{self.airport_name} красный', font=('Arial', 24))
            text.place(x=50, y=50)
            arsen = tkinter.Label(window, text=f'Пиши {self.devops_name}у!!!', font=('Arial', 26))
            arsen.place(x=25, y=170)
            timee = datetime.datetime.now()
            time_now = tkinter.Label(window, text=f'{timee}', font=('Arial', 14))
            time_now.place(x=25, y=220)
            who_made = tkinter.Label(window, text='Это приложение разработал Мирон', font=('Arial', 13))
            who_made.place(x=5, y=350)
            window.mainloop()

class SeleniumHelper:                               #необходимо переименовать класс в более подходящий, либо же разбить его на 2 класса, но тогда кодовая база будет больше
    def __init__(self, airport, browser):
        self.airport = airport.lower()
        self.browser = browser

    def go_grafana_main_page(self):
        self.browser.get('Скрыто в целях конфиденциальности. Ссылка на графану, основная страница.')

    def authorization_in_grafana(self, LOGIN, PASSWORD):
        self.browser.find_element(By.CSS_SELECTOR, '[name=user]').send_keys(LOGIN)
        self.browser.find_element(By.CSS_SELECTOR, '#current-password').send_keys(PASSWORD)
        self.browser.find_element(By.CLASS_NAME, 'css-1c5twjv-button').click()
        time.sleep(2)

    def go_to_dashbords_page(self):
        self.browser.get('Скрыто в целях конфиденциальности. Переход на страницу с дашбордами, которые мониторить будем')
        time.sleep(5)

    @property
    def return_rgba_value_of_dashbord(self):
        if self.airport == 'kzn':
            self.airport = 'mak'
        return self.browser.find_element(By.CSS_SELECTOR, f'[href="https://Скрыто в целях конфиденциальности/d/{self.airport}_prod_overview_project_main/overview"] > div').value_of_css_property('background-color')


RED_COLOR = 'rgba(245, 54, 54, 0.9)'


def browser():
    print("\nНачинаем мониторить ситуацию с аэропортами. Надеюсь, что вы не увидите оповещений о красном цвете")
    options = Options()
    options.add_argument('--headless=new')
    browser = webdriver.Chrome(options=options)
    return browser

def sync(browser):
    IATA1 = SeleniumHelper('IATA1', browser)
    IATA2 = SeleniumHelper('IATA2', browser)              #можно было через списочные выражения создать сразу много экземпляров, но читаемость кода снизится
    IATA3 = SeleniumHelper('IATA3', browser) 
    IATA4 = SeleniumHelper('IATA4', browser)
    IATA5 = SeleniumHelper('IATA5', browser)
    IATA6 = SeleniumHelper('IATA6', browser)
    IATA7 = SeleniumHelper('IATA7', browser)
    IATA8 = SeleniumHelper('IATA8', browser)
    IATA1.go_grafana_main_page()                          #без разницы через какой аэропорт проводить авторизацию
    IATA1.authorization_in_grafana(LOGIN, PASSWORD)       #просто я пока не нашел варианта получше ввиду малого опыта
    IATA1.go_to_dashbords_page()                          #в дальнейшем модернизирую по красоте, а пока так :)
    count = 0
    while count !=100:                                    
        #IATA1
        if RED_COLOR == IATA1.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA1')
            error.open_error_frame()
            count += 1

        #IATA2
        elif RED_COLOR == IATA2.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA2')
            error.open_error_frame()
            count += 1

        #IATA3
        elif RED_COLOR == IATA3.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA3')
            error.open_error_frame()
            count += 1

        #IATA4
        elif RED_COLOR == IATA4.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA4')
            error.open_error_frame()
            count += 1

        #IATA5
        elif RED_COLOR == IATA5.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA5')
            error.open_error_frame()
            count += 1

        #IATA6
        elif RED_COLOR == IATA6.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA6')
            error.open_error_frame()
            count += 1

        #IATA7
        elif RED_COLOR  == IATA7.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA7')
            error.open_error_frame()
            count += 1


        #IATA8
        elif RED_COLOR  == IATA8.return_rgba_value_of_dashbord:
            error = ErrorPage('IATA8')
            error.open_error_frame()
            count += 1


print('Введите секретную фразу:')
password = getpass.getpass('Пароль:')
if password == 'Скрыто в целях конфиденциальности':
    print('Успешно')
    sync(browser())
else:
    print('Неправильный пароль')
