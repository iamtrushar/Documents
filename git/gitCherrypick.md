# Cherry picking commits from other branches
This example illustrates the techinque of Cherry picking commits SHA from other branches and bringing them to yours

## Step 1, get the SHA hash from the other branch that you like. 

For example below, the `nuget-build-fix` branch has one commit with SHA `b3ecf5728cd0f3fe302aca7be1014148dd5fd6d9` that I am interested in:


```
git checkout nuget-build-fix

git log -2
commit b3ecf5728cd0f3fe302aca7be1014148dd5fd6d9 (HEAD -> nuget-build-fix, origin/nuget-build-fix)
Author: davidb <davidb@net.pandell.com>
Date:   Mon Apr 9 19:56:28 2018 -0600

    Git NuGet package build fix.

commit a31b50a6a199e91b029e55367d420c03f915d7cb
Author: Trushar Mistry <tmistry@landworks.com>
Date:   Mon Mar 26 15:09:45 2018 -0500

    Add package.config
```

Now fire cherrypick command after switching to your branch.
```
git checkout esri10.6
Switched to branch 'esri10.6'
Your branch is up to date with 'origin/esri10.6'.

git cherry-pick b3ecf5728cd0f3fe302aca7be1014148dd5fd6d9
[esri10.6 f2f7258] Fix NuGet packaging.
 Author: davidb <davidb@net.pandell.com>
 Date: Mon Apr 9 19:38:27 2018 -0600
 1 file changed, 1 insertion(+), 1 deletion(-)
```

When everything looks good, you can delete the old branch to clean up your work (less distraction if you happen to look at it later in life)
