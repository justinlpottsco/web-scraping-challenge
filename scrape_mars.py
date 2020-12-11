#!/usr/bin/env python
# coding: utf-8

# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


# Setup splinter (day2ex7)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Scrape NASA site
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[5]:


# Parse HTML with Beautiful Soup    
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


# Retrieve latest news title
most_recent_article = soup.find('li', class_ = 'slide')
news_title = most_recent_article.find('h3').get_text()
print(news_title)


# In[7]:


# Retrieve latest paragraph text
news_p = most_recent_article.find('div', class_ = 'rollover_description_inner').get_text()
print(news_p)


# In[8]:


# Visit the url for JPL Featured Space Image
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)


# In[9]:


# Find full size image url for current Featured Mars Image
full_image = browser.find_by_id('full_image')
full_image.click()

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

main_url = 'https://www.jpl.nasa.gov/'
image_url = soup.find('a', class_ = 'button fancybox')['data-fancybox-href']

featured_image_url =  main_url + image_url

print(featured_image_url)


# In[10]:


# Visit Mars facts url 
facts_url = 'https://space-facts.com/mars/'

fact_table = pd.read_html(facts_url)[0]
fact_table = fact_table.set_index(0)
fact_table.rename(columns = {
    1: ""
}).rename_axis(index = {0:""})


# In[11]:


#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)


# In[12]:


# Parse HTML with Beautiful Soup    
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[13]:


#You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
#Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
#Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# Create the dictionaries
hemispheres_image_urls = []

# Main image url
mainimg_url = 'https://astrogeology.usgs.gov/'

hemispheres = soup.find_all('div', class_ = 'item')

# Loop for titles & url
for hemi in hemispheres:
    title = hemi.find('h3').text
    
    browser.click_link_by_partial_text('Hemisphere Enhanced')
    img_html = browser.html
    img_soup = BeautifulSoup(img_html, 'html.parser')
    imgs_url = img_soup.find('img', class_ = 'wide-image')['src']
    
    image_url = mainimg_url + imgs_url
    hemispheres_image_urls.append({'title': title, 'img_url': image_url})

print(hemispheres_image_urls)


# In[ ]:

