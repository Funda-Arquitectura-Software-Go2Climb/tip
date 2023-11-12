from pydantic import BaseModel
from typing import Optional
from datetime import date

class Tip(BaseModel):
    id: Optional[str]
    name: str
    description: str
    travel: int
    
