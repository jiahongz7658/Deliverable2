import pandas as pd
from jinja2 import Environment, FileSystemLoader

# Paths to the CSV files
mens_csv_file = 'meets/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv'
womens_csv_file = 'meets/37th_Early_Bird_Open_Womens_5000_Meters_HS_Open_5K_24.csv'

# Function to read and parse CSV data
def read_csv_data(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract meet details and comments
    meet_name = lines[0].strip()
    meet_date = lines[1].strip()
    team_results_link = lines[2].strip()
    race_comments = lines[3].strip()

    # Find the start and end of each section
    teams_start = lines.index('Place,Team,Score\n') + 1
    athletes_start = lines.index('Place,Grade,Name,Athlete Link,Time,Team,Team Link,Profile Pic\n') + 1

    # Read team results
    team_results_lines = lines[teams_start:athletes_start-1]
    team_results = pd.DataFrame([line.strip().split(',') for line in team_results_lines], columns=['Place', 'Team', 'Score'])

    # Read athlete results
    athlete_results_lines = lines[athletes_start:]
    athlete_results = pd.DataFrame([line.strip().split(',') for line in athlete_results_lines], columns=['Place', 'Grade', 'Name', 'Athlete Link', 'Time', 'Team', 'Team Link', 'Profile Pic'])

    # Transform data into dictionary format
    teams = team_results.to_dict(orient='records')
    athletes = athlete_results.to_dict(orient='records')
    
    # Drop the 'Profile Pic' column from the athlete data
    for athlete in athletes:
        athlete.pop('Profile Pic', None)
    
    return meet_name, meet_date, team_results_link, race_comments, teams, athletes

# Read data from men's and women's CSV files
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, men_teams, men_athletes = read_csv_data(mens_csv_file)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, women_teams, women_athletes = read_csv_data(womens_csv_file)

# Setup Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader(searchpath="."))
template = env.get_template('template.html')

# Context data to pass to the template
context = {
    'mens_meet_name': mens_meet_name,
    'mens_meet_date': mens_meet_date,
    'mens_team_results_link': mens_team_results_link,
    'mens_race_comments': mens_race_comments,
    'men_teams': men_teams,
    'men_athletes': men_athletes,
    'womens_meet_name': womens_meet_name,
    'womens_meet_date': womens_meet_date,
    'womens_team_results_link': womens_team_results_link,
    'womens_race_comments': womens_race_comments,
    'woman_teams': women_teams,
    'women_athletes': women_athletes
}

# Render the HTML content with context data
html_content = template.render(context)

# Write rendered HTML to 'index.html'
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML file 'index.html' generated successfully!")