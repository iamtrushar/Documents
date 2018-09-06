
## Temp or bookmark branche in git

```
git checkout -b temp origin/widgetIssues
git checkout widgetIssues
git reset --hard lwMaps.Web
git cherry-pick ...
...
git branch -D temp

```


First, the above creates a "bookmark" branch `temp` (so you don't lose sight of what needs to be cherry-picked)
Then, `widgetIssues` gets reset to `lwMaps.Web` -- i.e. both branches point at exactly the same commit
After that comes the hard work of picking commits you want to preserve
And finally, the "bookmark" branch is deleted
