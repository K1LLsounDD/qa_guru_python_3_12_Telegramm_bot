import pytest
from selene.support.conditions import have
from selene.support.shared import browser
import allure
from allure_commons.types import Severity


@allure.title('Checking for the presence of text in the registration form')
@allure.tag('web', 'text')
@allure.severity(Severity.NORMAL)
@allure.link('https://demoqa.com/automation-practice-form', name='Registration form')
@allure.label('owner', 'KiLLsounD')
def test_approved():
    browser.open('/automation-practice-form')
    assert browser.element('#currentAddress-label').should(have.text('Current Address'))


def test_approved_2():
    browser.open('/automation-practice-form')
    pass


def test_approved_3():
    browser.open('/automation-practice-form')
    assert browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))


def test_approved_4():
    browser.open('/automation-practice-form')
    pass


@pytest.mark.skip(reason='Пропускаем тест, т.к. форма еще не реализована')
def test_skipped():
    browser.open('/automation-practice-form')
    pass


@pytest.mark.skip(reason='Тест пропущен. т.к. кнопка ПОДТВЕРЖДЕНИЯ не реализована')
def test_skipped_2():
    browser.open('/automation-practice-form')
    pass


@pytest.mark.skip(reason='Тест пропущен, т.к. рак на горе не свистнул')
def test_skipped_3():
    browser.open('/automation-practice-form')
    pass


def test_failed():
    browser.open('/automation-practice-form')
    real_text = browser.element('#userName-label').should(have.text('Name'))
    fake_text = browser.element('#userName-label').should(have.text('Gigi za shagi'))
    assert real_text == fake_text


def test_failed_2():
    browser.open('/automation-practice-form')
    assert 2 == 3
