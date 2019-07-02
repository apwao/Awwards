# Awwards
### July 2nd 2019
#### By **[Purity Sowayi]** (https://github.com/apwao)
## Description
This is a project that allows users to upload a project to the site with details such as description, link to the active site, image of the landing page and the name of the project. Other users can then rate the project based on usability, content and design. A user can also sign up to the application and view projects posted by other people and submit their vote.
## User Stories:
* As a user, I would like to sign up and be authenticated.
* As a user, I would like to log into the application.
* As a user, I would like to upload a project.
* As a user, I would like to view other people's projects and submit my vote.
* As a user, I would like to create a profile and view it. 
* As a user, I would like to vote on a project
## BDD
|Behavior                      |Input                       |Output
|------------------------------|----------------------------|----------------------------------------
|User signs up                 | Enters details and submits | User's account is activated
|User logs into account        | Submits Login Information  | Redirected to homepagee
|User uploads a project        | Submits project details    | Project adds to those displayed on homepage
|User creates a profile        | Submits profile form       | Creates a profile which they can view 
## Setup/Installation Requirements
* Ensure git is intalled in your computer
* Use 'git clone' command to Clone and then unzip the repository from github, https://github.com/apwao/Awwards.git
* Navigate to the cloned project through the terminal
* Create a virtual environment and install all dependencies in the requirements.txt file using the command 'pip install -r requirements.txt'
* Create a postgresql database
* Create an .env file in the root of the application and specify the environment variables required
* run migrations using the command 'python3.6 manage.py migrate'
* Run the command 'python3.6 manage.py runserver' to run the application
## Known Bugs
* No known bugs
## Technologies Used
* HTML
* CSS
* Git
* Django
* Bootstrap
* Heroku
## Support and contact details
Incase of any issues, ideas, questions or concerns, contact contributor at pasowayi@gmail.com.
In order to contribute to the code: Fork a copy of the repository, push changes to a branch called contributions. Issue a pull request to the contributor.
### License
Copyright (c) 2019 **Purity Sowayi**
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
