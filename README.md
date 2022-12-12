# TODO APP

    frontend: React
    backend: Flask
    db: Mongodb

## Steps to run project

### Step 1: Setup database

    docker pull mongo
    docker run --name=mongodb mongo
    docker inspect mongo (search for ip here)

    MONGO_URI= mongodb://{ip}:27017/{database name}

### Setup Backend

    cd backend
    python3 -m env .
    source ./env/bin/activate
    pip install flask
    pip install flask-mongo
    pip install virtualenv
    export FLASK_APP=app.py
    export FLASK_ENV=development
    
    flask run

### Setup Frontend

    cd client
    npm install
    npm start