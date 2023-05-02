import requests
"""Test of api.chucknorris.io"""
class test_new_joke:
    """Create new joke"""
    def __init__(self):
        pass
#     def create_new_random_joke(self):
#         """Create new random joke"""
#         url = "https://api.chucknorris.io/jokes/random"
#         print(url)
#         result = requests.get(url)
#         print("Status code : " + str(result.status_code))
#
#         if result.status_code == 200:
#             print("Success , we received new joke")
#         else:
#             print("Failure, request not successful")
#             result.encoding = 'utf-8'
#         print(result.text)
#         check = result.json()
#         check_info = check.get("categories")
#         print(check_info)
#         assert check_info == []
#         print("category is correct")
#
#         check_info_value = check.get("value")
#         print(check_info_value)
#         name = "Chuck"
#         if name in check_info_value:
#             print("Chusk is present")
#         else:
#             print("Chuck not present")
#
# random_joke = test_new_joke()
# random_joke.create_new_random_joke()