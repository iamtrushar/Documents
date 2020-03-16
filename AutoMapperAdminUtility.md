#### Install SQL Server (not express since that has 10gb limit)
```
docker run --name test-sqlserver --restart always -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=yourStrong@Password" -p 1433:1433 -v "C:/Temp:/tmp" -d mcr.microsoft.com/mssql/server:2017-latest
```

Config file stored in value is stored at `%AppData%\[company name]\[application name]` (using [Jot](https://github.com/anakic/Jot))
#### Set the target database to: Data Source=localhost,1433;Initial Catalog=test;User id=SA;Password=[****];
```
cd C:\git\Pandell\AutoMapper\src\Pandell.AutoMapper.AMAdmin
.\bin\Debug\netcoreapp3.1\AMAdmin.exe upgrade target set --target "Data Source=localhost,1433;Initial Catalog=test;User id=SA;Password=yourStrong@Password;"
```

#### Set the target database to: Data Source=trushar-win2016;Initial Catalog=test;User id=SA;Password=[****];
```
cd C:\git\Pandell\AutoMapper\src\Pandell.AutoMapper.AMAdmin
.\bin\Debug\netcoreapp3.1\AMAdmin.exe upgrade target set --target "Data Source=trushar-win2016;Initial Catalog=test;User id=SA;Password=yourStrong@Password;"
```

#### Create a db 
- Open Sql Management Studio
- Connect 
Server: `localhost, 1433`
User: `sa`
Password `yourStrong@Password`

#### Run upgrade to add schema
```
.\bin\Debug\netcoreapp3.1\AMAdmin.exe upgrade run --target "Data Source=trushar-win2016;Initial Catalog=test;User id=SA;Password=yourStrong@Password;"
```
