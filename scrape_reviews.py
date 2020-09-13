import requests
from bs4 import BeautifulSoup
import yaml

# Get webpage
web_addr = "https://www.healthgrades.com/physician/dr-daniel-gologorsky-y9qfc2z"
page = requests.get(web_addr)

# Scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
comment_items      = soup.find_all('div', class_='c-single-comment__comment')
comment_info_items = soup.find_all('div', class_='c-single-comment__commenter-info')

# Process webpage items
def get_name_date(o): 
	name,date = (span.text for span in o.children)
	name = name.rstrip(" ").rstrip("-").rstrip(" ")
	date = date.rstrip(" ")
	return (name, date)

text_data = list(o.text           for o in comment_items)
name_data = list(get_name_date(o) for o in comment_info_items)

comment_list = [{"name":name, "text":text, "date":date} for text, (name,date) in zip(text_data, name_data)]

# Write comment data to file
with open('_data/scraped_reviews.yml', 'w') as f:
   #data = yaml.dump(comment_list, f)
   stream = yaml.dump(comment_list, default_flow_style = False)
   f.write(stream.replace('\n- ', '\n\n- '))

# print(len(comment_items))
# print(len(comment_info_items))

# for i in range(len(comment_info_items)):
# 	print(f"Comment {i}")
# 	print(comment_items[i].prettify())
# 	print(comment_info_items[i].prettify())
