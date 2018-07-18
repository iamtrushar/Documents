## How to rebase on master

Here is an example of how rebase works with pull request. 

Make sure you have basic configuration setup in gitConfig from [here](https://github.com/pandell/SamplePliWeb/wiki/Git-configuration). Git config is found in %userprofile%\.gitConfig

Create two branches (`branch1` & `branch2`) from `master` repo, add two files (`file1`, `file2` respectively in each branch) and pushed them to remote. Next create a PR for `branch1` and approve it. See below upto this point:

```
git clone https://github.com/trusharmistry/practiceRepo

git branch branch1
git branch branch2

git push --set-upstream origin branch1
git push --set-upstream origin branch2

git checkout branch1

echo "content of file1.md" > file1.md

git add .\file1.md
git commit -m "added file1.md"

git push

git checkout branch2

echo "content of file2.md" > file2.md

git add .\file2.md
git commit -m "added file2.md"

git push
```

Since PR is approved I now do the rebase as per:

```
git checkout master 

git pull --all

git checkout branch2

# rebase put your changes on top of master
git rebase master

# git pf (is an alias git push --force-with-lease). This will push your rebase activity up to remote. 
git pf
```

Additionally, sometime merge conflict happens (see here how to setup git's merge tools [here](https://github.com/iamtrushar/Documents/blob/master/gitMergeTools.md))

Find the SHA using `git log -x or gitk --all`

```
git rebase -i ca6b47f92ea4248d5f762dc048d395a048a15408
```

This will open an editor (see how to use VIM editor [here](https://github.com/iamtrushar/Documents/blob/master/vimEditorHowTo.md))
```
pick 99a222ae Update ignore file from /.vs to *.vs
pick 162c8ebb Fix code analysis issues: Add [Serializable] attribute. Add GetObjectData implementation.

# Rebase ca6b47f9..162c8ebb onto ca6b47f9 (2 commands)
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit```
You change `pick` on the first line to `d` (or `drop`), then close the editor saving changes. Git will then perform interactive rebase, dropping the specified commit
```

## Milan's notes after `Lpm6` unirepo:

Please note that I rebased all branches (except pcp) on the new `master`, so you will have to update your local branch to point to the new commits:

```
git checkout your-branch
git fetch --all
git reset --hard origin/your-branch
```
(This assumes you have no pending local changes)


If you have local pending changes, you have to rebase onto the remote branch:

```
git checkout your-branch
git fetch --all
git rebase origin/your-branch
```

