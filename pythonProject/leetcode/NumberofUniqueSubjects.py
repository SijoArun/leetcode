import pandas as pd

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher =teacher.groupby(['teacher_id'])['subject_id'].apply(lambda group: group.drop_duplicates()).reset_index()
    teacher = teacher.groupby(['teacher_id'])['subject_id'].count().reset_index()
    teacher = teacher.rename(columns={'subject_id': 'cnt'}).filter(items={'teacher_id', 'cnt'})
    return teacher

count_unique_subjects(teacher)