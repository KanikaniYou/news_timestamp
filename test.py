from news_timestamp import *

TS = ScrapeNewsTimestamp()
news_timestamp = TS.main('https://www.mofa.go.jp/mofaj/press/release/press1_000423.html')
print(news_timestamp)
