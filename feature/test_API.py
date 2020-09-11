import requests
import pytest
from endpoint.EndPointFactory import EndPoint


@pytest.mark.parametrize("country", EndPoint.COUNTRIES_ID)
def test_ContriesWithID(country):
    response = requests.get(EndPoint.BASE_URI_API + EndPoint.ENDPOINT_COUNTRY + f"{country}", verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    if country == 1096:
        assert data["name"] == "India"
    elif country == 1229:
        assert data["name"] == "United States of America"

def test_search():
    response = requests.get(EndPoint.BASE_URI_API + EndPoint.ENDPOINT_COUNTRY, params=f"q={EndPoint.SEARCH_TEXT}", verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    ID = data[1]
    print(ID)
    assert ID["name"] == "United States of America"
    assert ID["id"] == 1229


@pytest.mark.parametrize("cities", EndPoint.CITIES_ID)
def test_CitiesWithID(cities):
    response = requests.get(EndPoint.BASE_URI_API + EndPoint.ENDPOINT_CITIES + f"{cities}", verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    if cities == 1002:
        assert data["name"] == "Los Angeles"
    elif cities == 1004:
        assert data["name"] == "Chicago"


@pytest.mark.parametrize("movies", EndPoint.MOVIES_ID)
def test_MoviesWithID(movies):
    response = requests.get(EndPoint.BASE_URI_API + EndPoint.ENDPOINT_MOVIES + f"{movies}", verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    if movies == 1010:
        assert data["name"] == "A Farewell to Arms"
    elif movies == 1029:
        assert data["name"] == "Algiers"


@pytest.mark.parametrize("shows", EndPoint.SHOWS_ID)
def test_ShowsWithID(shows):
    response = requests.get(EndPoint.BASE_URI_API + EndPoint.ENDPOINT_SHOWS + f"{shows}", verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    if shows == 1001:
        assert data["name"] == "Bonanza"
    elif shows == 1030:
        assert data["name"] == "Stories of the Century"

