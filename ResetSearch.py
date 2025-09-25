from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

legalAct = dropdown = Select(driver.find_element(By.ID, "edit-qa-legal-act"))
dropdown.select_by_index(4)
answerPrepared = dropdown = Select(driver.find_element(By.ID, "edit-qa-answer-source"))
dropdown.select_by_index(1)

questionID = driver.find_element(By.ID, "edit-qa-question-id").send_keys("4680")
periodPostedS = driver.find_element(By.ID, "edit-qa-submission-date-start").send_keys("01/01/2024")
periodPostedE = driver.find_element(By.ID, "edit-qa-submission-date-end").send_keys("31/01/2024")
publicationS = driver.find_element(By.ID, "edit-qa-final-publishing-date-start").send_keys("01/01/2025")
publicationE = driver.find_element(By.ID, "edit-qa-final-publishing-date-end").send_keys("31/01/2025")
keywords = driver.find_element(By.ID, "edit-keywords").send_keys("LGD")

driver.execute_script("window.scrollBy(0,1500)")
time.sleep(10)

driver.find_element(By.XPATH, "//button[@id='edit-submit-question-answers']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,1500)")
time.sleep(2)
driver.find_element(By.ID, "edit-reset").click()
time.sleep(5)

fields = [
    "edit-qa-question-id",
    "edit-qa-submission-date-start",
    "edit-qa-submission-date-end",
    "edit-qa-final-publishing-date-start",
    "edit-qa-final-publishing-date-end",
    "edit-keywords"
]

for field_id in fields:
    val = driver.find_element(By.ID, field_id).get_property("value")
    assert val == "", f"Field {field_id} not cleared (value was {val})"


val = driver.find_element(By.ID, "edit-qa-legal-act").get_property("value")
assert val == "", f"Legal Act not reset (value was {val})"

val = driver.find_element(By.ID, "edit-qa-answer-source").get_property("value")
assert val == "All", f"Answer Source not reset)"

print("All filters reset correctly")