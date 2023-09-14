from pydantic import BaseModel, conlist
from typing import List


class Iris(BaseModel):
    data: List[conlist(float, min_length=1, max_length=4)]
