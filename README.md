# Technical Demo Setup H+ README
## Task Description
Using python build a server with services to pull the profile and the appointments data from a DB. For this MVP, you can pull the data from a JSON mock file, as the actual access to the database will be implemented in future sprints.

Mandatory: Unit test, SOLID and a clean code approach

Nice to have: Containerize the solution OR implement the server side with AWS Lambdas
## Instructions
This task has been accomplished in 3 seperate ways.
The first implementation follows a strictly sole python approach, it creates a python based webserver which can pull from the mock db to display appointments or profiles
The second implementation utilises Flask as a backend web framework for the task. 
The final implementation makes use of AWS lambdas to fulfill all the requirements of the task

### Run 1st implementation
in the root of the project
1. Setup virtualenv
2. Activate Virtualenv
3. Install Pip packages and requirements
4. run ./backend.py

### Run Flask implementation
In the root of the project
1. Virtualenv
2. Install pip packages and requirements
3. run  ' flask run ' 
4. visit localhost:5000/

### Final Implementation
I will run through the process on AWS with testing endpoints

### Containerisation
The project is currently containerised using docker and can be made accessible via AWS following additional setup

### Thoughts
Creating the mock data requires some thought as to DB design
What am i exactly supposed to do here? Right a JSON file then just make a set of tools to read from them
AWS has alot of different ways to accomplish the task description
The task description is lacking

### Further development
Add further endpoints to:
1. Filter appointments by profile
2. Add authentication and login features