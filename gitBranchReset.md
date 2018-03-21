```
git checkout v2017
git reset --hard origin/cleanup
git push --force-with-lease
```
First line switches you back to `v2017` branch
Second line changes where `v2017` points to
Third line says "Tell GitHub to point `v2017` at `1528319f2d54d900db4a76018ab2a876abab1173` as well"


```
git branch -D cleanup
git push origin :cleanup
```
delete branch
push changes to remote
