import os

from selene import browser, have
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1920,1080')
browser.config.driver_options = options

def test_exp():
    browser.open('https://demoqa.com/automation-practice-form')

#ввод имя, телефон, почта, гендер
    browser.element('#firstName').type('Lena')
    browser.element('#lastName').type('Grigoryeva')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element("label.form-check-label[for=gender-radio-1]").click()
    browser.element('#userNumber').type('9433740936')

# ввод даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1989"]').click()
    browser.element('.react-datepicker__month-select').element('option[value="4"]').click()
    browser.element('.react-datepicker__day--020').click()

# ввод предметов
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()

# выбор чекбоксов
    browser.element("label.form-check-label[for=hobbies-checkbox-1]").click()
    browser.element("label.form-check-label[for=hobbies-checkbox-2]").click()
    browser.element("label.form-check-label[for=hobbies-checkbox-3]").click()

# загрузка изображения
    browser.element('#uploadPicture').send_keys(os.path.abspath('b2586f8eb5561542e587aded807478e8.jpg'))

# ввод адреса

    browser.element('#currentAddress').type('Полевой пер., д. 2 кв.145')
    browser.element('#react-select-3-input').click()
    browser.element('//div[text()="NCR"]').click()
    browser.element('#react-select-4-input').click()
    browser.element('//div[text()="Noida"]').click()

    browser.element('#submit').click()

#проверка данных
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.all('.table-responsive').element_by(have.text('Student Name')).should(have.text('Lena Grigoryeva'))
    browser.all('.table-responsive').element_by(have.text('Student Email')).should(have.text('test@gmail.com'))
    browser.all('.table-responsive').element_by(have.text('Gender')).should(have.text('Male'))
    browser.all('.table-responsive').element_by(have.text('Mobile')).should(have.text('9433740936'))
    browser.all('.table-responsive').element_by(have.text('Date of Birth')).should(have.text('20 May,1989'))
    browser.all('.table-responsive').element_by(have.text('Subjects')).should(have.text('Arts, Maths'))
    browser.all('.table-responsive').element_by(have.text('Hobbies')).should(have.text('Sports, Reading, Music'))
    browser.all('.table-responsive').element_by(have.text('Picture')).should(have.text('b2586f8eb5561542e587aded807478e8.jpg'))
    browser.all('.table-responsive').element_by(have.text('Address')).should(
        have.text('Полевой пер., д. 2 кв.145'))
    browser.all('.table-responsive').element_by(have.text('State and City')).should(
        have.text('NCR Noida'))
