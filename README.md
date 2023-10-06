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