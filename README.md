# meal-companion

## From scratach

```
cd backend
```
Linux:
```
python3 -m venv venv
./venv/bin/activate
```
Windows:
```
py -3 -m venv venv
.\venv\Scripts\activate
```
Then install flask
```
pip3 install flask
```

To init database before application starts run `flask init-db`


## Run Application

### In DEVELOPMENT mode

Setup backend:
Windows PowerShell
```
cd .\backend\
.\venv\Scripts\activate.ps1
$env:FLASK_APP = "main"
$env:FLASK_ENV = "development"
flask run
```

Frontend:
To run tests: `npm test`
To start development app: `npm start`