Clone the repository:

git clone https://github.com/Vishal-py-js/reminder.git

cd generator

Then install the dependencies:

pip install -r requirements.txt

Once pip has finished downloading the dependencies:

database setup:

run py manage.py makemigrations to prepare database tables

run py manage.py migrate to create database tables

run py manage.py runserver to start the server

Go to localhost:8000, this endpoint will take care of generating and saving images.
Once the process is complete, you can three images created inside your projects root folder
