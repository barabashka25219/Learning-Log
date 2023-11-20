# Learning-Log
## Requirements
- Anaconda 23.7.4
- Python 3.12.0
- Django 4.1
## Development 
- `git clone git@github.com:barabashka25219/Learning-Log.git` (SSH)
- `git clone https://github.com/barabashka25219/Learning-Log.git` (HTTPS)
- `conda env create -f environment.yml`
- `conda activate LearningLog`
### Add package 
- `conda install -n LearningLog $PACKAGE[=$VERSION]`
> You can search a package via `conda search $PACKAGE`
>> Make sure that the package is installed via `conda list -n LearningLog $PACKAGE`
- `conda env export > environment.yml`
- `git commit -m "Add $PACKAGE in environment"`
- `git push origin $BRANCH`
## Work with project
- `python Learning-Log/learning_log/manage.py migrate`
- `python Learning-Log/learning_log/manage.py createsuperuser`