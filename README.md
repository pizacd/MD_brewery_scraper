# Maryland Craft Beer Scraping project

<p>As a craft beer enthusiast, there are many outstanding breweries within the state of Maryland to visit.
  I follow many of them on social media to learn when new beers are released. However, staying on top of new releases requires scrolling through multiple accounts and posts
which can be tedious.</p>
<p>Therefore, I used my Data Scientist skills by building a web scraper to crawl the pages of different breweries and write rows of beers to a database.
This way, I can make faster decisions about which breweries to visit and which beers to try.</p>

## Database Used
#### AWS DynamoDB
<p>Most of my data science work uses relational databases, so I wanted to practice working with NoSQL databases.
A schemaless database also made better sense given my use case because not all breweries provide the same information about
their products (e.g. description).</p>

## Python 3.10.11
<p>This version of Python had the packages and dependencies I needed to complete the project.</p>


## Packages Used
#### Boto3
<p>AWS package for interacting with DynamoDB.</p>

#### Selenium
<p>Web scraping package. I chose Selenium over Scrapy or BeautifulSoup because of the need to 
interact with the web page. Since these products contain alcohol, breweries require confirmation of 
age by clicking a button to acknowledge they are age 21+.</p>
