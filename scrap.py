from selenium import webdriver
import pymongo
from pymongo import MongoClient



# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/home/swathi/chromedriver')
#print('hi')

client = MongoClient('mongodb://localhost:27017/')

db = client['job-database']
post = db.desc
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

# company=[]
# location=[]
# company_link = driver.find_elements_by_class_name('job-card__company-name')
# location_link = driver.find_elements_by_class_name('job-card__location')
# title = driver.find_elements_by_class_name('job-card__title-line')
# print(len(title))
# # for i in title:
# # 	print(i.text)
# print(len(company_link))
# print(len(location_link))
# for i in range(len(company_link)):
# 	print(str(company_link[i].text),"  ",str(title[i].text),"  ",str(location_link[i].text))

job_search = driver.find_element_by_id('jobs-search-box-keyword-id-ember45').send_keys('Microsoft')	
job_location = driver.find_element_by_id('jobs-search-box-location-id-ember45').send_keys('Bengaluru')
search_button = driver.find_element_by_css_selector("button.jobs-search-box__submit-button.artdeco-button.artdeco-button--3.ml2").click()
# print(search_button)
# job_location.send_keys(Keys.ENTER)
company = 'Microsoft'
location = 'Bengaluru'
description = []
URL = str('https://www.linkedin.com/jobs/search/?geoId=105214831&keywords='+company+'&location='+location)
driver.get(URL)

result1 = driver.find_elements_by_tag_name('h3')
#print(result[1])
result1[1].click()
first_URL = driver.current_url
#print(first_URL)
driver.get(first_URL)
first_result=driver.find_element_by_id('job-details')
description.append(first_result.text)
#first_result.click()

result2 = driver.find_elements_by_tag_name('h3')

result2[2].click()
second_URL = driver.current_url
#print(first_URL)
driver.get(second_URL)
second_result=driver.find_element_by_id('job-details')
description.append(second_result.text)

#print(driver.find_element_by_id('job-details').text)


# driver.get('https://www.linkedin.com/jobs/search/?currentJobId=1550936659&geoId=105214831&keywords=microsoft&location=Bengaluru%2C%20Karnataka')

# second_result = driver.find_element_by_id('job-details')
# description.append(second_result.text)

for i in range(len(description)):
	print(description[i])
	print('\n\n\n')

for d in range(len(description)):
	post_data = {'Company':company, 'Description':description[d]}
	post.insert_one(post_data)
