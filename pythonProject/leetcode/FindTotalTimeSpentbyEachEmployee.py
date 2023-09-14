import pandas as pd

data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees=employees.rename(columns={'event_day':'day'}).reset_index()
    employees['total_time'] = employees['out_time'] - employees['in_time']
    groupbydata = employees.groupby(['day', 'emp_id'])['total_time'].sum().reset_index()
    return groupbydata

print(total_time(employees))
