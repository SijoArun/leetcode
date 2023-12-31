import pandas as pd


data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity=activity.sort_values('event_date',ascending=True).reset_index()
    activity = activity.drop_duplicates('player_id').sort_values('player_id',ascending=True).reset_index()
    activity=activity.rename(columns={'event_date':'first_login'}).filter(items={'player_id','first_login'})
    return activity

game_analysis(activity)
