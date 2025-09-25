from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

URL = "https://www.eba.europa.eu/single-rule-book-qa/search"
driver.get(URL)
driver.maximize_window()


try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="#accept"]').click()
    print("Cookies accepted")
except:
    print("No cookie banner appeared")

driver.execute_script("window.scrollBy(0,1500)")

start_date = driver.find_element(By.ID, "edit-qa-final-publishing-date-start")
end_date = driver.find_element(By.ID, "edit-qa-final-publishing-date-end")

start_date.send_keys("01/01/2025")
end_date.send_keys("31/01/2025")


val_start = start_date.get_property("value")
val_end = end_date.get_property("value")

expected_start = "2025-01-01"
expected_end = "2025-01-31"
time.sleep(2)
try:
    assert val_start == expected_start, f"Start date mismatch, expected {expected_start}, got {val_start}"
    assert val_end == expected_end, f"End date mismatch, expected {expected_end}, got {val_end}"
except AssertionError as e:
    driver.save_screenshot("error.png")
    print(f"Assertion failed: {e}. Screenshot saved.")
    raise


print("Date fields stored correctly in ISO format")


driver.find_element(By.ID, "edit-submit-question-answers").click()


results = driver.find_elements(By.CSS_SELECTOR, ".teaser-qa__footer")
assert len(results) > 0, "No results returned for this date range"
print(f"Found {len(results)} results in the specified date range")


