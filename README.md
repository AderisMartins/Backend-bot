How to run
Add project path at PYTHONPATH variable in .env file.

Start postgres database and pgadmin

docker-compose up -d
Start environment

pipenv shell
Install python dependencies

pipenv install
Populate database

python populate.py
Start application

uvicorn main:app --port 8080
Compare sync and async views
There are two versions of assets/day_summary endpoint, so you can compare both performance.
