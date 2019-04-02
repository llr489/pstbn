import requests 
import pandas as pd
import datetime
import re

# Set the number of pastes to request at a time, max = 250 
pastes = 10

def pastebin_scrape(pastes):
    payload = {'limit': pastes}
    r = requests.get('https://scrape.pastebin.com/api_scraping.php', params=payload)

    return r.json()

def notedata_filter(r):
    df = pd.DataFrame(r)
    df = df.drop(columns=['full_url', 'scrape_url', 'size'])

    i = 0
    while i < pastes:
        if df['syntax'][i] != '' and (not re.match(r'text|html4strict|html5|xml', df['syntax'][i])):
            df = df.drop([i])
        i+=1
    
    return df


def temp_csv_write(df):
    filename = datetime.datetime.now().timestamp()
    df.to_csv(path_or_buf = f"{filename}.csv")


