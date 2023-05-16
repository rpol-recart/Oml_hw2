FROM python:3.9
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./model/predict_pipeline.pkl /code/predict_pipeline.pkl
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app/main.py /code/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]