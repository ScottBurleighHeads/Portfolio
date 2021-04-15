from flask import Blueprint, render_template, url_for
project = Blueprint("project",__name__)

@project.route('/project')
def projectIndex():
    projectData = {
        "intro":[
            "What better way to to show my skills then to show you."
            ],
        "frontend":[
            "This website was built using html, css and bootsrap.", 
            ],
        "backend":["Driving this website is Python and its web application framework Flask."
            ],
        "cloud":[
            "To save cost I have deployed this website using an S3 bucket on AWS." 
            "Using an S3 bucket dramatically decrease's expense's compared to an EC2."
        ],
        "devOps":[
            "Established a CI/CD pipeling with github actions."
        ],
        "database":["This is a static website. There is no database attached or required yet."
        ],
        "img1":[
            'img/image10.jpg'
        ],
        "img2":[
            'img/image11.jpg'
        ],
        "img3":[
            'img/DreamBig.jpg'
        ]
        }
    print(len(projectData["intro"]))
    
    return render_template("projects.html",projectData=projectData)