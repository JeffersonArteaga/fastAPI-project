from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import HTMLResponse, JSONResponse

from jwt_manager import create_token
import time

app = FastAPI()

app.title = "Mi aplicacion de peliculas"
app.version = "0.0.1"


class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, max_length=50)
    overview: str = Field(min_length=20, max_length=300)
    year: int = Field(le=time.localtime().tm_year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=3, max_length=20)

movies = [
    {
        'id': 1,
        'title': 'Avento',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content="<h1>FastAPI</h1>", status_code=200)

@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code=200)
def getMovies() -> List[Movie]:
    return JSONResponse(content=movies, status_code=200)

@app.get("/movies/{id}", tags=['movies'], response_model=Movie, status_code=200)
def getMovie(id: int = Path(ge=1, le=2000)):
    movie = list(filter(lambda movie: movie['id'] == id, movies))
    if movie:
        response = JSONResponse(content=movie, status_code=200)
    else:
        response = JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return response

@app.get("/movies/", tags=['movies'], response_model = List[Movie])
def getMovieByCategory(category: str = Query(min_length=5, max_length=12)):
    movie = list(filter(lambda movie: movie['id'] == id, movies))

    if len(movie):
        response = JSONResponse(content=movie, status_code=200)
    else:
        response = JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return response


@app.post("/movies", tags=['movies'], response_model=dict, status_code=201)
def createMovie(movie: Movie):
    movies.append(movie)
    
    return JSONResponse(content={"message": "Movie created successfully"}, status_code=201)

@app.put("/movies/editar/{id}", tags=['movies'])
def updateMovie(movie: Movie):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = movie.title
            movie['overview'] = movie.overview
            movie['year'] = movie.year
            movie['rating'] = movie.rating
            movie['category'] = movie.category
    
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)

@app.delete("/movies/{id}", tags=['movies'], response_model=dict)
def deleteMovie(id: int):

    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)

    return JSONResponse(content={"messagge": "Movie deleted successfully"}, status_code=200)


@app.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User):
    if ((user.email == "admin@mail.com") and (user.password == "admin")):
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token": token}, status_code=200)

    else:
        result = JSONResponse(content={"message": "Inavlid credentials"}, status_code=401)
    
    return result