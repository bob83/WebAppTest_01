import json
import jsonpath
from faker import Faker
import requests
from random import randint
import argparse

#create the data needed for post api
def main(name):
    fake = Faker()
    def create_data(child):
        data_nokid = {}
        data_kid = {}
        if child != 1:
            # create data set with all data request less chid
            data_nokid = {"first_name": fake.first_name(), "last_name": fake.last_name(),
                          "email": fake.company_email(), "address": fake.address(), "phone": fake.phone_number()}
            return data_nokid

        else:
            # create data set with all data required including child with age
            data_kid = {"first_name": fake.first_name(), "last_name": fake.last_name(),
                        "email": fake.company_email(), "address": fake.address(), "phone": fake.phone_number(),
                        "children": 1,"child_first": fake.first_name(), 
                        "child_last": fake.last_name(), "child_age": randint(1, 18)}
            return data_kid



    #api service to test json post
    api_url="https://reqres.in/api/users"
    #call create_data method to generater the correct dictionary
    post_dict = create_data(name)
    #use request.post method to sent post request to api tool
    resp = requests.post(api_url, data=post_dict)
    #Get response text then assert if returned status code is not successful (201)
    json_data = json.loads(resp.text)
    assert resp.status_code == 201
    print(resp.status_code)
    print(json_data)
    
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    	create a API post to web app with test data for a web signup form. use 0 for no child data
    	and 1 for child data.""")

    parser.add_argument("child", type=int, help='use 0 for no child and 1 for child')
    args = parser.parse_args()
    kid = args.child
    #print (kid)
    main(args.child)