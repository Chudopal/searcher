import sqlite3

from sqlite3 import connect, Row

# conn = connect("db.db")
# conn.row_factory = sqlite3.Row #because of dict
# cur = conn.cursor()

# cur.execute("""SELECT * FROM word WHERE id={};""".format(1))

# print("HERE")

# a = cur.fetchall()
# print(dict(a[0]))
# cur.close()
# conn.close()

#from infrastructure.quries import CreateWordQuery

# cq = CreateWordQuery([
#     {'label': "rhgjhkjh", 'weight': 12},
#     {'weight': 14, 'label': 'wrghtumtyh'}]
# ).build()
# print(cq)


# from infrastructure.quries import DeleteWordQuery
# q = DeleteWordQuery(
#     label='label4').build()


# conn = connect("db.db")
# conn.row_factory = sqlite3.Row #because of dict
# cur = conn.cursor()

# print(q)
# cur.execute(q)
# conn.commit()
# #a = cur.fetchall()
# #print([dict(i) for i in a])
# cur.close()
# conn.close()


# class CreateBaseQuery():

#     def __init__(self, data):
#         self.data = data
#         self.order = ['b', 'a']
#         self._query = ""

#     def bould(self):
#         self.append_params()
#         self.add_query_end()
#         return self._query

#     def append_params(self) -> None:
#         self._query += ",".join([
#             f"""({','.join([
#                     f'{data_item.get(order_item)!r}'
#                     for order_item in self.order
#             ])})""" for data_item in self.data
#         ])

#     def add_query_end(self) -> None:
#         self._query += ";"


# bq = CreateBaseQuery([{"a": 10, "b": 'c'}, {"a": 12, "b": 'c'}])
# print(bq.bould())



# from bs4 import BeautifulSoup
# import requests

# url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B0%D0%B4%D0%B0'

# page = requests.get(url)

# print(page)

# soup = BeautifulSoup(page.text, "html.parser")

# items  = " ".join( [item.text for item in soup.find(id='bodyContent').find_all('p')])


# import re
# print(re.sub("\[[\d, \w]*\]|,|\.|!|:|#|'|\(|\)|\n|\[|\]", "", items))

# a = "qazxs[10], doeonc[1002], wpcmepcwm[12321][wcwe]!"
# print(re.sub('\[[a-z. \d, A-Z]*\]|,|\.|!|:|#|', "", a))

# from infrastructure.web_scraping.wiki_scraper import WikiScrapper


# tokens = WikiScrapper(
#         link="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B0%D0%B4%D0%B0"
#         ).execute()
# print(tokens)
# print(len(tokens))
# print(len(set(tokens)))

from view.search_window import MainWindow

MainWindow(links =[
        "https://github.com/Chudopal/searcher",
        "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B0%D0%B4%D0%B0"
    ]).apply()
# MainWindow.add_links(
    
# )