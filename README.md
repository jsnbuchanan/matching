# matching

## Setup

If you haven't setup virtualenv, see http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref

To fire up the virtual environment, from the root source directory run the following command
```
source [environment name]/bin/activate
```

In my case
```
source venv/bin/activate
```
Then run:
```
pip install -r requirements.txt
```

That should install the latest required dependencies. If you add additional dependencies, run:
```
pip freeze > requirements.txt
```
To add them to the requirements.txt and then commit.

### Bower managed dependencies

Javascript and other client side libraries will be managed by bower.

To import those dependencies run:
```
./manage.py bower install
```

### Setting up MongoDb
I also had to install MongoDb with brew, using the following command:
```
brew install mongodb --with-openssl
```
To have launchd start mongodb at login:
```
  ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
```
Then to load mongodb now:
```
  launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
```
Or, if you don't want/need launchctl, you can just run:
```
  mongod --config /usr/local/etc/mongod.conf
```
Then syncdb
```
./manage.py syncdb
```
Create a super user:
```
./manage.py createsuperuser --username=totesadmin --email=hapgilmore23@gmail.com
```
And you'll be prompted for a password.

#### MongoDb is NOT a Relational Database

MongoDb is a different type of database. Far different from the relational databases you may be used to. See the tutorial at https://django-mongodb-engine.readthedocs.org/en/latest/tutorial.html for a quick primer.

## Starting the Web Server

To actually view the app running locally, use the following command:
```
python manage.py runserver
```
In your web browser go to:
```
http://127.0.0.1:8000/admin/
```

## Debugging

