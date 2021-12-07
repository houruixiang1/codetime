import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from requests import RequestException
from concurrent.futures import ThreadPoolExecutor


class doubandushu():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
        self.Client = MongoClient()

    def get_response(self,url):
        try:
            resp = requests.get(url,headers=self.headers)
            return resp.text
        except:
            return None
    # 解析标签页，拿到对应标签的名字和组装好的url
    def parse_tags(self,content):
        soup = BeautifulSoup(content, 'html.parser')
        # print(soup)
        url = 'https://read.douban.com'
        book_tags = []
        tags_url = []
        ul = soup.find("ul",class_="list kinds-list tab-panel")
        lis = ul.find_all("a")
        # print(lis)
        for item in lis:
            book_tags += [(item.attrs["href"],item.get_text())]
        # print(book_tags)
        for book_tag in book_tags:
            tags_url.append((url + book_tag[0],book_tag[1]))
        return tags_url
        # print(tags_url)

    # 进入对应得标签页，抓取想要的信息
    def detail_page(self,name,id):
        page_num = int(self.parse_page(id))
        print(page_num)
        # for page in range(1,page_num+1):
        data = {
            'kind': id,
            'page': 1,
            'query': "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n  title\n  cover\n  url\n  isBundle\n  coverLabel\n\n    \n  url\n  title\n\n    \n  author {\n    name\n    url\n  }\n  origAuthor {\n    name\n    url\n  }\n  translator {\n    name\n    url\n  }\n\n    \n  abstract\n  authorHighlight\n  editorHighlight\n\n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: false) {\n      inLibraryCount\n    }\n    ... on WorksBase @include(if: false) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ",
            'sort': "hot",
            'variables': {}
        }
        url = "https://read.douban.com/j/kind/"
        try:
            content = requests.post(url,headers=self.headers,json=data)
        except RequestException:
            return None
        xxx = content.json()
        try:
            list = xxx['list']
            for lis in list:
                dic = {}
                dic['name'] = lis['title']
                dic['author'] =[auth['name'] for auth in lis['author']]
                dic['link'] = lis['url']
                dic['id'] = lis['id']
                dic['price'] = lis['salesPrice']
                dic['wordCount'] = str(lis['wordCount'])+lis['wordCountUnit']
                kinds = lis['kinds']
                kind_list = []
                for kind in kinds:
                    kind_list.append(kind['shortName'])
                dic['kinds'] = kind_list
                if dic:
                    self.dic_save_in_mongo(name,dic)
        except:
            return '出错'

    # 解析id，其实就在第一个方法拿到的标签页url里边
    def get_id(self,url):
        id = url.split('/')[-1]
        return id


    # 将列表数据存入mongodb数据库
    def list_save_in_mongo(self,name,data_list):
        db = self.Client.豆瓣读书
        collection = db[name]
        for data in data_list:
            # print(data)
            # datas = json.dumps(data, ensure_ascii=False)
            collection.insert_one(data)

    # 将字典数据存入mongodb数据库
    def dic_save_in_mongo(self,name,data_dic):
        db = self.Client.豆瓣读书
        collection = db[name]
        collection.insert_one(data_dic)

    # 根据id解析相应的页数，抓取全部的信息
    def parse_page(self,id):
        url = "https://read.douban.com/j/kind/"
        data = {
            'kind': id,
            'page': 1,
            'query': "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n  title\n  cover\n  url\n  isBundle\n  coverLabel\n\n    \n  url\n  title\n\n    \n  author {\n    name\n    url\n  }\n  origAuthor {\n    name\n    url\n  }\n  translator {\n    name\n    url\n  }\n\n    \n  abstract\n  authorHighlight\n  editorHighlight\n\n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: false) {\n      inLibraryCount\n    }\n    ... on WorksBase @include(if: false) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ",
            'sort': "hot",
            'variables': {}
        }
        try:
            content = requests.post(url, headers=self.headers, json=data)
        except RequestException:
            return None

        xxx = content.json()
        if 'total' in str(xxx):
            total = xxx['total']
            page_num = (int(total) / 20) +1
        else:
            page_num = 20
        return page_num

   # 主程序，运行整个代码
    def main(self):
        url = "https://read.douban.com/ebooks/?"
        content = self.get_response(url)
        tag_url = self.parse_tags(content)
        for url in tag_url:
            id = self.get_id(url[0])
            print("开始抓取{}".format(url[1]))
            # args = [url[1], id]
            # threading_pool = ThreadPoolExecutor(max_workers=20)
            # threading_pool.submit(lambda p: self.detail_page(*p),args)
            self.detail_page(url[1],id)
            print("已存入{}".format(url[1]))
            # self.save_in_mongo(,data_list)

if __name__ == '__main__':
    task = doubandushu()
    task.main()