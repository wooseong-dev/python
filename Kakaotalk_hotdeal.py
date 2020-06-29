import requests
from bs4 import BeautifulSoup
import json


KAKAO_TOKEN=""# 토큰은 개인이 발급받은 토큰을 넣어 사용해야 합니다. Here is input your private token

header = {"Authorization" : "Bearer " + KAKAO_TOKEN}
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
post={
    "object_type": "text",
        "text": "연습메시지",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
}
data = {"template_object" : json.dumps(post)}

r = requests.post(url,headers=header,data=data)
print(r.text)

def hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&searcharea=deals&searchin=first&pp=20".format(keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.text,"lxml")
    rows = bs.select("div.resultRow")

    result=[]
    for r in rows:
        link=r.select("a.dealTitle")[0]
        href=link.get("href")
        if href is None:
            continue
        href = "https://slickdeals.net/" + href
        title = link.text
        price = r.select("span.price")[0].text.replace("$","").replace("from","").strip()
        if price.find("/")>=0 or price == "":
            continue
        price = float(price)
        hot = len(r.select("span.icon-fire"))
        result.append((title,href,price,hot))
    return result
#print(hotdeal("ipad"))