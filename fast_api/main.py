from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import HTMLResponse, JSONResponse
import time

app = FastAPI()

app.title = "Mi aplicacion de peliculas"
app.version = "0.0.1"

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

@app.get("/movies/", tags=['movies'])
def getMovieByCategory(category: str):
    moviesFiltered = [movie for movie in movies if movie['category'] == category]
    return moviesFiltered

@app.post("/movies", tags=['movies'])
def createMovie(id: int = Body(),
                title: str = Body(),
                overview: str = Body(),
                year: int = Body(),
                rating: float = Body(),
                category: str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put("/movies/editar/{id}", tags=['movies'])
def updateMovie(id: int,
                title: str = Body(),
                overview: str = Body(),
                year: int = Body(),
                rating: float = Body(),
                category: str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return movies

@app.delete("/movies/{id}", tags=['movies'])
def deleteMovie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies