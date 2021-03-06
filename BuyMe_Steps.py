import time
import random

from selenium.webdriver.common.keys import Keys

def after_Register(driver):
    toregister = driver.find_element_by_xpath("//span[@data-ember-action='1698']")
    toregister.click()
    # find & fill first name
    first_name = driver.find_element_by_id("ember1717")
    first_name.clear()
    first_name.send_keys("RRR")
    # find & fill email
    email = driver.find_element_by_id("ember1719")
    email.clear()
    r=random.randint(0, 300)
    email.send_keys("rrt"+r+"@gg.com")
    # find & fill password
    password = driver.find_element_by_id("valPass")
    password.clear()
    password.send_keys("Rr12345678")
    # find & fill password verification
    passwordvf = driver.find_element_by_id("ember1723")
    passwordvf.clear()
    passwordvf.send_keys("Rr12345678")
    passwordvf.send_keys(Keys.TAB)

    # go to agree radio button
    iagree = driver.find_element_by_id("ember1724-id")
    iagree.send_keys(Keys.SPACE)

    # register
    send = driver.find_element_by_class_name("ui-btn")
    send.send_keys(Keys.ENTER)



def register(driver):

    register=driver.find_element_by_xpath("//li[@data-ember-action='636']")
    register.click()

    toregister = driver.find_element_by_xpath("//span[@data-ember-action='994']")
    toregister.click()
    #find & fill first name
    first_name = driver.find_element_by_id("ember1019")
    first_name.clear()
    first_name.send_keys("RRR")
    # find & fill email
    email = driver.find_element_by_id("ember1021")
    email.clear()
    r = random.randint(0, 300)
    email.send_keys("tttr" + str(r) + "@gg.com")
    # find & fill password
    password = driver.find_element_by_id("valPass")
    password.clear()
    password.send_keys("Rr12345678")
    # find & fill password verification
    passwordvf = driver.find_element_by_id("ember1025")
    passwordvf.clear()
    passwordvf.send_keys("Rr12345678")
    passwordvf.send_keys(Keys.TAB)

    #go to agree radio button
    iagree=driver.find_element_by_id("ember1026-id")
    iagree.send_keys(Keys.SPACE)

    #register
    send=driver.find_element_by_class_name("ui-btn")
    send.send_keys(Keys.ENTER)
    time.sleep(5)

def home(driver):
    #select price
    selectdropdownprice=driver.find_element_by_id("ember664_chosen")
    selectdropdownprice.click()
    selectprice= driver.find_element_by_xpath("//li[@data-option-array-index='1']")
    selectprice.click()

    #select Area
    selectdropdownarea=driver.find_element_by_id("ember679_chosen")
    selectdropdownarea.click()
    selectarea= driver.find_element_by_xpath("//li[@data-option-array-index='1']")
    selectarea.click()

    #select catagory
    selectdropdowncatagory=driver.find_element_by_id("ember688_chosen")
    selectdropdowncatagory.click()
    selectcatagory= driver.find_element_by_xpath("//li[@data-option-array-index='2']")
    selectcatagory.click()

    #find me a gift card
    findme= driver.find_element_by_xpath("//a[@href='https://buyme.co.il/search?budget=1&category=16&region=13']")
    #findme=driver.find_element_by_id("ember723")
    findme.click()
    time.sleep(5)

def business_screen(driver):
    # select gift
    selectcatagory= driver.find_element_by_xpath("//div[@data-ember-action='1175']")
    selectcatagory.click()
    # type price and send
    typeprice= driver.find_element_by_xpath("//input[@data-parsley-type='number']")
    typeprice.send_keys("99")
    typeprice.send_keys(Keys.ENTER)

def send_receiver_info(driver):
    #gift reciver name
    giftfor= driver.find_element_by_xpath("//input[@data-parsley-required-message='מי הזוכה המאושר? יש להשלים את שם המקבל/ת']")
    giftfor.send_keys("Tom")

    #gift from name
    giftby= driver.find_element_by_xpath("//input[@data-parsley-required-message='למי יגידו תודה? שכחת למלא את השם שלך']")
    giftby.send_keys("Rotem")

    #blessing
    blessing= driver.find_element_by_xpath("//textarea[@data-parsley-group='main']")
    blessing.send_keys("happy birthday!")

    # enter a picture
    pictureupload= driver.find_element_by_xpath("//input[@name='fileUpload']")
    pictureupload.send_keys("c:\happy.jpg")

    #select event
    #selectdropdownevent = driver.find_elements_by_id("ember1324_chosen")
    selectdropdownevent= driver.find_element_by_xpath("//div[@id='ember1324_chosen']")
    selectdropdownevent.click()
    selectevent = driver.find_element_by_xpath("//li[@data-option-array-index='2']")
    selectevent.click()

    #radio button after payment
    #radioafter = driver.find_element_by_class_name("send-now")
    #radioafter.send_keys(Keys.SPACE)

    #pick email option
    emailpic=driver.find_element_by_class_name("icon-envelope")
    emailpic.click()

    #enter email

    emailtext= driver.find_element_by_xpath("//input[@placeholder='כתובת המייל של מקבל/ת המתנה']")
    emailtext.send_keys("rotem@gmail.com")
    emailtext.send_keys(Keys.ENTER)

    #submit
    driver.find_element_by_xpath("//button[@type='submit']").click()
