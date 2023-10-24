import configparser
auto_save = bool("choose")

#General settings to get user input
name = input("Enter your name: ")
age = input("How old are you?: ")
email = input("Enter your email address: ")

#Setting section
theme = input("Enter the theme: ")
language = input("Enter the langage: ")
auto_save = bool('auto_save')  

#Database settings
host = input("Enter the localhost: ")
port = int("Enter the port: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

print(f"My name is {name} I am {age} years old my email address = {email}")
print(f"theme = {theme} language = {language} auto_save = {auto_save}")
print(f"host = {host} port = {port} username = {username} password= {password}")