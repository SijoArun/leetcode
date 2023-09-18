import pandas as pd

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    two_df = students.merge(subjects, how='cross')
    print(two_df)
    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()
    print(exam_count)

    all_df = two_df.merge(exam_count, on=['student_id', 'subject_name'], how='left').sort_values(
        by=['student_id', 'subject_name'])
    return all_df.fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']]



print(students_and_examinations(students,subjects,examinations))