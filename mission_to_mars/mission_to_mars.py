{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "73c70b5c-7965-4674-93e9-e27d1186194b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13338f2a-463f-472e-84db-1ebe8bef8137",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "INFO:WDM:====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 102.0.5005\n",
      "INFO:WDM:Current google-chrome version is 102.0.5005\n",
      "[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "INFO:WDM:Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "[WDM] - Driver [/Users/anthonygarcia/.wdm/drivers/chromedriver/mac64/102.0.5005.61/chromedriver] found in cache\n",
      "INFO:WDM:Driver [/Users/anthonygarcia/.wdm/drivers/chromedriver/mac64/102.0.5005.61/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "# set up splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c579e130-872a-494d-b987-650d4297496d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "996578b1-dc56-486d-a65c-2d2c8440ad77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "12307ee5-8589-4f81-b482-f33393896403",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's MAVEN Maps Winds in the Martian Upper Atmosphere that Mirror the Terrain Below and Gives Clues to Martian Climate\""
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find and print title of latest news title\n",
    "title = soup.find('div', class_=\"content_title\").get_text()\n",
    "title\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cb26586b-595a-463b-b675-7954bcf1e45c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Researchers have created the first map of wind circulation in the upper atmosphere of a planet besides Earth, using data from NASA’s MAVEN spacecraft that were collected during the last two years.'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find and print the latest paragraph\n",
    "title_p = soup.find('div', class_=\"article_teaser_body\").get_text()\n",
    "title_p\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "736ce0ed-edc0-4f62-94d7-e2b4bb153b62",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Assign the text to variables\n",
    "title = 'NASA Moves Forward With Campaign to Return Mars Samples to Earth'\n",
    "title_p = 'During this next phase, the program will mature critical technologies and make critical design decisions as well as assess industry partnerships.'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01887fbd-6caa-47a7-835e-db18e9e0e176",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e188439b-7830-4555-920b-6739ed7f9a18",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2ad96f0c-db30-4289-91bf-15578292a2e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Featured Space Image site\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)\n",
    "\n",
    "# Scrape page into Soup\n",
    "web = browser.html\n",
    "soup_ = bs(web, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d31cea2b-5c8a-49ff-b848-12878b5556cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find the image URL for current featured Mars image\n",
    "img = soup_.find('img', class_=\"headerimage fade-in\")\n",
    "\n",
    "img_link= img['src']\n",
    "img_link"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "870cf8c7-4ccc-4946-b131-a1972bd104fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Assign the URL to a variable\n",
    "\n",
    "featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01826e82-0f42-4199-be4b-98d45be305a1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdd63f03-5676-4355-b7a3-5e6501df6a96",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c40ce32f-d749-4409-8d98-f3560bcdd318",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5          Length of Year:   687 Earth days      365.24 days\n",
       "6             Temperature:     -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use pandas to scrape the table containing facts about the planet\n",
    "mars_facts = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "mars_facts\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5e72831c-ec1b-47fe-a903-39c953a8b56b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.to_html of                          0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5          Length of Year:   687 Earth days      365.24 days\n",
       "6             Temperature:     -87 to -5 °C      -88 to 58°C>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use pandas to convert the data to an HTML table string\n",
    "mars_facts.to_html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79a9bff5-e387-4183-9c4c-8008897c163b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "dde2f7b8-ec22-4b99-9b23-b9085287a958",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use browser to access the webpage\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "\n",
    "# scrape page into soup\n",
    "web = browser.html\n",
    "hemispheres = bs(web, 'html.parser')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ddde56ed-f8fc-4ac6-80cd-eac4f4bbed06",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get all the items for hemispheres information\n",
    "items = hemispheres.find_all('div', class_='item')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8eb465ca-9dce-4d43-8cbb-b1156701d90b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list for the images and titles.\n",
    "hemisphere_image_urls = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "50325500-069e-4e38-87ac-bc9cb7fcdd30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "_url = \"https://astrogeology.usgs.gov/\"\n",
    "\n",
    "# Use a loop to scrape all hemisphere information\n",
    "for item in items:\n",
    "    hemisphere = {}\n",
    "    \n",
    "    titles = item.find('h3').text\n",
    "    \n",
    "    \n",
    "    link_ref = item.find('a', class_='itemLink product-item')['href']\n",
    "   \n",
    "    \n",
    "    browser.visit(_url + link_ref)\n",
    "   \n",
    "    \n",
    "    html = browser.html\n",
    "    img_soup = bs(html, 'html.parser')\n",
    "    download = img_soup.find('div', class_= 'downloads')\n",
    "    img_url = download.find('a')['href']\n",
    "    \n",
    "    print(titles)\n",
    "    print(img_url)\n",
    "    \n",
    "    # append to list\n",
    "    hemisphere['img_url'] = img_url\n",
    "    hemisphere['title'] = titles\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bfd34e46-0bcd-465c-9795-b8f80d92d00d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the list of each images urls and titles \n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "13b0687c-5e3e-4c6c-b6ff-2a00791df039",
   "metadata": {},
   "outputs": [],
   "source": [
    "#close browser after scraping\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb60178c-ae50-49bc-9886-4a6dd7b4a4e3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6138ef4a-d08d-4ddd-bf2f-1f2923f434b3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e50b1d1a-9722-40d1-8dee-9ad74e86e7dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86093ce2-deda-4ac6-935a-5aa05ab85b97",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c22a0e80-e2a4-48bf-b55d-f1f7f984173f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa9b817d-7d65-4c80-ba2f-d22fab75f88c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c44f428-705d-4e45-aae0-0c28cf4740b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51c2807c-3c29-4e49-a2f3-bb277b42e623",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
