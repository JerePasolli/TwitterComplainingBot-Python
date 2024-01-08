import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

UP_SPEED = 8
DOWN_SPEED = 110
TWITTER_MAIL = os.environ.get('TWITTER_MAIL')
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        test_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/'
                                                         'div[3]/div[1]/a/span[4]')
        test_button.click()
        time.sleep(80)
        down_result = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/'
                                                         'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/'
                                                         'div/div[2]/span')
        self.down_speed = float(down_result.text)
        up_result = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/'
                                                       'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                       'div/div[2]/span')
        self.up_speed = float(up_result.text)

    def tweet_at_provider(self):
        if self.down_speed < DOWN_SPEED or self.up_speed < UP_SPEED:
            print("Logging in to Twitter...")
            self.driver.get("https://twitter.com/")
            time.sleep(3)
            log_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/'
                                                        'div[1]/div[1]/div/div[3]/div[5]/a')
            log_in.click()
            time.sleep(5)
            mail = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/'
                                                      'div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/'
                                                      'div[5]/label/div/div[2]/div/input')
            mail.send_keys(TWITTER_MAIL)
            mail.send_keys(Keys.ENTER)
            time.sleep(5)
            user_name = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/'
                                                           'div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/'
                                                           'div/div[2]/label/div/div[2]/div/input')
            user_name.send_keys("JeremiasPasolli")
            user_name.send_keys(Keys.ENTER)
            time.sleep(3)
            password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/'
                                                          'div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/'
                                                          'div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)

            print("Writing complain and posting...")
            text_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/'
                                                          'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/'
                                                          'div/div/div/div/div/div/div/div/div/div')
            text_box.send_keys(f"Esto es una queja sobre el servicio de IPTEL, mi proveedor de internet, ya que tengo"
                               f"contratados 120Mb de bajada y 12Mb de subida. Sin embargo ahora mismo mi servicio de "
                               f"internet esta funcionando a {self.down_speed}Mb de bajada y {self.up_speed}Mb de "
                               f"subida")
            post_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/'
                                                             'div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/d'
                                                             'iv[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
            post_button.click()
            print("Complaint posted successfully...")
        else:
            print("Internet speeds are ok, it is not necessary to post a complain...")


bot = InternetSpeedTwitterBot()
print("Bot initialized...")
time.sleep(3)
print("Starting internet test using Speedtest.net...")
bot.get_internet_speed()
print("Internet test finished. Up and down speeds saved...")
bot.tweet_at_provider()
print("Bot finished. Goodbye...")




