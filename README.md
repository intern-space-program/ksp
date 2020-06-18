# ksp
Software projects done in Kerbal Space Program, programmed by Johnson Space Center's Intern Space Program club!

## Setup
First, ensure Python 3.8.3, the latest version of pip, and git are installed on your machine.

### Clone the Repo
From the command line, run `$ git clone https://github.com/intern-space-program/ksp.git` to create a ksp directory with the contents of the repo.

### Install the Python Packages
Two options are given to install dependencies: installation via requirements.txt, and installation via pipenv. There are no current plans to support Anaconda installations, since the kRPC mod for Kerbal Space Program is not hosted on Anaconda.

#### Option 1: Install via requirements.txt
From the command line, run `$ pip install requirements.txt` from the `ksp` directory.

#### Option 2: Install the Pipenv Environment
From the `ksp` directory, run:
`$ pip install pipenv`
`$ pipenv install`

This will install all of the correct versions of the packages we will be using.

To run python using the pipenv environment for the project, run `$ pipenv run python` from the command line.
