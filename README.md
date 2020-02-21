scrape newssite's timetamps
====

## Description
Get the update date of the article from each news site.

## Requirement
requests
bs4
jeraconv

## Usage
from news_timestamp import *

TS = ScrapeNewsTimestamp()
news_timestamp = TS.main('https://www.mofa.go.jp/mofaj/press/release/press1_000423.html')
print(news_timestamp)

## Author

[KanikaniYou](https://github.com/KanikaniYou)
