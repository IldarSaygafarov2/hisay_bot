import requests

from data.config import BASE_URL


def get_services():
    endpoint = BASE_URL + '/services'
    response = requests.get(endpoint).json()
    return response


def get_service_id(name):
    endpoint = BASE_URL + '/services/' + name
    service_id = requests.get(endpoint).json()
    return service_id


def get_service_name(service_id):
    endpoint = BASE_URL + f'/services/get/{service_id}/'
    res = requests.get(endpoint)
    return res.json()


def create_service_profile(service_data, file):
    endpoint = BASE_URL + '/service-profile/create/'
    requests.post(endpoint, data=service_data, files=file)


def get_service_profiles_ids():
    endpoint = BASE_URL + "/service-profiles/ids/"
    result = requests.get(endpoint).json()
    return result


def get_simple_users_profiles_ids():
    endpoint = BASE_URL + "/simple-users-profiles/ids/"
    result = requests.get(endpoint).json()
    return result


def create_simple_user(user_data):
    endpoint = BASE_URL + "/users/create/"
    requests.post(endpoint, data=user_data)


def create_user_request(request_data):
    endpoint = BASE_URL + "/services/create/"
    resp = requests.post(endpoint, request_data)


def check_verification_code(verification_code):
    endpoint = BASE_URL + f'/users/code/check/{verification_code}/'
    requests.post(endpoint)


def get_hashtags_by_service(service_id):
    endpoint = BASE_URL + f"/services/{service_id}/hashtags/"
    res = requests.get(endpoint)
    try:
        return res.json()
    except Exception as e:
        print(e, e.__class__)


def add_hashtags_to_service(service_id, tags_list):
    endpoint = BASE_URL + "/services/hashtags/add/"
    data = {
        "service_id": service_id,
        "tags_list": tags_list
    }
    requests.post(endpoint, data=data)


