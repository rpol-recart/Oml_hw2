from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Request
import pickle
import pandas as pd

with open('predict_pipeline.pkl','rb') as f:
    model=pickle.load(f)



    


app = FastAPI()
@app.get("/")
async def root():
    return {"greeting":""}

@app.get("/data/")
async def clasiify(age: int,
                    sex:str,
                    cp:str,
                    trestbps:float,
                    chol:float,
                    fbs: str,
                    restecg:str,
                    thalch:float,
                    exang: str,
                    oldpeak: float,
                    slope: str):
    results = {'age': age,
                'sex':sex,
                'cp':cp,
                'trestbps':trestbps,
                'chol':chol,
                'fbs': fbs,
                'restecg':restecg,
                'thalch':thalch,
                'exang': exang,
                'oldpeak': oldpeak,
                'slope': slope}
    data=pd.DataFrame(results,index=[0])
    res=model.predict(data).tolist()
    print(res)
    
    return {'predicted':res}
