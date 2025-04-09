from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    # Open product page
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Uncomment for visual check (step 2 in criteria)
    # import time
    # time.sleep(30)

    # Check add to basket button presence
    add_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_button) > 0, "Add to basket button is not found"

    # Alternative more specific check (optional)
    # assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed()