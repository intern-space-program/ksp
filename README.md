# ksp
Software projects done in Kerbal Space Program, programmed by Johnson Space Center's Intern Space Program club!

## Setup
First, ensure **Python 3.8.3**, the latest version of pip, and git are installed on your machine.

### Clone the Repo
From the command line, run `$ git clone https://github.com/intern-space-program/ksp.git` to create a ksp directory with the contents of the repo.

### Install the Python Packages
Two options are given to install dependencies: installation via requirements.txt, and installation via pipenv. There are no current plans to support Anaconda installations, since the kRPC mod for Kerbal Space Program is not hosted on Anaconda.

#### Option 1: Install via requirements.txt
From the command line, run `$ pip install -r requirements.txt` from the `ksp` directory.

#### Option 2: Install the Pipenv Environment
From the `ksp` directory, run:
`$ pip install pipenv`
`$ pipenv install --python python3.7`

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

**Develop:** Use the issues created during the design process to guide your software development. For each function you write, develop unit tests that check for nominal behavior under nominal inputs, and safe, expected behavior for unexpected inputs (e.g. make sure your function isn't going to ever divide by zero and crash). Unit tests should be written using PyTest, and once approved, added to the Continuous Integration pipeline via GitHub's Actions feature.

**Test:** Write higher-level tests for your system. Rather than check that each function individually works, check that the entire callstack works as expected when called from start to finish. These tests should have clearly defined inputs, outputs, and effects. For example, if you wrote a script that initiates a trans-lunar injection burn, ensure that the script properly recognizes the burn parameters as the inputs, executes the burn as an effect, and outputs success or error codes.

## Code Standards
This project will be almost entirely developed in python 3.8. As such, all software should follow PEP8 style standards (if you are unfamiliar with these, PyCharm is a popular IDE that automatically highlights when code does not meet PEP8, and gives descriptions why).

Software should be developed with the KISS principle: "Keep It Simple, Stupid." If your code is getting complex, chances are good that you should go back to the Design, or even the Define, step before you continue programming. Good commenting helps, but well-written code with good commenting is way better.

Pull Requests will act as "Code Reviews." You shouldn't approve your own Pull Requests, and you should get someone from another team to approve them. It can be difficult to understand large Pull Requests, so it's best to keep them small (think along the lines of closing one issue at a time, not implementing your entire feature set at once). It helps a lot of you get really granular with your team's issues, make a branch for each issue, and make a Pull Request for each branch.

If you use any unconventional tricks for performance in your algorithms, be sure to cite why, and draw attention to this during design reviews and in Pull Requests.

## Technical References

### Launch and Entry Vehicle Design Presentations
Launch and Entry Vehicle Design [slides](https://github.com/intern-space-program/ref/blob/master/Course-Slides/Launch-Entry-Design) are available for reference. These presentations include launch, entry, and orbit state equations, heuristics for approximating physical quantities, delta-v calculations, and more. Access is only provided to __Intern Space Program__ members.

### Planar Launch State Equations
The following [Jupyter Notebook](https://gist.github.com/cadojo/31b76538ed1452ec7450ccf9ff1f948f) summarizes state equations for an ascending launch vehicle. These equations are valid as long as the launch vehicle stays in one plane. The notebook also has Python code that propagates the launch. The resultant plots aren't correct, but the equations and Python example might still be a helpful reference. 

## Git Tips & Tricks

### Git Config & Aliases

#### More Useful `git log`

The following [aliases](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git/34467298#34467298) print out decorated commit history that many find easier to read than `git log`. There are tons of examples of aliases that produce (arguably) more useful `git log` outputs, but these are provided here for reference. Of course, find what works best for you.

```
# Source: https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git/34467298#34467298
[alias]
    lg = lg1
    lg1 = lg1-specific --all
    lg2 = lg2-specific --all
    lg3 = lg3-specific --all

    lg1-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)'
    lg2-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
    lg3-specific = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed: %cD)%C(reset) %C(auto)%d%C(reset)%n''          %C(white)%s%C(reset)%n''          %C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'
```

### Configuring commit author and email

There are many ways to make sure that the proper name and email are associated with your commits. If you use the same name and email for all your projects, you can run the following [commands](https://stackoverflow.com/a/3580841/6118741) to set them once.

```
# Source: https://stackoverflow.com/a/3580841/6118741
git config --global user.name "Your Name"
git config --global user.email "name@domain.example"
``` 

## Gitignore Info
The .gitignore file was generated using [gitignore.io](https://www.toptal.com/developers/gitignore)
