from kafka import KafkaConsumer
import mysql.connector
import json
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Transfluthrin@1779",
    database="stocks"
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10),
    price FLOAT,
    timestamp DATETIME
)
""")

consumer = KafkaConsumer(
    'stock_price_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for messages...")

for message in consumer:
    data = message.value
    print("Inserting into MySQL:", data)
    cursor.execute(
        "INSERT INTO stock_prices (ticker, price, timestamp) VALUES (%s, %s, %s)",
        (data['Ticker'], data['Price'], data['time']) 
    )
    conn.commit()