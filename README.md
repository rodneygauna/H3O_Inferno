# H3O_Inferno

![H3O Inferno](/src/static/assets/logo/h3o-inferno-logo-1024x1024.png "H3O Inferno")

## HealthTrio Innovation Day - 2023 Q3

This project was created for the HealthTrio Innovation Day - 2023 Q3 Event.

## 3rd Party Request Process

### Step 1: APP / Organization Submission​

1. Third-party applications follow instructions to connect to APIs via payer's website or materials.​
2. Submission request captures basic App and developer/organization information.​
3. Upon 'Register Now' click, the product management team at HealthTrio initiates Jira ticket for review.​

### Step 2: Intake and Review​

1. Compliance check with CMS final rules (OAuth2, FHIR, etc.).​
2. Evaluation for exploitable vulnerabilities and undesirable behaviors.​
3. Research App with CARIN Alliance, Medicare's Blue Button Apps, and CAQH Endpoint Directory.​
4. Review of the developer's websites for additional insights.​

### Step 3: APP Summary and Health Plan Review​

1. Step 2 findings summarized in Jira and presented to health plan in APP review.​
2. Health plan review to approve or deny the request.​

### Step 4: Approval - API Connection and Health Plan Notification​

1. HealthTrio technical team initiates connectivity steps based on API type.​
2. Confirmation from health plan leads to "live" status for Third-Party App.​
3. OAuth framework, scopes, redirect URLs, logout support, token endpoint authentication method, Client IDs, Client Secret managed.

### The Problem

In the context of our Health Plan's FHIR APIs, the integration of third-party applications has historically been a time-intensive process.​

+ HealthTrio's product management team engages in the laborious task of collecting, reviewing, validating, and processing connection requests from external applications. This involves navigating through a multitude of sources to compile and verify the requisite information.
+ This decentralized approach often results in inefficiencies, with connection requests occasionally slipping through the cracks, leading to a lack of comprehensive tracking.​
+ Streamlining this process to ensure a more efficient and accurate integration pathway is crucial to enhance operational effectiveness.​

### The Solution

+ Optimize the efficiency of information compilation by embracing automation to streamline the process of gathering connection requests. By automating key elements, the time investment required for this task can be significantly reduced.
+ Implement an automated validation mechanism for the requestors' applications across the platforms of CARIN, Medicare, and CAQH. This automation will alleviate the time-consuming burden of manual validation efforts.
+ Enhance request tracking capabilities through the incorporation of a comprehensive tracking system. This system will encompass tracking various facets, including the request initiation, its current status, and pertinent reporting metrics such as time cycles, requester submissions, and successful connections with the health plan.

## How To Run The Project

**Important:** Before starting you're own instance of this application, it is recommened to fork this GitHub project. Learn more about forking here:
[GitHub - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

Summary to run this application:

1. Have Python (3.10 or higher installed)
2. Have WKHTMLTOPDF
3. Have Chrome browser installed
4. Set up a Python Virtual Environment (optional but recommened)
5. Install the needed Python packages
6. Configure email settings
7. Add the environment keys
8. Create the database
9. Run the app

Additional details for each step are below

### Step 1: Python

In order to run the application, you'll need to have Python (version 3.10 or higher) installed on the host machine.
You can download it here [Python](https://www.python.org/)

### Step 2: WKHTMLTOPDF

There is a feature in the application that will generate a PDF (from an HTML page). Ensure WKHTMLTOPDF is installed and reachable for the page to generate.

Linux (Debian 11) Steps:

1. Open the terminal
2. Update your packages `sudo apt install wkhtmltopdf`
3. Install dependencies `sudo apt install libxrender1 libfontconfig1 libxext6 libx11-6`
4. Install WKTHMLTOPDF `sudo apt install wkhtmltopdf`

Confirm the installation was successful using the `wkhtmltopdf --version` command.

For Windows and Mac, you can find more information here: [WKHTMLTOPDF](https://wkhtmltopdf.org/)

### Step 3: Selenium and Chrome WebDriver Configuration

This application scrapes the Medicare Blue Button Apps website. To have the feature function, a Chrome browser must be installed.
You're probably asking "Why?!". Great question. It's because that site is such a dumpster fire (no pun intended), that we have to have Selenium parse the site before it can be passed to Beautiful Soup. Yet, sucks.

You can download Chrome here: [Chrome Downloads](https://www.google.com/chrome/)

Install with these steps:

1. Open the terminal
2. Update your packages with `sudo apt update`
3. Upgrade your packages with `sudo apt upgrade`
4. Install Chromium with `sudo apt install chromium-browser`
5. Note the version with `chromium-browser --version`
6. Go to the [ChromeDriver - Downloads page](https://sites.google.com/chromium.org/driver/downloads)
7. Download the latest version (or one the fits the Chromium version you installed) with `wget linkToZipFile.zip`
8. Unzip the file with `unzip chromedriver_linux64.zip`
9. Move the driver with `sudo mv chromedriver /usr/local/bin/`
10. Make it an executable file with `sudo chmod +x /usr/local/bin/chromedriver`

Confirm that the installation is successful using `chromedriver --version`

### Step 4: Python VENV (Optional but Recommended)

After installing Python, it's recommeneded to set up a virtual enviromnet.
This ensures that all packages for the application are specific to this instance and will not cause any conflicts with other Python projects.

Follow these steps in the terminal:

1. Navigate outside the project folder (ensure you one directory above the 'H3O_Inferno' folder)
2. Type the following command:
Windows: `python -m venv H3O_Inferno\venv`
MacOS or Linux: `python3 -m venv H3O_Inferno/venv`

Once completed, you should see a direction/folder titled 'venv' as a sub-directory in the 'H3O_Inferno' folder.

### Step 5: Python Packages

Once the Python virtual enviroment is set up, navigate into the 'H3O_Inferno' directory and follow these steps using the terminal:

1. Active your Python virtual environment with the following command:
Windows - Command Prompt: `venv\Scripts\activate.bat`
Windows - PowerShell: `venv\Scripts\Activate.ps1`
MacOS or Linux: `source venv/bin/active`
2. Using pip (Python's package installation manager), install the required packages using this command:
Windows: `pip install -r requirements.txt`
MacOS or Linux: `pip3 install -r requirements.txt`

Python will install all the packages and their appropriate versions from the requirements.txt file.

### Step 6: Email Configuration

Next, change the configuration of flask-mail settings in the `__init__.py` file (`src/__init__.py`).

Find the flask-mail configurations starting with the comment "# Mail configuration and initialization" (around line 51).

Update the information to reflect where outgoing emails should come from; such as the 'MAIL_SERVER', 'MAIL_PORT', etc.

Save the changes you've made.

### Step 7: Enviroment Keys

After changing your email settings, create a new file in the parent directory ('H3O_Inferno') with the filename of `.env`.

Open the '.env' file and add the following:

```text
SECRET_KEY=""
EMAIL_PASSWORD=""
```

The 'SECRET_KEY' is used by Flask for security and encryption of the forms when saving (POST) to the database.

The 'EMAIL_PASSWORD' is the password that's used to log into the email account you set up in step 5.

Here is an example of what your '.env' file could look like:

```text
SECRET_KEY="this is a super secret string of letters and numbers 123456"
EMAIL_PASSWORD="Password1234"
```

Save the changes you've made.

### Step 8: Create Database

Last step before running the app is to create and initialize the database. We are using SQLite3 for this project.

In the terminal, type the following command:
`flask commands create_db`

You should see the following output:
"Database created!"

This will create the database and tables for the application.
You should find the database in the 'src' folder (H3O_Inferno/src/database.db).

### Step 9: Run App

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

+ Nicole Naegeli
+ Robert (Bob) Martin
+ Rodney Gauna
+ Sherri Yandell

## Support

If you have any questions, you can do one of the following:

+ Send an email to [rodney.gauna@healthtrio.com](mailto:rodney.gauna@healthtrio.com)
+ Send an email to [rodneygauna@gmail.com](mailto:rodneygauna@gmail.com)
+ Create an issue in the GitHub repo - guide here [GitHub - Create an issue or pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request-from-github-desktop)
