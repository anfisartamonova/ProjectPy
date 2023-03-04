documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


print((directories.keys()))
def p(number):
    ans = " "
    for i in range(len(documents)):
        num = list(documents[i].values())
        if l[1] == number:
            ans = num[2]
    
    if ans == " ":
        return "Документ не найден в базе"
    else:
        return ans


def s(number):
    per = ""
    ans = "Документ не найден в базе"
    for i in range(len(documents)):
        num = list(documents[i].values())
        if num[1] == number:
            per = num[1]
    if per != "":
        for i in range(len(directories)):
            if per in str(list(list(directories.items())[i])[1]):
                ans = list(list(directories.items())[i])[0]

    return ans
       
def slesh():
    
    for i in range(len(documents)):
        print("№: " , list(documents[i].values())[1], ", тип:", list(documents[i].values())[0], ", владелец: ", list(documents[i].values())[2] , ", полка хранения: ", s(list(documents[i].values())[1]))
    
    


def ads(num):
    ans = "Такая полка уже существует. "
    for i in range(len(directories)):
        if(num in list(directories.keys())):
            ans = "Такая полка уже существует. Текущий перечень полок: "
    else:
        key, value = "num", ""
        directories[key] = value
        ans = "Полка добавлена. Текущий перечень полок: " 
    s = ""
    for i in range(len(directories)):
        s += (list(directories[i])
        s += "; " 
    return ans, s    
        
        
        
    
    
    
    
num = 10    
print(ads(num))    
    



#s = input()
#while s != 'q':
 #   s = input()
    

