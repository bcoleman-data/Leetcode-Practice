import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #drop duplicates from dataframe sort in descending order and reset index
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    # base case if number of distinct salaries is less than N return null
    if(len(salaries) < 2 ) : return pd.DataFrame({"SecondHighestSalary": [None]})

    return pd.DataFrame({"SecondHighestSalary": [salaries.iloc[1]]})
    