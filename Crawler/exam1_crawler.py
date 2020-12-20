from bs4 import BeautifulSoup
import requests
i = int(input("페이지 수를 입력하시오 : "))
url = "https://store.musinsa.com/app/?n_media=27758&n_query=%EB%AC%B4%EC%8B%A0%EC%82%AC&n_rank=1&n_ad_group=grp-a001-01-000000014243257&n_ad=nad-a001-01-000000095050246&n_keyword_id=nkw-a001-01-000002707949946&n_keyword=%EB%AC%B4%EC%8B%A0%EC%82%AC&n_campaign_type=1&NaPm=ct%3Dkbtb2qds%7Cci%3D0yu0001%2DedbsT5FMvf0O%7Ctr%3Dsa%7Chk%3De73f5151442e5594a432afe6d2963653c7f79f37"



r = requests.get(url)

bs = BeautifulSoup(r.text, "lxml")


ls=bs.select("strong.title")

lists=[]
for l in ls:
    lists.append(l.text)

print(lists)
