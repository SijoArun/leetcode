import pandas as pd
import re

data = [[1, 'Winston', 'Freida(A1oA2N7tK@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email_pattern = r'\b[+A-Za-z0-9_.-]+@leetcode.com\b'
    drop_pattern= r'\b[0-9.!%&&*()]\b'
    users=users[~(users['mail'].str[0].isin(['.','-']))]
    users = users[~(users['mail'].str[0:50].isin(['(']))]
    print(users)
    users['mail']=users['mail'].map(lambda row: re.findall(email_pattern,str(row)))
    print(users)
    users['mail']=users['mail'].map(lambda row: str(row).replace('[','')).map(lambda row: str(row).replace(']',''))
    users['mail'] = users['mail'].map(lambda row: str(row).replace('\'', ''))
    users = users[users['mail'] != '']
    users = users[(users['mail'].map(lambda row: False if re.match(drop_pattern, str(row)[0]) else True))]
    return users

print(valid_emails(users))