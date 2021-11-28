@echo off
setlocal EnableDelayedExpansion
setlocal EnableExtensions

:WHILE_0
if 1 EQU 1 (
  python manage.py runserver
  sleep 2
  goto WHILE_0
)