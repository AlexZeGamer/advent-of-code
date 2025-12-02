import requests
from dotenv import load_dotenv
import os
import sys
import datetime

load_dotenv()

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

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
        print(f'{GREEN}Downloaded input file for {year}/{day}{RESET}')
    else:
        print(
            f'{RED}' \
            f'Error getting input for day {day} of year {year} (Status code: {r.status_code})\n' \
            f'Message: "{r.text.strip()}"' \
            f'(Maybe update the cookie in the .env file?)' \
            f'{RESET}'
        )
else:
    print(f'{YELLOW}File {year_directory}/{day_directory}/input.txt already exists, ignoring...{RESET}')

# Create python template
if not os.path.exists(f"{year_directory}/{day_directory}/code.py"):
    with open(f"{year_directory}/{day_directory}/code.py", "w") as f:
        with open('template.py', 'r') as template_file:
            template_content = template_file.read()
            f.write(template_content.replace("{year}", str(year)).replace("{day}", str(day)).replace("{author}", AUTHOR))
    print(f'{GREEN}Created template for {year}/{day}{RESET}')
else:
    print(f'{YELLOW}File {year_directory}/{day_directory}/code.py already exists, ignoring...{RESET}')
