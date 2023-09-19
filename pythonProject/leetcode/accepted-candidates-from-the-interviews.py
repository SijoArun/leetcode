import pandas as pd

data = [[11, 'Atticus', 1, 101], [9, 'Ruben', 6, 104], [6, 'Aliza', 10, 109], [8, 'Alfredo', 0, 107]]
candidates = pd.DataFrame(data, columns=['candidate_id', 'name', 'years_of_exp', 'interview_id']).astype({'candidate_id':'Int64', 'name':'object', 'years_of_exp':'Int64', 'interview_id':'Int64'})
data = [[109, 3, 4], [101, 2, 8], [109, 4, 1], [107, 1, 3], [104, 3, 6], [109, 1, 4], [104, 4, 7], [104, 1, 2], [109, 2, 1], [104, 2, 7], [107, 2, 3], [101, 1, 8]]
rounds = pd.DataFrame(data, columns=['interview_id', 'round_id', 'score']).astype({'interview_id':'Int64', 'round_id':'Int64', 'score':'Int64'}
def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    print(candidates)
    print(rounds)

accepted_candidates(candidates,rounds)