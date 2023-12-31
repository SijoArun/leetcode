import pandas as pd

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if scores.empty:
        return pd.DataFrame(columns=['score', 'rank'])
    scores=scores.sort_values('score',ascending=False)
    df = pd.DataFrame(scores)
    df['rank'] = df['score'].rank(ascending=False,method='dense').astype(int)
    df=df.filter(items=['score','rank'])
    return df

print(order_scores(scores))
