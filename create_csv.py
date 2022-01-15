#!/usr/bin/python3
import sys
import time

# Check if proper domain name specified
if (len(sys.argv) < 2):
    print("USAGE: create_csv.py [domain]")
    exit(0)
elif (sys.argv[1].find(".") == -1):
    print("Domain format: [sub_domain].[top_domain]") 
    exit(0)

# Get domain components
sub_domain = sys.argv[1].split(".")[0]
top_domain = sys.argv[1].split(".")[1]

# Print full domain name
print(f'Domain: {sub_domain}.{top_domain}')
time.sleep(.2)

# Open files
fin = open("names.txt", "r")
fout = open("users.csv", "w")

# Read lines from input file
lines = fin.readlines()

# write headers to output file
fout.write("name,given_name,surname,principal_name,ou\n")

for line in lines:
    # Extract name, surname
    words = line.split(" ")
    name = words[0]
    surname = words[1].strip()

    # Create principal name
    principal_name = line.strip().lower().replace(" ", ".")

    # Write to outfile
    fout.write(f'{name} {surname},')
    fout.write(f'{name},')
    fout.write(f'{surname},')
    fout.write(f'{principal_name},')
    fout.write(f'"OU=new_users,DC={sub_domain},DC={top_domain}"\n')
    print(f'[OK] {name} {surname}')
    time.sleep(.1)

