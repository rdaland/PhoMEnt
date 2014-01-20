print """
I found that I had to stage my change, commit it, and then push it.
Despite the very clear directions about how to make a repository,
I found it frustrating that GitHub did not include clear directions
on how to make changes to an existing repo, which is surely far
and away the most frequent and important thing that anyone ever
does on GitHub.

I believe this is the exact sequence of commands I used:
$ git clone https://github.com/rdaland/PhoMEnt.git
$ gedit README.md &
    [edit README to add my name]
$ git stage README.md
$ git commit
$ git push

The first line creates a local clone of the original repository.
The second line initiates my preferred editor, to make changes to
    the relevant file.
The third line adds README.md to the "staging area", whatever that
    means.
The fourth line "commits" the change to version control, meaning
    that I have created a new *version* of the code on my *local*
    copy of the repository.
The fifth line "pushes" my version to the master branch on GitHub.

I don't know yet what sequence of commands I have to include to
add this file, but I am guessing it is the following:

$ git add RobertDaland.py
$ git stage RobertDaland.py
$ git commit
$ git push
"""
