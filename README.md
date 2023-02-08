# Spiff Data Engineering Candidate Coding Exercise -- Commission Estimator

## To Run 
1. In whatever python editor you choose, cd to the project directory
2. Create a virtual enviornment (poetry is a great option, steps are below) 
3. To run: 'python main.py' 
4. The example output is 'Total Commissions: Ian made $23340.0 in commissions between 2023-04-15 and 2023-05-15' 
    a. Change the print_lines boolean to False if you do not want to see the dataframe that breaks the data down by deal for the sales rep in the time parameter given.  I think it's useful to see them line by line and sales reps like visibility too. 

## Poetry Setup 
1. cd to project directory
2. 'poetry new {project_name}'
3. cd to that new project folder 
4. create the virtual environment: 'python -m venv .venv'
5. activate the virtual environment: 'source .venv/bin/activate' 
6. 'pip install -r requirements.txt'