import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

def nth_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    sorted_salary = employee['Salary'].sort_values(ascending=False).drop_duplicates()
    N = sorted_salary.count()
    print(N)
    if N < 2:
        return pd.DataFrame({f'SecondHighestSalary': [None]})
    elif N > 2:
        second_highest_salary = sorted_salary.iloc[N - (N-1)]
        return pd.DataFrame({f'SecondHighestSalary': [second_highest_salary]})
    else:
        second_highest_salary = sorted_salary.iloc[1]
        return pd.DataFrame({f'SecondHighestSalary': [second_highest_salary]})


print(nth_highest_salary(employee))