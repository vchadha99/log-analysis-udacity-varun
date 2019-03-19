# Log-Analysis

### Project Overview
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

#### PreRequisites:
  * Python3
  * Vagrant
  * VirtualBox

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.

#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:

  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

  2. Use `psql -d news` to connect to database.

  3. Create view id_table using for top three articles:
  ```
    create view id_table as select title, count(*) as reads from articles
    join log on substr(log.path , 10) like articles.slug
     group by title order by reads desc
  ```
  | Column  | Type    |
  | :-------| :-------|
  | title   | text    |
  | reads   | Integer |

  4. Create view id2_table using for top authors:
  ```
  create view id1_table as select authors.name, count(*) as reads from articles
  join authors on authors.id = articles.author join log on substr(log.path, 10)
  like articles.slug group by authors.name order by reads desc
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | name          | text    |
  | reads         | Integer |

  4. Create view error_table using for top authors:
  ```
  create view error_table as select date(time) as day,
  count(*) filter (where status like '4%') * round(100.0 / count(*), 3) as
  error_rate from log group by day having (count(*)
  filter(where status like '4%') * 100 / count(*)) > 1")
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | date          | date    |
  | error_rate    | decimal |

#### Project Dependencies And How To Run
>This code assumes that you have latest python compiler that is python 3 and pycodestyle you can install the pycodestyle tool to test this, with "pip install pycodestyle" or "pip3 install" pycodestyle . Keep this project folder in vagrant folder and with news database and run "python projectlogvarun.py" in the directory where python soure code is presend.
# log-analysis-udacity-varun
