from selenium import webdriver

# Inițializare WebDriver pentru Chrome
driver = webdriver.Chrome()

# Deschide Google
driver.get("https://www.google.com")

# Închide browser-ul
driver.quit()
