It's a bit confusing, but by convention we refer to the remote repository as 'origin' and the initial local repository as 'master'. 

## Adding all files

```git add -p <optional filename>```

It will step through each change and allow you to include it or not.  You can even manually edit a patch if you want part of a change, but noticed you had left in some debugging output or something.


## General workflow

This is actually a multi-step process. First you'll need to add all your files to the current stage:
```git add .```

You can verify that your files will be added when you commit by checking the status of the current stage:
```git status```

The console should display a message that lists all of the files that are currently staged, like this:
```
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#   new file:   README
#   new file:   src/somefile.js
#
```

If it all looks good then you're ready to commit. Note that the commit action only commits to your local repository.
```git commit -m "some message goes here"```

[Optional since you already cloned from git]
If you haven't connected your local repository to a remote one yet, you'll have to do that now. Assuming your remote repository is hosted on GitHub and named "Some-Awesome-Project", your command is going to look something like this:
```git remote add origin git@github.com:username/Some-Awesome-Project```

When you're ready to push your commits to the remote repository (origin), you'll need to use the 'push' command:
```git push origin master```

For more information check out the tutorial on GitHub: http://learn.github.com/p/intro.html
