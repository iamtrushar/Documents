4/24/2020

```
# run webservice project
cd C:\git\Pandell\AutoMapper> 
dotnet run --project .\src\Pandell.AutoMapper.WebService\

# output:
[11:09:58 INF] AutoMapper is starting ?? <s:Pandell.AutoMapper.WebService.Program>
[11:09:58 INF] Upgrading database <s:Pandell.AutoMapper.WebService.Program>
[11:09:59 INF] Now listening on: https://localhost:44310 <s:Microsoft.Hosting.Lifetime>
[11:09:59 INF] Now listening on: http://localhost:44311 <s:Microsoft.Hosting.Lifetime>
[11:09:59 INF] gRPC server is now listening on localhost:55310 <s:Pandell.AutoMapper.WebService.WebServiceExtensions+GrpcServer>
[11:09:59 INF] Application started. Press Ctrl+C to shut down. <s:Microsoft.Hosting.Lifetime>
[11:09:59 INF] Hosting environment: Development <s:Microsoft.Hosting.Lifetime>
[11:09:59 INF] Content root path: C:\git\Pandell\AutoMapper\src\Pandell.AutoMapper.WebService <s:Microsoft.Hosting.Lifetime>

```
```
# test amadmin connection (another terminal)
cd C:\git\Pandell\AutoMapper\src\Pandell.AutoMapper.AMAdmin\bin\Debug\netcoreapp3.1> 
.\AMAdmin.exe grpc testConnection "localhost:55310"

# output: 
Trying unsecured channel to localhost:55310
Service Version: 0.0.0.0 Database Version: 1.A4343DA6-BC1D-417C-ABD6-1D0EDA7948FE

Trying secured channel to localhost:55310
Connection failed.
...
...
```

```
# version check
PS C:\git\Pandell\AutoMapper\src\Pandell.AutoMapper.AMAdmin\bin\Debug\netcoreapp3.1> 
.\AMAdmin.exe --version
# output
AMAdmin version 0.0.0.0
```














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

---

Start Services
```
yarn start-service
```

