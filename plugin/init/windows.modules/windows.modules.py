import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.modules/windows.modules.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Offset	Base	Size	Name	Path','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 5:(i + 1) * 5] for i in range((len(my_list) + 4) // 5 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table modules (Offset text, Base text, Size text, Name text, Path text)")

cur.executemany("insert into modules values (?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()