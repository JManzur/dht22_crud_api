from fastapi import APIRouter
from config.db import conn
from models.dht22_model import sensor_data

dht22 = APIRouter()

#GET all Sensor Data
@dht22.get("/dht22")
def get_all():
    return conn.execute(sensor_data.select()).fetchall()

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
@dht22.put("/dht22")
def put_sensordata():
    return "This will create all records"

#Delete records older than 24 hours
@dht22.delete("/dht22/{}")
def del_sensordata():
    return "This will delete records older than 24 hours"