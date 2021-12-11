# Expense Tracker
The target of our project is to create an expense tracker that could do two of the followings. First, it can record the user's expense and its details (category, amount, and description). Second it can display the expenses in table and graph for better visualization.


## Installation
There are a few packages needed in order for the code to work. Install flask, flask-table, matplotlib, and sqlite3 in order to run the code.

Here are the following modules:
```bash
  pip install flask
  pip install flask-table
  pip install matplotlib
  pip install pysqlite3
```

# Execution
Run the app.py file and it will show an IP address for the project's website.

## Content 
### app.py
This python folder is used for several functions, which mainly are used to create a table and collect the data from the user. This folder uses the sqlite3 package, which is used to connect the database in order to execute the code.
### table.py
This python folder is used to generate a table output filled with the information provided by the user. This folder uses flask_table package, which is used to display the table in the flask.
### bar_chart.py
This python folder is used to filter the necessary information (amount and category) from the user's input in order to generate a bar graph of total expense ($) per category based on the information provided. This folder uses matplotlib package to help create the graph.
### line_chart.py
This python folder is used to filter the necessary information (amount and date) from the user's input in order to generate a line chart of total expense ($) during different time based on the information provided. This folder uses matplotlib package to help create the graph.
### app.py
This python folder is used to set up the website and route each link to their respective html file. This folder uses the flask and sqlite3 package.
### templates
The templates file include multiple html files that is used to design the website. Files explainarion is as followed: main_page.html (home page), new_entry_form.html (form page for the user to fill out their expense), entry_success.html (redirect the page to result if entry is successful), entry_fail.html (shows error message if information is lacking), results.html (page that shows the result in table), delete.html (page to delete all of the previous data), and graph.html (page to show the graph).
### static
This file is to save the image output from the bar_chart.py and line_chart.py
