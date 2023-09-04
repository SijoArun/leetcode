import pickle,student

f=open("student.dat","wb")
s=student.student("122","john","100")
pickle.dump(s,f)
f.close()
