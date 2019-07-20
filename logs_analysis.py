import psycopg2


def connect(query):
	# Connect to database
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    # Execute queries
    cursor.execute(query)
    # Fetch results
    results = cursor.fetchall()
    conn.close()
    return results

# 1- Print the top three articles of all time:

def top_three_articles():
    results = connect("""select articles.title, count(*) as views 
            from log, articles
            where log.status='200 OK' 
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by views desc
            limit 3;""")
    print('\n Displaying the top three articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


# 2- Print the most popular article authors of all time:
def top_authors():
    results = connect("""select authors.name, sum(article_views.views) as views
            from article_authors, article_views,log
            where log.status='200 OK'
            and article_authors.title = article_views.title
            group by authors.name
            order by views desc;""")
    print('\n Displaying the most popular article authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


# 3-Print the days in which there were more than 1% of requests lead to errors
def error_percentage():
    results = connect("""select errorlogs.date, round(100.0*errorcount/logcount,2) as percent
            from logs, errorlogs
            where logs.date = errorlogs.date
            and errorcount > logcount/100;""")
    print('\n The days when more than 1% of requests lead to errors:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")
 




if __name__ == '__main__':
	# Print results
    top_three_articles()
    top_three_authors()
    high_error_days()




