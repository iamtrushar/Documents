## Here's how to update the ORM - by Charles F.
1.  Create a new branch
2.  Get the updated ORM from the DB team
3.  Copy the ModelSQL.Designer.cs and ModelSQL.edmx files into the LW-LPM6\src\Domain\Model\SQL (they will overwrite the existing ORM)
4.  Compile LW-LPM6 and fix any compilation errors caused by the new ORM
5.  Run the SmartClient and other applications using an DB upgraded to the new ORM to catch any obvious run-time errors
6.  Push the changes to the branch, rebase onto the master, and created a pull request
7.  When your pull request goes through, let the DB know so they can update the rest of the DBs
