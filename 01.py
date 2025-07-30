from xml.dom.minidom import Element


def unique(lst):
    unique=[]
    for item in lst:
        if lst.count(item)==1:
            unique.append(item)
    return unique
def create_lst(n):
    lst=[]
    for i in range(n):
        Element=input(f"Enter{i+1}:")
        try:
            Element=int(Element)
        except ValueError:
            pass
        lst.append(Element)
    return lst
n=int(input("Enter number of element to the list:"))
my_list=create_lst(n)
unique=unique(my_list)
print("unique element in the list:",unique)


