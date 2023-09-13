import pandas as pd

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patient1 = patients[(patients['conditions'].map(lambda row: str(row).__contains__('DIAB1')))]
    patient2 = patient1[~(patients['conditions'].map(lambda row: str(row).__contains__('SADI')))]

    return patient2


print(find_patients(patients))