# Covid19-Data-India
A simple form asking your email id your state and district and it will automatically send an email of latest covid19 cases of your area 

## How to Use

1. Type your name, gmail email address as both are required fields.

2. Select Your State and District, both must match else it will show error.

3. After clicking Submit, You will recieve an email showing Corona virus Active,Confirmed and Death cases of your State and District.

## How to Use

### Initialize the project

##### Create and activate a virtualenv:

1. `virtualenv venv`. This will a create a vitual environment called "venv" that helps with controlling dependencies.
2. `source venv/bin/activate`. 


##### Install dependencies:

(while in the activated virtual environment)
```bash
pip install -r requirements.txt
```
NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.

Add a new package to requirements.txt and run the following command to auto-update requirements.txt file
```bash
pip freeze > requirements.txt
```

Run the following command to sync your virtualenv
```bash
pip-sync
```
 This will install/upgrade/uninstall everything necessary to match the requirements.txt contents.

##### Migrate, Create a Superuser, and Run the Server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
