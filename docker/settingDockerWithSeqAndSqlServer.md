### Use docker to run your veryown sql server and seq server.

Wiki for installing [Seq](https://pandell.atlassian.net/wiki/spaces/PLI/pages/306348220/Logging+Seq) server on your Docker
Wiki for installing [SQL](https://pandell.atlassian.net/wiki/spaces/PLI/pages/90701825/Setup+SQL+Server+in+Docker) Server on your Docker

Sql Server

## list all the docker containers/images
docker ps -a

## setup docker image for sql server
docker run -d --name test-sqlserver --restart always -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=yourStrong@Password" -e "MSSQL_PID=Express" -p 1433:1433 -v "C:/Temp:/tmp" mcr.microsoft.com/mssql/server:latest

## setup env variable 
$env:PLI_TEST_SQLSERVERS = "[{ host: 'localhost,1433', path: '/tmp/', share: 'C:\\Temp', username: 'sa', password:'yourStrong(!)Password' }]"

## Powershell to see all the path
Get-Childitem -Path Env:* | Sort-Object Name

## login into the test-sqlserver
docker exec -it test-sqlserver "bash"
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "yourStrong@Password"

## create simple network
docker network create simple-network

## connect the sql server to network
docker network connect simple-network test-sqlserver

## inspect the network to make sure it's connected and grab the ip address of sql server
docker network inspect simple-network

## get IP address of the running server
docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" test-sqlserver


