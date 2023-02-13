## MESSAGE QUEUE BETWEEN TWO DJANGO PROJECTS USING RABBITMQ

This repo contains two Django projects which simulates an application with Users and Portfolio.

Once a Portfolio is created, that User's portfolio count in the User's Database increases by one.
This is done asynchronously.


### How to run the project.
The User Project
Create a virtual environment for the User project and run
```
cd user
python -m venv venv
```

Next activate the virtual environment.
For Windows users (powershell / terminal)
```
./venv/Scripts/activate
```

For *nix Users (MacOS, Linux / WSL)
```
source ./venv/bin/activate
```

Once the virtual environment has been created, install the libraries needed.
```
python -m pip install -r requirements.txt
```

Next,
```
python manage.py runserver
```

In a seperate terminal tab, pane or window
```
python consumers.py
```



### How to run the portfolio project.
The Portfolio Project
Create a virtual environment for the Portfolio project and run
```
cd portfolio
python -m venv venv
```

Next activate the virtual environment.
For Windows users (powershell / terminal)
```
./venv/Scripts/activate
```

For *nix Users (MacOS, Linux / WSL)
```
source ./venv/bin/activate
```

Once the virtual environment has been created, install the libraries needed.
```
python -m pip install -r requirements.txt
```


Next,
```
python manage.py runserver
```

In a seperate terminal tab, pane or window
```
cd portfolio/core
python producer.py
```


With everything set up, if you create a portfolio from the portfolio project, the user database 
will be increased with the portfolio count.

Happy tweaking.
:)


_In case of any issue you may encounter, feel free to reach me using any handle from my profile._
