# ---------------------------------------------------------------------------
# Edit the values below to update the site. Empty strings ("") are hidden.
# ---------------------------------------------------------------------------

profile = {
    "name": "Ashley",
    "tagline": "Business & Technology Builder",
    "intro": "Dedicated to building modern, thoughtful digital experiences. Explore my journey and portfolio below.",
    "photo": "default/logo.jpeg",
    "resume": "",  # e.g. "resume.pdf" placed in app/static/
}

contact = {
    "email": "",      # e.g. "you@example.com"
    "linkedin": "",   # e.g. "https://www.linkedin.com/in/your-handle"
    "github": "https://github.com/ashywen",
}

about_me = [
    {
        "about": "Hi! My name is Ashley. I am passionate about technology and business, creating modernized solutions to existing systems.",
        "images": ["default/logo.jpeg"]
    }
]

work_experience = [
    {
        "role": "Web Developer Intern",
        "company": "Startup Company",
        "dates": "",  # e.g. "2024 - 2025"
        "description": "Built CMS-based websites and improved UI components for the soft launch of an AI product.",
        "highlights": []  # optional bullet points, e.g. ["Shipped X", "Improved Y"]
    }
]

education = [
    {
        "school": "Ivey Business School",
        "program": "Business Administration",
        "year": "3rd Year"
    },
    
    {
        "school": "Western University",
        "program": "Computer Science",
        "year": "1st and 2nd Year"
    }
]

hobbies = [
    {
        "name": "Café Discovery",
        "images": [
            "hobbies/Cafes1.jpg",
            "hobbies/Cafes2.jpg",
            "hobbies/Cafes3.jpg",
            "hobbies/Cafes4.jpg",
            "hobbies/Cafes5.jpg"
        ]
    },
    {
        "name": "Makeup",
        "images": [
            "hobbies/Makeup.jpg"
        ]
    }
]

travel = [
    {
        "name": "Map",
        "images": ["hobbies/Travel.png"]
    }
]

# Add your projects here. "image" is relative to app/static/img/ (optional).
projects = [
    # {
    #     "name": "Project Name",
    #     "description": "One or two sentences about what it does.",
    #     "tech": "Flask, Docker, MySQL",
    #     "live": "https://...",
    #     "github": "https://github.com/...",
    #     "image": "projects/screenshot.png",
    # },
    {
        "name": "Personal Portfolio",
        "description": "This site: a Flask app with a timeline API, containerized with Docker and deployed with CI/CD.",
        "tech": "Flask, Jinja, Docker, MySQL, GitHub Actions",
        "live": "",
        "github": "https://github.com/ashywen/pe-portfolio-site",
        "image": "",
    },
]

pages = [
    {"name": "Home", "endpoint": "home"},
    {"name": "Hobbies", "endpoint": "hobbies_page"},
    {"name": "Timeline", "endpoint": "timeline"}
]