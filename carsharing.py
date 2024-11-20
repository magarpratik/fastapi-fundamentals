from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [
    { 'id': 1, 'size': 's', 'fuel': 'petrol', 'doors': 3, 'transmission': 'auto' },
    { 'id': 2, 'size': 's', 'fuel': 'electric', 'doors': 3, 'transmission': 'auto' },
    { 'id': 3, 'size': 's', 'fuel': 'petrol', 'doors': 5, 'transmission': 'manual' },
    { 'id': 4, 'size': 'm', 'fuel': 'electric', 'doors': 3, 'transmission': 'auto' },
    { 'id': 5, 'size': 'm', 'fuel': 'hybrid', 'doors': 5, 'transmission': 'auto' },
    { 'id': 6, 'size': 'm', 'fuel': 'petrol', 'doors': 5, 'transmission': 'manual' },
    { 'id': 7, 'size': 'l', 'fuel': 'diesel', 'doors': 5, 'transmission': 'manual' },
    { 'id': 8, 'size': 'l', 'fuel': 'electric', 'doors': 5, 'transmission': 'auto' },
    { 'id': 9, 'size': 'l', 'fuel': 'hybrid', 'doors': 5, 'transmission': 'auto' },
]

@app.get('/')
def welcome():
    return 'Hello World!'

@app.get('/ping')
def pong():
    return 'Pong'

@app.get('/now')
def now():
    return { 'now': datetime.now() }

@app.get('/api/cars')
def cars(size: str|None = None, doors: int|None = None) -> object:
    cars = db

    if size:
        cars = [car for car in cars if car['size'] == size]

    if doors:
        cars = [car for car in cars if car['doors'] >= doors]

    return { 'data': cars }

@app.get('/api/cars/{id}')
def carById(id: int):
    result = [car for car in db if car['id'] == id]

    if len(result) == 0:
        raise HTTPException(status_code=404, detail=f'car with id {id} does not exist')

    return result[0]