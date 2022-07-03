
# Token based user authentication 
# fetch('http://<base-url>/api/method/frappe.auth.get_logged_user', {
#     headers: {
#         'Authorization': 'token api_key:api_secret'
#     }
# })
# .then(r => r.json())
# .then(r => {
#     console.log(r);
# })
#curl http://<base-url>/api/method/frappe.auth.get_logged_user -H "Authorization: token api_key:api_secret"



# Password Based Authentication
# fetch('http://<base-url>/api/method/login', {
#     method: 'POST',
#     headers: {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#     },
#     body: JSON.stringify({
#         usr: 'username or email',
#         pwd: 'password'
#     })
# })
# .then(r => r.json())
# .then(r => {
#     console.log(r);
# })
# curl --cookie-jar snowcookie --request POST "http://<base-url>/api/method/login" -H 'Content-Type: application/json' -H 'Accept: application/json' --data-raw "{ \"usr\" : \"<username>\", \"pwd\": \"<password>\" }"
# {"message":"Logged In","home_page":"/app","full_name":"<user:full_name>","dashboard_route":"/sites"}

# ➜ curl --cookie snowcookie --request POST "http://<base-url>/api/method/frappe.auth.get_logged_user" -H 'Accept: application/json'
# {"message":"<username>"}



# Access Token
# fetch('http://<base-url>/api/method/frappe.auth.get_logged_user', {
#     headers: {
#         'Authorization': 'Bearer access_token'
#     }
# })
# .then(r => r.json())
# .then(r => {
#     console.log(r);
# })


# Listing Documents 
# GET /api/resource/:doctype
# GET /api/resource/:doctype?fields=["field1", "field2"]






# CRUD Operations
# headers
# {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }


# Create
# POST /api/resource/:doctype
# Body
# {"description": "New ToDo"}

# Read
# GET /api/resource/:doctype/:name

# Update
# PUT /api/resource/:doctype/:name
# Body
# {"description": "New description"} #just send the field you want to update


# Delete
# DELETE /api/resource/:doctype/:name


# Remote Method Calls
# GET /api/method/frappe.auth.get_logged_user



# File Uploads
# There is a dedicated method    /api/method/upload_file     that accepts binary file data and uploads it into the system.
#  curl -X POST \
#   http://<base-url>/api/method/upload_file \
#   -H 'Accept: application/json' \
#   -H 'Authorization: token xxxx:yyyy' \
#   -F file=@/path/to/file/file.png
