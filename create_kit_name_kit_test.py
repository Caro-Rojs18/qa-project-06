import sender_stand_request
import data

def positive_assert(kit_response, expected_status_code, name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == name

def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code

def test_kit_creation_1():
    # Numeros permitido de caracteres (1)
    kit_body = data.kit_bodies["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])


def test_kit_creation_2():
    # Numero de permitido de caracteres (511)
    kit_body = data.kit_bodies["Maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])


def test_kit_creation_3():
    # El numero de caracteres es menor a la permitida (0)
    kit_body = data.kit_bodies["Empty_string"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, expected_status_code=400)

 def test_kit_creation_3():
        # El numero de caracteres es mayor a la permitida (512)
        kit_body = data.kit_bodies["Maximum_plus_one_characters"]
        kit_response = sender_stand_request.post_new_client_kit(kit_body)
        negative_assert(kit_response, expected_status_code=400)
