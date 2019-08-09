from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class IGBOT():
    def __init__(self, email, password):
        self.browser_profile = webdriver.ChromeOptions()
        self.browser_profile.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome("/home/nadaked/Desktop/chromedriver", chrome_options=self.browser_profile)
        self.email = email
        self.password = password

    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        email_input = self.browser.find_element_by_xpath("//input[@name='username']")
        password_input = self.browser.find_element_by_xpath("//input[@name='password']")

        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def follow_with_username(self, username):
        self.browser.get("https://www.instagram.com/" + username + "/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_css_selector("button[type*='button'")
        if follow_button.text != "Following":
            follow_button.click()
            time.sleep(2)

    def unfollow_with_username(self, username):
        self.browser.get("https://www.instagram.com/" + username + "/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_css_selector("button")
        if follow_button.text == "Following":
            follow_button.click()
            time.sleep(2)
            confirm_button = self.browser.find_element_by_xpath("//button[text() = 'Unfollow']")
            confirm_button.click()


username = "your username or email"
password = "your password"
follow_user = "nnadaked"
bot = IGBOT(email=username, password=password)
bot.sign_in()
bot.unfollow_with_username(username=follow_user)
