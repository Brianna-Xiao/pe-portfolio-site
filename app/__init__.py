import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

TRAVEL_LOCATIONS = [
    {
        "name": "Toronto, Canada",
        "latitude": 43.6532,
        "longitude": -79.3832,
        "description": (
            "My hometown and the place where many of my academic, creative, and community "
            "experiences began."
        ),
    },
    {
        "name": "London, Ontario, Canada",
        "latitude": 42.9849,
        "longitude": -81.2453,
        "description": (
            "Home of Western University, where I study Computer Science and continue building "
            "projects and communities."
        ),
    },
    {
        "name": "Xi'an, China",
        "latitude": 34.3416,
        "longitude": 108.9398,
        "description": (
            "A city that shaped part of my childhood and helped me stay connected to my "
            "cultural background."
        ),
    },
    {
        "name": "Beijing, China",
        "latitude": 39.9042,
        "longitude": 116.4074,
        "description": "A city I have visited for its history, culture, and energy.",
    },
    {
        "name": "Shanghai, China",
        "latitude": 31.2304,
        "longitude": 121.4737,
        "description": (
            "A city that represents technology, business, and modern urban life in China."
        ),
    },
    {
        "name": "Hangzhou, China",
        "latitude": 30.2741,
        "longitude": 120.1551,
        "description": "A beautiful city known for West Lake, culture, and scenery.",
    },
    {
        "name": "Guangzhou, China",
        "latitude": 23.1291,
        "longitude": 113.2644,
        "description": "A southern Chinese city I have visited and explored.",
    },
    {
        "name": "Shenzhen, China",
        "latitude": 22.5431,
        "longitude": 114.0579,
        "description": (
            "A city known for innovation, startups, technology, and rapid growth."
        ),
    },
    {
        "name": "Japan",
        "latitude": 35.6762,
        "longitude": 139.6503,
        "description": (
            "A place I have traveled to and enjoyed for its culture, food, design, and city life."
        ),
    },
    {
        "name": "Thailand",
        "latitude": 13.7563,
        "longitude": 100.5018,
        "description": (
            "A country I have traveled to and enjoyed for its warm atmosphere, food, and "
            "beautiful destinations."
        ),
    },
    {
        "name": "San Francisco, United States",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "description": "A city connected to technology, startups, and innovation.",
    },
    {
        "name": "Seattle, United States",
        "latitude": 47.6062,
        "longitude": -122.3321,
        "description": "A city known for technology, coffee culture, and scenic views.",
    },
    {
        "name": "Los Angeles, United States",
        "latitude": 34.0522,
        "longitude": -118.2437,
        "description": (
            "A city I have visited for its entertainment, creativity, and culture."
        ),
    },
]


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        locations=TRAVEL_LOCATIONS,
    )
