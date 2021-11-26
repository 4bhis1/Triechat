def encrypt(name):
    name=name.lower()
    l=int(len(name)/2)
    
    # name=name.replace('a','#')
    # name=name.replace('e','*')
    name=name.replace('i','_')
    name=name.replace('o','0')
    name=name.replace('u','%')
    name=name.replace('z','7')
    name=name.replace('s','5')
    name=name.replace('b','6')
    name=name.replace('p','9')
    name=name.replace('h','4')
    
    
    first=name[0:l][::-1]
    secnd=name[l:][::-1]
    
    name1=first+secnd
    return name1


def decrypt(name):
    #     name=name.lower()
    
    # name=name.replace('#','a')
    # name=name.replace('*','e')
    name=name.replace('_','i')
    name=name.replace('0','o')
    name=name.replace('%','u')
    name=name.replace('7','z')
    name=name.replace('5','s')
    name=name.replace('6','b')
    name=name.replace('9','p')
    name=name.replace('4','h')
    
    
    l=int(len(name)/2)
    first=name[0:l][::-1]
    secnd=name[l:][::-1]
    
    name1=first+secnd
    return name1