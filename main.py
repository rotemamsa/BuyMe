from BuyMe import BuyMe_Steps
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/GIT/devopsCourse/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://buyme.co.il/")

#main class to call each buyme step seperatly
#BuyMe_Steps.register(driver)
BuyMe_Steps.home(driver)
BuyMe_Steps.business_screen(driver)
BuyMe_Steps.send_receiver_info(driver)
#BuyMe_Steps.after_Register(driver)

# submit payment
#driver.find_element_by_xpath("//button[@data-toggle='modal']").click()
