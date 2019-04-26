import psycopg2

DBASE = "news"


def getDbConnection():
    # code to Get Database connection
    try:
        connection = psycopg2.connect(database=DBASE)
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))


def closeDbConnection(connection):
    # code close Database connection
    try:
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))

# What are the most popular 3 articles of all time?
SELECT_QUERY_1 = '''
select title, count(*) as num
from log, articles
where path like concat('%', slug)
group by title
order by num desc
limit 3;'''

# Who are the most popular article authors of all time?
SELECT_QUERY_2 = '''
select name,count(*) as num
from log, articles, authors
where path like concat('%', slug)
and articles.author = authors.id
group by name
order by num desc;'''

# On which days did more than 1% of requests lead to errors?
SELECT_QUERY_3 = '''
select * from
        (select day, avg((Error::float) /(Rate::float) * 100) as Error_R
        from All_Rate
        group by day) as Error_R
where Error_R > 1;'''


def first_query(query):
    try:
        print("Q1: What are the most popular 3 articles of all time?")
        print("\t")
        connection = getDbConnection()
        cur = connection.cursor()
        cur.exectue(query)
        rows = cur.fetchall()
        for row in rows:
            print("Article:", row[0])
            print("Views:", row[1])
            print("\n")
        closeDbConnection(connection)
    except(Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))


def second_query(query):
    try:
        print("Q2: Who are the most popular article authors of all time?")
        print("\t")
        connection = getDbConnection()
        cur = connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print("name:", row[0])
            print("views:", row[1])
            print("\n")
        closeDbConnection(connection)
    except(Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))


def third_query(query):
    try:
        print("Q3: On which days more than 1% of requests lead to errors?")
        print("\t")
        connection = getDbConnection()
        cur = connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print("date:", row[0])
            print("error %:", row[1])
            print("\n")
        closeDbConnection(connection)
    except(Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))


if __name__ == '__main__':
    # printing the results of queries
    first_query(SELECT_QUERY_1)
    second_query(SELECT_QUERY_2)
    third_query(SELECT_QUERY_3)

