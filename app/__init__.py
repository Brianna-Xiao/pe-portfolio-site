import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

PAGES = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Hobbies", "endpoint": "hobbies"},
]

HOBBIES = [
    {
        "name": "Debate",
        "description": (
            "Debate has been one of the most influential activities in my life. Over the past "
            "six years, I have competed in dozens of tournaments and taken on leadership roles "
            "that allowed me to mentor younger students and help organize events. What I enjoy "
            "most about debate is the combination of critical thinking, communication, and "
            "problem-solving. Every round challenges me to analyze complex issues, think on my "
            "feet, and communicate ideas clearly under pressure. Beyond competitions, debate has "
            "helped me build confidence, develop leadership skills, and connect with people from "
            "diverse backgrounds."
        ),
        "image": "img/debate.jpg",
    },
    {
        "name": "Violin",
        "description": (
            "I have been playing the violin since I was young, and it remains one of my favorite "
            "creative outlets. Learning an instrument taught me discipline, patience, and the "
            "value of consistent practice. I enjoy both the technical side of mastering difficult "
            "pieces and the artistic side of interpreting music and expressing emotion through "
            "performance. Playing violin has given me an appreciation for lifelong learning and "
            "has been a constant part of my life alongside academics and technology."
        ),
        "image": "img/violin.jpg",
    },
    {
        "name": "Visual Art",
        "description": (
            "Visual art is one of the ways I explore creativity outside of programming. I enjoy "
            "sketching, digital illustration, and experimenting with different styles and mediums. "
            "Art allows me to communicate ideas visually and approach problems from a different "
            "perspective. Whether I am designing graphics, drawing for fun, or creating layouts "
            "for projects, visual art has strengthened my attention to detail and creative "
            "thinking. It also serves as a balance to the more technical aspects of computer "
            "science."
        ),
        "image": "img/art.jpg",
    },
]


@app.context_processor
def inject_pages():
    return {"pages": PAGES}


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hobbies",
        url=os.getenv("URL"),
        hobbies=HOBBIES,
    )
