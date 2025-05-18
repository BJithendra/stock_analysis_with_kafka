from kafka import KafkaProducer
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import json
import time
ist=ZoneInfo('Asia/Kolkata')
def get_stock_price():
    now = datetime.now()
    b=now.strftime('%B')
    ticker='BTC-USD'
    last_price=0.00
    url=f'https://www.google.com/finance/quote/{ticker}'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    class1="zQTmif SSPGKf u5wqUe"
    p=soup.find(class_=class1).text
    if "(BTC / USD)" in p:
        index1=p.find("(BTC / USD)")
        p = p[index1:].strip()
    if '.' in p:
        index2=p.find(b)
        p=p.replace(b,'#')
        p=p[:index2].strip()
    if ')' in p:
        index1=p.find(')')
        p=p[index1+1:].strip()
    if ',' in p:
        p=p.replace(',',"")
        p=float(p)
    if last_price!=p:
        print(p)
        last_price=p
    return {
            "Ticker":ticker,
            "Price": p,
            "time": datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

        }

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
while True:
    stock_data = get_stock_price()
    print("Sending to Kafka:", stock_data)
    producer.send("stock_price_topic", stock_data)
    time.sleep(20)
