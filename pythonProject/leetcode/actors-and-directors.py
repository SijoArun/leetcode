import pandas as pd

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director=actor_director.groupby(['actor_id','director_id' ])['timestamp'].apply(lambda group: (group.count()>=3)).reset_index()
    actor_director=actor_director[(actor_director['timestamp']== True)].reset_index()
    return actor_director[['actor_id','director_id']]

print(actors_and_directors(actor_director))