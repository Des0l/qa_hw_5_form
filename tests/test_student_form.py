from selene import browser, have, be
import os


def test_demoqa_form():
    # Проверяем, что попали на нужную страницу
    browser.element(".text-center").should(have.text("Practice Form"))

    # Вводим первоначальные данные
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('vanvan@mail.ru')
    browser.element("label[for='gender-radio-1']").should(
        have.exact_text('Male')
    ).click()
    browser.element('#userNumber').should(be.blank).type('89879879879')

    # Работа с календарем
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().all('option').element_by(
        have.text('May')
    ).click()
    browser.element('.react-datepicker__year-select').click().all('option').element_by(
        have.text('1996')
    ).click()
    browser.all('.react-datepicker__day--003').element(0).click()

    # Вводим предметы
    browser.element('#subjectsInput').type('Biology').press_enter().type(
        'Physics'
    ).press_enter().type('Chemistry').press_enter()

    # Проставляем чек-боксы хобби
    browser.element('//label[text()="Sports"]').click()

    browser.element('//label[text()="Music"]').click()

    # Вставляем файл
    browser.element('#uploadPicture').type(
        os.path.abspath('../additional_files/photo.jpg')
    )

    # Работаем с адресом
    browser.element('#currentAddress').should(be.blank).type('Барселона, ул. Ленина 14')

    browser.element('#state').click().all(
        'div[id^="react-select-3-option"]'
    ).element_by(have.text('Haryana')).click()

    browser.element('#city').click().all('div[id^="react-select-4-option"]').element_by(
        have.text('Panipat')
    ).click()

    # Отправляем форму
    browser.element('#submit').click()

    # Проверка корректности введенных данных
    browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )

    expected_labels = [
        "Student Name",
        "Student Email",
        "Gender",
        "Mobile",
        "Date of Birth",
        "Subjects",
        "Hobbies",
        "Picture",
        "Address",
        "State and City",
    ]

    expected_values = [
        "Ivan Ivanov",
        "vanvan@mail.ru",
        "Male",
        "8987987987",
        "03 May,1996",
        "Biology, Physics, Chemistry",
        "Sports, Music",
        "photo.jpg",
        "Барселона, ул. Ленина",
        "Haryana Panipat",
    ]

    browser.all("tbody tr td:nth-child(1)").should(have.texts(*expected_labels))
    browser.all("tbody tr td:nth-child(2)").should(have.texts(*expected_values))

    # Закрываем окно
    browser.element('#closeLargeModal').click()

    # Проверяем, что снова попали на страницу формы
    browser.element(".text-center").should(have.text("Practice Form"))
