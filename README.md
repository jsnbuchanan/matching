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

## Starting the Web Server

To actually view the app running locally, use the following command:
```
python manage.py runserver
```

## Debugging

I've gotten the error:
```
ServerSelectionTimeoutError: localhost:27017: [Errno 61] Connection refused
```
when the mongodb service is not running. To enable it, run:
```
brew services start mongodb
```

