# matching

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

