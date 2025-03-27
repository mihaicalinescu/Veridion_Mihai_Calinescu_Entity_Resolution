from selenium import webdriver

driver = webdriver.Chrome()  # Inițializare Chrome
driver.get("https://www.google.com")  # Deschide Google
print(driver.title)  # Afișează titlul paginii
driver.quit()  # Închide browser-ul