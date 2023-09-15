import pandas as pd

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses =((courses.groupby(['class']).count())).reset_index()
    return courses[(courses['student']>=5)].filter(items={'class'})


print(find_classes(courses))