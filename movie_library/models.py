from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list)
    watched: bool = None
    rating: int = 0
    tags: list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None


@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: list[str] = field(default_factory=list)
