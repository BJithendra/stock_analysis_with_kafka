# stock_analysis_with_kafka
Parsing the google finance website and using kafka to create a topic between producer and consumer and store the values in mysql later for data analysis

In this project we parse the www.google.com/finance website and get the real time value of stock/ticker and store the values in mysql with schema ticker ,price, timestamp to do this we need
1.Apache Kafka
2.VS Code
3.Mysql
I recommend to download kafka in Linux or You are using the windows better use WSL(Windows sub linux ).
After installation of kafka follow these steps
  1. create a random uuid
  2. format the kafka-storage.sh files
  3. start the kafka server
Requirements in pyhton
  1. bs4
  2. kafka-pyhton
  3. mysql-connector
Create a topic in Kafka in which producer and consumer send messages.
Run the kafkaprod.py first and then Kafkacon.py
You have completed the applicatioin of kafka.
