#!/usr/bin/env python3

import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        return db
    except ValueError:
        print("Unable to connect to the database")


def top_articles():
    db = connect()
    c = db.cursor()
    print("The top three articles are as follow ")
    c.execute("""create view id_table as select title, count(*) as reads from
                 articles join log on substr(log.path , 10) like articles.slug
                 group by title order by reads desc""")
    c.execute("select * from id_table limit 3")
    rows = c.fetchall()
    for row in rows:
        print("\"{1:s}\" —  {0:d} views".format(row[1], row[0]))
    print("\n")


def top_authors():
    db = connect()
    c = db.cursor()
    print("The top authors are as follow ")
    c.execute("""create view id1_table as select authors.name, count(*) as
                 reads from articles join authors on
                 authors.id = articles.author join log on substr(log.path, 10)
                 like articles.slug group by authors.name
                 order by reads desc""")
    c.execute("select * from id1_table limit 5")
    rows = c.fetchall()
    for row in rows:
        print("\"{1:s}\" —  {0:d} views".format(row[1], row[0]))
    print("\n")


def errors():
    db = connect()
    c = db.cursor()
    c.execute("""create view error_table as select date(time) as day,
               count(*)
               filter (where status like '4%') * round(100.0 / count(*), 3)
               as error_rate from log group by day having
               (count(*)
               filter(where status like '4%') * 100 / count(*)) > 1""")
    c.execute("select * from error_table limit 1")
    rows = c.fetchall()
    for row in rows:
        print(str(row[1]) + "% errors on " + str(row[0]))
    print("\n")


top_articles()
top_authors()
errors()
