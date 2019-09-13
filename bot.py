# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import win10toast
import time

class AdminBot:
    def __init__(self, username, password, delay):
        self.username = username
        self.password = password
        self.delay = delay
        self.driver = webdriver.Chrome()
    def login(self):
        driver = self.driver
        driver.get("https://account.eslgaming.com/login")
        time.sleep(2)
        login = driver.find_element_by_xpath('//*[@id="input_0"]')
        login.click()
        login.send_keys(self.username)
        login.send_keys(Keys.RETURN)
        time.sleep(1)
        passsword = driver.find_element_by_xpath('//*[@id="input_1"]')
        passsword.send_keys(self.password)
        passsword.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get("https://play.eslgaming.com/counterstrike/csgo/csgo/major/esl-mistrzostwa-polski/esl-mistrzostwa-polski-2019-sezon-2-qualifier-1/admin_leaguejoins/overview/")
        time.sleep(2)
        confirm_btn = driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button[2]')
        confirm_btn.click()
        time.sleep(2)
        logadmin = driver.find_element_by_xpath('//*[@id="block-te-eslid-login"]')
        logadmin.click()
        time.sleep(2)
        selectadmin = driver.find_element_by_xpath('//*[@id="main-content"]')
        selectadmin.click()
        time.sleep(1)
        logtoadminpanel = driver.find_element_by_xpath('//*[@id="adminEnableLink"]')
        logtoadminpanel.click()
        time.sleep(1)
    def checkLeagueJoins(self):
        toaster = win10toast.ToastNotifier()
        driver = self.driver
        driver.minimize_window()
        while True:
            if driver.find_elements_by_css_selector('body > div.l-page > div.l-main > div > div.l-content > article > div > div > div > div > div > div:nth-child(1) > div:nth-child(3) > table > tbody'):
                toaster.show_toast("ESL MP", "Znaleziono leaguejoinsy do akceptacji",  icon_path ="images/icon.ico", duration = 5)
                driver.maximize_window()
                break
            driver.refresh()
            time.sleep(self.delay)
    def closeBrowser(self):
        driver = self.driver
        driver.close()
