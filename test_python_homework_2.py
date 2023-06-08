from selene.support.shared import browser
from selene import be, have


def test_successful_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_new_empty_search(open_browser):
    browser.element('[name="q"]').type('aedfirgjsdufjbnsdufbsdufb').press_enter()
    browser.element('[id="center_col"]').should(have.text('По запросу aedfirgjsdufjbnsdufbsdufb ничего не найдено'))
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))