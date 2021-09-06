import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = " https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

# Oldal betöltése
driver.get(URL)

# Lokátorok
start = driver.find_element_by_id("start")
stop = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")
random_color = driver.find_element_by_id("randomColor")
test_color = driver.find_element_by_id("testColor")
random_color_name = driver.find_element_by_id("randomColorName")
test_color_name = driver.find_element_by_id("testColorName")


def test_right_appearence_page():
    """Helyesen jelenik meg az applikáció betöltéskor:

        Alapból egy random kiválasztott szín jelenik meg az == bal oldalán.
        A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ] """

    assert random_color.is_enabled()
    assert random_color.is_displayed()
    assert test_color.text == "[     ]"


def test_start_and_stop_game():
    assert start.is_enabled()
    assert start.is_displayed()
    assert stop.is_displayed()
    assert stop.is_enabled()

    start.click()
    time.sleep(2)
    stop.click()
    test_color = driver.find_element_by_id("testColor")

    assert test_color != "[     ]"


def test_correct_no_correct():
    """Eltaláltam, vagy nem találtam el.

        Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és a jobb oldal ugyan
        azt a színt tartalmazza akkor a Correct! felirat jelenik meg. ha akkor amikor eltérő szín van a jobb és bal
        oldalon akkor az Incorrect! felirat kell megjelenjen."""

    color_list = ["IndianRed", "Pink", "HotPink", "Coral", "OrangeRed", "DarkOrange", "Yellow", "DarkKhaki", "Violet",
                  "MediumOrchid", "DarkMagenta", "Chartreuse", "MediumSpringGreen", "DarkGreen", "DarkCyan",
                  "Turquoise", "RoyalBlue", "NavajoWhite", "SaddleBrown", "Gray", "Black", "AliceBlue",
                  "OldLace", "Chocolate"]
    start.click()
    for i in color_list:
        if i != random_color_name.text:
            stop.click()
    else:
        start.click()

    assert result.text == "Incorrect"
