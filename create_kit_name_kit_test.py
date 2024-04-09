import sender_stand_request
import data

def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name

def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code != expected_status_code

def test_kit_creation_1():
    # Número permitido de caracteres (1)
    kit_body = data.kit_bodies["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])

def test_kit_creation_2():
    # Número permitido de caracteres (511)
    kit_body = data.kit_bodies["Maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])

def test_kit_creation_3():
    # El número de caracteres es menor a la permitida (0)
    kit_body = data.kit_bodies["empty_string"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, expected_status_code=400)

def test_kit_creation_4():
    # El número de caracteres es mayor a la permitida (512)
    kit_body = data.kit_bodies["Maximum_plus_one_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, expected_status_code=400)

def test_special_characters_5():
    # Cuerpo de la solicitud y la respuesta esperada
    kit_body = data.kit_bodies["name"] = '"№%@",'
    kit_response, response_data = sender_stand_request.post_new_client_kit(data=kit_body)
    # Ajusta los datos esperados según lo que devuelva la solicitud
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])

def test_spaces_allowed_6():
    # Se permiten espacios
    kit_body = data.kit_bodies["name"] = '"A Aaa "'
    kit_response, response_data = sender_stand_request.post_new_client_kit(data=kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])

def test_numbers_allowed_7():
    # Números permitidos
    kit_body = data.kit_bodies["name"] = '" 123 "'
    kit_response, response_data = sender_stand_request.post_new_client_kit(data=kit_body)
    positive_assert(kit_response, expected_status_code=201, expected_name=kit_body['name'])

def test_parameter_not_passed_8():
    # El cuerpo de la solicitud vacío
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, expected_status_code=400)

def test_different_parameter_type_9():
    # Solicitud con un tipo de parámetro diferente (número)
    kit_body = {"name": 123}
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, expected_status_code=400)

