from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class meet_bot:
    def __init__(self):
        self.bot = webdriver.Chrome("chromedriver.exe")

    def login(self, email, pas):
        bot = self.bot
        bot.get(
            "https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        time.sleep(2)
        email_in = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        email_in.send_keys(email)
        next_btn = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
        next_btn.click()
        time.sleep(2)
        pas_in = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        pas_in.send_keys(pas)
        next1_btn = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
        next1_btn.click()
        time.sleep(5)

    def join(self, meeting_link):
        bot = self.bot
        bot.get(meeting_link)
        time.sleep(10)
        v_button = bot.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div")
        v_button.click()
        time.sleep(1)
        a_button = bot.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div")
        a_button.click()
        time.sleep(1)
        diss_btn = bot.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
        diss_btn.click()


link = open("meeting.txt", "r").read()
obj = meet_bot()
obj.login("abc@gmail.com", "password")
time.sleep(6)
obj.join(link)