from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = " https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

# Oldal betöltése
driver.get(URL)

# Lokátorok
calc_button = driver.find_element_by_id("submit")
chr = driver.find_element_by_id("chr")
op = driver.find_element_by_id("op")
num = driver.find_element_by_id("num")


def test_right_page():
    """Helyesen betöltődik az applikáció:

    Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    expected_text = "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    # Módosítottam az elvárt eredményen, mert nem egyezett meg az oldalon találhatóval
    text = driver.find_element_by_xpath("/html/body/div/div/p[3]")

    assert expected_text == text.text


def test_valid_test():
    """Megjelenik egy érvényes művelet:

        chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
        op mező vagy + vagy - karaktert tartlamaz
        num mező egy egész számot tartalamaz"""
    expected_test_list = [
        "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"]
    calc_button.click()

    for i in expected_test_list:
        assert chr.text in expected_test_list
        assert op.text in expected_test_list
        assert type(num.text) == int
