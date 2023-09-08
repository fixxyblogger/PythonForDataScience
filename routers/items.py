from fastapi import APIRouter
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn import tree


router = APIRouter()


@router.get("/items/", tags=["items"])
async def read_items():
    iris = datasets.load_iris()
   # Let's convert to dataframe
    iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['species'])
    # replace the values with class labels
    iris.species = np.where(iris.species == 0.0, 'setosa', np.where(iris.
                                                                    species == 1.0, 'versicolor', 'virginica'))
    # let's remove spaces from column name
    iris.columns = iris.columns.str.replace(' ', "")
    print(iris.value_counts())
    return iris
