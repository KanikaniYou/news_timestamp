import bs4
import requests
import datetime
import re
from jeraconv import jeraconv

class ScrapeNewsTimestamp:
    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        }

    def scrape_return_timestamp_1(self,bs4Obj):
        try:
            #朝日新聞
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y年%m月%d日 %H時%M分")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_2(self,bs4Obj):
        try:
            #日経新聞 時は金なり
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[1].string, "%Y年%m月%d日 %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_3(self,bs4Obj):
        try:
            #日経新聞 海外金融ニュース
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('.cmnc-publish')[0].string, "%Y/%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_4(self,bs4Obj):
        try:
            #日経新聞 春秋
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('.cmnc-publish')[0].string, "%Y/%m/%d付")
            return news_timestamp
        except Exception as e:
            return None


    def scrape_return_timestamp_5(self,bs4Obj):
        try:
            #産経新聞 国際
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('#__r_publish_date__')[0].string, "%Y.%m.%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_6(self,bs4Obj):
        try:        
            #読売新聞 国内
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y/%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_7(self,bs4Obj):
        try:                
            #毎日新聞 東京朝刊
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y年%m月%d日　東京朝刊")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_8(self,bs4Obj):
        try:        
            #毎日新聞 東京夕刊
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y年%m月%d日　東京夕刊")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_9(self,bs4Obj):
        try:
            #毎日新聞　速報
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y年%m月%d日 %H時%M分")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_10(self,bs4Obj):
        try:
            #毎日新聞　プレミア
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('time')[0].string, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_11(self,bs4Obj):
        try:
            #Yahoo!ニュース
            bs4Obj = bs4Obj
            m1 = re.match(r'\d{1,2}/\d{1,2}',str(bs4Obj.select('p.source')[0].string))
            tmp1 = m1.group()
            m2 = re.search(r'\d{1,2}:\d{1,2}',str(bs4Obj.select('p.source')[0].string))
            tmp2 = m2.group()
            news_timestamp = datetime.datetime.strptime(str(datetime.datetime.now().year)+tmp1+' '+tmp2, "%Y%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_12(self,bs4Obj):
        try:
            #CNN
            bs4Obj = bs4Obj
            m1 = re.search(r'Updated (\d{4}) GMT', str(bs4Obj.select('.update-time')[0].getText()))
            m2 = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})', str(bs4Obj.select('.update-time')[0].getText()))
            nes_timestamp_tmp = m2.groups()[2]+m2.groups()[1]+m2.groups()[0]+m1.groups()[0]
            news_timestamp = datetime.datetime.strptime(nes_timestamp_tmp, "%Y%d%B%H%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_13(self,bs4Obj):
        try:
            #Bloomberg
            bs4Obj = bs4Obj
            timesamp_tmp = re.sub(' ','',str(bs4Obj.select('time')[0].string))
            timesamp_tmp = re.sub('\n','',timesamp_tmp)
            news_timestamp = datetime.datetime.strptime(timesamp_tmp, "%Y年%m月%d日%H:%MJST")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_14(self,bs4Obj):
        try:
            #BBC
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select("div.date.date--v2")[0].string, "%d %B %Y")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_15(self,bs4Obj):
        try:
            #Reuter
            bs4Obj = bs4Obj
            m1 = re.match(r'(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}',str(bs4Obj.select(".ArticleHeader_date")[0].string))
            m2 = re.search(r'\d{1,2}:\d{1,2}',str(bs4Obj.select(".ArticleHeader_date")[0].string))
            news_timestamp = datetime.datetime.strptime(m1.group()+' '+m2.group(), "%B %d, %Y %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_16(self,bs4Obj):
        try:
            #Wall Street Journal
            bs4Obj = bs4Obj
            m = re.sub(' ','',str(bs4Obj.select(".timestamp.article__timestamp")[0].string))
            m = re.sub('\n','',m)
            m = re.match(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).(\d{1,2}),(\d{4})(\d{1,2}):(\d{1,2})',str(m))
            tmp = m.groups()
            timesamp_tmp = tmp[0]+' '+ tmp[1].zfill(2)+' '+tmp[2]+' '+tmp[3].zfill(2)+' '+tmp[4].zfill(2)
            news_timestamp = datetime.datetime.strptime(timesamp_tmp, "%b %d %Y %H %M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_17(self,bs4Obj):
        try:
            #Forbes Japan
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select("time")[0].string, "%Y/%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_18(self,bs4Obj):
        try:
            #Newsweek
            bs4Obj = bs4Obj
            m = re.search(r'(\d{1,2})/(\d{1,2})/(\d{1,2}) at (\d{1,2}:\d{1,2}) ', str(bs4Obj.select('time')[0].string))
            tmp = m.groups()
            timesamp_tmp = tmp[0].zfill(2)+' '+ tmp[1].zfill(2)+' '+'20'+tmp[2].zfill(2)+' '+tmp[3]
            news_timestamp = datetime.datetime.strptime(timesamp_tmp, "%m %d %Y %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_19(self,bs4Obj):
        try:
            #CNN.co.jp
            bs4Obj = bs4Obj
            m1 = re.search(r'\d{4}.\d{2}.\d{2}', str(bs4Obj.select("div .metadata-updatetime")[0]))
            m2 = re.search(r'\d{1,2}:\d{1,2}', str(bs4Obj.select("div .metadata-updatetime")[0]))
            news_timestamp = datetime.datetime.strptime(m1.group()+' '+m2.group(), "%Y.%m.%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_20(self,bs4Obj):
        try:
            #BBC 2
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select("div.date.date--v2")[0].string, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_21(self,bs4Obj):
        try:
            #ABC News
            bs4Obj = bs4Obj
            tmp = re.match(r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4}), (\d{1,2}:\d{1,2}) (AM|PM)',bs4Obj.select(".Byline__Meta.Byline__Meta--publishDate")[0].string)
            hour = int(tmp.groups()[3].split(':')[0])
            mini = tmp.groups()[3].split(':')[1]
            if tmp.groups()[4] == 'PM':
                hour += 12
            hour = str(hour)
            news_timestamp = datetime.datetime.strptime(tmp.groups()[0]+' '+tmp.groups()[1]+' '+tmp.groups()[2]+' '+hour+' '+mini,"%B %d %Y %H %M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_22(self,bs4Obj):
        try:
            #外務省
            bs4Obj = bs4Obj
            j2w = jeraconv.J2W()
            m = bs4Obj.select('.rightalign')[0].string
            y =  m.split('年')[0]
            md = m.split('年')[1]
            news_timestamp = datetime.datetime.strptime(str(j2w.convert(str(y)+'年'))+'年'+ md, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_23(self,bs4Obj):
        try:
            #AFP BB
            bs4Obj = bs4Obj
            for meta_tag in bs4Obj.find_all('meta', attrs={'property':"article:modified_time"}):
                m = re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',meta_tag.get('content'))
                news_timestamp = datetime.datetime.strptime(m.group(),"%Y-%m-%dT%H:%M:%S")
                return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_24(self,bs4Obj):
        try:
            #NHK News
            bs4Obj = bs4Obj
            for meta_tag in bs4Obj.find_all('time'):
                news_timestamp = datetime.datetime.strptime(meta_tag.get('datetime'),'%Y-%m-%dT%H:%M')
                return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_25(self,bs4Obj):
        try:
            #日経新聞 株
            bs4Obj = bs4Obj
            m = re.search(r'\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}',bs4Obj.select('.cmnc-publish')[0].string)
            news_timestamp = datetime.datetime.strptime(m.group(), "%Y/%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_26(self,bs4Obj):
        try:
            #日刊工業新聞
            bs4Obj = bs4Obj
            m = re.search(r'\d{4}/\d{1,2}/\d{1,2} \d{2}:\d{1,2}',str(bs4Obj.select('.date')[1]))
            news_timestamp = datetime.datetime.strptime(m.group(), "%Y/%m/%d %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_27(self,bs4Obj):
        try:
            #朝日新聞　論座
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('.date')[0].string, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_28(self,bs4Obj):
        try:  
            #朝日新聞　中高生新聞
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select('.date')[0].string, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_28(self,bs4Obj):
        try:  
            #EUROPA NEWSWIRE
            bs4Obj = bs4Obj          
            m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}), (\d{4})',bs4Obj.select(".icon-cal")[0].string)
            news_timestamp = datetime.datetime.strptime(''.join(m.groups()), "%b%d%Y")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_29(self,bs4Obj):
        try:
            #国連広報センター
            bs4Obj = bs4Obj
            news_timestamp = datetime.datetime.strptime(bs4Obj.select("#cm_header_text")[0].string, "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None    

    def scrape_return_timestamp_29(self,bs4Obj):
        try:
            #OPCW News
            bs4Obj = bs4Obj 
            m = re.search(r'(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}',bs4Obj.select(".news__date")[0].get_text())
            news_timestamp = datetime.datetime.strptime(m.group(), "%d %B %Y")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_30(self,bs4Obj):
        try:
            #HAARETZ
            bs4Obj = bs4Obj
            m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4} \d{1,2}:\d{1,2}',bs4Obj.select("time")[1].get_text())
            news_timestamp = datetime.datetime.strptime(m.group(), "%b %d, %Y %H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_31(self,bs4Obj):
        try:
            #THE DAILY STAR
            bs4Obj = bs4Obj
            m = re.match(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec). (\d{1,2}), (\d{4}) \| (\d{1,2}):(\d{1,2})',bs4Obj.select("time")[0].get_text())
            news_timestamp = datetime.datetime.strptime(''.join(m.groups()), "%b%d%Y%H%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_32(self,bs4Obj):
        try:
            #INDEPENDENT
            bs4Obj = bs4Obj
            m = re.search(r'\d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}',str(bs4Obj.select("amp-timeago")[0]))
            news_timestamp = datetime.datetime.strptime(m.group(), "%Y-%m-%dT%H:%M")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_33(self,bs4Obj):
        try:
            #ジェトロ
            bs4Obj = bs4Obj
            m = re.search(r'\d{4}年\d{1,2}月\d{1,2}日',str(bs4Obj.select('p')))
            news_timestamp = datetime.datetime.strptime(m.group(), "%Y年%m月%d日")
            return news_timestamp
        except Exception as e:
            return None

    def scrape_return_timestamp_34(self,bs4Obj):
        try:
            #夕刊フジ
            bs4Obj = bs4Obj 
            m = re.search(r'\d{4}.\d{1,2}.\d{1,2}',str(bs4Obj.select('#__r_publish_date__')[0]))
            news_timestamp = datetime.datetime.strptime(m.group(), "%Y.%m.%d")
            return news_timestamp
        except Exception as e:
            return None


    def main(self,URL):
        self.URL = URL
        try:
            get_url_info = requests.get(URL,headers=self.headers)
            bs4Obj = bs4.BeautifulSoup(get_url_info.content, 'lxml')
        except Exception as e:
            print(e)
            return 'URLにアクセスできません'

        for i in range(1,35):
            func_name = 'self.scrape_return_timestamp_' + str(i)
            ts_temp = eval(func_name)(bs4Obj)
            if ts_temp:
                return ts_temp



