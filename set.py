#Roll No :65
#Program for set operations
set1=set();
set2=set();

for i in range(1,7):
    set1.add(i);

for i in range(3,9):
    set2.add(i);

print("Elements of set1 :");
print(set1);

print("Elements of set2 :");
print(set2);

print("SET OPERATIONS");

print("--Length of set1 and set2--");
print("Length of set1 :",len(set1));
print("Length of set2 :",len(set2));

print("--Union of set1 and set2--");# set1 | set2
print(set1.union(set2)); 


print("--Intersection of set1 and set2--");#set1 & set2
print(set1.intersection(set2));


print("--Difference between set1 and set2--");#set1 - set2
print(set1.difference(set2));

print("--Check whether set1 is superset--");
print(set1>=set2);

print("--check whether set1 issubset--");
print(set1<=set2);

print("--check whether set1 and set2 is disjoint--");
print(set1.isdisjoint(set2));

print("Symmetric difference of set 1 and set2");#set1 ^ set2
print(set1.symmetric_difference(set2));



