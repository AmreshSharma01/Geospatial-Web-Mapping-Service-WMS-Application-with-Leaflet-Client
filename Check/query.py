#!C:\ms4w\Python\python

import sqlite3
import cgi

# Get form data from the standard input
form = cgi.FieldStorage()

# Get the value of the 'direction' field from the form
value = form.getvalue('direction')

# Get the value of the 'direction' field from the form
limit = form.getvalue('limit')

print ("Content-Type: text/plain;charset=utf-8")
print() 


conn = sqlite3.connect('canvec_231031_433813.gpkg')

# Check if form data is provided
if value is None or limit is None:
    print("Please Enter the data in HTML form")
else:
    conn = sqlite3.connect('canvec_231031_433813.gpkg')

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    query = f"SELECT road_segment_name_en from road_segment_1 where of_municipal_quadrant_left = '{value}' LIMIT {limit};"

    # Execute an SQL query
    cur.execute(query)

    # Fetch the results (if any)
    results = cur.fetchall()

    # Process the results
    result_string = ','.join([row[0] for row in results])

    print(result_string)

    # Close the cursor and connection
    cur.close()
    conn.close()
