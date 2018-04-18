from splinter import Browser
import re
from selenium.webdriver.common.keys import Keys

class Prawojazdy:
    def __init__(self):
        self.browser = Browser("chrome", user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

    def otworz_strone(self, strona):
        if strona.startswith('http://') or strona.startswith('https://'):
            self.browser.visit(strona)
        else:
            strona = 'http://' + strona
            self.browser.visit(strona)

    def zamknij_strone(self):
        self.browser.close()

    def zaloguj_sie(self):
        self.otworz_strone("https://www.prawojazdy.com.pl/zaloguj")

    def zalogowano(self):
        logged_in_url = "https://www.prawojazdy.com.pl/panel"
        if self.browser.url == logged_in_url:
            return True
        else:
            return False

    def kurs_wybrany(self):
        kurs_url = "https://ekurs.prawojazdy.com.pl/prawojazdy/lekcja"
        if self.browser.url.startswith(kurs_url):
            return True
        else:
            return False

    def next_button(self):
        button = ""
        xpath = "/html/body/div[6]/div[2]/div/div[2]/div[2]/div[3]/i"
        try:
            button = self.browser.find_by_xpath(xpath)
        except:
            raise Exception('Nie znaleziono przycisku')
        return button

    def nastepna_strona(self):
        active_web_element = self.browser.driver.switch_to_active_element()
        active_web_element.send_keys(Keys.ARROW_RIGHT)

    def find_cookies(self):
        """
        Zwraca ciasteczko sesyjne (PHPSESSID)

        :return: Ciasteczko sesyjne.
        """
        cookies = self.browser.cookies.all()
        try:
            return cookies["PHPSESSID"]
        except:
            raise Exception("Nie znaleziono ciasteczek.")

    def find_slide_string(self):
        xpath = """//*[@id="idSlideQuestion"]"""
        return self.browser.find_by_xpath(xpath).first.text

    def find_slide_number(self):
        string = self.find_slide_string()
        re1 = '.*?'
        re2 = '(\\d+)'
        rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
        m = rg.search(string)
        if m:
            number = m.group(1)
            return number
        else:
            raise Exception("Nie znaleziono numeru slajdu")

    def check_if_ended(self):
        expression1 = self.browser.is_text_present('Gratulacje!')
        expression2 = self.browser.is_text_present('Aby rozpocząć ćwiczenia dokończ naukę')
        return expression1 or expression2

    def get_url(self):
        return self.browser.url


if __name__ == "__main__":
    strona = Prawojazdy()
    strona.zaloguj_sie()
    while not strona.zalogowano():
        continue
    print("Przejdź do nauki i wybierz kurs...")
    while not strona.kurs_wybrany():
        continue
    # button = strona.next_button()
    strona.nastepna_strona()