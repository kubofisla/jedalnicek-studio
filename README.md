# meal-companion

## Docker deployment
Create ./frontend/.env.local file and provide API URL in REACT_APP_API_URL env variable. E.g:
```
vim ./frontend/.env.local
```
Put this content into it and replace \<API_SERVER_URL\> with url of backend server:
```
#API server proxy url
REACT_APP_API_URL=<API_SERVER_URL>
```

To deploy application (currently just in DEVELOPMENT mode) run following command:
```
docker compose up
```

## Environment Configuration
You can configure the ports used by docker compose by creating a `.env` file in the root directory.
This file is git ignored so you can have your own local configuration.

Example `.env` file content with default values:
```env
BACKEND_PORT=5000
FRONTEND_PORT=3000
```


## From scratach
Install python and pip: https://packaging.python.org/en/latest/tutorials/installing-packages/

```
cd backend
```
Linux:
```
python3 -m venv venv
. venv/bin/activate
```
Windows:
```
py -3 -m venv venv
.\venv\Scripts\activate
```
Then install flask and necessary libraries (backend)
```
pip3 install flask
pip3 install SQLAlchemy
pip3 install flask-cors
```
Front end
```
npm install
```

## Run Application

### In DEVELOPMENT mode

Start backend:
Windows PowerShell
```
cd .\backend\
.\venv\Scripts\activate
flask --app main --debug run --host=0.0.0.0
```
To init database before application starts run `flask --app main init-db`

Frontend:
To start development app:
```
cd .\frontend\
npm start
```
To run tests: `npm test`

