import numpy as np

def metodos (ite, tol, K, F, n):
    u_k = []
    u_k1 = []
    for v in range(n):
        u_k.append(1)
        u_k1.append(1)
    
    maximo = 0

#GAUSS-SEIDEL        
    for k in range(ite):
        for j in range(n-2):
            conta1 = F[j]
            conta2 = F[j+1]
            for d in range(n-1):
                conta1-=K[j][j+d]*u_k[j+d]
                conta2-=K[j+1][j+1+d]*u_k1[j+1+d]
                
                
            if j == 0:
                u_k1[j]=(conta1)/K[j][j]
                u_k1[j+1]=(conta2)/K[j+1][j+1]
                # u_k1[j]=(F[j]-K[j][j+1]*u_k[j+1])/K[j][j]
                # u_k1[j+1]=(F[j+1]-K[j+1][j]*u_k1[j])/K[j+1][j+1]
                j+=1
            
            else:
                u_k1[j+1]=(conta2)/K[j+1][j+1]
                j+=1

            print(u_k, u_k1)
        if k==0:
            u_k = u_k1
        else: 
            for i in range(n-2):
                if u_k[i]!=0:
                    erro = (u_k1[i]-u_k[i])/u_k[i]
                    if erro>maximo:
                        maximo = erro
            if maximo !=0 and maximo<tol:
                return u_k1 
            u_k = u_k1     
        k+=1
    return u_k1

x=(10^5)/2
K=[[3*x, -1*x, 0, 0],
   [-x, 3*x, 0, -2*x],
   [0, 0, 3*x, x],
   [0, -2*x, x, 3*x]]

F = [0,0,0,-1000]
ite = 100
tol =  0.0001
n = 4

print(metodos(ite, tol, K, F, n))

