# flask_api_example_auth
A very simple and non-secure API authentication example flask application


# example auth request:

```bash
curl --location --request POST 'http://127.0.0.1:5000/auth' \
--header 'Content-Type: application/json' \
--data-raw '{
	"username":"Jose",
	"password":"mypassword"
}'
```

Example auth request return:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTA1OTI1NzMsImlhdCI6MTU5MDU5MjI3MywibmJmIjoxNTkwNTkyMjczLCJpZGVudGl0eSI6MX0.o3K7dHbgIKbTKI1ibuHcoJHBilbbStztFjh1YCn74mQ"
}
```

Example API call using token:

```bash
curl --location --request GET 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTA1OTI1NzMsImlhdCI6MTU5MDU5MjI3MywibmJmIjoxNTkwNTkyMjczLCJpZGVudGl0eSI6MX0.o3K7dHbgIKbTKI1ibuHcoJHBilbbStztFjh1YCn74mQ' \
--data-raw ''
```

Example authenticated API return:

```json
{
    "hello": "world"
}
````
