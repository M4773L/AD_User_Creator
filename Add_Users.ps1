# Name: Add_Users.ps1
# Author: M4773L
# Description: This script will add the users from 'New_Users.csv' file into Active Directory.

# Import the Active Directory module
Import-Module ActiveDirectory

# Load the CSV file containing the created users and store as variable $USERS
$USERS = Import-Csv .\New_Users.csv

# For loop to iterate through each row of user details in the CSV file
foreach ($USER in $USERS) {
    $USERNAME = $USER.Username

    # Check to see if the user already exists in Active Directory
    if (Get-ADUser -F {SamAccountName -eq $USERNAME}) {
        Write-Warning "Error: User - $USERNAME already exists in Active Directory!"
    }
    else {
        $userProps = @{
            SamAccountName          = $USER.Username
            Path                    = $USER.OU
            GivenName               = $USER.Firstname
            Surname                 = $USER.Lastname
            Name                    = $USER.Fullname
            Initials                = $USER.Initials
            UserPrincipalName       = $USER.Email
            City                    = $User.City
            State                   = $USER.State
            Country                 = $USER.Country
            Department              = $USER.Department
            MobilePhone             = $USER.Phone
            AccountPassword         = (ConvertTo-SecureString $USER.Password -AsPlainText -Force)
            ChangePasswordAtLogon   = $true
            Enabled                 = $true
        }

        New-ADUser @userProps
        Write-Host -ForegroundColor Cyan "User $USER was created successfully!"
    }
}
