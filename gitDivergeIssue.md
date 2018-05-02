If changes are on the same branch and you have fetched those changes, then you would do a rebase to put your changes on top of his:

```git rebase origin/VS2017 VS2017```

That will take all of the changes that are in `VS2017` but not in `origin/VS2017` and add them to the end of `origin/VS2017`.
If you don't have his changes locally yet, you would fetch them with:

```git fetch --all```
