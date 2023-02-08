# Spiff Data Engineering Candidate Coding Exercise -- Commission Estimator

## To Run 
1. In whatever python editor you choose, cd to the project directory
2. Create a virtual enviornment (poetry is a great option, steps are below)
    a. cd to project directory
    b. 'poetry new {project_name}'
    c. cd to that new project folder 
    d. create the virtual environment: 'python -m venv .venv'
    e. activate the virtual environment: 'source .venv/bin/activate' 
    f. 'pip install -r requirements.txt'
3. To run - 'python main.py' 
4. The example output is 'Total Commissions: Ian made $23340.0 in commissions between 2023-04-15 and 2023-05-15' 
    a. Change the print_lines boolean to False if you do not want to see the dataframe that breaks the data down by deal for the sales rep in the time parameter given.  I think it's useful to see them line by line and sales reps like visibility too.  