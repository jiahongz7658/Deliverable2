# Deliverable2
Overview

This Python script processes a CSV file containing race results, processes athlete and team data, incorporates images from a specified directory, and uses the Jinja2 template engine to generate an HTML file. The generated HTML file is a report of the race details, including team and athlete results, images, and additional comments.

Dependencies Before running the script, please ensure you have the following Python packages installed:

    pandas: For handling CSV data manipulation.
    jinja2: For templating and generating HTML output.

You can install these packages using pip if they're not already installed:

    bash
    pip install pandas jinja2

Files and Directories

- CSV File: Update the script to specify the correct path to the CSV file containing race data.
- Images Directory: Ensure the directory path to images is accurate. Images in this directory will be listed and used in the report.
- Template File: A Jinja2 HTML template (template.html) is required to render the final HTML report. Make sure this template is in the current working directory or update the script with the correct path.
- Output File: The script will generate an index.html file in the current directory containing the rendered race report.

How to Run the Script

1. Set Paths: Modify the script to ensure the paths to the CSV file and the images directory are correct. Update these lines in the script:
2. python
csv_file = 'meets/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv' images_directory = 'earlybird'
3. Prepare Environment: Ensure the CSV file, images directory, and template.html are correctly structured and available in the specified paths.
4. Execute Script: Run the script from the command line by navigating to the directory where the script is located and typing:
5. bash
    python your_script_name.py
6. Replace your_script_name.py with the actual name of your Python file.
7. Output: After running, the script will generate an index.html file in the current directory. Open this file in a web browser to view the report.
