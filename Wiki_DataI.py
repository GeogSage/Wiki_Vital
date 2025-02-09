"""
GeogSage

Started:
January 18th 2025
Last Updated: February 8th 2025
Time Spent: ~5 hours

For fun: import antigravity
For advice: import this
"""

#'A common mistake that people make when trying to design something completely foolproof
# is to underestimate the ingenuity of complete fools.' -Douglas Adams
print("DON'T PANIC!\n")

#'A beginning is the time for taking the most delicate care that the balances are correct' - Frank Herbert
print('Beginning initialization. . .\n')


# Time to request coffee and pandas.
print('Importing modules. . .')

# import time model to time code
## “Time will not slow down when something unpleasant lies ahead.”
import time

# import requests to access API
import requests as rq

# import json5 to parse javascript
import json5 as j

# importing pandas despite so-called panda diplomacy
import pandas as pd

print('Modules imported.\n')
print('Starting timer')
start = time.time()

print('Setting data paths and workspace. . .\n')

# Wiki URl
wikiURL = "https://en.wikipedia.org/w/api.php"
pageInfo = 'https://xtools.wmcloud.org/api/page/pageinfo/en.wikipedia.org/'
pageLinks = 'https://xtools.wmcloud.org/api/page/links/en.wikipedia.org/'

# The page you're interested in getting data for.
## "Wikipedia:Vital_articles/Level/1", "Wikipedia:Vital_articles/Level/2", "Wikipedia:Vital_articles/Level/3",
## "Wikipedia:Vital_articles/Level/4/People", etc.
vital = "Wikipedia:Vital_articles/Level/3"


# Change this to where you want to save the CSV!!!!1!
## Example: 'C:/Misc/Wiki/RawStats_Vital1.csv'
Out_data = 'A:/Misc/Wiki/RawStats_Vital3.csv'
#### Set your file path above before running####

print('All set!\n')

# Checks the article section. If it is level 1, this variable needs to be 1, otherwise it needs to be 2.
if vital == "Wikipedia:Vital_articles/Level/1":
    section = 1
else:
    section = 2

# Parameters for the Wiki API.
PARAMS = {
    'action': "parse",
    'page': vital,
    'prop': 'links',
    'section': section,
    'format': "json"
}

# Gets page names from the target page using Wiki API.
S = rq.Session()
res = S.get(url=wikiURL, params=PARAMS)
data = res.json()
wikitext = data['parse']['links']


# Creates a list of articles from the target page by parsing wikitext.
## Don't mess with this variable!!1!
articles = [item['*'] for item in wikitext if item.get('ns') == 0 and '*' in item]

# Prints the list of articles for spot checking.
print(articles)

# Target variables from each page.
page_list = {'page': [], 'watchers': [], 'pageviews': [], 'pageviews_offset': [], 'revisions': [], 'editors': [],
             'created_at': [], 'links_ext': [], 'links_out': [], 'links_in': [], 'redirects': []}

# For each article in the list of articles.
for article in articles:

    # prints the article currently being quieried
    print(f'Getting data for "{article}"')

    # Format json
    format = '?format=json'

    # link for page info from the xtools API
    info = f'{pageInfo}{article}{format}'

    # link for link info from the xtools API
    link = f'{pageLinks}{article}{format}'

    # Gets the page info using the xtools API
    r1 = rq.get(info)

    # Gets the link info using the xtools API
    r2 = rq.get(link)

    # parses the returns into text
    genInfo = j.loads(r1.text)
    linkInfo = j.loads(r2.text)

    # Adds general page statistics from return
    page_list['page'].append(genInfo["page"])
    page_list['watchers'].append(genInfo["watchers"])
    page_list['pageviews'].append(genInfo["pageviews"])
    page_list['pageviews_offset'].append(genInfo["pageviews_offset"])
    page_list['revisions'].append(genInfo["revisions"])
    page_list['editors'].append(genInfo["editors"])
    page_list['created_at'].append(genInfo["created_at"])

    # Adds information on page links from return
    page_list['links_ext'].append(linkInfo["links_ext_count"])
    page_list['links_out'].append(linkInfo["links_out_count"])
    page_list['links_in'].append(linkInfo["links_in_count"])
    page_list['redirects'].append(linkInfo["redirects_count"])

    # current run time.
    timer = time.time()
    print(f'Current runtime: {timer-start:0.02f} seconds\n')

# converts page_list dictionary to a dataframe
pagedf = pd.DataFrame.from_dict(page_list, orient='columns')
print(pagedf)

# exports dataframe to CSV
pagedf.to_csv(f'{Out_data}')

end = time.time()
print(f'\n\nRun completed in: {end-start:0.02f} seconds\n\n"The best error message is the one that never shows up."')

#"Everything not saved will be lost." -Nintendo Quit screen
