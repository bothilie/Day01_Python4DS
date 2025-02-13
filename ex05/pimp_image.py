import numpy as np

#cas testé
#-  arr null
#- pas 3 pixels dans chaque array
#- Pas 3 dimensions?



def ft_invert(arr: []) -> []:
    ft_invert.__doc__= "filter the image in the inverse colors"
    try:
        if arr == () or arr[0] == () or arr[1] == () :
            return []
    except:
        M1=arr
        n=len(M1)
        p=len(M1[0])
        for i in range(n):
            for j in range(p):
                #print(M1[i][j])
                M1[i][j]= [255-M1[i][j][0], 255-M1[i][j][1], 255-M1[i][j][2]]
        M1 = np.array(M1)
        return M1 
        return arr

def ft_red(arr: []) -> []:
    ft_red.__doc__= "filter the image in red"
    try:
        if arr == () or arr[0] == () or arr[1] == () :
            return []
    except:
       # AssertionError("AssertionError")
        M1=arr
        n=len(M1)
        p=len(M1[0])
        for i in range(n):
            for j in range(p):
                if len(M1[i][j]) != 3:
                    return[]
                #print(M1[i][j])
                M1[i][j]= M1[i][j]*[0.8, 0, 0]
        M1 = np.array(M1)
        return M1


def ft_green(arr: []) -> []:
    ft_green.__doc__= "filter the image in green"
    try:
        if arr == () or arr[0] == () or arr[1] == () :
            return []
    except:
        M1=arr
        n=len(M1)
        p=len(M1[0])
        for i in range(n):
            for j in range(p):
                M1[i][j]-= np.array([M1[i][j][0], 0, M1[i][j][2]], dtype='uint8')
        M1 = np.array(M1)
        return M1

def ft_blue(arr: []) -> []:
    ft_blue.__doc__= "filter the image in blue"
    try:
        if arr == () or arr[0] == () or arr[1] == () :
            return []
    except:
        M1=arr
        n=len(M1)
        p=len(M1[0])
        for i in range(n):
            for j in range(p):
                M1[i][j][0]= np.array(0)
                M1[i][j][1]= np.array(0)
        M1 = np.array(M1)
        return M1

def ft_grey(arr: []) -> []:
    ft_grey.__doc__= "filter the image in grey"
    try:
        if arr == () or arr[0] == () or arr[1] == () :
            return []
    except:
        M1=arr
        n=len(M1)
        p=len(M1[0])
        M1 = M1[:,:,1]
        #for i in range(n):
        #    for j in range(p):
        #        M1[i][j][0]= np.array(0)
        #        M1[i][j][1]= np.array(0)
        #        M1[i][j][2]= np.array(0)
        M1 = np.array(M1)
        return M1


if __name__ == "__main__":
    main()