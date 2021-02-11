# Swtich Project:

This Projetc is a coding challenge designed and created to follow N’osairis Technology Solutions requirements.

## Deployment: 
Official Github Documentation on cloning a repository: [Github-cloning](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

1. Navigate to Main Page of the repository
2. Click on "Code" button
3. Choose "Clone with HTTPs" & copy URL
4. Open Terminal
5. Change the current working directory to preferred location
6. Type git clone and past copied URL git clone https://github.com/besheraj/milestone4.git
7. Press Enter to create local Clone - Make sure your environment supports python3 -
8. Type pip3 install -r requirements.txt into Terminal
9. install MYSQL and link it name the DataBase as the following: 
https://codefires.com/how-connect-mysql-database-django-using-mysqlclient-package/
make sure to update the Setting file DataBases section.
9. Migrate the models and create the database by typing the following commands into the terminal:
python3 manage.py makemigrations
python3 manage.py migrate
10. Create a superuser for accessing the django admin view with the following command: python3 manage.py createsuperuser You will be asked for an email address, username and password.
11. You should be all set and when using the command python3 manage.py runserver the project should run.
12. You can access the django admin view by adding ~/admin to the end of your (local) URL.

