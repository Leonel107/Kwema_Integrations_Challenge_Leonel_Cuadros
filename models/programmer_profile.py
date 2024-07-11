from pydantic import BaseModel
from typing import Optional

class Programmer_Profiles(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    language_1: str
    language_2: str
    language_3: str
    Repository_Most_Metged_Pull_Requests_1: str
    Repository_Most_Metged_Pull_Requests_2: str
    Repository_Most_Metged_Pull_Requests_3: str