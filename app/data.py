# ---------------------------------------------------------------------------
# Edit the values below to update the site. Empty strings ("") are hidden.
# ---------------------------------------------------------------------------

profile = {
    "name": "Ashley",
    "full_name": "Ashley Deng",
    "tagline": "Business & Computer Science | Product, Data & Software",
    "intro": "Business Administration student at Ivey with a Computer Science foundation from Western, working where technology meets business.",
    "photo": "default/logo.jpeg",
    "resume": "",
}

contact = {
    "email": "adeng.canada06@gmail.com",
    "linkedin": "https://www.linkedin.com/in/ashleyhdeng/",
    "github": "https://github.com/ashywen",
}

about_me = [
    {
        "about": "I'm a Business Administration student at Ivey Business School with a Computer Science foundation from Western University. I work where technology meets business: turning data into decisions, shaping product strategy, and building software that solves real problems.",
        "images": ["default/logo.jpeg"]
    }
]

work_experience = [
    {
        "role": "IT Web Development Intern",
        "company": "Ontario Public Service",
        "location": "Toronto, ON",
        "dates": "May 2026 – Aug 2026",
        "description": "Built executive reporting and analytics for cross-ministry leadership, turning operational data into dashboards that guide budget and resourcing decisions.",
        "highlights": [
            "Translated ministry data into 6 decision-ready Power BI dashboards across executive, director, and operational reporting tiers, serving 50+ cross-ministry directors and managers.",
            "Defined and validated KPI criteria for a Benefits Realization dashboard tracking internal efficiency and resourcing across a $100M operations budget, informing executive decisions.",
            "Consolidated requirements from 30 ministries into an executive-facing report for the Secretary of the Cabinet and Deputy Minister, strengthening the Protect Ontario initiative, which serves 4 million citizens.",
            "Identified a manual reporting bottleneck and automated refresh cycles across 3 dashboards, saving 12 hours of maintenance per week.",
        ]
    },
    {
        "role": "Product Marketing Intern",
        "company": "Web Industrial Solutions – XEO",
        "location": "Markham, ON",
        "dates": "May 2025 – Aug 2025",
        "description": "Led go-to-market and web experience work for the soft launch of a website builder and SEO product.",
        "highlights": [
            "Planned and executed the soft launch of a website builder and SEO tool, generating 45 beta sign-ups at a 22% landing-page conversion rate and early validation of product-market fit.",
            "Redesigned the website experience using Drupal, HTML, and PHP, reducing bounce rate by 18%.",
            "Built and automated a 14-email lifecycle campaign in SendGrid, achieving a 62% retention rate.",
            "Managed content across 6+ social platforms, publishing 25 posts that grew each platform by an average of 250+ followers within two months.",
            "Analyzed organic performance data to optimize campaigns, lifting engagement by 15% and reducing cost-per-click by 12%.",
        ]
    },
]

education = [
    {
        "school": "Ivey Business School",
        "program": "Bachelor of Arts, Business Administration",
        "year": "Expected May 2028",
        "highlights": ["Advanced Entry Opportunity (AEO)"]
    },
    {
        "school": "Western University",
        "program": "Bachelor of Science, Computer Science",
        "year": "2024 – 2026",
        "highlights": [
            "Cumulative GPA: 3.8 / 4.0",
            "Western Scholarship of Distinction · Western Scholar (Dean's List)",
            "Coursework: Data Structures, Data Science, Decision-Making with Analytics, Finance, Calculus",
        ]
    },
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
# Set "coming_soon": True for a project that isn't public yet.
projects = [
    {
        "name": "HorseRacer",
        "meta": "Software Engineering Term Project · Jan – Apr 2026",
        "description": "A TypeRacer-inspired multiplayer typing game where each player's speed and accuracy drive a live horse race. Built by a 5-person team over 16 weeks and 10 agile sprints. As Scrum Master, I ran 12 sprint ceremonies, maintained the Gantt chart and dependency tracking, and owned requirements, scope, and risk documentation.",
        "tech": "Java, JavaFX, Maven, Agile / Scrum",
        "live": "",
        "github": "https://github.com/ashywen/HorseRacer",
        "devpost": "",
        "image": "",
    },
    {
        "name": "SafeSpeak",
        "meta": "SheHacks+ 10 Hackathon · Jan 2026",
        "description": "An AI safety app that simulates a realistic phone call to help women feel safer in rideshares and when travelling at night. It pairs Google Gemini for adaptive dialogue with ElevenLabs text-to-speech for a natural voice. We scoped and shipped the MVP in 36 hours, and I led UX/UI across 15 high-fidelity Figma screens.",
        "tech": "React Native, Expo, TypeScript, Google Gemini, ElevenLabs, Figma",
        "live": "",
        "github": "https://github.com/ashywen/safespeak",
        "devpost": "https://devpost.com/software/safespeak-4d6sfp",
        "image": "",
    },
    {
        "name": "Momentum",
        "meta": "In development",
        "description": "A new project currently in the works. Details coming soon.",
        "tech": "",
        "coming_soon": True,
    },
]

pages = [
    {"name": "Home", "endpoint": "home"},
    {"name": "Hobbies", "endpoint": "hobbies_page"},
    {"name": "Timeline", "endpoint": "timeline"}
]