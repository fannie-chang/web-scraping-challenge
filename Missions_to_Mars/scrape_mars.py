from splinter import Browser
from bs4 import BeautifulSoup as bs 
import time 
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
	executable_path = {'executable_path': ChromeDriverManager().install()}

	browser = Browser('chrome', **executable_path, headless = False)
	url = 'https://mars.nasa.gov/news/'
	browser.visit(url)

	time.sleep(1)

# Latest Mars News 


	html = browser.html
	soup = bs(html,"html.parser")
	news_title = soup.find('div' , class_="content_title").text
print(f"news_title :{news_title}")
news_p = soup.find('div' , class_="article_teaser_body").text
print(f"news_p :{news_p}")


	



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
	html_table = df.to_html()
	html_table.replace('\n', '')
	df.to_html('mars_facts.html', index = False)
	facts_df = df.to_html(classes = 'table table-striped')
	facts_df

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


# Store data in dictionary

	mars_data = {
		"news_title": news_title,
		"news_p": news_p,
		"featured_image_url": featured_image_url,
		"facts_df": facts_df,
		"hemisphere_image_urls": hemisphere_image_urls

		
	}



# Close the browser after scraping
	browser.quit()

# Return results
	return mars_data
