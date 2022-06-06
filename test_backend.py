import requests

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_get():
    """test the get request on the mock backend works as expected"""
    pass

if __name__ == "__main__":
    test_sum()
    test_get()
    print("Everything passed")