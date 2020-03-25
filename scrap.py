from selenium import webdriver


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/home/swathi/chromedriver')
#print('hi')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

# locate email form by_class_name
username = driver.find_element_by_name('session_key').send_keys('swathishivakumar317@gmail.com')


# send_keys() to simulate key strokes
#username.send_keys('swathishivakumar317@gmail.com')

# # locate password form by_class_name
password = driver.find_element_by_name('session_password').send_keys("31#07#98")

# # send_keys() to simulate key strokes
# password.send_keys('31#07#98')

# # locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('login__form_action_container ')

# # locate submit button by_class_id
# log_in_button = driver.find_element_by_class_id('login submit-button')

# # locate submit button by_xpath
# log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# # .click() to mimic button click
log_in_button.click()

jobs_button = driver.find_element_by_id('jobs-nav-item')
jobs_button.click()

driver.get('https://www.linkedin.com/jobs/')

company=[]
location=[]
company_link = driver.find_elements_by_class_name('job-card__company-name')
location_link = driver.find_elements_by_class_name('job-card__location')
title = driver.find_elements_by_class_name('job-card__title-line')
print(len(title))
# for i in title:
# 	print(i.text)
print(len(company_link))
print(len(location_link))
for i in range(len(company_link)):
	print(str(company_link[i].text),"  ",str(title[i].text),"  ",str(location_link[i].text))
	