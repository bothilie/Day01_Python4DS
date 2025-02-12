import numpy as np

def ft_invert(arr: []) -> []:
    return arr

def ft_red(arr: []) -> []:
    ft_red.__doc__= "filter the image in red"
    M1=arr
    n=len(M1)
    p=len(M1[0])
    for i in range(n):
        for j in range(p):
            #print(M1[i][j])
            M1[i][j]= M1[i][j]*[0.8, 0, 0]
    M1 = np.array(M1)
    return M1

if __name__ == "__main__":
    main()