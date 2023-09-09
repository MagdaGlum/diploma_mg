import requests
import config
import data

def create_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json=body,
                         headers=data.headers)
response = create_new_order(data.order_body);
print(response.status_code)
print(response.json())

def get_order_track():
    order_body = data.order_body
    response = create_new_order(order_body)
    return response.json()['track']
#print(response.json()['track'])

def get_order_info():
    number = get_order_track()
    return requests.get(config.URL_SERVICE + config.GET_ORDER_INFO + '?t=' + str(number))

response = get_order_info();
print(response.status_code)
print(response.json())

