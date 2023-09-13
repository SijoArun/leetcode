import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salary = employee['Salary'].sort_values(ascending=False).drop_duplicates()
    if N > len(sorted_salary):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    nth_highest = sorted_salary.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})


print(nth_highest_salary(employee,2))