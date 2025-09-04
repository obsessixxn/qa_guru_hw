from selene import browser
from selenium import webdriver
import pytest
import time


def test_search_guru(setup_browser, setup_resolution):
    browser.open('https://ya.ru')
    browser.element('[id="text"]').type('qa guru').press_enter()
    browser.element('[title="Нет, спасибо"]').click()
    browser.element('//a[contains(@href,"qa.guru")]').click()
    browser.element('//h1[contains(text(),"Школа QA")]')
    time.sleep(3)
