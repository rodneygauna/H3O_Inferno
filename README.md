# H3O_Inferno

![H3O Inferno](/src/static/assets/logo/h3o-inferno-logo-1024x1024.png "H3O Inferno")

## HealthTrio Innovation Day - 2023 Q3

This project was created for the HealthTrio Innovation Day - 2023 Q3 Event.

## Backgroud

Background goes here

### The Problem

Problem(s) summary goes here

### The Solution

Solution summary goes here

## How To Run The Project

**Important:** Before starting you're own instance of this application, it is recommened to fork this GitHub project. Learn more about forking here:
[GitHub - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

Summary to run this application:

1. Have Python (3.10 or higher installed)
2. Have WKHTMLTOPDF
3. Set up a Python Virtual Environment (optional but recommened)
4. Install the needed Python packages
5. Add the enviroment keys
6. Create the database
7. Run the app

Additional details for each step are below

### Step 1: Python

In order to run the application, you'll need to have Python (version 3.10 or higher) installed on the host machine.
You can download it here [Python](https://www.python.org/)

### Step 2: WKHTMLTOPDF

There is a feature in the application that will generate a PDF (from an HTML page). Ensure WKHTMLTOPDF is installed and reachable for the page to generate.

Linux (Debian 11) Steps:

1. Open the terminal
2. Update your packages
```bash
sudo apt install wkhtmltopdf
```
3. Install dependencies
```bash
   sudo apt install libxrender1 libfontconfig1 libxext6 libx11-6
```
4. Install WKTHMLTOPDF
```bash
sudo apt install wkhtmltopdf
```

Confirm the installation was sucessful using the `wkhtmltopdf --version` command.

For Windows and Mac, you can find more information here: [WKHTMLTOPDF](https://wkhtmltopdf.org/)


### Step 3: Python VENV (Optional but Recommended)

After installing Python, it's recommeneded to set up a virtual enviromnet.
This ensures that all packages for the application are specific to this instance and will not cause any conflicts with other Python projects.

Follow these steps in the terminal:

1. Navigate outside the project folder (ensure you one directory above the 'H3O_Inferno' folder)
2. Type the following command:
Windows: `python -m venv H3O_Inferno\venv`
MacOS or Linux: `python3 -m venv H3O_Inferno/venv`

Once completed, you should see a direction/folder titled 'venv' as a sub-directory in the 'H3O_Inferno' folder.

### Step 4: Python Packages

Once the Python virtual enviroment is set up, navigate into the 'H3O_Inferno' directory and follow these steps using the terminal:

1. Active your Python virtual environment with the following command:
Windows - Command Prompt: `venv\Scripts\activate.bat`
Windows - PowerShell: `venv\Scripts\Activate.ps1`
MacOS or Linux: `source venv/bin/active`
2. Using pip (Python's package installation manager), install the required packages using this command:
Windows: `pip install -r requirements.txt`
MacOS or Linux: `pip3 install -r requirements.txt`

Python will install all the packages and their appropriate versions from the requirements.txt file.

### Step 5: Enviroment Keys

After changing your email settings, create a new file in the parent directory ('H3O_Inferno') with the filename of `.env`.

Open the '.env' file and add the following:

```text
SECRET_KEY=""
```

The 'SECRET_KEY' is used by Flask for security and encryption of the forms when saving (POST) to the database.

Here is an example of what your '.env' file could look like:

```text
SECRET_KEY="this is a super secret string of letters and numbers 123456"
```

Save the changes you've made.

### Step 6: Create Database

Last step before running the app is to create and initialize the database. We are using SQLite3 for this project.

In the terminal, type the following command:
`flask commands create_db`

You should see the following output:
"Database created!"

This will create the database and tables for the application.
You should find the database in the 'src' folder (H3O_Inferno/src/database.db).

### Step 7: Run App

To run the app, type the following command in the terminal:

Windows: `python app.py`
MacOS or Linux: `python3 app.py`

To stop running the application, press CTRL + C in the terminal.

## CLI Commands

Using the following commands for testing and seeding the database with fake (using the PYthon package [Faker](https://faker.readthedocs.io/en/master/)):

+ Drop the database: `flask commands drop_db` (**Warning:** this will destory and delete the database)
+ Create the database: `flask commands create_db`
+ Seed the database: `flask commands seed_db`

## Credits

Meet **Team Inferno**!

+ Rodney Gauna

## Support

If you have any questions, you can do one of the following:

+ Send an email to [rodney.gauna@healthtrio.com](mailto:rodney.gauna@healthtrio.com)
+ Send an email to [rodneygauna@gmail.com](mailto:rodneygauna@gmail.com)
+ Create an issue in the GitHub repo - guide here [GitHub - Create an issue or pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request-from-github-desktop)
