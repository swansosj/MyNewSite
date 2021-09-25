from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

sheldon = {
    'firstName': 'Sheldon',
    'lastName': 'Swanson',
    'age': '33'
}

degrees = [
    {
    'name': 'Master of Science',
    'focus': 'Digitial Forensics',
    'year': '2018',
    'school': 'University of South Florida',
    'ref': 'https://www.usf.edu'
    },
    {
    'name': 'Bachelor of Science',
    'focus': 'Computer Networking and Telecomunications',
    'year': '2017',
    'school': 'Florida State Collge at Jacksonville',
    'ref': 'https://www.fscj.edu'
    },
    {
    'name': 'Associate of Arts',
    'focus': 'General Education',
    'year': '2013',
    'school': 'Florida State College at Jacksonville',
    'ref': 'https://www.fscj.edu'
    }
]


certifications = [
    {
    'name': 'Master Training Specialist',
    'organization': 'Naval Education Center for Professional Development',
    'status': 'Active',
    'focus': 'Adult Learning, Curiculum Development, Public Speaking',
    },
    {
    'name': 'Fortinet Network Security Expert Level 4',
    'organization': 'Fortinet',
    'status': 'Active',
    'focus': 'FortiOS 6.4'
    },
    {
    'name': 'Cisco Certified Networking Profesional Enterprise Core',
    'organization': 'Cisco Systems',
    'status': 'Active',
    'focus': 'Cisco Enterprise Solutions'
    },
    {
    'name': 'Security+',
    'organization': 'CompTIA',
    'status': 'Active',
    'focus': 'Vendor Neutral Security'
    },
    {
    'name': 'Network+',
    'organization': 'CompTIA',
    'status': 'Active',
    'focus': 'Vendor Neutral Networking'
    },
    {
    'name': 'A+',
    'organization': 'CompTIA',
    'status': 'Active',
    'focus': 'Vendor Neutral Hardware and Software'
    }
]

jobs = [
    {
    'title': 'Network Engineer',
    'company': 'NewFold Digital',
    'type': 'Full-Time',
    'years': '2019 - Present'
    },
    {
    'title': 'Network Engineer',
    'company': 'Publix Supermarkets',
    'type': 'Full-Time',
    'years': '2018 - 2019'
    },
    {
    'title': 'Network Administrator',
    'company': 'Swisher International',
    'type': 'Contract',
    'years': '2017 - 2017'
    },
    {
    'title': 'IT Support Speacialist',
    'company': 'Jacksonville Port Authority',
    'type': 'Part-Time',
    'years': '2016 - 2017'
    }
]

military = [
    {
    'title': 'Course Supervisor',
    'command': 'Center for Security Forces (CENSECFOR)',
    'branch': 'US Navy',
    'rank': 'Petty Officer First Class E-6',
    'years': '2013 - 2016'
    },
    {
    'title': 'Work Center Supervisor',
    'command': 'USS Gettysburg (CG-64)',
    'branch': 'US Navy',
    'rank': 'Petty Officer Second Class E-5',
    'years': '2008 - 2013'
    },
    {
    'title': 'AEGIS FCS/ORTS/400Hz Techician',
    'command': 'AEGIS Training and Readiness Center (ATRC)',
    'branch': 'US Navy',
    'rank': 'Seaman E-3',
    'years': '2008 - 2008'
    },
    {
    'title': "Firecontrolman 'A' School",
    'command': 'Center for Surface Combat Systems',
    'branch': 'US Navy',
    'rank': 'Seaman Apprentice E-2',
    'years': '2007 - 2008'
    },
    {
    'title': "Advanced Technical Training (ATT)",
    'command': 'Center for Surface Combat Systems',
    'branch': 'US Navy',
    'rank': 'Seaman Apprentice E-2',
    'years': '2007 - 2008'
    }
]

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='Portfolio', degrees=degrees,certifications=certifications,
                                                                jobs=jobs, military=military)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
