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

# Print the top three articles of all time

def top_three_articles():
    results = connect("""SELECT * FROM article_views LIMIT 3;""")
    print('\n Displaying the most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


# Print the most popular article authors of all time
def top_authors():
    results = connect("""SELECT name, sum(article_views.views) AS views
            FROM article_authors, article_views
            WHERE article_authors.title = article_views.title
            GROUP BY name
            ORDER BY views desc;""")
    print('\n Displaying the most popular authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


# Print the days in which there were more than 1% of requests lead to errors
def error_percentage():
    results = connect("""SELECT errorlogs.date, round(100.0*errorcount/logcount,2) as percent
            FROM logs, errorlogs
            WHERE logs.date = errorlogs.date
            AND errorcount > logcount/100;""")
    print('\n The days when more than 1% of requests lead to error:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")
 




if __name__ == '__main__':
	# Print results
    top_three_articles()
    top_three_authors()
    high_error_days()


