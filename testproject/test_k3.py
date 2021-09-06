from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

# Oldal betöltése
driver.get(URL)

#Lokátorok
title = driver.find_element_by_id("title")

#Tesztadatok
title_data = ["abcd1234", "teszt233@", "abcd" ]
excepted_error_msg = ["", "Only a-z and 0-9 characters allewed",
                      "Title should be at least 8 characters; you entered 4."]
error_msg = driver.find_element_by_xpath("/html/body/form/span")

def test_valid_fill():
    """Helyes kitöltés esete:

        title: abcd1234
        Nincs validációs hibazüzenet"""
    title.send_keys(title_data[0])

    assert error_msg.text == ""


def test_illegal_datas():
    title.clear()
    title.send_keys(title_data[1])

    assert error_msg.text == excepted_error_msg[1]


def test_short_text_data():
    title.clear()
    title.send_keys(title_data[2])

    assert error_msg.text == excepted_error_msg[2]





