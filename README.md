# Random AD User Creator

This Python3 program will create a CSV file containing fictitious user's for an Active Directory test-lab. The program
will assign the following values for each user; first name, last name, initials, username, email address, Password, 
city, state, country, phone number and path.
The csv file can easily be parsed and the user's imported using the included Powershell (.ps1) script.
The AD_User_Creator.py program uses only Python3's built-in CSV and Random packages meaning there are no additional 
python pip packages to install.

**Note:**
The organisational unit must be updated within the program to match your Active Directory setup, otherwise you will run
into issues when adding the users into AD.

## Usage
Be sure to check the OU's in your Active Directory matches the OU's in the program otherwise you will run into issues
when adding the users to the directory. (See below if unsure)
```
python3 AD_User_Creator.py
```

When prompted by the program enter the number of user's you would like to create.  
```
---> How many users would you like to create? 100
```
**OR** 
```
echo "100" | python3 AD_User_Creator.py
```
Both of these methods of execution will result in:  
```
-----> 100 Users created successfully!  
-----> File containing the created users: 'New_Users.csv'! <-----
```

## Add Users To AD Using Powershell
1. Open Powershell on Windows Server on your Domain Controller as Administrator.
2. Transfer "New_Users.csv" & Add_Users.ps1 to your domain controller.  
  
Host where you ran this program
```
m4773l@Python:~//Python/AD_User_Creator$ python3 -m http.server 8010
Serving HTTP on 0.0.0.0 port 8010 (http://0.0.0.0:8010/) ...
10.0.0.107 - - [13/Jun/2022 16:39:10] "GET /Add_Users.ps1 HTTP/1.1" 200 -
10.0.0.107 - - [13/Jun/2022 16:43:57] "GET /New_Users.csv HTTP/1.1" 200 -
```
Powershell on Domain Controller
```
PS C:\Users\Administrator\Downloads> Invoke-WebRequest -Uri http://10.0.0.110:8010/Add_Users.ps1 -OutFile Add_Users.ps1
PS C:\Users\Administrator\Downloads> Invoke-WebRequest -Uri http://10.0.0.110:8010/New_Users.csv -OutFile New_Users.csv
```
3. Run the script!
```
PS C:\Users\Administrator\Downloads> .\Add_Users.ps1
```

Output will show
```
User @{Firstname=Zee; Lastname=Joseph; Initials=ZJ; Fullname=Zee Joseph; Username=z.joseph; Email=z.joseph@m4773l.lab; Password=Password-22!; City=Brisbane; 
State=QLD; Country=AU; Phone=61421455783; Department=Analysts; OU=OU=Analysts,OU=IT_Services,OU=AD_Users,DC=m4773l,DC=lab} was created successfully!
```

## Updating Python Program To Match Your AD Environment
1. Open the .py file in a text editor.
2. Navigate to the create_email function.
```
def create_email(username):
    domain = "EDIT_ME"
```
3. Replace "EDIT_ME" with your AD domain name.
```
def create_email(username):
    domain = "m4773l.lab"
```
4. Navigate to the get department function.
```
def get_department():
    departments = ["Developers", "Finance", "Analysts"]
```
5. Update the departments or add the departments from the program into your AD Environment.
6. Navigate to the create_ou_path function.
```
    def create_ou_path(department):
```
7. Update the Organisational Unit's and the Domain Name to those of your AD Environment. 
```
        if department == "Developers":
        ou_path = f"OU={department},OU=IT_Services,"
```
8. Update the string in the return statement to reflect your AD environment.
```
    return ou_path + "OU=AD_Users,DC=m4773l,DC=lab"
```
9. Save and run the program!