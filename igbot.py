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
        self.url = "https://www.instagram.com/"
        self.like_unlike_button_path = "/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button"

    def sign_in(self):
        self.browser.get(self.url + "accounts/login/")
        email_input = self.browser.find_element_by_xpath("//input[@name='username']")
        password_input = self.browser.find_element_by_xpath("//input[@name='password']")
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def follow_with_username(self, username):
        self.browser.get(self.url + username + "/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_css_selector("button[type*='button'")
        if follow_button.text != "Following":
            follow_button.click()
            time.sleep(2)

    def unfollow_with_username(self, username):
        self.browser.get(self.url + username + "/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_css_selector("button")
        if follow_button.text is "Following":
            follow_button.click()
            time.sleep(2)
            confirm_button = self.browser.find_element_by_xpath("//button[text() = 'Unfollow']")
            confirm_button.click()

    def like_profile(self, username):
        self.browser.get(self.url + username + "/")
        self.scroll()
        page = self.browser.page_source
        splt = page.split("v1Nh3 kIKUG  _bz0w")
        for spl in splt:
            if spl.find('href="/p') is not -1:
                photo_link = spl[spl.find('href="/p') + 7: spl.find('/"') + 1]
                print(photo_link)
                self.browser.get(self.url + photo_link)
                like_button = self.browser.find_element_by_xpath(self.like_unlike_button_path)
                if like_button.get_attribute("innerHTML").find("Unlike") is not 1:
                    like_button.click()
                    time.sleep(2)

    def unlike_profile(self, username):
        self.browser.get(self.url + username + "/")
        self.scroll()
        page = self.browser.page_source
        splt = page.split("v1Nh3 kIKUG  _bz0w")
        for spl in splt:
            if spl.find('href="/p') is not -1:
                photo_link = spl[spl.find('href="/p') + 7: spl.find('/"') + 1]
                self.browser.get(self.url + photo_link)
                unlike_button = self.browser.find_element_by_xpath(self.like_unlike_button_path).click()
                time.sleep(2)

    def scroll(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


username = "your username"
password = "your password"
follow_user = "sancaktarmk"
bot = IGBOT(email=username, password=password)
bot.sign_in()
bot.follow_with_username(username=follow_user)
# bot.unfollow_with_username(username=follow_user)
# bot.like_profile(username=follow_user)
# bot.unlike_profile(username=follow_user)
