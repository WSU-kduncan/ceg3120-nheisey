# Project 1 Documentation

## Setup

**User setup/files/permissions**

I created a user called "git" to store the repositories used in this project. I gave git it's own .ssh directory giving it the permission "700" so only the user git and root have access to it. I then created a text file called "authorized-keys" which will store authorized public keys and authenticate those keys. I gave that text file chmod 600 permissions so only git has access to it.

**Setting up the Repository**

I created a repository called "p1repo" by entering the following line into terminal 'git init --bare p1repo.git' I used --bare specifically to set it up as a remote repository as well as being empty.

**SSH key directions**

To actually clone the repository into my home system I used the following command: 'git clone git@54.174.1.237:/home/git/p1repo.git' which successfully cloned it. 

## Usage

- clone - create a copy of a repository, in this project I used clone to copy p1repo from my server to my local machine
- init - when used along with git it allows the creation of a repository, in this project I used git init to create the repository "p1repo"
- add - the only case I really remember using this is through the command adduser to create a new user
- commit - records the changes to a repository but not yet pushed, I used commit to confirm this README.md file and the Project1 folder it resides in before I pushed it into my Github repository
- push - push uploads the changes made in a repository locally into the remote repository, I used this command to upload the changes I made to the repository that being the creation of both Project1 folder and the README.md text file

## Proof

Here is proof of the repositories creation on AWS:

![Repository in AWS](/images/repAWS.png

Here is proof of the sucessful cloning of the repository on my local system:

![Cloned to my local system](/images/repLOC.png
