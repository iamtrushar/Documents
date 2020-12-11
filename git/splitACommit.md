Checkout the branch that you want to modify (e.g. pj/feature) 
- Start an interactive rebase which includes your commit. OR At a minimum, `git rebase -i commit^` will start the rebase at the commit you want to split
- Mark the commit(s) that you want to split with `edit`
- When git presents the commit that you want to split:
  - Reset state to the previous commit using `git reset HEAD^`
  - Use `git add <files>` to carefully and incrementally add changes to the index
  - Run `git commit` when you have a set of atomic changes that you are ready to commit
  - Repeat the git add and git commit process until you have processed each set of changes represented by the commit
- Run `git rebase --continue` to resume or finish the rebase
