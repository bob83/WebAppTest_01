# WebAppTest_01
This project is a simple  CLI module that can generate JSON test data  and Send that data as a POST to a Web sign-up form. The default Schema for JSON is 
{
    "firstName": "Michael",
    "lastName": "Brady",
    "Address": ["11222 Dilling St , North Hollywood, CA 91602"],
    "phoneNumber": 323-555-1234,
    "children": [
        {
            "firstName": "Greg",
            "age": 10
        },
        {
            "firstName": "Marcia",
            "age": 8
        }
    ]
}

 

Usage: 
WebAppTest -- p (port) default 8080
           -- f  (fqdn of webservice) default  "https://reqres.in/api/users"
           -- n (number of users) default 10
           -- c (children used in Json; yes, n) default n
           --nc (number if children used in Json) default 2
           
