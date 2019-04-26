
import psycopg2

DBASE = "news"

#conn = psycopg2.connect(database=DBASE)

def getDbConnection():
    # code to Get Database connection
    try:        
        connection = psycopg2.connect(database=DBASE)
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))

def closeDbConnection(connection):
    #code close Database connection
    try:
        connection.close()
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to conect to database {}".format(error))

SELECT_QUERY_1 = '''
                select title, count(*) 
					as num 
                  from log, articles 
                  where path like concat('%', slug, '%') 
                  group by title 
                  order by num desc 
				  limit 3;
 '''
 

SELECT_QUERY_2 = ''' 
                select name,count(*) 
				    as num 
                  from log, articles, authors 
                  where path like concat('%', slug, '%') 
                    and articles.author = authors.id 
                  group by name 
                  order by num desc;
''' 

SELECT_QUERY_3 = '''  
				select * 
				  from 
			   (select day,
				  avg((Error::float) / (Rate::float) * 100)
				   as Error_R 
				  from All_Rate
				  group by day) 
				   as Error_R
				  where Error_R > 1;
'''

def first_query(query):
	try:	
		print ("First Quistion: What are the most popular 3 articles of all time?")
		print ("\t")
		connection = getDbConnection()
		cur = conn.cursor()
		cur.execute(SELECT_QUERY_1)
		rows1 = cur.fetchall()

		for row in rows1:
			print("article:", row[0])
			print("views:", row[1])
			print("\n")
			
			closeDbConnection(connection)
			 
	except (Exception, psycopg2.Error) as error:
		print("Failed to conect to database {}".format(error))
		


def second_query(query):
	try:
		print ("Second Quistion: Who are the most popular article authors of all time?")
		print ("\t")
		connection = getDbConnection()
		cur = conn.cursor()
		cur.execute(SELECT_QUERY_2)
		rows2 = cur.fetchall()
		for row in rows2:
			print("name:", row[0])
			print("views:", row[1])
			print("\n")
			
			closeDbConnection(connection)
			
	except (Exception, psycopg2.Error) as error:
		print("Failed to conect to database {}".format(error))
		
def third_query(query):
	try:		
		print ("Third Quistion: On which days did more than 1% of requests lead to errors?" )
		print ("\t")
		connection = getDbConnection()
		cur = conn.cursor()
		cur.execute(SELECT_QUERY_3)
		rows3 = cur.fetchall()
		for row in rows3:
			print("date:", row[0])
			print("error %:", row[1]) 
			print("\n")

		    closeDbConnection(connection)
			
	except (Exception, psycopg2.Error) as error:
		print("Failed to conect to database {}".format(error))
		
     

if __name__=='__main__':
	
	first_query(query)
	second_query(query)
	third_query(query)

 
