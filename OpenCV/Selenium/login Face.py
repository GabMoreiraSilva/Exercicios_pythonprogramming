from selenium import webdriver
from secret import login, senha
from time import sleep

class facebook:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\bielm\PycharmProjects\facebook\chromedriver.exe')
    
    def login(self):
        self.driver.get('https://web.facebook.com/?_rdc=1&_rdr')
        login_box = self.driver.find_element_by_xpath('//*[@id="email"]')
        login_box.send_keys(login)
        password_box = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_box.send_keys(senha)
        btn_face = self.driver.find_element_by_xpath('//*[@id="u_0_b"]') 
        btn_face.click()

bot = facebook()
bot.login()