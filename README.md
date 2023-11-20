# Learning-Log
## Requirements
- Anaconda 23.7.4
- Python 3.12.0
- Django 4.1
## Development 
- `git clone git@github.com:barabashka25219/Learning-Log.git`
- `conda env create -f environment.yml`
- `conda activate LearningLog`
### Add package 
- `conda search $PACKAGE`
> Show available version of a packet 
- `conda install -n LearningLog $PACKAGE[=$VERSION]`
- `conda list -n LearningLog $PACKAGE`
> Make sure that the packet is installed in your environment via this command
- `conda env export > environment.yml`
- `git commit -m "Add $PACKET in environment"`
- `git push origin $BRANCH`
## Work with project
- `python Learning-Log/learning_log/manage.py migrate`
- `python Learning-Log/learning_log/manage.py createsuperuser`
