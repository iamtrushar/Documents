```
git pull
git checkout lwMapsUI # <- notice rebasing the LAST branch in chain
git rebase origin/master
git pf
git checkout widgetIssues
git reset --hard <find-sha1-for-this-branch-under-rebased-lwMapsUI>
git pf
git checkout lwMaps.Web
git reset --hard <find-sha1...>
git pf
```
