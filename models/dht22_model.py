from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, DateTime
from config.db import meta, engine

dht22_table = Table("sensor_data", meta,
    Column("id", Integer, primary_key=True),
    Column("timestamp", DateTime),
    Column("temperature",Integer),
    Column("humidity", Integer))

meta.create_all(engine)