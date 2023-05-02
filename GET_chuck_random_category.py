import requests

"""Test of api.chucknorris.io"""
class test_new_joke:
    """Create new joke"""
    def __init__(self):
        pass
    def create_random_joke_by_category(self):
        """Create new random joke by category"""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        result = requests.get(url)
        print("Status code : " + str(result.status_code))
        print((url))
        if result.status_code == 200:
            print("Success , we received Sport joke")
        else:
            print("Failure, request not successful")
            result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Category Sport")

        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("name 'Chusk' is present")
        else:
            print("name 'Chuck' not present")

sport_joke = test_new_joke()
sport_joke.create_random_joke_by_category()