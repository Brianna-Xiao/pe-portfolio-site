import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Brianna Xiao",
        url=os.getenv("URL"),
        work_experiences=WORK_EXPERIENCES,
        education=EDUCATION,
    )
