# python-rest-api
rest api for handeling crud in blogs or cms systems.

#Still being worked on. Adding features like updating users and updating posts and adding a password reset functionality and more etc..., It is not ready to be used yet.


## Setup
To run this project, you would have to clone this repository onto your server or host and install the requirements.txt.

 ```
 $ pip3 install -r requirements.txt
 ```
 
 ## Endpoints
 ```
 /v1/newuser
 
 Method: POST
 
 Parameters: email, password, name , admin , apikey
 
 Sample request: http://127.0.0.1:4000/v1/newuser?email=email&password=password&name=name&admmin=admin&api_key=your_api_key
 
 The admin parameter is the admins username who is making the request and the api key is the api key which corresponds with the admins username. All the user passwords will be hashed aswell.
 
 There are many more routes and I will be updating this readme.md more soon.
 ```
 
