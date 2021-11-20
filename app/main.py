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



from infrastructure.database.query_creator import QueryCreator
from infrastructure.database.model_database_mapper import WordMapper
from infrastructure.database.database_manager import DatabaseManager
from infrastructure.database.database_connection import DatabaseConnection

from domain.models import Word

mapper = {Word: WordMapper}

qc = QueryCreator(mapper)

dbc = DatabaseConnection('db.db')

dbm = DatabaseManager(database_connection=dbc, query_creator=qc)

#dbm.create(Word, [{"label":"qwd11", "weight":16}, {"label":"qwdasd11", "weight":20}])
print(dbm.get(Word, weight=16))

