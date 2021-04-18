from flask import Blueprint, render_template, url_for
project = Blueprint("project",__name__)

@project.route('/project')
def projectIndex():
    projectData = {
        "heading":[
            "Portfolio","Calorie Counter"
        ],
        "intro":[
            "What better way to to show my skills then to show you.",
            "Calorie Counter is a website that can query search a third party API"
            "for a certain food item. Once found it can return the calories, protein"
            "fat and carbs. Once signed in to the website the user has an option to store"
            "results of the query search onto a database."
            ],
        "frontend":[
            "This website was built using html, CSS, Jinja2 and bootsrap.", 
            "The website was built using html, Jinja2 and bootstrap"
            ],
        "backend":[
            "Driving this website is Python and its web application framework Flask.",
            "The Calorie Counter website is ran using Python and its web application framework Flask. "
            "There was an ORM built with SQLalchemy."
            ],
        "cloud":[
            "To save cost I have deployed this website using an S3 bucket on AWS." 
            "Using an S3 bucket dramatically decrease's expense's compared to an EC2.",
            "I temporarily deployed the website on an EC2 hosted by AWS. I set up a PostgreSQL server "
            "that was running on an RDS using AWS."
        ],
        "devOps":[
            "Established a CI/CD pipeling with github actions.",
            "Basic roles were established for the PostgreSQL database and EC2."
        ],
        "database":[
            "This is a static website. There is no database attached or required yet.",
            "A PostgreSQL server was driving the database."
        ],
        "img1":[
            'img/homeIndex.JPG',
            'img/calorieHome.JPG'
        ],
        "img2":[
            'img/about1.JPG',
            'img/calorieCount1.JPG'
        ],
        "img3":[
            'img/about2.JPG',
            'img/Recipe1.JPG'
        ],
        "img4":[
            None,
            'img/LogIn.JPG'
        ]
        }
    print(len(projectData["intro"]))
    
    return render_template("projects.html",projectData=projectData)