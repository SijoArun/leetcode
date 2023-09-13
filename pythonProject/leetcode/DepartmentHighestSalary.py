import pandas as pd

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
     if employee.empty or department.empty:
          return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

     merged_df = employee.merge(department, left_on='departmentId', right_on='id',
                                suffixes=('_employee', '_department'))

     highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])

     highest_salary_df = highest_salary_df.reset_index(drop=True)

     result_df = highest_salary_df[['name_department', 'name_employee', 'salary']]


     result_df.columns = ['Department', 'Employee', 'Salary']

     return result_df




print(department_highest_salary(employee,department))
