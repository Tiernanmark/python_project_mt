# Project Name: Frasier Episode Log

## Website Goal

The aim of this project was to create a dynamic *Frasier* website using Python and Flask. Users can search for episodes, view information about the show, submit a contact form, and vote for their favourite character.

The project builds on the HTML and CSS skills developed in the previous module and demonstrates how Python and Flask can be used to add dynamic and interactive features.

## Design

The website uses a simple design inspired by the colours and visual style associated with *Frasier*. Bootstrap and custom CSS were used to create a consistent and responsive layout across desktop, tablet, and mobile devices.

A custom Google Font was also used to replicate the style of the font used in the *Frasier* logo.

A `base.html` template was created using Flask's template inheritance. This allowed common elements such as the navigation bar and page structure to be shared across all pages without repeating the same code.

## Website Pages

### Home Page

The Home page introduces the website and *Frasier*. It also displays the character currently leading the voting system. The character image links to the voting page.

### About Page

The About page provides background information about *Frasier* and its origins as a spin-off from *Cheers*.

### Episodes Page

The Episodes page allows users to search through a collection of *Frasier* episodes. Python is used to process the search and display matching results.

### Contact Page

The Contact page allows users to submit a message. Flask processes the form and validates that the required fields have been completed.

### Character Ranking Page

Users can vote for their favourite character. Votes are stored using a Python dictionary and displayed as a ranking. The highest-ranked character is also displayed on the Home page.

## Main Features

- Responsive design using Bootstrap and CSS.
- Episode search functionality.
- Contact form with validation.
- Character voting system.
- Dynamic content generated using Python and Flask.
- Template inheritance using `base.html`.
- User interaction through forms.

## Site Structure

```text
app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── episodes.html
│   ├── ranking.html
│   └── contact.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── data/   
│       └── episodes.json 
│
├──README.md
│
└──requirements.txt
```
## Technologies Used

- **Python 3** – application logic and data processing.
- **Flask** – web framework and routing.
- **Jinja2** – dynamic HTML templates.
- **HTML5** – page structure.
- **CSS3** – custom styling.
- **Bootstrap 5.3** – responsive design and UI components.
- **Google Fonts** – custom typography.
- **Visual Studio Code** – development environment.
- **Git and GitHub** – version control and source code management.

## Use of AI

AI was used throughout the project as a learning and development tool. It was mainly used to help with debugging, explain Python and Flask concepts, and suggest possible solutions when I was unable to resolve an issue independently.

Microsoft Copilot was used when developing the Character Ranking feature and when querying how to create Python methods. The suggestions provided were reviewed, adapted, and tested before being added to the project.

ChatGPT was also used to review code, identify corrections, and help improve the wording of documentation throughout the project.

AI was not used to create the complete project. I attempted to solve problems myself first and used AI to help understand errors and unfamiliar concepts. This helped improve my understanding of Flask routing, forms, Python data structures, and dynamic content.

One limitation was that AI sometimes suggested additional code or features that were not required. This meant that prompts sometimes had to be made more specific and that all suggestions needed to be checked before being used.

## Learning Outcome

This project demonstrated the progression from static HTML and CSS development to a dynamic Flask application.

I developed an understanding of Flask routing, Python data structures, form handling, validation, template inheritance, user input, and dynamic content.

The project also demonstrated how front-end technologies can be combined with Python and Flask to create an interactive full-stack web application.

## Deployment
Hosted using GitHub Pages. To deploy your own version follow these steps:
1. Navigate to the project repository on GitHub.
2. Click on the **Settings** tab.
3. Scroll down to the **Pages** section on the left sidebar.
4. Under **Build and deployment**, set the source branch to `main` and folder to
`/root`.
5. Click **Save**. The live URL will appear at the top of the section shortly.

## Local Cloning
To run this project locally:
1. Clone the repository using `https://github.com/Tiernanmark/python_project_mt.git`.
2. Open the directory in your preferred code editor.
3. Open `index.html` in any web browser to view the site.

## Hosted Application

The live version of this project is available online and can be viewed at:

`https://python-project-mt.onrender.com`

No installation or setup is required to use the hosted version of the application.

## Credits

### Logo Image

The *Frasier* logo was sourced from [Fine Art America](https://fineartamerica.com/featured/frasier-frasier-logo-brand-a.html?product=kids-tshirt).

### Character Images

The character images were sourced from the [Frasier Wiki](https://frasier.fandom.com/wiki/Frasier_Wiki).

### Custom Font

The custom font was sourced using [Google Fonts](https://fonts.google.com/).

### Artificial Intelligence

#### Microsoft Copilot

- Used to query how to create Python methods.
- Assisted with developing the Character Ranking feature.

#### ChatGPT

- Used to review code and identify corrections.
- Used to explain Python and Flask concepts.
- Used to assist with rewording and improving project documentation.

### Ferdia O'Brien - Director of Engineering - Scorebuddy

- Advised on json data structures and use of Postman
- Reviewed and critiqued the code where needed (example: switching debugger to False befor deployment)