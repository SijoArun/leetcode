import pandas as pd

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['Bonus'] = (~(employees['name'].map(lambda row: str(row).startswith('M'))) & (employees['employee_id'] % 2 == 1)) == True
    employees.loc[employees['Bonus'] == False, 'salary'] = 0
    return employees.rename(columns={'salary':'bonus'}).filter(items={'employee_id','bonus'}).sort_index(axis=1, ascending=False).sort_values(by='employee_id',ascending=True)


print(calculate_special_bonus(employees))