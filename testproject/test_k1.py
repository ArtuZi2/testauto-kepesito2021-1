from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = " https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

# Oldal betöltése
driver.get(URL)

# Lokátorok
a_input = driver.find_element_by_id("a")
b_input = driver.find_element_by_id("b")
c_result = driver.find_element_by_id("result")
calc_button = driver.find_element_by_id("submit")

# Tesztadatok

a = [2, ""]
b = [3, ""]
c = [10, "NaN"]


def fill_and_clear_input(element):
    element.clear()


def test_empty_page():
    """Helyesen jelenik meg az applikáció betöltéskor:

        a: <üres>
        b: <üres>
        c: <nem látszik>"""

    calc_button.is_enabled()
    assert a_input.text == ""
    assert b_input.text == ""
    results = driver.find_element_by_id("results")
    assert results.is_displayed() == False


def test_normal_count():
    """Számítás helyes, megfelelő bemenettel

        a: 2
        b: 3
        c: 10"""

    a_input.send_keys(a[0])
    b_input.send_keys(b[0])
    calc_button.click()

    assert c_result.text == str(c[0])


def test_empty_fill():
    """Üres kitöltés:

        a: <üres>
        b: <üres>
        c: NaN"""
    fill_and_clear_input(a_input)
    fill_and_clear_input(b_input)
    a_input.send_keys(a[1])
    b_input.send_keys(b[1])
    calc_button.click()

    assert c_result.text == c[1]
