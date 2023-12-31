# CS 396 Project

## Author

Matthew Irizarry,
<matthew@irizarry.dev>

## Project Description

The goal of this project is to create a user friendly web application that can act as the foundation for a learning management software. Core features include:
- Student, Teacher, and Administrator Accounts
- Course Management
    - Lessons
        - Rich Text Body
        - Supports file uploads
    - Assignments
        - Multiple Choice
        - Automatic Grading
- Teacher Gradebook
- Student Gradebook
- Discussion Posts

## Implemented Functions

For the majority of the implemented functions, you will find them in the `/dashboard/views.py`. In the Django model, this is where data is retrieved and processed. Therefore, the majority of implemented functions are in this file. 

### User Accounts

Instead of creating separate tables for students, teachers, and administrators, I opted to use the built-in Django user model. This model supports the ability to create users with different permissions, and is the recommended way to do so. Also, by default it provides a `user.is_staff` which allows us to determine if a user is a teacher or administrator.

### Course Management

#### Assignment

To create an assignment, log-in to the teacher account, and you MUST login to the admin panel to create an assignment. This is for security purposes. Once you create the assignment, you will need to associate it with a course. However, you will need to create some questions that go along with it. Navigate to the `Multiple Choice` tab in the admin panel, and create a question that belongs to the course you just created. It will automatically be associated with the assignment, and display to the user.

#### Lessons

Teachers can log-in to their admin panel, where they will be able to create a lesson. Lessons are associated with a course, and can be created in the admin panel. Lessons support rich text, and file uploads.

### Discussion Posts

Discussion posts can be created by anybody, and can be done so through the mane page. As a security concern, you must delete ANY discussion post from the admin panel. This is to prevent any malicious users from deleting posts, and to preserve the integrity of the discussion board.

### Gradebook

#### Student Gradebook

This page shows all the courses that the student is in. Then beneath each course, it displays the assignments associated with the course. Underneath each assignment shows if the user has submissions associated with the assignment. The grade will be displayed in table format.

#### Teacher Gradebook

This page shows all the courses that the teacher is the instructor of. Then, it shows a list of all the assignments, along with all the student submissions. Because students can submit multiple times, we show the highest submission here.

## Technical Details

### Database Server

Currently, the database server being used is SQLite3. However, as the application is deployed on Heroku, there is little configuration that needs to change in order to use a different database server.

### Plugins

The only outside library I used was `ckeditor` and that was to provide the rich text functionality to the comments, discussion posts, and lessons. This made implementing this functionality very easy, and I would recommend it to anybody who needs to implement rich text.

### Deployment

This app is deployed to the cloud through an IaaS provider called Heroku. Heroku is a platform that allows developers to deploy their applications to the cloud, and provides a lot of the infrastructure that is needed to run a web application. This includes things like a database server, and a web server. Heroku also provides a lot of tools to make deployment easy, such as a CLI tool, and a web interface. 

In order to make this deployment work, I followed this very helpful guide from https://realpython.com/django-hosting-on-heroku/. This guide walks you through the process of deploying a Django application to Heroku, and is very helpful.

## Features you like to highlight

### User Experience

Overall, my biggest focus was user experience. I wanted to make sure that the application was easy to use, and that the user could easily navigate the application. I think I did a good job of this, and I think the application is very easy to use. Moreover, the design is very clean, and I think it looks very nice. 

### Security

From the beginning, users can NOT sign up for teacher accounts. A student account must be promoted to teacher by an administrator. This makes sure that only authorized users can create teacher accounts.

## Discussion

I really enjoyed using Django to create this app. Once I understood how it worked, it was very easy to scaffold models, and get things on the page. However, I do have some complaints. 

First, there are no components that I am aware of. Therefore, HTML templates must be kept consistent, and could pose issues on a larger scale. Because of this, I thought about using React for the front-end and Django on the backend, but I wanted to keep things simpler for this project.

Second, some of the error messages were not very clear. Also, I found myself having to clear `__pycache__` folders quite regularly. Otherwise, I was very pleased with Django, and it allowed me to build this application very quickly.

Overall, I will be keeping Django in my toolbelt for future projects, as I think a couple of my ideas could be built in a very short time using Django.

## Setup Local Environment

0. ### Setup Database 

```
brew install postgresql
echo 'export PATH="/usr/local/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
brew services start postgresql@16
```

1. ### Install Heroku CLI

    Follow the guide below for steps depending on your operating system.

    https://devcenter.heroku.com/articles/heroku-cli

2. ### Install Dependencies

    Run the command `make install` to install the necessary depenedencies for this project.

    Once you are done with this project, you can use the command `make clean` to remove packages associated with this project.

3. ### Setup Environment Variables

    Run the command to generate a secret key for the application.
    ```
    echo "SECRET_KEY=$(openssl rand -base64 32)" > .env
    ```
    Heroku will add this `SECRET_KEY` to the Django environment when it is started up.

4. ### Start Server

    Once you have performed all the commands above, you should be ready to run you server.

    Start the server with the command `heroku local` and you should be up and running at `0.0.0.0:$PORT` where `$PORT` is the port that Heroku assigns to your application.

    This will display in your terminal.

## Test Accounts

Log-in to any of these accounts to test their access.

| Username | Password | Role |
|----------|----------|------|
| matt     | x5dws169!| Admin |
| dratici  | qejMWjuaM)SFB2Y | Teacher |
| drxia | qejMWjuaM)SFB2Y | Teacher |
| DrLi | qejMWjuaM)SFB2Y | Teacher |
| mattirizarry | etu6Mpf.{Q | Student |

# Project phase 2

For phase two of this project, I already had completed a few of the requirements in Phase 1, such as multiple courses, due dates, etc. The new functionalities that I have implemented in Phase 2 are pretty simple.

## NEW / Updated Functionalities 

### Assignments

Assignments now have a limited number of submissions that can be specified in the backend assignment creation process.

### Improved Gradebook

Both interfaces for students and teachers have been improved to provide more detailed information about assignment submissions.

#### Teachers

Teachers can now see each submission for an assignment. For each submission, the teacher can see what the student answered, compared to what the actual answer should be. Teachers can see the details for all the courses they teach, for each student that is enrolled in the course. 

#### Students

Students have a similar functionality but can only see the information pertinent to their courses.

### Database ERD and Normalization

Below is my ERD. I generated this using pgAdmin4 and connecting to my Heroku Postgres instance. It should follow at LEAST 3rd normal form.

![erd](https://github.com/mattirizarry/CS396-Project/assets/42564599/3cdeab42-59ba-4138-894c-50953caa8a99)


Students are required to learn multiple subjects, such as Math, Science, Reading, Writing, etc, There are a number of questions for each subject, and students need to finish all of them. For each question, students have three submission attempts. 

>- Multiple Courses
>- Courses should have many questions, and students should have a due date. Finally, each one should have `n` submission attempts.

The task in project phase 2 is to keept students’ learning outcomes for students and teachers. Teachers are able to see all students’ scores for each subject,  each question number and each attempt. All questions should be kept in the database.  

>- Teachers able to see all student's grades for each subject, question number, and attempt. 

The database design should be in the 3rd normal form.

> - Database design should be in 3rd normal form.

You should provide a search function for users to search information based on key words. 

> - Search through lessons??

Please submit a zip file, including 1. ReadMe 2. Project report 3. Source codes.
ReadMe file includes major instruction steps for repeating your project results. Anyone should be able to follow the instructions and run your source codes correctly. Please do not forget system setting up.
In project report, please include:
1. Project description
2  Functions that you have implemented 
3. Database Design (ER model),  Database Schema, Normalization (3rd norml checking).
4. Summary/Discussion

# Project Phase 3

Based on project phases 1 and 2, the goal of phase 3  is to provide users with tools to measure and check students’ performance. Minimum requirements include:
- Students can check the percentiles of their scores. 
- Please use a bar chart to display students’ subject scores (Math/Science/Reading) over the past semesters (>=5). 
- ~~Teachers can see all students’s scores, sort scores (ascending and descending), highest, lowest scores, and average scores.~~
- ~~Teachers can compute students’ weight scores according to user-defined weights.~~
- ~~Teachers can assign letter grades based on the weighted scores. Students can see only their grades~~
- Use a pie chart to display the percentages of the letter grades.
