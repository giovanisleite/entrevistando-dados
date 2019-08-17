import requests


API_URL = (
    'https://jarbas.serenata.ai/api/chamber_of_deputies/reimbursement/'
    '?format=json&month=2&state=PR&subquota_number=13&year=2019'
)


def get_data():
    print('Start extracting')
    response = requests.get(API_URL)
    receipts = []
    while(True):
        data = response.json()
        receipts += data.get('results', [])
        next_page = data.get('next', False)
        if next_page:
            response = requests.get(next_page)
        else:
            break
    print('Finish extracting')
    return receipts
