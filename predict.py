import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

# input data

input_dict = {'age': 67,
              'sex': 'Male',
              'cp': 'asymptomatic',
              'trestbps': 120.0,
              'chol': 229.0,
              'fbs': 'False',
              'restecg': 'lv hypertrophy',
              'thalch': 129.0,
              'exang': 'True',
              'oldpeak': 2.6,
              'slope': 'flat'}


def model_request(input_dict, server_url='http://localhost:8082/data/'):
    '''
    Функция отправляет данные на инференс и получает результаты

    Параметры:
    input_dict (dict): Словарь с данными для инференса
    server_url (str): URL-адрес сервера

    Результат:
    dict: Словарь с результатом завпроса
    '''
    try:
        response = requests.get(server_url, params=input_dict)
        response.raise_for_status()
        data = response.json()
        result = {'data': data['predicted'][0], 'result': True}
    except requests.exceptions.RequestException as e:
        logger.error(e)
        result = {'result': False}
    return result


if __name__ == '__main__':
    predicted = model_request(input_dict)
    if predicted['result']:
        print('Предсказанный результат -', predicted['data'])
    else:
        print('Server error')
