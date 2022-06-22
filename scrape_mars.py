# Dependencies
import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
# set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    #store results in data
    mars_paragraph = mars_news(browser) 
    mars_title = mars_news(browser)
    data = {
        "news_title": mars_title,
        "news_paragraph": mars_paragraph,
        "featured_image": mars_featured(browser),
        "mars_facts": mars_facts(),
        "hemispheres": hemispheres(browser)
        }
    browser.quit()
    return data

   


def mars_news(browser):

     # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    try:
        #find and print title of latest news title
        title = soup.find('div', class_="content_title").get_text()
    
         #find and print the latest paragraph
        title_p = soup.find('div', class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return title, title_p



    
    

def mars_featured(browser):

    # Visit the Featured Space Image site
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    time.sleep(1)
    # Scrape page into Soup
    web = browser.html
    soup_ = bs(web, "html.parser")

    try:

        #Find the image URL for current featured Mars image
        img = soup_.find('img', class_="headerimage fade-in")

        img_link= img['src']
        img_link

    except AttributeError:
        return None

    #Assign the URL to a variable
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'
    return featured_image_url

def mars_facts():
    try:

        #Use pandas to scrape the table containing facts about the planet
        mars_facts = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

      
    #Convert table to html format 
    return mars_facts.to_html(header=False)


def hemispheres(browser): 

    #Use browser to access the webpage
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    # Scrape page into soup
    web = browser.html
    hemispheres = bs(web, 'html.parser')

    # get all the items for hemispheres information
    items = hemispheres.find_all('div', class_='item')

    # 2. Create a list for the images and titles.
    hemisphere_image_urls = []


    _url = "https://astrogeology.usgs.gov/"

    # Use a loop to scrape all the hemisphere information
    for item in items:
        hemisphere = {}
        
        titles = item.find('h3').text
        
        link_ref = item.find('a', class_='itemLink product-item')['href']
    
        
        browser.visit(_url + link_ref)
    
        
        html = browser.html
        img_soup = bs(html, 'html.parser')
        download = img_soup.find('div', class_= 'downloads')
        img_url = download.find('a')['href']
        
        print(titles)
        print(img_url)
        
        # append to list
        hemisphere['img_url'] = img_url
        hemisphere['title'] = titles
        hemisphere_image_urls.append(hemisphere)
        browser.back()

    
        
    # 4. Print the list of each images urls and titles.
    return hemisphere_image_urls


















    


    

    

