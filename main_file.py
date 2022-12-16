import re
data =[]
data1 =[]
cost_map = dict()
common = []

# Function created to load the files
def load():
    file = open("values.txt","r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        else:
            temp = list(map(str, line.split()))
            cost_map[temp[0]] = int(temp[1])
    file.close()

# Assigning the different scores
def cost(abb, name_list):
    first, last, score = "", "", 0
    for i in name_list:
        if len(i) > 1:
            last += i[-1]
        first += i[0]

    for j in abb[1:]:
        if j in first:
            score += 0
            first = first[first.index(j):]

        elif j in last:
            if j=="E":
                score+=20
            else:
                score += 5
            last = last[last.index(j):]
        else:
            l=[]
            for i in name_list:
                if j in i:
                    l.append(min(i.index(j), 3))
            score+=min(l)+cost_map[j]
    return score

# Creating the abbrevations from the names
def abbrev(name_list):
    name = "".join(name_list)
    n = len(name)
    abb = dict()
    for i in range(1,n):
        for j in range(i+1,n):
            temp = name[0]+name[i]+name[j]
            if temp in common:
                continue
            else:
                abb[temp.upper()] = cost(temp, name_list)

    return abb

if __name__ == "__main__":

    name= input("Enter the file name: ")

    file = open(name,"r")
    load()

    while True:
        line = file.readline()
        if len(line) == 0:
            break
        else:
            data.append(list(map(str, re.split(" |,|-|'", line.upper().strip()))))
            data1.append(list(map(str, re.split(" |,|-|'", line.strip()))))

    mylist  =[]

    for i in data:
            mylist.append(set(abbrev(i).keys()))
# Saving our final result in different file named as Final_Result.txt
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            temp = mylist[i].intersection(mylist[j])
            if len(temp)>0:
                common+=temp
    out = open("Final_Result.txt","w")
# This will store the name with the smallest calculated score abbrevation
    for i in range(len(data)):
        temp = abbrev(data[i])
        out.write(" ".join(data1[i]) + "\n")

        if len(temp)>0:
            m = min(temp.items(),key = lambda x: x[1])[1]
            for j in temp.keys():
                if temp[j]==m:
                    out.write(j+" ")
        out.write("\n")
    out.close()
    file.close()
    print("Success")

# Opening the file Final_Result.txt
data_file = open('Final_Result.txt','r')
data = data_file.read()
result = data.split('\n')

#creating two list
alpha = []
digits = []
i = 0
while i<len(result):
    if i%2 == 0:
        alpha.append(result[i])
    else:
        digits.append(result[i])
    i = i + 1

# # converted the two lists into list of tuples
list_of_tuples = list(zip(alpha, digits))
# # Converted the list of tuples into dictionary
d = dict(list_of_tuples)
print(d)

for k,v in d.items():
    print(k ," : ",v)