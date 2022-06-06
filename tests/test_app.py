import json

def test_request_example(client):
    """Test basic root route"""
    response = client.get("/")
    assert b"Try /appointments or /profiles" in response.data

def test_appointments(client):
    """Test appointments route"""
    f = open("mock_data.json")
    data = json.load(f)
    appointments = []
    for i in data["appointments"]:
        appointments.append(data["appointments"][i])
    response = client.get("/appointments")
    assert b"profile_requestor_pk" in response.data
    
def test_profiles(client):
    """Test profiles route"""
    f = open("mock_data.json")
    data = json.load(f)
    profiles = []
    for i in data["profiles"]:
        profiles.append(data["profiles"][i])
    response = client.get("/profiles")
    assert b"1" in response.data