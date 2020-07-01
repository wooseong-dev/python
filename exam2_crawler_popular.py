import requests
from bs4 import BeautifulSoup

def Musinsa_crawler(start,end):
    lists=[]
    for i in range(start,end):
        url_popular= "https://store.musinsa.com/app/items/lists/026004/?category=&d_cat_cd=026004&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90&page={}&page_kind=category&list_kind=small&free_dlv=&ex_soldout=&sale_goods=&exclusive_yn=&price=&color=&a_cat_cd=&sex=&size=&tag=&popup=&brand_favorite_yn=&goods_favorite_yn=&blf_yn=&campaign_yn=&bwith_yn=&price1=&price2=&brand_favorite=&goods_favorite=&chk_exclusive=&chk_sale=&chk_soldout=".format(i)
        r=requests.get(url_popular)
        bs=BeautifulSoup(r.text, "lxml")

        res = bs.select("div.list-box")

        for re in res:
            #info=re[0].text
            #sale_info=re[1].text
            lists.append({ 
                "info" : re.text
                })

        #if lists
    return lists

print(Musinsa_crawler(1,20))


#bs.find_all("li",{"class" : "classname"})
#title = li(반복자).find("span",attrs={"class" : "class_name"}).text


