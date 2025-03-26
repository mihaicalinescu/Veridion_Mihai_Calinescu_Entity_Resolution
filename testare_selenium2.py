class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element('id', 'username')
        self.password = driver.find_element('id', 'password')
        self.login_button = driver.find_element('id', 'login')

    def login(self, user, pwd):
        self.username.send_keys(user)
        self.password.send_keys(user)
        self.login_button.click()

page = LoginPage(driver)
page.login('test', 'pass')
