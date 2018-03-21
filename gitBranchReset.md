```
git checkout v2017
git reset --hard origin/cleanup
git push --force-with-lease
```
1. First line switches you back to `v2017` branch
2. Second line changes where `v2017` points to
3. Third line says "Tell GitHub to point `v2017` at `1528319f2d54d900db4a76018ab2a876abab1173` as well"


```
git branch -D cleanup
git push origin :cleanup
```
1. delete branch
2. push changes to remote

