### How to set `base` for `follow-up` branch correctly during merge:

Typical scenario: master -> branchA -> branchB -> .... -> branch-N

Assume your PR is approved for the following branches:

1. Merge PR `branchA`
2. Rebase `branchB` on the new master, push
3. Update PR `branchB` to go against `master`
4. Delete remote branch for the PR that got merged in step 1
5. Once `branchB` finishes building, merge that one as well
6. Delete remote branch for the PR that got merged in step 5
