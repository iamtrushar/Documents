```
git clone https://github.com/iamtrushar/sqashRepo.git

cd .\sqashRepo\

git checkout -b squash

git push --set-upstream origin squash
echo "" > f1
git add .\f1
git commit -m "f1"
echo "" > f2
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

# commit SHA for f1: b236e95592ffff52acc362c1a60a68d1b18e8d0c

# -i option will be interactive
git rebase -i b236e95592ffff52acc362c1a60a68d1b18e8d0c

# opens vi
# squash f3, f4 into f2
pick a0913d1 f2
squash fa5e8c4 f3
squash 1b59dfb f4

#save and add a new commit message
```


