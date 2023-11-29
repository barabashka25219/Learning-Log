# Learning-Log
## Requirements
- Anaconda 23.7.4
- Python 3.12.0
- Django 4.1
- uWSGI 2.0.21
## Development 
- `git clone git@github.com:barabashka25219/Learning-Log.git` (SSH)
- `git clone https://github.com/barabashka25219/Learning-Log.git` (HTTPS)
- `conda env create -f environment.yml`
- `conda activate LearningLog`
### Add package 
- `conda install -n LearningLog $PACKAGE[=$VERSION]`
> You can search a package via `conda search $PACKAGE`
>> Make sure that the package is installed via `conda list -n LearningLog $PACKAGE`
- `cd Learning-Log`
- `conda env export > environment.yml`
- `git commit -m "Add $PACKAGE in environment"`
- `git push origin $BRANCH`
## Docker
### Creation
- `cd Learning-Log/learning_logs`
- `pip list --format=freeze > requirements.txt`
- `docker build -t barabashka25219/learninglog .`
### Run container
- `docker run -p 8000:5000 --name learninglog barabashka25210/learninglog`
## Features
1. Topics creation
2. Creation entries of a topic
3. Users creation and authentication
