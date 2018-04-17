## How to rebase on master


Here is an example of how rebase works with pull request. 

Make sure you have basic configuration setup in gitConfig from here https://github.com/pandell/SamplePliWeb/wiki/Git-configuration. Git config is found in %userprofile%\.gitConfig

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

