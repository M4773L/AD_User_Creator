"""
Program: Random_AD_User_Creator
Author: M4773L
Date: 26/01/2022
Description: This program will create a Comma Separated Value (CSV) file that contains ready to be imported into an
            Active Directory Test-lab environment. The program begins by checking that the First_Names.txt and
            Last_Names.txt files exist, the script will then create the New_Users.csv file and write the headings to
            each column in the first row. The script will then ask the user how many users to create, upon receiving
            valid input (an integer), the script will loop through the main function the number of times specified and
            write each user created to a new row in the .csv file.
"""

from random import choice, randint
import csv


# Initial function to check the required name files exist and to create and then write the header to the .csv file.
def init():
    # Print a title for the program and let the user know what is happening.
    print("-----------------------------------------------------------------")
    print("------------------> Fictitious AD User Creator <-----------------")
    print("-----------------------------------------------------------------")
    print("\n---> Checking First & Last name-files exist! ")

    # Check First_Names.txt exists and count the number of names
    try:
        with open("First_Names.txt", 'r') as in_file:
            file = in_file.read()
            first_names = file.split()
            print(f"---> 'First_Names.txt' Exists! The file contains: {len(first_names)} first names!")
            in_file.close()

    except Exception as e:
        print(f"---> Error: 'First_Names.txt' does NOT exist!!! {e}")

    # Check Last_Names.txt exists and count the number of names
    try:
        with open("Last_Names.txt", 'r') as in_file:
            file = in_file.read()
            last_names = file.split()
            print(f"---> 'Last_Names.txt'  Exists! The file contains: {len(last_names)} last names!")
            in_file.close()

    except Exception as e:
        print(f"---> Error: 'Last_Names.txt' does NOT exist!!! {e}")

    # Try to write header to .csv file.
    try:
        header = ["Firstname", "Lastname", "Initials", "Fullname", "Username", "Email", "Password", "City", "State",
                  "Country", "Phone", "Department", "OU"]
        with open("New_Users.csv", 'w', encoding='UTF8') as out_file:
            writer = csv.writer(out_file, delimiter=",")
            writer.writerow(header)
            out_file.close()
        print("---> Headers written to CSV file!")

    except Exception as e:
        print(f"---> Error: Unable to create CSV file! {e}")

    print("---> Checks Complete - Everything is good!")


# This function will return a random name from the first_names list.
def get_firstname():
    with open("First_Names.txt", 'r') as name_file:
        first_names = name_file.read().splitlines()
        name_file.close()
        random_firstname = choice(first_names)
    return random_firstname


# This function will return a random name from the last_names list.
def get_lastname():
    with open("Last_Names.txt", 'r') as name_file:
        last_names = name_file.read().splitlines()
        name_file.close()
        random_lastname = choice(last_names)
    return random_lastname


def user_initials(firstname, lastname):
    first_initial = str(firstname[0])
    last_initial = str(lastname[0])
    user = first_initial + last_initial.capitalize()
    return user


# Create a username for each user created, the naming convention is: 'first_name_initial.lastname' e.g. 'j.smith'
def create_username(firstname, lastname):
    first_initial = str(firstname[0])
    username = f"{first_initial}.{lastname}".lower()
    return username


# From the username add the domain name to create an email address for each user.
def create_email(username):
    domain = "<Change_Me>"
    email = f"{username}@{domain}"
    return email


# The same password will be used for each of the created users, at first login they will be required to change password.
def login_password():
    password = "Password-22!"
    return password


# Randomly select a city from the list of Australian cities provided.
def choose_city():
    cities = ["Adelaide", "Sydney", "Brisbane", "Perth"]
    city = choice(cities)
    return city


def get_state(city):
    if city == "Adelaide":
        return "SA"
    elif city == "Sydney":
        return "NSW"
    elif city == "Brisbane":
        return "QLD"
    elif city == "Perth":
        return "WA"


# Create a mobile number for each user created, the last 3 digits of the number are randomly chosen.
def create_phone_number():
    prefix = "61"
    main_number = "499455"
    random_user_number = str(randint(100, 999))
    user_phone_number = prefix + main_number + random_user_number
    return user_phone_number


# Randomly choose a department from the list for each of the users created.
def get_department():
    departments = ["Developers", "Finance", "Analysts"]
    department = choice(departments)
    return department


# Match each department to apply the appropriate Organisational Units (OU)
# Update this section of the program with the Organisational Unit's from your Active Directory
def create_ou_path(department):
    if department == "Developers":
        ou_path = f"OU={department},OU=IT_Services,"
    elif department == "Finance":
        ou_path = f"OU={department},OU=Business_Management,"
    elif department == "Analysts":
        ou_path = f"OU={department},OU=IT_Services,"

    return ou_path + "OU=AD_Users,DC=<Change_Me>,DC=>Change_Me"


# This function compiles all the fields generated about each user into a list ready to write to the csv file.
def create_row(firstname, lastname, initials, fullname, username, email, password, city, state, country,
               phone_number, department, ou):
    new_user = [firstname, lastname, initials, fullname, username, email, password, city, state, country,
                phone_number, department, ou]
    return new_user


# Write the new_user list to the New_Users.csv file.
def write_csv(new_user):
    with open("New_Users.csv", 'a', encoding='UTF8') as out_file:
        writer = csv.writer(out_file, delimiter=",")
        writer.writerow(new_user)
        out_file.close()


# Main function - where it is all tied in together.
def create_user():
    firstname = get_firstname()
    lastname = get_lastname()
    initials = user_initials(firstname, lastname)
    fullname = firstname + " " + lastname
    username = create_username(firstname, lastname)
    email = create_email(username)
    password = login_password()
    city = choose_city()
    state = get_state(city)
    country = "AU"
    department = get_department()
    ou = create_ou_path(department)
    phone_number = create_phone_number()

    new_user = create_row(firstname, lastname, initials, fullname, username, email, password,
                          city, state, country, phone_number, department, ou)
    write_csv(new_user)

    # Print the usernames of the users the program has created to the terminal.
    user_list = [username]
    for user in user_list:
        print(f"\t\t\t\t\t\t{user}")

    return True


# Main program
if __name__ == "__main__":
    init()
    while True:
        try:
            number_of_users = int(input("\n---> How many users would you like to create? "))
            break

        except ValueError:
            print("---> Error: Not an integer - Try again!")
            continue

    print("\n---> Usernames Created:")
    for i in range(number_of_users):
        create_user()

    print(f"\n-----> {number_of_users} Users created successfully!")
    print("-----> File containing the created users: 'New_Users.csv'! <-----")
    print("-----------------------------------------------------------------\n")
