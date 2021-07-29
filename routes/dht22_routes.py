from fastapi import APIRouter
from config.db import conn
from models.dht22_model import dht22_table
from schemas.sensor_data import DHT22Model

dht22 = APIRouter()

#GET all Sensor Data
@dht22.get("/dht22")
def get_all():
    return conn.execute(dht22_table.select()).fetchall()

#GET temperature records
@dht22.get("/dht22/temperature")
def get_temp():
    return "This will show all temperature records"

#GET humidityrecords
@dht22.get("/dht22/humidity")
def get_humd():
    return "This will show all humidity records"

#GET timestamp recors
@dht22.get("/dht22/timestamp")
def get_timestamp():
    return "This will show all timestamp records"

#Insert records from DHT22 sensor
@dht22.post("/dht22")
def post_sensordata(sensor_data: DHT22Model):
    post_data = {
        "id": sensor_data.id, 
        "timestamp": sensor_data.timestamp,
        "temperature": sensor_data.temperature,
        "humidity": sensor_data.humidity
    }
    result = conn.execute(dht22_table.insert().values(post_data))
    print(result)
    return "This will create all records"

#Delete records older than 24 hours
@dht22.delete("/dht22/{}")
def del_sensordata():
    return "This will delete records older than 24 hours"