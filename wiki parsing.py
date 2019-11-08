# Crolling - https://www.fun-coding.org/crawl_basic3.html
# HTML Parsing - https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
import requests
from bs4 import BeautifulSoup

client_key = 'CsODwdUTyG9vOI1uIeIf'
client_secret = 'YmIx0GW8JG'
# 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌

print("시작")
def parse_wiki(root, url):
    # headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
    header_params = {"X-Naver-Client-Id": client_key, "X-Naver-Client-Secret": client_secret}
    response = requests.get(root + url)

    if (response.status_code == 200):
        whole = BeautifulSoup(response.text, 'html.parser')
        # lst = whole.select('#mw-content-text > div > ul')
        lst = whole.select('li')
        for content in lst:
            example = content.text
            if ('출간' in example):
                break

            try:
                int(example[0])
            except:
                print(example)

            # examples = example.split(':')
            # if (len(examples) == 1):
            #     print("exception : " + example[0])
            # else:
            #     print(examples[0].strip() + " : " + examples[1].strip())
    else:
        print("Error Code:" + str(response.status_code))

# parse_wiki('https://ko.wikipedia.org', '/wiki/%EC%9D%80%EC%96%B4_(%EC%96%B8%EC%96%B4%ED%95%99)') # 은어 검색 결과
parse_wiki('https://ko.wikipedia.org', '/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%8B%A0%EC%A1%B0%EC%96%B4_%EB%AA%A9%EB%A1%9D') # 대한민국의 인터넷 신조어 목록
