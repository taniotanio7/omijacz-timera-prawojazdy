import automator.automator as automator
import automator.automator_api as automator_api
import time

if __name__ == "__main__":
    strona = automator.Prawojazdy()
    # Logowanie i wybieranie kursu
    strona.zaloguj_sie()
    while not strona.zalogowano():
        continue
    print("Przejdź do nauki i wybierz kurs...")
    while not strona.kurs_wybrany():
        continue
    # Tworzenie klasy dla API
    cookies = strona.find_cookies()
    url = strona.get_url()
    ajax = automator_api.Prawojazdy_API(cookies, url)
    ajax_header = ajax.get_header()
    # Pętla zaliczania slajdów
    while strona.check_if_not_ended():
        # Odczytywanie danych ze strony
        slide_numer = strona.find_slide_number()
        # Tworzenie i przekazywanie zapytania AJAX
        content = ajax.get_content(slide_numer)
        ajax.send_request(content, ajax_header)
        time.sleep(2)
        # Przechodzenie do następnej strony
        strona.nastepna_strona()
