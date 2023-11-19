# Learning-Log
## Requirements
- Anaconda 23.7.4
## Development 
- `git clone git@github.com:barabashka25219/Learning-Log.git`
- `conda env create -f environment.yml`
### Add package 
- `conda search $PACKAGE`
> Show available version of a packet 
- `conda install -n LearningLog $PACKAGE[=$VERSION]`
- `conda list -n LearningLog $PACKAGE`
> Make sure that the packet is installed in your environment via this command
- `conda env export > environment.yml`
- `git commit -m "Add $PACKET in environment"`
- `git push origin $BRANCH`
