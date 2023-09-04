print("Pick any 3 Sandwich : \n1.onion \n2.lettuce \n3.Tomato \n4.Olivers \n5.pepper \n6.Tomatoes")

lst = [str(x) for x in input("Enter the sandwich selection (by comma separator):").split(",")]

print("Selected sandwich :", lst)

print("{} sandwich selected and Total cost is {}".format((len(lst)), (len(lst)) * 5))
