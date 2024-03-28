import sqlite3 as sq
# #
# #
# # def create_db():
# #     base = sq.connect('test_db2.db')
# #     cursor = base.cursor()
# #     sql_query = """CREATE TABLE IF NOT EXISTS Students(
# #                         name TEXT,
# #                         s_name TEXT,
# #                         age INT,
# #                         date_s DATE,
# #                         group_s TEXT,
# #                         grants INT
# #                         )"""
# #     sql_query_2 = """CREATE TABLE IF NOT EXISTS Departments(
# #                         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                         name_d TEXT,
# #                         phone TEXT)"""
# #     sql_query_3 = """CREATE TABLE IF NOT EXISTS Teachers(
# #                         name_t TEXT,
# #                         s_name_t TEXT,
# #                         dep_id INT,
# #                         FOREIGN KEY (dep_id) REFERENCES Departments (id))"""
# #     cursor.execute(sql_query)
# #     cursor.execute(sql_query_2)
# #     cursor.execute(sql_query_3)
# # create_db()
# #
# # def insert_data_db():
# #     base = sq.connect('test_db2.db')
# #     cursor = base.cursor()
# #     sql_query = """
# #     INSERT INTO Students(name, s_name, age, date_s, group_s, grants) VALUES
# #     ('Джеймс', 'Хант', 22, '2012-08-21', 'B', 1200),
# #     ('Ніккі', 'Лауда', 25, '2011-05-22', 'A', 1300),
# #     ('Артур', 'Сенна', 22, '2013-04-23', 'B', 1500),
# #     ('Міхаель', 'Шумахер', 25, '2016-07-24', 'A', 1800),
# #     ('Кен', 'Блок', 35, '2010-02-35', 'B', 2500),
# #     ('Коллін', 'Макрей', 21, '2017-10-26', 'A', 2200)
# #     """
# #     create_teachers = """
# #     INSERT INTO Teachers (name_t, s_name_t, dep_id) VALUES
# #     ('Алан', 'Тюрінг', 1),
# #     ('Ада', 'Лавлейс', 1),
# #     ('Лінус', 'Торвальдс', 2),
# #     ('Гвідо', 'ван Россум', 2),
# #     ('Джеймс', 'Гослінг', 2),
# #     ('Андерс', 'Хейлсберг', 5),
# #     ('Брем', 'Коен', 3),
# #     ('Брендан', 'Айк', 4),
# #     ('Лінус', 'Торвальдс', 6),
# #     ('Бярне', 'Страуструп', 6),
# #     ('Дональд', 'Кнут', 4),
# #     ('Денніс', 'Річі', 3);
# #     """
# #     create_deps = """
# #     INSERT INTO Departments(name_d, phone) VALUES
# #     ('Cybersecurity', '2205-800'),
# #     ('Python', '1236-500'),
# #     ('Java', '3584-100'),
# #     ('Frontend', '4545-700'),
# #     ('C++', '4545-700'),
# #     ('DevOps', '4545-700');
# #     """
# #     cursor.execute(sql_query)
# #     cursor.execute(create_teachers)
# #     cursor.execute(create_deps)
# #     base.commit() ##### !!!!!!!!!!!!!
# # insert_data_db()
# new_data = [('GDDDen', 'FDDles', 58, '2002-21-05', 'C', 40800), ('Gsaen', 'FSAles', 18, '2002-21-05', 'C', 80800)]
#
# def insert_data_db(n):
#
#     base = sq.connect('test_db2.db')
#     cursor = base.cursor()
#
#     sql = """INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?)"""
#
#     cursor.executemany(sql, n)
#
#     base.commit() ##### !!!!!!!!!!!!!
#
# insert_data_db(new_data)
#
#
#
# def select_data_db():
#
#     # name = (input('Enter name: '),)
#     # s_name = (input('Enter second name: '),)
#     #
#     # values = name + s_name
#
#     base = sq.connect('test_db2.db')
#     cursor = base.cursor()
#     # 'Джеймс', 'Хант'
#
#     sql_query = """SELECT * FROM Students """ #WHERE name == ? AND s_name == ?
#
#     cursor.execute(sql_query)
#
#     records = cursor.fetchall()
#     for i in records:
#         print(i)
#
# select_data_db()

#
# def create_db():
#     conn = sq.connect('file_db.db')
#     cursor = conn.cursor()
#
#     sqlq = """CREATE TABLE IF NOT EXISTS new_employe (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 photo BLOB NOT NULL,
#                 resume BLOB NOT NULL)
#                 """
#
#     cursor.execute(sqlq)
#
# create_db()
#
#
# def conv_to_bin(filename):
#     with open(filename, 'rb') as file:
#         blob_data = file.read()
#     return blob_data
#
#
# def insert_data(emp_id, emp_name, photo, resume):
#     try:
#         conn = sq.connect('file_db.db')
#         cursor = conn.cursor()
#
#         sqlq = """INSERT INTO new_employe VALUES (?, ?, ?, ?)"""
#
#         bin_photo = conv_to_bin(photo)
#         bin_resume = conv_to_bin(resume)
#
#         data_tuple = (emp_id, emp_name, bin_photo, bin_resume)
#
#         cursor.execute(sqlq, data_tuple)
#         conn.commit()
#         cursor.close()
#     except sq.Error as error:
#         print('ERROR: ', error)
#     finally:
#         if conn:
#             conn.close()
#             print('Connection close')
#
# #insert_data(1111, 'Smith', 'python_2.jpg', 'file_2.txt')
#
# ###########################
#
# def conv_from_bin(filename, bin_data):
#     with open(filename, 'wb') as file:
#         file.write(bin_data)
#
#
# def select_data(name):
#     try:
#         conn = sq.connect('file_db.db')
#         cursor = conn.cursor()
#
#         sqlq = """SELECT * FROM new_employe WHERE name == ?"""
#
#         data_tuple = (name, )
#
#         cursor.execute(sqlq, data_tuple)
#         result = cursor.fetchall()
#         print(result)
#         conv_from_bin('image.jpg', result[0][2])
#         conv_from_bin('resume.txt', result[0][3])
#
#         cursor.close()
#     except sq.Error as error:
#         print('ERROR: ', error)
#     finally:
#         if conn:
#             conn.close()
#             print('Connection close')
#
# select_data('Smith') # [(1111, 'Smith' 'xccxzc' 'dsadsa')]
import time

conn = sq.connect('database.db')

with open('shema.sql') as f:
    conn.executescript(f.read())

cursor = conn.cursor()

cursor.execute("""INSERT INTO posts (title, content)
                    VALUES (?, ?)""",
               ('First post', 'Text content of first post'))
#time.sleep(2)
cursor.execute("""INSERT INTO posts (title, content)
                    VALUES (?, ?)""",
               ('Second post', 'Text content of second post'))

conn.commit()
conn.close()

def select_shema():

    conn = sq.connect('test_db2.db')
    cursor = conn.cursor()

    sqlq = """PRAGMA TABLE_INFO(Departments)"""

    cursor.execute(sqlq)

    rec = cursor.fetchall()

    for i in rec:
        print(i)

select_shema()
