def grades(mark:int)->str:
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"
def display(name:str,mark:int) ->None:
    grade=grades(mark)
    print(f"name:{name}")
    print(f"grade:{grade}")
name:str=input("enter name:")
mark:int=int(input("enter mark:"))

display(name,mark)