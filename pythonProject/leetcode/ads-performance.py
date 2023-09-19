import pandas as pd

data = [[1, 1, 'Clicked'], [2, 2, 'Clicked'], [3, 3, 'Viewed'], [5, 5, 'Ignored'], [1, 7, 'Ignored'], [2, 7, 'Viewed'], [3, 5, 'Clicked'], [1, 4, 'Viewed'], [2, 11, 'Viewed'], [1, 2, 'Clicked']]
ads = pd.DataFrame(data, columns=['ad_id', 'user_id','action']).astype({'ad_id':'Int64', 'user_id':'Int64', 'action':'object'})

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    unique_df = pd.DataFrame({'ad_id': ads['ad_id'].unique()}).reset_index()
    click_reset_df = ads.groupby(['ad_id']).apply(lambda x: (x['action'] == 'Clicked')).reset_index()
    total_reset_df=ads.groupby(['ad_id']).apply(lambda x:(x['action']=='Clicked') | (x['action']=='Viewed')).reset_index()
    total_reset_df=total_reset_df[total_reset_df['condition_met']==True]
    click_reset_df = click_reset_df[click_reset_df['condition_met'] == True]
    total_result_df=total_reset_df.groupby(['ad_id'])['condition_met'].count().reset_index()
    ctl_result_df = click_reset_df.groupby(['ad_id'])['condition_met'].count().reset_index()
    total_result_df=total_result_df.merge(ctl_result_df,on='ad_id',how='left')
    mergeresult=unique_df.merge(total_result_df,on='ad_id',how='left').fillna(0)
    mergeresult['ctr'] = ((mergeresult['condition_met_y'] / mergeresult['condition_met_x']) * 100).__round__(2).fillna(0)
    return (mergeresult[['ad_id','ctr']].sort_values(by='ctr',ascending=False))


print(ads_performance(ads))