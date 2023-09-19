import pandas as pd


data = [['draft1.txt', 'The stock exchange predicts a bull market which would make many investors happy.'], ['draft2.txt', 'The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.'], ['final.txt', 'The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.']]
files = pd.DataFrame(data, columns=['file_name', 'content']).astype({'file_name':'object', 'content':'object'})
def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bear=files['content'].str.count(r'\bbear\b').sum()
    bull=files['content'].str.count(r'\bbull\b').sum()
    data=[['bear',bear],['bull',bull]]
    return pd.DataFrame(data,columns=['word','count']).astype({'word':'object', 'count':'object'})

print(count_occurrences(files))