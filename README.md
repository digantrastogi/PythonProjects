# PythonProjects
A collection of projects done using Python, JSON, XML, APIs and SQL based on the course py4e by Dr Charles Severance
## [jsontosql.py](https://github.com/digantrastogi/PythonProjects/blob/main/jsontosql.py)
JSON to SQL parses JSON file and extracts student details with courses enrolled in and creates  SQL databases that stores USER details, COURSE details and MEMBER which is a relational table linking USER and COURSES
## [xmltosql.py](https://github.com/digantrastogi/PythonProjects/blob/main/xmltosql.py)
This program parses XML data extracted from a popular onine Music streaminG platform and creates an SQL database storing Artist, Album, Name and Gnere details in a proper format. The program can then be used to extract the songs from a particular genre or artist etc.
## [webcrawler1.py](https://github.com/digantrastogi/PythonProjects/blob/main/webcrawler1.py)
This is a simple webcrawler using python ibraries- urlib, Bs4 and ssl. The program requires a url, visits the website and builds a list of links used in that page then moves to the first link found and scraps the new web page for _new_ links only. This way pages can then be indexed upon number of time they are found.
## [geodata](https://github.com/digantrastogi/PythonProjects/tree/main/geodata)
We use Google PLaces API with a database and then visualize a user entred location on the world map. The user enters a rough location. Due to the rate limit on using the Google API we break the process into two subparts. We run the geoload.py program that check first if we have already retrieved location data, if not it uses the API to extract all location data for the location and stores it in the database, geodata.sqllite
Once we have some data loaded into geodata.sqlite, we visualize the same using geodump.py that reads the database and extracts location, latitude and longitude in the form of executable JavaScript code in where.js
The file (where.html) consists of HTML and JavaScript to visualize a Google Map.  It reads the most recent data in where.js to get the data to be visualized.
