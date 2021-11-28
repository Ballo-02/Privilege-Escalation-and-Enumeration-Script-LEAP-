# LEAP

LEAP: Local Enumeration And Privesc. Framework for 4061CEM project.


## What is here?

Not much.

This project requires you to generate most of the actual code
yourselves.  To start with, each team should work on a fork of this
repository together to define the common features of the individual
pieces of functionality - we'll refer to them as "plugins". This is a
kind of **design by contract**, which you can read about here:
<https://www.sciencedirect.com/topics/computer-science/design-by-contract>. Some
things to decide might be:
  - Will each piece of functionality be in a separate file or subdirectory?
  - Will your team have a naming convention?  For example, maybe all
    windows enumerators will begin with "wEnum_", linux with "lEnum_"
    and so on. 
  - What will each function return or display? Will each function
    print out to the user? Or will it return a block of text in a
    string? Or a list of lines? Or maybe a dict with some meta-info
    (version, plugin name, plugin author, date, time, etc.) and text
    data? Or JSON? All are possibilities.
  - Will you have a standard set of parameters to be passed in? Or can
    each plugin have a different set of required parameters?
  - What plugins will be implemented? Who will be the author?
	
You should document these decisions here in the `README.md` file. Once
you are all happy with this, stage, commit and push it to your shared
fork. Then, each team member can begin writing their own tool by
creating an individual fork or using branching. Naming your tool
something sensible and uniquely identifiable at this point will be
very helpful.  If you all keep the simple name "LEAP", you will might
it tricky to remember which repository you are working on later.  You
can call your own fork whatever you like.

When the individual tools are working and each team member has their
own plugins working, it is their responsibility to liaise with the
other members of the team to import the other plugins.  Each team
member should create a fork of the repositories of each of their
team-mates, integrate their plugins and submit a pull-request for each
fork. If using branches, then each team member can merge into their
branch from either the master (if any system changes are made) or from
other users' forks (to incorporate their plugins).

If using forks, with team members being A, B, C and D, they will have
one fork to start with in which the team collaborates on defining the
basics.  Then A will create a personal fork of the shared repository
and work on their tool and plugins.  When they're done, they will
create forks from their team-mate's repositories. Let's call them
LEAP-B, LEAP-C and LEAP-D. A will then port their plugins to each of
these new forks and submit pull requests for them to be merged into
the repositories of their teammates.

## Why?

This might seem overly complex, but it's not.  In reality, this is one
of the common ways people collaborate using git.  You can fork any
public project and work on your own copy without needing to ask
permission or get added to the original repo, then if you want to
recommend your changes to the original author you create a pull
request and they can decide to merge it into their work or not.

In this project you will be getting experience of working on a project
and receiving multiple pull-requests from contributors and at the same
time, contributing to the repositories of others.


# Team Discussion:

## Team Member Letter ID and github usernames

This is used in the naming conventions of our functions and classes.

Person A = ballo3
Person B = bontoftf
Person C = gouveiacom
Person D = sharpm2


## Naming conventions

### Files names
Lower case except for starting letter in new words in name.
E.g. fileName.py

### Classes
Start with captital letter; name relevant to purpose.
E.g. Enumeration()


### Functions
Lower case, except for Member ID, with Underscore and name relevant to purpose.
E.g. enum_A1()

### Variables
Lower case, except for new word, with out underscore.
E.g. choose_enumerations

