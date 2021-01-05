import csv

def organizeKeys(Test):  # returns the list of keys with respect to the alphabetical order

    li = list()
    for i in range(len(Test)):  # takes a list as variable
        li.append(" , ".join(Test[i].keys()))
    # print the list containing all the keys of the hole list of dictionaries     e.g : ['a , b , c , d', 'a , z , c , b', 'a , x , b , c']

    A1 = ",".join(li)
    # String and not a list anymore                  e.g : a , b , c , da , z , c , ba , x , b , c

    Bli = ""  # Ommiting the spaces from the string a1         e.g : a,b,c,da,z,c,ba,x,b,c
    for i in range(len(A1)):
        if A1[i] == " ":
            Bli = Bli
        else:
            Bli = Bli + A1[i]
    # print(Bli)

    li = list(Bli.split(","))
    # print(li)

    Cli = []  # Ommiting redundant elements
    for i in range(len(li)):
        if li[i] not in Cli:
            Cli.append(li[i])
        else:
            Cli = Cli
    # print(Cli)

    Lifinal = sorted(Cli)
    return Lifinal


def sizemaxkey(List, key):  # returns for each key in the hole list of dictionaries the size of the biggest value
    maxsize = 0
    for dic in List:
        if key in dic.keys():
            if len(dic[key]) > maxsize:
                maxsize = len(dic[key])
        else:
            maxsize = maxsize

    return maxsize


def arrange(List, key):     # make all values of the same key within the list of dictionaries have the same size of the biggest value corresponding to that key
    maximum = sizemaxkey(List, key)
    for dic in List:
        if key in dic.keys():
            if len(key)<maximum:
                sizetempo = maximum - len(dic[key])
                dic[key] = dic[key] + sizetempo * " "
                dic[key + (maximum-len(key))*" "] = dic[key]
                del dic[key]
            else:
                sizetempo = len(key) - len(dic[key])
                dic[key] = dic[key] + sizetempo * " "


        else:
            if len(key)<maximum:
                dic[key] = maximum * " "
                dic[key + (maximum - len(key)) * " "] = dic[key]
                del dic[key]

            else:
                dic[key] = len(key) * " "

            #dic[key + (maximum - len(key)) * " "] = dic[key]
            #del dic[key]
    return List


def Resizekey (Lkey,List,key):  # The size of all the keys is equal to the size of the largest value of the key of the loop
    maximum = sizemaxkey(List, key)
    L = list()
    for i in range(len(Lkey)):
        if maximum > len(Lkey[i]):
            L.append(Lkey[i] + (maximum - len(Lkey[i])) * " ")
        else:
            L.append(Lkey[i])
    return L


def xtostr(d):       # converting all values to string
    dx = dict()
    for i in d.keys():
        j = str(i)
        dx[j] = str(d[i])
    return dx

def list2csv (L):
    Lis = list()
    for i in range(len(L)):
        Dico = dict()
        Dico = xtostr(L[i])
        Lis.append(Dico)

    ListKey = organizeKeys(Lis)  # returns a list of keys respecting the alphabetical order. Each key has a str format.
    organized_list = list()
    csv_columns = list()
    for i in ListKey:
        organized_list.append(Resizekey(ListKey, Lis, i))  # returns a list of lists. Each sublist contains spaced keys


    for i in range(len(organized_list)):
        csv_columns.append(organized_list[i][i])  # returns one list that will be used as a header to our csv file. The keys have the same size of the values



    for i in ListKey:
        arrange(Lis,i)  # returns the modified version of the first list of dictionaries. The keys and values have now the same size.
                        # This is the final dictionary

    csv_file = "Code.csv"

    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        for donnees in Lis:
            writer.writerow(donnees)

