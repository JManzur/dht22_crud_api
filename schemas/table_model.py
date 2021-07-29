from typing import Optional
from pydantic import BaseModel

class DHT22Model(BaseModel):
        id: Optional[str]
        timestamp: Optional[str]
        temperature: str
        humidity: str