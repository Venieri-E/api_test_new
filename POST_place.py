import requests
class test_new_location:
    """"Work with new location"""
    def test_create_new_location(self):
        """"Create new location"""

        base_url = "https://rahulshettyacademy.com" # base URL
        key = "?key=qaclick123" # Parameter for all requests
        post_resourse = "/maps/api/place/add/json" # Resource of method POST

        post_url = base_url + post_resourse + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)

        print("Status code : " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Create new location - Successful")
        else:
            print("Failure, request not successful")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code of answer :" + check_info_post)
        assert check_info_post == "OK"
        print("Status of answer is correct")
        place_id = check_post.get("place_id")
        print("Place_ID : " + place_id)

        """"Check if new place is created"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Check of creating new location was successful")
            print("Status code = 200")
        else:
            print("Failure, request not successful")

        put_resourse = "/maps/api/place/update/json"  # Resource of method PUT
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location ={
            "place_id": place_id,
            "address": "100 Main street, US ",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url,json = json_for_update_new_location)
        print(result_put.text)
        print("Статус код :" + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Changing of  new location was successful")
        else:
            print("Failure, request not successful")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Message  : " + check_put_info)
        assert check_put_info == "Address successfully updated"

        result_get = requests.get(get_url)
        if result_get.status_code == 200:
            print("Status code = 200")
        else:
            print("Error")
        check_adress = result_get.json()
        check_adress_info = check_adress.get("address")
        print("Message  : " + str(check_adress_info))
        assert check_adress_info == "100 Main street, US "
        print("Adress correctt")

        """"Check if location is delete"""
        delete_resourse = "/maps/api/place/delete/json"  # Resource of method DELETE
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        if result_delete.status_code == 200:
            print("Status code = 200")
        else:
            print("Error")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Message  : " + str(check_status_info))
        assert check_status_info == "OK"
        print("Status correctt")

        """"Check if location was delete"""
        result_get = requests.get(get_url)
        print(result_get.text)
        assert  404 == result_get.status_code
        if result_get.status_code == 404:
            print("Succes deleted location")
        else:
            print("Error")
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        print("Message  : " + check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Testing of Test_new_location was sucessful")

new_place = test_new_location()
new_place.test_create_new_location()