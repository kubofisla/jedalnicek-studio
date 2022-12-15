# meal-companion

## From scratach
Install python and pip: https://packaging.python.org/en/latest/tutorials/installing-packages/

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
flask --app main --debug run
```
To init database before application starts run `flask init-db`

Frontend:
To start development app:
```
cd .\frontend\
npm start
```
To run tests: `npm test`