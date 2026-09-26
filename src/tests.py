from main import Calculator, create_app


def test_sums_2_numbers():
    assert Calculator().suma(2, 2) == 4


def test_resta_2_numbers():
    assert Calculator().resta(5, 3) == 2


def test_suma_api():
    client = create_app().test_client()
    response = client.get("/api/suma?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_resta_api_disabled_without_flag():
    client = create_app().test_client()
    response = client.get("/api/resta?a=5&b=3")
    assert response.status_code == 403