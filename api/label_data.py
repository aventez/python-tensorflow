#!/usr/bin/env python
import pandas as pd

def main():

    blacklist = 'phishing_database.csv'
    whitelist = 'whitelist.txt'

    urls = {}
    
    blacklist = pd.read_csv(blacklist)

    for url in blacklist['url']:
        urls[url] = 1
    
    with open(whitelist, 'r') as f:
        lines = f.read().splitlines()
        for url in lines:
            urls[url] = 0

    return urls

if __name__ == "__main__":
    main()
