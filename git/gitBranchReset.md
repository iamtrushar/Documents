## Reset branch to point to a head of other branch

Here is an example where I wanted reset my branch  `v2017` to `cleanup` (which Milan created). Now I wanted all the latest changes from `cleanup` since he already picked up from mine. 

```
git checkout v2017
git reset --hard origin/cleanup
git push --force-with-lease
```
1. First line switches you back to `v2017` branch
2. Second line changes where `v2017` points to
3. Third line says "Tell GitHub to point `v2017` at `1528319f2d54d900db4a76018ab2a876abab1173` as well"


## Just clean up after your are done

```
git branch -D cleanup
git push origin :cleanup
```
1. delete branch
2. push changes to remote

