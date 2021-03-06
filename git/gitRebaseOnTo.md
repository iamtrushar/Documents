## Shows how to use `git rebase --onto <parm> <parm>` command

```
mkdir onToRepo
cd .\onToRepo\
echo "# onToRepo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/iamtrushar/onToRepo.git
git push -u origin master
git checkout -b b1
git push --set-upstream origin b1
echo "" > f1
git add .\f1
git commit -m "f1"
cho "" > f2
git add .\f2
git commit -m "f2"
echo "" > f3
git add .\f3
git commit -m "f3"
echo "" > f4
git add .\f4
git commit -m "f4"
echo "" > f5
git add .\f5
git commit -m "f5"
git push

git checkout -b b2
git push --set-upstream origin b2
echo "" > f6
git add .\f6
git commit -m "f6"
echo "" > f7
git add .\f7
git commit -m "f7"
echo "" > f8
git add .\f8
git commit -m "f8"
echo "" > f9
git add .\f9
git commit -m "f9"
echo "" > f10
git add .\f10
git commit -m "f10"
git push

# checkout master and create a new branch
git checkout master

git checkout -b someOtherBranch
git push --set-upstream origin someOtherBranch
echo "" > f0
git add .\f0
git commit -m "f0"
git push

# goto git hub and do a PR and merge with master for someOtherBranch

git checkout master
git pull --all

git checkout b1
git rebase master


git checkout b2
# Find the SHA before using this command git rebase --onto lwMaps.Web <sha1-just-before-first-commit-to-rebase>
git rebase --onto b1 01274f4236a72f173f519abd18f576e161b1416c


git checkout b1
git pf

git checkout b2
git pf
```

History in gitk ![gitk all](https://github.com/iamtrushar/Documents/images/gitkHistory.PNG "History")