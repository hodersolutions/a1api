@echo off
title Run School Sync
echo 1. Running from Office
echo 2. Running from Home
echo(
set /p home=Where are you running this sync from: 
if %home% == 1 goto office
if %home% == 2 goto home

:office
cls
python dbfill.py office sqllite %*
pause
exit

:home
cls
echo Okay, you running this sync from Home
echo(
echo 1. MSSQL
echo 2. PostgreSQL
echo 3. SQLLite
echo(
set /p sql=Which db are you running this sync on: 
if %sql% == 1 goto mssql
if %sql% == 2 goto postgres
if %sql% == 3 goto sqllite

:mssql
cls
python dbfill.py home mysql %*
pause
exit

:postgres
cls
python dbfill.py home postgresql %*
pause
exit

:sqllite
cls
python dbfill.py home sqllite %*
pause
exit