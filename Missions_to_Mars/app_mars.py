from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # Mars news------------------------------
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the title
    news_all = soup.find_all('div', class_='list_text')
    news = news_all[0]
    news_title = news.find('div', class_='content_title').find('a').text
    news_p = news.find('div', class_='article_teaser_body').text
    
    # JPL Mars Space Images - Featured Image------------------------
    # name and visit the url for JPL Featured Space Image
    url_mars = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_mars)
    html = browser.html
    soup = bs(html, 'html.parser')
    url = soup.find('a', class_='button fancybox')['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + url

    # Mars Hemispheres Images
    url_ch = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_ch)
    html = browser.html
    soup = bs(html, 'html.parser')
    title_ch = soup.find('h2', class_='title').text
    img_ch = soup.find('div', class_='downloads').find('a')['href']

    url_sh = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_sh)
    html = browser.html
    soup = bs(html, 'html.parser')
    title_sh = soup.find('h2', class_='title').text
    img_sh = soup.find('div', class_='downloads').find('a')['href']

    url_sm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_sm)
    html = browser.html
    soup = bs(html, 'html.parser')
    title_sm = soup.find('h2', class_='title').text
    img_sm = soup.find('div', class_='downloads').find('a')['href']

    url_vm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_vm)
    html = browser.html
    soup = bs(html, 'html.parser')
    title_vm = soup.find('h2', class_='title').text
    img_vm = soup.find('div', class_='downloads').find('a')['href']
    
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    hemisphere_image_urls = [
    {"title":title_ch, "img_url":img_ch},
    {"title":title_sh, "img_url":img_sh},
    {"title":title_sm, "img_url":img_sm},
    {"title":title_vm, "img_url":img_vm},
    ]
   # Store data in a dictionary
    scrape_data = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    
    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return scrape_data