s="rererer sijo adfd sfdffre sijo sfdfdf"
sub="sijo"
pos=-1
found= False
length=len(s)
while True:
    pos=s.find(sub,pos+1,length)
    if(pos==-1):
        print("data is not found" )
        break
    print("Pos found at ",pos)
    found = True
if found == False:
    print("String not  found")

