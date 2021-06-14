from splinter import Browser
from bs4 import BeautifulSoup  
import time 
import requests
import pymongo
from splinter import Browser
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager


def scrape():
	# browser = init_browser()
	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless = False)
	
	time.sleep(1)
	

# Latest Mars News 

	url = "https://redplanetscience.com/"
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	news_title = soup.find('div' , class_="content_title").text

	news_p = soup.find('div' , class_="article_teaser_body").text
	

# Featured Mars Image

	url = 'https://spaceimages-mars.com/'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	images = soup.find('a', class_='fancybox-thumbs')['href']
	featured_image_url = url + images
	

# Mars Facts

	url = 'https://galaxyfacts-mars.com'
	tables = pd.read_html(url)
	df = tables[0]
	df.columns = [ 'Description','Mars', 'Earth']
	table_df = df.set_index('Description' )
	facts_df = table_df.to_html(classes = 'table table-striped')

	

# Mars Hemispheres   

	url = 'https://marshemispheres.com/'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	hemispheres = soup.find_all('div', class_='item')
	hemisphere_image_urls = []

	for h in hemispheres:
	    img_title = h.find('h3').text
	    img_pic = h.find('img', class_='thumb')['src']
	    hemisphere_image_urls.append({"title": img_title, "img_url":f" {url}{img_pic}"})
	    print(hemisphere_image_urls)
	Cerberus_title = hemisphere_image_urls[0]['title']
	Cerberus_img= hemisphere_image_urls[0]['img_url']

	Schiaparelli_title = hemisphere_image_urls[1]['title']
	Schiaparelli_img= hemisphere_image_urls[1]['img_url']

	Syrtis_title = hemisphere_image_urls[2]['title']
	Syrtis_img = hemisphere_image_urls[2]['img_url']

	Valles_title = hemisphere_image_urls[3]['title']
	Valles_img = hemisphere_image_urls[3]['img_url']
	    

		 


	


# Store data in dictionary

	mars_data = {
		"news_title": news_title,
		"news_p": news_p,
		"featured_image_url": featured_image_url,
		"facts_df": facts_df,
		"Cerberus_title": Cerberus_title,
		"Cerberus_img" : Cerberus_img,
		"Schiaparelli_title" :Schiaparelli_title,
		"Schiaparelli_img":Schiaparelli_img,
		"Syrtis_title":Syrtis_title,
		"Syrtis_img":Syrtis_img,
		"Valles_title":Valles_title,
		"Valles_img":Valles_img

				
	}



# Close the browser after scraping
	browser.quit()

# Return results
	return mars_data
