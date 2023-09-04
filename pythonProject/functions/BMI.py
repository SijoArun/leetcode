def calcbmi(height,weight):
    heightinmeter=height * 0.4567
    bmi = weight/(heightinmeter * heightinmeter)
    return bmi

print(calcbmi(5.8,70))
