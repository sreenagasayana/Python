# sets are define
Python = {"Jane", "Jack", "Chau", "Ram"};
Webdesign = {"Chau", "Ram", "Herbert", "Rose"};

#Common students
print("Students who are attending both the classes :", Python & Webdesign)

#Uncommon students
print("Students who are not common in both the classes :", (Python | Webdesign) - (Python &Webdesign))
