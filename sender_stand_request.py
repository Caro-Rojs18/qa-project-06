import configuration
import requests
import data

def post_new_user (body):
    return requests.post(
        configuration.URL_SERVICE +
        configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers,
    )

response = post_new_user(data.user_body)

def auto_token():
    user = post_new_user(data.user_body)
    user_json = user.json()

    return user_json['authToken']

def post_new_client_kit(kit_body_key):
    token = auto_token()
    headers = data.headers.copy()
    headers ['Authorization'] = f'Bearer {token}'

    kit_body = kit_body_key  # Kit adecuado

    return requests.post(
        configuration.URL_SERVICE +
        configuration.KITS_PATH,
        json=kit_body,
        headers=headers,
    )
