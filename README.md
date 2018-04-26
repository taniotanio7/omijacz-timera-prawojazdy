<h1 align="center">🚘 Omijacz Timera Prawojazdy 🚔</h1>

[![Build Status](https://travis-ci.org/taniotanio7/omijacz-timera-prawojazdy.svg?branch=master)](https://travis-ci.org/taniotanio7/omijacz-timera-prawojazdy)
[![Maintainability](https://api.codeclimate.com/v1/badges/f1483bc09e7003232cb7/maintainability)](https://codeclimate.com/github/taniotanio7/omijacz-timera-prawojazdy/maintainability)
[![Updates](https://pyup.io/repos/github/taniotanio7/omijacz-timera-prawojazdy/shield.svg)](https://pyup.io/repos/github/taniotanio7/omijacz-timera-prawojazdy/)

> 🎉 Żyj! 🎉
>
> Nie trać czasu na nudne, powtarzające się slajdy...

## Opis

Skrypt pozwala na "ominięcie" slajdów w kursie e-learningowym na stronie **prawojazdy.com.pl**
Wykorzystuje sposób działania serwisu oraz fakt, że po stronie serwera nie następuje żadna weryfikacja czy slajd został faktycznie obejrzany.


## Instalacja

Musisz posiadać zainstalowanego Pythona, pip oraz **Google Chrome**.

W wierszu poleceń / terminalu wpisz:

```python
pip install omijacz-timera
```
lub
```python
pip3 install omijacz-timera
```
*Komenda zależy od twojej instalacji Pythona*

### Ręczna instalacja

Pobierz .zip: https://github.com/taniotanio7/omijacz-timera-prawojazdy/archive/master.zip i rozpakuj.

Przejdź do folderu z projektem:

```
cd omijacz-timera-prawojazdy
```

Zainstaluj z użyciem setup.py:
```
python setup.py install
```
## Korzystanie

1. W wierszu poleceń / terminalu wpisz:

```
omijacz_timera
```

Otworzy się nowy proces Google Chrome:

![Nowe okno Google Chrome ze stroną do logowania](/readme_images/login_screen.png)

2. Zaloguj się!

![Strona po wpisaniu danych do logwania](/readme_images/login_screen_filled.png)

> Twoje hasło nie jest nigdzie zapisywane zostaje użyte tylko do zalogowania się w przeglądarce

3. Kliknij w przycisk "Przejdź do kursu"

![Przycisk przejdź do kursu](/readme_images/course_select_main.png)

4. Wybierz lekcję

![Wybór lekcji](/readme_images/course_select_choice.png)

5. Ciesz się obejrzaną lekcją!

![Automatyzacja slajdów](/readme_images/course_automated.png)

### :rotating_light: Dobra rada :rotating_light:

> Mimo wszystko zalecałbym po "odhaczeniu" lekcji obejrzenie wszystkich slajdów.
>
> Dzięki temu coś zapamiętasz, a nie będziesz musiał dodatkowo marnować swojego czasu
> na odczekanie, aż będziesz mógł przejść dalej


## :poop: Zgłaszanie błędów

Problemy można zgłaszać tutaj: https://github.com/taniotanio7/omijacz-timera-prawojazdy/issues

## :construction_worker: Development environment

Te instrukcje pomogą Ci uruchomić kopię projektu na twoim lokalnym urządzeniu w celu programowania lub testowania. 

### Zanim zaczniesz

Co potrzebujesz, aby rozpocząć

- Python
- pip
- git

### Instalacja

Krok po kroku jak utworzyć środowisko programistyczne.

Utwórz kopię repozytorium git

```
git clone https://github.com/taniotanio7/omijacz-timera-prawojazdy.git
```

Zainstaluj potrzebne zależności

```
pip install -r requirements.txt
```

## :recycle: Todo

- [ ] Przyśpieszyć działanie
- [ ] Refaktoryzacja
- [ ] Poprawa obsługi slajdów z pytaniem
- [ ] Możliwość wyboru innych przeglądarek niż Chrome

## :sunglasses: Autorzy

* **Jonatan Witoszek** - *Początek* - [taniotanio7](https://github.com/taniotanio7)

Zobacz pełną listę [osób](https://github.com/taniotanio7/omijacz-timera-prawojazdy/contributors), która pomogła w projekcie.

## :page_facing_up: Licence

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## :clap: Acknowledgments

* Hat tip to Kenneth Reitz for his setup.py example!
