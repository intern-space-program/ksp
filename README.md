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

## Permissions
By default, all members of this project have the ability to write directly to the repo. You are entrusted to not push any code, unit tests, or integration tests without approval from at least two people other than yourself in a Pull Request.

You may push vehicle craft files, documentation, updated comments, README updates, gitignore updates, and similar non-software-changing updates without a Pull Request.

## Teams
The conventional teams are as follows (could change depending on the project being tackled):
- Admin: Handles logistics, facilitates inter-group communication, ensures quality standards within the repo, leads group meetings.
- Vehicle Design: Designs the various vehicles to be used during the project.
- Orbital Mechanics: Does all the orbital mechanics calculations for the project.
- Ascent/Entry: Does ascent & entry calculations for the project.
- RPOD: Handles multi-vehicle rendezvous, proximity operations, and docking procedures.
- Landing: Designs the landing control system for any propulsively landed vehicles.

## Development Process: Define, Design, Develop, Test
**Define:** You should begin by defining the boundary conditions of your team's effort. What information does your team need to output, and where does that information go? What information does your team need to do your calculations, and where does that information come from?

**Design:** Begin high-level design work on your team's projects. Make extensive use of GitHub issues to assign tasks to team members. Set up milestones and due dates. This is the phase in which you should define all your equations and algorithms. Hold a design review with other teams to get feedback on your design.

**Develop:** Use the issues created during the design process to guide your software development. For each function you write, develop unit tests that check for nominal behavior under nominal inputs, and safe, expected behavior for unexpected inputs (e.g. make sure your function isn't going to ever divide by zero and crash).

**Test:** Write higher-level tests for your system. Rather than check that each function individually works, check that the entire callstack works as expected when called from start to finish. These tests should have clearly defined inputs, outputs, and effects. For example, if you wrote a script that initiates a trans-lunar injection burn, ensure that the script properly recognizes the burn parameters as the inputs, executes the burn as an effect, and outputs success or error codes.

## Code Standards
This project will be almost entirely developed in python 3.8. As such, all software should follow PEP8 style standards (if you are unfamiliar with these, PyCharm is a popular IDE that automatically highlights when code does not meet PEP8, and gives descriptions why).

Software should be developed with the KISS principle: "Keep It Simple, Stupid." If your code is getting complex, chances are good that you should go back to the Design, or even the Define, step before you continue programming. Good commenting helps, but well-written code with good commenting is way better.

Pull Requests will act as "Code Reviews." You shouldn't approve your own Pull Requests, and you should get someone from another team to approve them. It can be difficult to understand large Pull Requests, so it's best to keep them small (think along the lines of closing one issue at a time, not implementing your entire feature set at once). It helps a lot of you get really granular with your team's issues, make a branch for each issue, and make a Pull Request for each branch.

If you use any unconventional tricks for performance in your algorithms, be sure to cite why, and draw attention to this during design reviews and in Pull Requests.

## Gitignore Info
The .gitignore file was generated using [gitignore.io](https://www.toptal.com/developers/gitignore)
