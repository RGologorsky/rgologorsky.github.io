import requests
from bs4 import BeautifulSoup
import yaml

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time

# svg https://deeditor.com/

#launch url
url = "https://www.healthgrades.com/physician/dr-daniel-gologorsky-y9qfc2z/comments"

# create a new Crhome session
driver = webdriver.Chrome("/Users/rachelgologorsky/Documents/Git/chromedriver")
driver.implicitly_wait(10)
driver.get(url)
time.sleep(10)

# Load all reviews
done = True
wait_time = 0.3

while not done:
	try:
		comments = driver.find_elements_by_class_name('c-single-comment')
		last_comment = comments[-1]
		driver.execute_script("arguments[0].scrollIntoView();", last_comment)
		#print("Scrolled")
		time.sleep(wait_time)

		show_more_link = driver.find_element_by_class_name('c-comment-list__show-more')
		driver.execute_script("arguments[0].click();", show_more_link)
		#print("Clicked")
		time.sleep(wait_time)
	except:
		done = True
		#print("Done")
		time.sleep(wait_time)

# Clikc on more details (if comments folded)
# more_details = driver.find_elements_by_class_name('c-single-comment__more-details')
# print(len(more_details))
# for o in more_details:
# 	driver.execute_script("arguments[0].scrollIntoView();", o)
# 	time.sleep(wait_time)
# 	driver.execute_script("arguments[0].click();", o)
# 	print("Clicked more details")

# Give page to Beautiful Soup to parse
soup = BeautifulSoup(driver.page_source)
#soup = BeautifulSoup(page.content, 'html.parser')

# Scrape webpage
comment_items      = soup.find_all('div', class_='c-single-comment__comment')
comment_info_items = soup.find_all('div', class_='c-single-comment__commenter-info')
comment_stars      = soup.find_all('div', class_='c-single-comment__stars')

print(comment_stars[0].children)
print(len(comment_items), len(comment_info_items), len(comment_stars))

# Process webpage items
def get_name_date(o): 
	name,date = (span.text.rstrip(" ") for span in o.children)
	if len(name) == 0: name = "Anonymous"
	else:              name = name.rstrip("\u2013").rstrip(" ")
	return (name, date)

text_data = list(o.text           for o in comment_items)
name_data = list(get_name_date(o) for o in comment_info_items)

comment_list = [{"name":name, "text":text, "date":date} for text, (name,date) in zip(text_data, name_data)]

# Write comment data to file
with open('_data/scraped_reviews.yml', 'w') as f:
   #data = yaml.dump(comment_list, f)
   stream = yaml.dump(comment_list, default_flow_style = False)
   f.write(stream.replace('\n- ', '\n\n- '))
