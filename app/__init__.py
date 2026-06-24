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


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Brianna Xiao",
        url=os.getenv("URL"),
        work_experiences=WORK_EXPERIENCES,
    )
