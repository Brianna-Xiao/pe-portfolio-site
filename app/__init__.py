import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from peewee import (
    CharField,
    DateTimeField,
    Model,
    MySQLDatabase,
    SqliteDatabase,
    TextField,
)
from playhouse.shortcuts import model_to_dict

load_dotenv()

app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect(reuse_if_open=True)
mydb.create_tables([TimelinePost], safe=True)

PAGES = [
    {
        "name": "Home",
        "endpoint": "index",
        "sections": [
            {"name": "About Me", "anchor": "about"},
            {"name": "Education", "anchor": "education"},
            {"name": "Work Experience", "anchor": "work-experience"},
            {"name": "Travel Map", "anchor": "travel-map"},
        ],
    },
    {
        "name": "Hobbies",
        "endpoint": "hobbies",
    },
    {
        "name": "Timeline",
        "endpoint": "timeline",
    },
]

WORK_EXPERIENCES = [
    {
        "company": "CIBC",
        "role": "Software Engineering Intern",
        "description": (
            "Contributed to backend and infrastructure-focused projects supporting production "
            "banking services. Worked with Go and Java to build and improve reliable backend "
            "components, with a focus on scalability, latency, and service reliability. Used "
            "Redis for caching strategies and Kubernetes for containerized deployments, and "
            "helped with latency testing, performance analysis, monitoring, and troubleshooting "
            "production-style systems."
        ),
    },
    {
        "company": "TLN Media Group",
        "role": "Web Developer",
        "description": (
            "Developed responsive web pages and dynamic media features using React, JavaScript, "
            "HTML/CSS, and backend services. Worked with REST APIs, MongoDB, Redis, and "
            "deployment tools to improve content management, media playback, and site performance."
        ),
    },
    {
        "company": "Vita Learning",
        "role": "Software Developer",
        "description": (
            "Designed and built backend services using Spring Boot, Spring MVC, Spring Cloud, "
            "Kafka, MongoDB, and PostgreSQL. Worked in a Scrum environment and contributed to "
            "microservice architecture, documentation, and live lecture recording features."
        ),
    },
    {
        "company": "Toronto Global Spotlight",
        "role": "Marketing Specialist",
        "description": (
            "Organized community-focused initiatives and helped run a large-scale fundraising "
            "tournament that raised over $1,700 for Toronto refugee centers. Collaborated with "
            "community leaders to promote social impact projects."
        ),
    },
]

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


@app.context_processor
def inject_pages():
    return {"pages": PAGES}


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Brianna Xiao",
        url=os.getenv("URL"),
        work_experiences=WORK_EXPERIENCES,
        education=EDUCATION,
        locations=TRAVEL_LOCATIONS,
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Hobbies",
        url=os.getenv("URL"),
        hobbies=HOBBIES,
    )

@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    content = request.form.get("content", "").strip()

    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if "@" not in email:
        return "Invalid email", 400

    timeline_post = TimelinePost.create(
        name=name,
        email=email,
        content=content,
    )

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_post():
    timeline_posts = (
        TimelinePost.select()
        .order_by(TimelinePost.created_at.desc())
    )

    return {
        "timeline_posts": [
            model_to_dict(post)
            for post in timeline_posts
        ]
    }

@app.route("/timeline")
def timeline():
    return render_template(
        "timeline.html",
        title="Timeline",
        url=os.getenv("URL"),
    )