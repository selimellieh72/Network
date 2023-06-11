# Network - A Social Media Web App

![Login](https://github.com/selimellieh72/Network/blob/main/preview/login.png?raw=true)

## Description
Network is a lightweight social media application built using Django and incorporating CSS animations for a seamless and visually engaging user experience. The app allows users to authenticate, login, register, add, read, and like posts.

## Features
- User Authentication: Built-in registration and login system that uses Django's built-in User model.
- Smooth Transitions: CSS Animations are incorporated into the web design for a seamless experience.
- Posts: Users can create, read, and like posts.
- Secure: The application leverages Django's built-in security features to prevent cross-site scripting (XSS), cross-site request forgery (CSRF), and SQL injection attacks.
## Installation
Before starting, make sure you have Python3, pip and Django installed on your machine.

### Clone the repository

```bash
git clone https://github.com/selimellieh72/network.git
```


### Navigate to the project directory

```bash
cd network
```
### Create a virtual environment

```bash
python3 -m venv env
```

### Activate the virtual environment

#### On Windows
```bash
.\env\Scripts\activate
```
#### On Unix or Linux
```bash
source env/bin/activate
```
### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```
Now, you should be able to see the application running at localhost:8000 in your web browser.

# Usage
###  Registration and Login:
 On the homepage, click on the 'Register' button to create a new account or 'Login' if you already have an account.

### Create Post: 
Once logged in, you can create a new post by clicking on 'Create Post' and entering the post content.

### View and Like Posts:
 You can view all the posts on the 'Home' page. To like a post, simply click on the 'Like' button below the post.

## Contributing
If you want to contribute to this project, please create a new issue detailing the change you want to make or propose your change in a pull request.

## License
This project is licensed under the terms of the MIT license.

## Contact
If you have any questions, feel free to reach out to us at selim.cod4r@gmail.com.# Network
