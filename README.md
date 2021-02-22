WebAppTest_01 
===================
## Project source can be downloaded from https://github.com/bob83/WebAppTest_01
## Author and Contributor List
Bob Ciulla
## File List
WebAppTest.py
## packages 
Faker
#### This project is a simple  CLI module that can generate  dictionary test data using random data from Faker()  and Send that data as a POST to a Web sign-up form. The default Schema for JSON is 

```JS

    "firstName": "Michael",
    "lastName": "Brady",
    "email": "mbrady@aol.com",
    "Address": ["11222 Dilling St , North Hollywood, CA 91602"],
    "phone": 323-555-1234,
    "children": 1 [
        {
            'child_first': "Greg",
            'child_last':  "Brady
            "age": 10
        }
    ]
```
 

## Usage: 
* WebAppTest 0 or 1. 0 for no child in post and 1 for adding a child in the post. The script will assert if a response code other than a 201 is received
           

## To do
add cli capability to change URL for api tool (easy)
iterate tru data to create x number of different requests. Where X is a cmd line agr for number if iterations
add default cli data to tool
Fix to indent children in post 
add docopt or other CLI data validation tool


