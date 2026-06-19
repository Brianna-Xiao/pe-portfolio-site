import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

EDUCATION = [
    {
        "school": "Western University",
        "location": "London, Ontario",
        "program": "Honours Specialization in Computer Science",
        "dates": "Expected Graduation: April 2028",
        "highlights": [
            "GPA: 3.9/4.0",
            (
                "Relevant Coursework: Object-Oriented Software Development, Data Structures and "
                "Algorithms, Algorithm Design and Data Abstraction, Information Systems and Design"
            ),
            (
                "Activities: Computer Science Undergraduate Society (VP Events), Western Founders "
                "Network (Director of Projects)"
            ),
            "Awards: SheHacks Best Beginner Hack, Hack Western Canada Life Track Winner",
        ],
    },
    {
        "school": "St. Robert Catholic High School",
        "location": "Markham, Ontario",
        "program": "International Baccalaureate (IB) Diploma Programme",
        "dates": "Graduated: 2024",
        "highlights": [
            "IB Score: 40/45",
            "Debate Club President",
            "DECA Head Trainer",
            "Social Justice Council Executive",
            "Model United Nations Organizer",
            (
                "Organized large-scale academic and leadership events for students across "
                "York Region"
            ),
        ],
    },
]


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        education=EDUCATION,
    )
