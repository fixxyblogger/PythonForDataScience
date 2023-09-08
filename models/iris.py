from pydantic import BaseModel, conlist, confloat
from typing import List


class Iris(BaseModel):
    data: conlist(conlist(confloat(ge=0.0)))
