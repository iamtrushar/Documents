# Stash and Pop

```
# Save your stash
git stash save

# Retrive your stash on the branch in question
git stash pop
```

### Alternate

Just check out the branch you want your changes on, and then ```git stash apply```. Then use ```git diff``` to see the result.
After you're all done with your changes—the apply looks good and you're sure you don't need the stash any more—then use ```git stash drop``` to get rid of it.
I always suggest using git stash apply rather than ```git stash pop```. 
The difference is that apply leaves the stash around for easy re-try of the apply, or for looking at, etc. 
If pop is able to extract the stash, it will immediately also drop it, and if you the suddenly realize that you wanted to extract it somewhere else (in a different branch), or with --index, or some such, that's not so easy. If you apply, you get to choose when to drop.
It's all pretty minor one way or the other though, and for a newbie to git, it should be about the same. (And you can skip all the rest of this!)
