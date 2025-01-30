# FooFi API

FooFi API is a Django-based REST API that allows users to manage their tasks. Each user must first **create an account**, log in to obtain an **authentication token**, and then use that token to create, view, or modify their tasks.

## Getting Started

### 1. Clone the Project
Download the project and navigate into the directory:

```bash
git clone https://github.com/p-yavari/FooFi-API.git
cd FooFi-API
```
### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```
pip install -r requirements.txt
```
### 3. Apply Migrations
Before using the API, set up the database:
```
python manage.py migrate
```
### 4. Create a Superuser (Optional)
If you want access to the Django admin panel, create a superuser:
```
python manage.py createsuperuser
```
### 5. Start the API
Run the API server:
```
python manage.py runserver
```
By default, the server runs on `http://127.0.0.1:8000/`.

## Authentication & Tokens
### Step 1: Create an Account
Before making API requests, you must **create a user account** using the `/profile/` endpoint.

#### Example Request (POST `/profile/`):
```
{
    "email": "user@example.com",
    "name": "John Doe",
    "password": "securepassword"
}
```
### Step 2: Log In & Get a Token
Once your account is created, log in via the `/login/` endpoint to receive your **authentication token**.

#### Example Request (POST `/login/`):
```
{
    "username": "user@example.com",
    "password": "securepassword"
}
```
#### Example Response:
```
{
    "token": "your-generated-token-here"
}
```
### Step 3: Use the Token in Requests
Include this token in the **Authorization header** of all requests to access your tasks:
```
Authorization: Token your-generated-token-here
```
## API Endpoints
### User Authentication
- `POST /profile/` → Create a new user account
- `POST /login/` → Get an authentication token
## Task Management (Requires Authentication)
- `GET /tasks/` → View all tasks you have created
- `POST /tasks/` → Create a new task
- `GET /tasks/{id}/` → Get details of a specific task
- `PUT /tasks/{id}/` → Update a task
- `DELETE /tasks/{id}/` → Delete a task
## Database & Migrations
- The first time you set up the project, **you must run migrations:**
```
python manage.py migrate
````
- If new models or fields are added in the future, migrations must be applied again.

## Running the Server on a Different Port
If you need to change the default port (8000), specify it when running the server:
```python manage.py runserver 8080  # Runs on port 8080```
## Final Notes
- Every request that modifies or views tasks **requires authentication.**
- The token is **unique to each user** and must be included in headers.
##
- If you get a **403 Forbidden** error, ensure you are **logged in and using the correct token.**

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or contributions, feel free to reach out at
[pooriayavari@yahoo.com](mailto:pooriayavari@yahoo.com).
