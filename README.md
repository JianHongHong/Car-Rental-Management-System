
# Car Rental System (Update and rectified further by JianHong Lee) 


### Required Files
* python 3.7.0
* mysqlserver
* Restore carrentaldb.sql into mysqlserver database
* Install required pip files: `pip install -r requirements.txt`
* Migrate settings and database: `python manage.py migrate`

### Notes
 - To run the server: `python manage.py runserver`
 - Add the your database password in settings.py
 - To run tests: `python manage.py test` or `python manage.py test -v 2` (To show more details of tests)
 - Artefacts and documents related to the project are located in "artefacts" folder
 - Localhost can be exposed to public using ngrok => For presentation to others

 ### Test Login
- Customer login = username: crctest, password: test
- Staff login = username: ssoscarl1, password: test
- Administrator = username: dev, password: dev

### Submission
- Course title: IFB299 IT Project Design and Development
- Tutor: Ms Parvaneh Boroujeni
- Team Number : 23
- Date: 29 October 2018


### Created by :
 1. Francis King (N10198067)
 2. Samuel Gillespie (N9990186)
 3. Aidan Perera (N10109960)
 4. JianHong Lee (N9790136)
 5. Tom Kirby (N10014195)

 ## Outdated (Ignore)
* Django: `pip install Django`
* django-bootstrap4: `pip install django-bootstrap4`
* MySQL: MySQL server, MYSQL client, MYSQL workbench
* MYSQL python connector: `pip install mysql-connector-python`
* argon2-cffi library to enable the password hashing: `pip install django[argon2]`
* Selenium: `pip install selenium`
* Selenium IDE in chrome: Install any selenium recorder