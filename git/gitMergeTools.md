## Git diff tool - examdiff
Running into git merge conflict when rebasing is like stepping into another world. Fortunately we have tools out there. 
Here is are the ones that Milan. G and Jason. H introduced me. 

### Good quality 3-way merge tool:

[ExamDiff](https://www.prestosoft.com/edp_examdiffpro.asp), 
[Beyond Compare (Pro)](http://www.scootersoftware.com/features.php) &
[P4Merge is a decent free 3-way merge tool from Perforce](https://www.perforce.com/downloads/visual-merge-tool)

Milan's provided me with Pandell licensed `ExamDiff` found [here](https://github.com/iamtrushar/Documents/blob/master/exe/examdiff.sfx.exe). It is password protected so ask me.

Edit your `.gitconfig` (or `git config --global --edit`):

```# Diff/merge configuration
[diff]
    tool = examdiff
[difftool]
    prompt = false
[difftool "p4merge"]
    path = c:/Users/milang/AppData/Local/Perforce/p4merge.exe
[difftool "examdiff"]
    cmd = ~/Dropbox/Private/Setup/Bin/dev/examdiff/ExamDiff.exe \"$LOCAL\" \"$REMOTE\" -nh
[merge]
    # Don't keep .orig files
    keepbackup = false
    tool = examdiff
[mergetool]
    keepBackup = false
    prompt = false
[mergetool "p4merge"]
    path = c:/Users/milang/AppData/Local/Perforce/p4merge.exe
[mergetool "examdiff"]
    cmd = ~/Dropbox/Private/Setup/Bin/dev/examdiff/ExamDiff.exe -merge \"$LOCAL\" \"$BASE\" \"$REMOTE\" -o:\"$MERGED\" -dn1:Theirs -dn2:Base -dn3:Yours -dno:Output -nh
    trustExitCode = false
```

Notice the config for both `p4merge` and `examdiff`, with `examdiff` being the default tool.
Once you have that in place, you simply:

```git mergetool```
Git will then open conflicting files one by one and your job is to resolve conflicts (each 3-way merge tool has a mechanism to chose "their" changes, "your" changes, mixture thereof or manually edit the change)
Once conflicts are resolved, resume rebase:

```git rebase --continue```

(Optional Step) Next, start examdiff import setting from examdiff_milan_options.txt ![see image](https://github.com/iamtrushar/Documents/blob/master/images/ExamDiff%20Import%20From%20File.png) I used Milan's setting.

