## The software and data are required:
  This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from  [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and **logs_analysis.py** files from the respository and move them to your **vagrant** directory within your VM.
To build the reporting tool, you'll need to load the site's data into your local database. 

 Run these commands from the terminal in the folder where your vagrant is installed in:

1-```vagrant up``` to start up the VM.

2-```vagrant ssh``` to log into the VM.

3-```cd /vagrant``` to change to your vagrant directory.

4-```psql -d news -f newsdata.sql``` to load the data and create the tables.

5-```python3 logs_analysis.py ```to run the reporting tool.

## The questions the reporting tool should answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Helpful Resources

* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
