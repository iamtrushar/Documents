### How to Upgrade Lpm Db to latest:

Go to `C:\git\LW-LPM6\build\Debug\DbUpgrade`

Enter the following command: 
`LwDbUpgrade.exe -d "hsql2016d;agmt_lpm_ds;agmt_lpm_ds;agmt" --upgradeLpm`

Sample Result:
Initializing: OK (5%)
Running command: In progress (5%)
    Upgrading LPM: In progress (5%)
        Readying database: OK (14%)
        Applying upgrade tasks: OK (71%)
        Applying synchronization tasks: OK (100%)

LwDbUpgrade succeeded (total time 00:00:00.3980419)

Upgraded LPM database: Data Source=hsql2016d;Initial Catalog=agmt_lpm_ds;Integrated Security=False;User ID=agmt_lpm_ds;Password=[****];Pooling=False

C:\git\LW-LPM6\build\Debug\DbUpgrade>
