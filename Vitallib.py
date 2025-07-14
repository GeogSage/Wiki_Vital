"""
GeogSage

Started:
January 18th 2025
Last Updated: May 20th 2025
Time Spent: ~25 hours

For fun: import antigravity
For advice: import this
"""

# import time model to time code
## “Time will not slow down when something unpleasant lies ahead.”
import time

# import requests to access API
import requests as rq

# import json5 to parse javascript
import json5 as j

import numpy as np

# importing pandas despite so-called panda diplomacy
import pandas as pd

if __name__ == '__main__':

    #'A common mistake that people make when trying to design something completely foolproof
    # is to underestimate the ingenuity of complete fools.' -Douglas Adams
    print("DON'T PANIC!\n")

    print('This is a library, take your queries somewhere else!\n')

# The page you're interested in getting data for.
## "Wikipedia:Vital_articles/Level/1", "Wikipedia:Vital_articles/Level/2", "Wikipedia:Vital_articles/Level/3",
## "Wikipedia:Vital_articles/Level/4/People", etc.
#vital = "Wikipedia:Vital_articles/Level/3"

# Returns either a list of variables or a dictionary of quotas at level 5. For URL, input 'URL', for quota, input 'quota'
# It's a hardcode life for us.
def vitalPageList(var):

    if var == 'level':
        return ['1', '2', '3', '4', '5']

    if var == 'level4':
        return [
            '/People',
            '/History',
            '/Geography',
            '/Arts',
            '/Philosophy_and_religion',
            '/Everyday_life',
            '/Society_and_social_sciences',
            '/Biology_and_health_sciences',
            '/Physical_sciences',
            '/Technology',
            '/Mathematics',
               ]

    if var == 'level5':
        return [
            '/People/Writers_and_journalists',
            '/People/Artists,_musicians,_and_composers',
            '/People/Entertainers,_directors,_producers,_and_screenwriters',
            '/People/Philosophers,_historians,_political_and_social_scientists',
            '/People/Religious_figures',
            '/People/Politicians_and_leaders',
            '/People/Military_personnel,_revolutionaries,_and_activists',
            '/People/Scientists,_inventors,_and_mathematicians',
            '/People/Sports_figures',
            '/People/Miscellaneous',
            '/History',
            '/Geography/Physical',
            '/Geography/Countries',
            '/Geography/Cities',
            '/Arts',
            '/Philosophy_and_religion',
            '/Everyday_life',
            '/Everyday_life/Sports,_games_and_recreation',
            '/Society_and_social_sciences/Social_studies',
            '/Society_and_social_sciences/Politics_and_economics',
            '/Society_and_social_sciences/Culture',
            '/Biology_and_health_sciences/Animals',
            '/Biology_and_health_sciences/Biology',
            '/Biology_and_health_sciences/Health',
            '/Biology_and_health_sciences/Plants',
            '/Physical_sciences/Basics_and_measurement',
            '/Physical_sciences/Astronomy',
            '/Physical_sciences/Chemistry',
            '/Physical_sciences/Earth_science',
            '/Physical_sciences/Physics',
            '/Technology',
            '/Mathematics']

    if var == 'URL':
        return [
                '1', '2', '3', '4/People', '4/History', '4/Geography', '4/Arts', '4/Philosophy_and_religion',
              '4/Everyday_life', '4/Society_and_social_sciences', '4/Biology_and_health_sciences',
              '4/Physical_sciences',
              '4/Technology', '4/Mathematics', '5/People/Writers_and_journalists',
              '5/People/Artists,_musicians,_and_composers',
              '5/People/Entertainers,_directors,_producers,_and_screenwriters',
              '5/People/Philosophers,_historians,_political_and_social_scientists', '5/People/Religious_figures',
              '5/People/Politicians_and_leaders', '5/People/Military_personnel,_revolutionaries,_and_activists',
              '5/People/Scientists,_inventors,_and_mathematicians', '5/People/Sports_figures', '5/People/Miscellaneous',
              '5/History', '5/Geography/Physical', '5/Geography/Countries', '5/Geography/Cities', '5/Arts',
              '5/Philosophy_and_religion', '5/Everyday_life', '5/Everyday_life/Sports,_games_and_recreation',
              '5/Society_and_social_sciences/Social_studies', '5/Society_and_social_sciences/Politics_and_economics',
              '5/Society_and_social_sciences/Culture', '5/Biology_and_health_sciences/Animals',
              '5/Biology_and_health_sciences/Biology', '5/Biology_and_health_sciences/Health',
              '5/Biology_and_health_sciences/Plants', '5/Physical_sciences/Basics_and_measurement',
              '5/Physical_sciences/Astronomy', '5/Physical_sciences/Chemistry', '5/Physical_sciences/Earth_science',
              '5/Physical_sciences/Physics', '5/Technology', '5/Mathematics'
                ]

    if var == 'subpage':
        return{
            '5/People/Writers_and_journalists': "Writers and journalists",
            '5/People/Artists,_musicians,_and_composers': "Artists, musicians, and composers",
            '5/People/Entertainers,_directors,_producers,_and_screenwriters': "Entertainers, directors, producers, and screenwriters",
            '5/People/Philosophers,_historians,_political_and_social_scientists': "Philosophers, historians, and social scientists",
            '5/People/Religious_figures': "Religious figures",
            '5/People/Politicians_and_leaders':"Politicians and leaders",
            '5/People/Military_personnel,_revolutionaries,_and_activists': "Military personnel, revolutionaries, and activists",
            '5/People/Scientists,_inventors,_and_mathematicians': "Scientists, inventors, and mathematicians",
            '5/People/Sports_figures': "Sports figures",
            '5/People/Miscellaneous': "Miscellaneous",
            '5/History': "History",
            '5/Geography/Physical': "Physical geography",
            '5/Geography/Countries': "Countries and subdivisions",
            '5/Geography/Cities': "Cities",
            '5/Arts': "Arts",
            '5/Philosophy_and_religion': "Philosophy and religion",
            '5/Everyday_life': "Everyday life",
            '5/Everyday_life/Sports,_games_and_recreation': "Sports, games and recreation",
            '5/Society_and_social_sciences/Social_studies': "Social studies",
            '5/Society_and_social_sciences/Politics_and_economics': "Politics and economics",
            '5/Society_and_social_sciences/Culture': "Culture",
            '5/Biology_and_health_sciences/Animals': "Animals",
            '5/Biology_and_health_sciences/Biology': "Biology, biochemistry, anatomy, and physiology",
            '5/Biology_and_health_sciences/Health': "Health, medicine, and disease",
            '5/Biology_and_health_sciences/Plants': "Plants, fungi, and other organisms",
            '5/Physical_sciences/Basics_and_measurement': "Basics and measurement",
            '5/Physical_sciences/Astronomy': "Astronomy",
            '5/Physical_sciences/Chemistry': "Chemistry",
            '5/Physical_sciences/Earth_science': "Earth science",
            '5/Physical_sciences/Physics': "Physics",
            '5/Technology': "Technology",
            '5/Mathematics': "Mathematics"
            }

    if var == 'quota':
        return {
            "Writers and journalists": [2000, 15100],
            "Artists, musicians, and composers": [2200, 15100],
            "Entertainers, directors, producers, and screenwriters": [2200, 15100],
            "Philosophers, historians, and social scientists": [1400, 15100],
            "Religious figures": [500, 15100],
            "Politicians and leaders": [2400, 15100],
            "Military personnel, revolutionaries, and activists": [900, 15100],
            "Scientists, inventors, and mathematicians": [1300, 15100],
            "Sports figures": [1100, 15100],
            "Miscellaneous": [1100, 15100],
            "History": [3300, 3300],
            "Physical geography": [1900, 5200],
            "Countries and subdivisions": [1300, 5200],
            "Cities": [2000, 5200],
            "Arts": [3700, 3700],
            "Philosophy and religion": [1400, 1400],
            "Everyday life": [1300, 2500],
            "Sports, games and recreation": [1200, 2500],
            "Social studies": [500, 4000],
            "Politics and economics": [1900, 4000],
            "Culture": [1600, 4000],
            "Biology, biochemistry, anatomy, and physiology": [1100, 5600],
            "Animals": [2400, 5600],
            "Plants, fungi, and other organisms": [1000, 5600],
            "Health, medicine, and disease": [1100, 5600],
            "Basics and measurement": [300, 4800],
            "Astronomy": [900, 4800],
            "Chemistry": [1200, 4800],
            "Earth science": [1200, 4800],
            "Physics": [1200, 4800],
            "Technology": [3200, 3200],
            "Mathematics": [1200, 1200]
            }
    else:
        print('This function requires an input. \n'
              'Input "URL" for the vital article URLs, or "quota" for the level 5 quota.')

# Parameters for creating the Vital Article master list for query
def VitalParams(level, section):

    # Wiki URl
    wikiURL = "https://en.wikipedia.org/w/api.php"

    # Parameters for the Wiki API.
    PARAMS = {
        'action': "parse",
        'page': level,
        'prop': "links",
        'section': section,
        'format': "json"
    }

    # Gets page names from the target page using Wiki API.
    headers = {'User-Agent': 'VitalBot/0.0 (https://github.com/GeogSage/Wiki_Vital/)'}
    S = rq.Session()
    res = S.get(url=wikiURL, params=PARAMS, headers=headers)
    data = res.json()

    # Error handling
    if 'parse' not in data:
        print(f"Error: 'parse' not in response for level {level}. Response was: {data}")


    wikitext = data['parse']['links']

    # Creates a list of articles from the target page by parsing wikitext.
    ## Don't mess with this variable!!1!
    article = [item['*'] for item in wikitext if item.get('ns') == 0 and '*' in item]

    return article

# Function to get article information from Xtools API
def xtools_api(page, url):
    # Headers
    headers = {'User-Agent': 'VitalBot/0.0 (https://github.com/GeogSage/Wiki_Vital/)'}

    # Format json
    format = '?format=json'

    # link for page info from the xtools API
    info = f'{url}{page}{format}'

    # Gets the page info using the xtools API
    r = rq.get(url=info, headers=headers)

    # parses the returns into text
    text = j.loads(r.text)

    return text

# Function to get QID from for an article using Wiki API
def wiki_api_qid(page, url):
        # Parameters to get page information from Wiki API
        headers = {'User-Agent': 'VitalBot/0.0 (https://github.com/GeogSage/Wiki_Vital/)'}
        params = {
            "action": "query",
            "titles": page,
            "prop": "pageprops",
            "format": "json"
        }

        S = rq.Session()
        r = S.get(url=url, params=params, headers=headers).json()
        pageid = next(iter(r["query"]["pages"]))
        qid = r["query"]["pages"][pageid]["pageprops"]["wikibase_item"]
        return qid

# Function to get total number of site links for an article using Wiki API. Requires article QID
def wiki_api_sitelinks(qid):

        # Fetch Wikidata entity data
        wikidata_url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
        data = rq.get(wikidata_url).json()

        entity = data["entities"][qid]
        sitelinks = entity.get("sitelinks", {})
        l = len(sitelinks)
        return l

# Function to get Total number of language links for an article using Wiki API
def wiki_api_languagelinks(page, url):
    headers = {'User-Agent': 'VitalBot/0.0 (https://github.com/GeogSage/Wiki_Vital/)'}
    # Parameters to get language links from Wiki API
    params = {
        'action': "parse",
        'page': page,
        'prop': "langlinks",
        'format': "json"
    }

    S = rq.Session()
    # Gets language links
    ll = []
    r = S.get(url=url, params=params, headers=headers)
    data = r.json()

    parse = data['parse']['langlinks']
    for language in parse:
        ll.append(language)

    num_ll = len(ll)

    return num_ll


# takes a list of values corresponding to the vital article levels
def WikiVitalList(vital, out_CSV=None):
    start = time.time()

    # Dictionary of article names and their vital level
    articles = {'Article': [], 'Vital_Level': []}
    stats = {'Article': [], 'Vital_Category': [], 'Level_Quota': [], 'SubPage_Quota': []}

    for v in vital:
        print(f'Getting pages at level {v}\n')
        # Checks the article section.
        # If it is level 1, section needs to be 1,
        if v == '1':
            level = f"Wikipedia:Vital_articles/Level/{v}"
            section = 1
            article = VitalParams(level, section)
            for a in article:
                articles['Article'].append(a)
                articles['Vital_Level'].append(v)
                # Prints the list of articles for spot checking.

        # If it is level 2, section needs to be 2
        elif v == '2':
            level = f"Wikipedia:Vital_articles/Level/{v}"
            section = 2
            article = VitalParams(level, section)
            for a in article:
                if a in articles['Article']:
                    continue
                else:
                    articles['Article'].append(a)
                    articles['Vital_Level'].append(v)
                    # Prints the list of articles for spot checking.

        # If it is level 3, section needs to be 2
        elif v == '3':
            level = f"Wikipedia:Vital_articles/Level/{v}"
            section = 2
            article = VitalParams(level, section)
            for a in article:
                if a in articles['Article']:
                    continue
                else:
                    articles['Article'].append(a)
                    articles['Vital_Level'].append(v)
                    # Prints the list of articles for spot checking.

        # else, section needs to be 1
        elif v == '4':
            subPage = vitalPageList('level4')
            section = 1
            for s in subPage:
                sub = f'{v}{s}'
                level = f"Wikipedia:Vital_articles/Level/{sub}"
                print(f'Getting pages at subpage from {sub}\n')
                article = VitalParams(level, section)
                for a in article:
                    if a in articles['Article']:
                        continue
                    else:
                        articles['Article'].append(a)
                        articles['Vital_Level'].append(v)
                        # Prints the list of articles for spot checking.

        elif v == '5':
            subPage = vitalPageList('level5')
            section = 1
            for s in subPage:
                sub = f'{v}{s}'
                level = f"Wikipedia:Vital_articles/Level/{sub}"
                article = VitalParams(level, section)
                print(f'Getting pages at subpage from {sub}\n')
                for a in article:
                    h = vitalPageList('subpage')
                    q = vitalPageList('quota')
                    cat = h[sub]
                    key = q[cat]
                    lq = key[1]
                    subq = key[0]
                    stats['Article'].append(a)
                    stats['Vital_Category'].append(cat)
                    stats['Level_Quota'].append(lq)
                    stats['SubPage_Quota'].append(subq)
                    if a in articles['Article']:
                        continue
                    else:
                        articles['Article'].append(a)
                        articles['Vital_Level'].append(v)
                        # Prints the list of articles for spot checking.
    for key, value in articles.items():
        print(f" Vital articles scanned, values for each variable:\n {key} : {len(value)}")

    art_df = pd.DataFrame(articles)
    stat_df = pd.DataFrame(stats)
    merged_df = art_df.merge(stat_df, left_on='Article', right_on='Article')

    if out_CSV is None:
        return merged_df
    else:
        merged_df.to_csv(f'{out_CSV}', index=False)

def VitalStats(in_CSV, out_CSV, temp=None):
    start = time.time()
    # Gets page names from the target page using Wiki API.
    wiki_url = f"https://en.wikipedia.org/w/api.php"
    pageInfo = 'https://xtools.wmcloud.org/api/page/pageinfo/en.wikipedia.org/'
    pageLinks = 'https://xtools.wmcloud.org/api/page/links/en.wikipedia.org/'


    page_list = {'Article': [], 'Vital_Level': [], 'Vital_Category': [], 'Level_Quota': [], 'SubPage_Quota': [],
                 'watchers': [], 'pageviews': [], 'pageviews_offset': [], 'revisions': [], 'editors': [],
                 'created_at': [], 'links_ext': [], 'links_out': [], 'links_in': [], 'redirects': [], 'Site_links': [],
                 'Language_Links': [], 'Qid': []}

    # Load CSV into a DataFrame
    df = pd.read_csv(in_CSV)

    # Iterate over DataFrame rows
    count = 0
    for index, row in df.iterrows():

        # variables in dataframe
        a = row['Article']
        v = row['Vital_Level']
        vc = row['Vital_Category']
        lq = row['Level_Quota']
        sq = row['SubPage_Quota']

        print(f'Getting data for {a}. . .\n')

        # Adds general page information from dataframe
        page_list['Article'].append(a)
        page_list['Vital_Category'].append(vc)
        page_list['Vital_Level'].append(v)
        page_list['Level_Quota'].append(lq)
        page_list['SubPage_Quota'].append(sq)

        gen = xtools_api(a, pageInfo)
        # Adds general page statistics from return
        page_list['watchers'].append(gen["watchers"])
        page_list['pageviews'].append(gen["pageviews"])
        page_list['pageviews_offset'].append(gen["pageviews_offset"])
        page_list['revisions'].append(gen["revisions"])
        page_list['editors'].append(gen["editors"])
        page_list['created_at'].append(gen["created_at"])

        links = xtools_api(a, pageLinks)

        # Adds information on page links from return
        page_list['links_ext'].append(links["links_ext_count"])
        page_list['links_out'].append(links["links_out_count"])
        page_list['links_in'].append(links["links_in_count"])
        page_list['redirects'].append(links["redirects_count"])

        qid = wiki_api_qid(a, wiki_url)

        page_list['Qid'].append(qid)

        l = wiki_api_sitelinks(qid)

        page_list['Site_links'].append(l)

        ll = wiki_api_languagelinks(a, wiki_url)

        page_list['Language_Links'].append(ll)


        count = count + 1
        # current run time.
        timer = time.time()
        print(f'Data added for {a}.\n {count} articles in {timer - start:0.02f} seconds\n')
        if count % 100 == 0:
            for key, value in page_list.items():
                print(f" Vital articles scanned\n: {key} : {len(value)}")
            tempdf = pd.DataFrame.from_dict(page_list, orient='columns')
            tempdf.to_csv(f'{temp}.csv', index=False)
            continue
        else:
            continue
    for key, value in page_list.items():
        print(f"Data for articles\n: {key} : {len(value)}")

    pagedf = pd.DataFrame.from_dict(page_list, orient='columns')

    if out_CSV is None:
        return pagedf
    else:
        pagedf.to_csv(f'{out_CSV}', index=False)

def percentile(in_list, num):

    p100 = np.percentile(in_list, 99)
    p90 = np.percentile(in_list, 90)
    p80 = np.percentile(in_list, 80)
    p70 = np.percentile(in_list, 70)
    p60 = np.percentile(in_list, 60)
    p50 = np.percentile(in_list, 50)
    p40 = np.percentile(in_list, 40)
    p30 = np.percentile(in_list, 30)
    p20 = np.percentile(in_list, 20)
    p10 = np.percentile(in_list, 10)

    if num >= p100:
        return 10
    elif num >= p90:
        return 9
    elif num >= p80:
        return 8
    elif num >= p70:
        return 7
    elif num >= p60:
        return 6
    elif num >= p50:
        return 5
    elif num >= p40:
        return 4
    elif num >= p30:
        return 3
    elif num >= p20:
        return 2
    elif num >= p10:
        return 1
    else:
        return 0


def VitalIndex(in_CSV, out_CSV):
    start = time.time()
    page_list = {'Article': [], 'Vital_Level': [], 'Vital_Category': [], 'Level_Quota': [], 'SubPage_Quota': [],
                 'watchers': [], 'pageviews': [], 'revisions': [], 'editors': [], 'created_at': [], 'links_ext': [],
                 'links_out': [], 'links_in': [], 'redirects': [], 'Site_links': [], 'Language_Links': [], 'Qid': [],
                 'project_links': [], 'Per_watchers': [], 'Per_editors': [], 'Per_PageViews': [], 'Per_revisions': [],
                 'Per_linksIn': [], 'Per_sitelinks': [], 'Per_projectLinks': [], 'Per_langlinks': [], 'Theme1': [],
                 'Theme2': [], 'Theme3': [], 'Theme4': [], 'IndividualScore': [], 'VitalScore': [], 'Error': [],
                 'Notes': []}

    # Load CSV into a DataFrame
    df = pd.read_csv(in_CSV, low_memory=False, encoding='us-ascii', encoding_errors='ignore')

    # Iterate over DataFrame rows
    count = 0

    # flag 1: Editor interest
    watchers = []
    editors = []

    # flag 2: Activity
    pageviews = []
    revisions = []

    # flag 3: project relevance
    linksIn = []
    sitelinks = []
    projectLinks = []

    # flag 4: Global significance
    langlinks = []

    for index, row in df.iterrows():

        # variables in dataframe
        w = row['watchers']
        pv = row['pageviews']
        r = row['revisions']
        e = row['editors']
        li = row['links_in']
        sl = row['Site_links']
        ll = row['Language_Links']
        pl = (sl - ll) - 1

        watchers.append(w)
        editors.append(e)
        pageviews.append(pv)
        revisions.append(r)
        linksIn.append(li)
        sitelinks.append(sl)
        projectLinks.append(pl)
        langlinks.append(ll)

    for index, row in df.iterrows():

        # variables in dataframe
        a = row['Article']
        v = row['Vital_Level']
        vc = row['Vital_Category']
        lq = row['Level_Quota']
        sq = row['SubPage_Quota']
        pv = row['pageviews']
        w = row['watchers']
        r = row['revisions']
        e = row['editors']
        c = row['created_at']
        le = row['links_ext']
        lo = row['links_out']
        li = row['links_in']
        rd = row['redirects']
        sl = row['Site_links']
        ll = row['Language_Links']
        Qid = row['Qid']
        note = row['Notes']
        error = row['Error']
        pl = (sl - ll) - 1

        perW = percentile(watchers, w)
        perE = percentile(editors, e)
        perPv = percentile(pageviews, pv)
        perR = percentile(revisions, r)
        perLi = percentile(linksIn, li)
        perSl = percentile(sitelinks, sl)
        perPl = percentile(projectLinks, pl)
        perLl = percentile(langlinks, ll)
        # variables in dataframe

        # Editor attention
        Theme1 = (perW + perE)/2

        # Article activity.
        Theme2 = (perPv + perR)/2

        #
        Theme3 = (perLi + perPl)/2
        Theme4 = perLl
        IndividualScore = Theme1 + Theme2 + Theme3 + Theme4

        if v == 1:
            VitalScore = ((IndividualScore * 5)/sq) * 100

        elif v == 2:
            VitalScore = ((IndividualScore * 4)/sq) * 100

        elif v == 3:
            VitalScore = ((IndividualScore * 3) / sq) * 100

        elif v == 4:
            VitalScore = ((IndividualScore * 2) / sq) * 100

        elif v == 5:
            VitalScore = ((IndividualScore * 1) / sq) * 100

        else:
            VitalScore = (IndividualScore / sq) * 100

        page_list['Article'].append(a)
        page_list['Vital_Category'].append(vc)
        page_list['Vital_Level'].append(v)
        page_list['Level_Quota'].append(lq)
        page_list['SubPage_Quota'].append(sq)
        page_list['Qid'].append(Qid)
        page_list['Error'].append(error)
        page_list['Notes'].append(note)

        page_list['watchers'].append(w)
        page_list['pageviews'].append(pv)
        page_list['revisions'].append(r)
        page_list['editors'].append(e)
        page_list['created_at'].append(c)
        page_list['Site_links'].append(sl)
        page_list['Language_Links'].append(ll)


        # Adds information on page links from return
        page_list['links_ext'].append(le)
        page_list['links_out'].append(lo)
        page_list['links_in'].append(li)
        page_list['redirects'].append(rd)
        page_list['project_links'].append(pl)

        # Adds percentiles
        page_list['Per_watchers'].append(perW)
        page_list['Per_editors'].append(perE)
        page_list['Per_PageViews'].append(perPv)
        page_list['Per_revisions'].append(perR)
        page_list['Per_linksIn'].append(perLi)

        page_list['Per_sitelinks'].append(perSl)
        page_list['Per_projectLinks'].append(perPl)
        page_list['Per_langlinks'].append(perLl)

        page_list['Theme1'].append(Theme1)
        page_list['Theme2'].append(Theme2)
        page_list['Theme3'].append(Theme3)
        page_list['Theme4'].append(Theme4)
        page_list['IndividualScore'].append(IndividualScore)
        page_list['VitalScore'].append(VitalScore)

        count = count + 1
        timer = time.time()
        if count == 1:
            print(f'{a} watcher score is {perW}')
        if count % 1000 == 0:
            print(f'{a} vital score: {VitalScore}\n Individual score:{IndividualScore}')
            print(f'Caclculated scores for {count} articles in {timer - start} seconds. . .\n')
        else:
            continue
    for key, value in page_list.items():
        print(f"Data for articles\n: {key} : {len(value)}")
    pagedf = pd.DataFrame.from_dict(page_list, orient='columns')
    pagedf.to_csv(f'{out_CSV}', index=False)

# "Everything not saved will be lost." -Nintendo Quit screen