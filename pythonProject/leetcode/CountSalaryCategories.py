import pandas as pd

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowsalary = accounts[accounts['income']<20000]['income'].count()
    avgsalary = accounts[(accounts['income'] <= 50000) & (accounts['income']>=20000)]['income'].count()
    Highsalary = accounts[accounts['income'] > 50000]['income'].count()
    data = [['Low Salary', lowsalary], ['Average Salary ', avgsalary], ['High Salary', Highsalary]]
    output=pd.DataFrame(data, columns=['category', 'accounts_count'])
    return output.sort_values('accounts_count',ascending=False)


print(count_salary_categories(accounts))