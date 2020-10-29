# SQL lite

## Create table

`CREATE TABLE Users (Name VARCHAR(128),email VARCHAR(128))`

## Insert row

`insert into Users(name,email) values ('Ulrich','ulrich@nilsson.se')`  
`insert into Users(name,email) values ('Person2','person2@nilsson.se')`

## Delete

`DELETE FROM Users WHERE Name='Person2'`

## Update

`UPDATE Users SET name='Person 3' where name='Person2'`
