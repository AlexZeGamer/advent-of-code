import requests
from dotenv import load_dotenv
import os
import sys
import datetime

load_dotenv()

AOC_COOKIE = os.environ['AOC_COOKIE']   # Connection cookie from https://adventofcode.com/ ("session" cookie)
AUTHOR = os.environ['AUTHOR']           # Author name

day  = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.datetime.now().day
year = int(sys.argv[2]) if len(sys.argv) > 2 else datetime.datetime.now().year


# Create the folder for the year and/or day if they don't exist
year_directory = str(year)
if not os.path.exists(year_directory):
    os.mkdir(year_directory)

day_directory = f'{day:02d}'
if not os.path.exists(f'{year_directory}/{day_directory}'):
    os.mkdir(f'{year_directory}/{day_directory}')


# Download the input file
if not os.path.exists(f'{year_directory}/{day_directory}/input.txt'):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.get(url=url, cookies={"session": AOC_COOKIE})

    if r.ok:
        with open(f"{year_directory}/{day_directory}/input.txt", "wb") as f:
            f.write(r.content)
        print('\033[92m', end='') # Green
        print(f'Downloaded input file for {year}/{day}')
        print('\033[0m', end='')
    else:
        print('\033[91m', end='') # Red
        print(f'Error getting input for day {day} of year {year} (Status code: {r.status_code})')
        print(f'Message: "{r.text.strip()}"')
        print('(Maybe update the cookie in the .env file?)')
        print('\033[0m', end='')
else:
    print('\033[93m', end='') # Yellow
    print(f"File {year_directory}/{day_directory}/input.txt already exists, ignoring...")
    print('\033[0m', end='')


# Create python template
if not os.path.exists(f"{year_directory}/{day_directory}/code.py"):
    with open(f"{year_directory}/{day_directory}/code.py", "w") as f:
        f.write(
            f"# Advent of Code {year} - Day {day}\n"
            f"# https://adventofcode.com/{year}/day/{day}\n"
            f"# Author: {AUTHOR}\n" 
            f"\n"
            f"with open('input.txt', 'r') as f:\n"
            f"    text = f.read()\n"
            f"\n\n"
            f"# Part 1\n"
            f"total = 0\n"
            f"\n\n\n"
            f"print(f'Part 1 : {{total}}')\n"
            f"\n\n"
            f"# Part 2\n"
            f"total = 0\n"
            f"\n\n\n"
            f"print(f'Part 2 : {{total}}')\n"
        )
    print('\033[92m', end='') # Green
    print(f"Created template for {year}/{day}")
    print('\033[0m', end='')
else:
    print('\033[93m', end='') # Yellow
    print(f"File {year_directory}/{day_directory}/code.py already exists, ignoring...")
    print('\033[0m', end='')
