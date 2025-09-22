

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
Id = "4680"
try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="#accept"]').click()
    print("Cookies accepted")
except:
    print("No cookie banner appeared")
driver.find_element(By.ID, "edit-qa-question-id").send_keys(Id)



driver.execute_script("window.scrollBy(0,1500)")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='edit-submit-question-answers']").click()
results = driver.find_elements(By.CSS_SELECTOR, ".teaser-qa__footer")
if len(results) == 1 and Id in results[0].text:
    print("Found exactly one correct result", Id)
elif len(results) == 0:
    print("No results found")
elif len(results) > 1:
    print(f"Expected 1 result, but found, {len(results)}")
else:
    print("One result found, but it does not match the expected ID")