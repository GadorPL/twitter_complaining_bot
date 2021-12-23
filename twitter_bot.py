from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

PROMISED_DOWN = 20
PROMISED_UP = 0.5
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_NAME = os.getenv("TWITTER_NAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
CHROME_DRIVER_PATH = "/Development/chromedriver"
NET_PROVIDER_TT = "@Orange_Polska"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        sleep(5)
        i_consent = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        i_consent.click()
        sleep(4)
        go = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go.click()
        sleep(50)
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        dl_txt = float(download_speed.text)
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        ul_txt = float(upload_speed.text)
        if dl_txt > self.down and ul_txt > self.up:
            sleep(3)
            self.driver.quit()
        return {
            "download_speed": dl_txt,
            "upload_speed": ul_txt
        }

    def tweet_at_provider(self, up_speed, down_speed):
        self.driver.get("https://twitter.com/i/flow/login")
        self.driver.maximize_window()
        sleep(4)
        input_tt_name = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                 '2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        input_tt_name.send_keys(TWITTER_EMAIL)
        sleep(2)
        continue_btn = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                '2]/div[2]/div[1]/div/div[6]/div')
        continue_btn.click()
        sleep(3)
        try:
            input_password = self.driver.find_element(By.XPATH,
                                                      '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
                                                      '2]/div[1]/input')
            input_password.send_keys(TWITTER_PASSWORD)
            sleep(2)
            login_btn = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                 '2]/div/div/div[2]/div[2]/div[2]/div/div/div')
            login_btn.click()
        except:
            sleep(3)
            input_tt_name_except = self.driver.find_element(By.XPATH,
                                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                            '2]/label/div/div[2]/div/input')
            input_tt_name_except.send_keys(TWITTER_NAME)
            continue_btn_except = self.driver.find_element(By.XPATH,
                                                           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                           '2]/div/div/div[2]/div[2]/div[2]/div/div')
            continue_btn_except.click()
            sleep(3)
            input_password_except = self.driver.find_element(By.XPATH,
                                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                             '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                             '3]/div/label/div/div[2]/div[1]/input')
            input_password_except.send_keys(TWITTER_PASSWORD)
            sleep(1)
            login_btn_except = self.driver.find_element(By.XPATH,
                                                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div[2]/div/div/div')
            login_btn_except.click()
        finally:
            sleep(5)
            tweet_btn = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div['
                                                 '3]/a/div')
            tweet_btn.click()
            sleep(3)
            input_tweet = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                   '1]/div/div/div/div/div[2]/div/div/div/div')
            input_tweet.send_keys(f"Hej {NET_PROVIDER_TT}, why is my internet speed {down_speed}down/{up_speed}up"
                                  f" when I pay for 20down/1up?")
            sleep(2)
            tweet_btn_final = self.driver.find_element(By.XPATH,
                                                       '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div['
                                                       '3]/div/div/div[2]/div[4]/div')
            tweet_btn_final.click()
            sleep(10)
            self.driver.quit()
