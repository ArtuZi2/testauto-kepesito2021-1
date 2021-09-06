from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

# Oldal betöltése
driver.get(URL)

# Lokátorok
init_button = driver.find_element_by_id("init")
play_button = driver.find_element_by_id("spin")


def test_right():
    """"Az applikáció helyesen megjelenik:

    A bingo tábla 25 darab cellát tartalmaz
    A számlista 75 számot tartalmaz"""

    cells_number = driver.find_elements_by_tag_name("td")
    assert len(cells_number) == 25

    number_list = driver.find_elements_by_tag_name("li")
    assert len(number_list) == 75


def test_bingo():
    """Bingo számok ellenőzrzése:

    Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
    Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a
    már kihúzott számok közül kerültek-e ki"""
    bingo_msg = driver.find_element_by_id("messages")

    for i in range(75):
        play_button.click()
    if bingo_msg.is_displayed():
        init_button.click()
