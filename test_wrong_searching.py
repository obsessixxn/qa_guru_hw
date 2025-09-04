from selene import browser, have, be


def test_wrong_search(setup_browser, setup_resolution):
    browser.open("https://duckduckgo.com/")
    browser.element('[id="searchbox_input"]').type('3213ddfadwad').press_enter()
    browser.element('//span[contains(text(), "ничего не найдено")]')
    print("Такого здесь нет")
