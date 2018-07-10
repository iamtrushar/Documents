## Git's Default Editor Vim - How To

By default Git will open Vim as editor. 
- You basically need to type 'I' to start editing. 
- After that ESC and type :q to quit or :w to save the file. 
- You can also combine them: :wq to save and exit Vim.
- You can make vim exit with a non-zero exit code to cancel the rebase by typing :cq. 
From the vim help page we see that cq is short for cquit:
*:cq* *:cquit*
:cq[uit][!]             Quit Vim with an error code, so that the compiler
                        will not compile the same file again.
                        WARNING: All changes in files are lost!  Also when the
                        [!] is not used.  It works like ":qall!" |:qall|,
                        except that Vim returns a non-zero exit code.
For more information about Vim check the [official documentation](https://www.vim.org/docs.php)

- You can do find and replace as follows:
Replace All:
:%s/foo/bar/g
Find each occurrence of 'foo' (in all lines), and replace it with 'bar'.

For specific lines:
:6,10s/foo/bar/g
Change each 'foo' to 'bar' for all lines from line 6 to line 10 inclusive.

To change Vim for any other editor check the [Git Environment Variables](https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables) or [older posts](https://stackoverflow.com/questions/2596805/how-do-i-make-git-use-the-editor-of-my-choice-for-commits) with a similar question: How do I make Git use the editor of my choice for commits?
