def metodos (ite, tol, K, F, n):
    U = [0,0,0,0]
    U2 = [0,0,0,0]
    max_erro = 0
    
    for k in range(ite):
        for i in range(n):
            if K[i][i] == 0:
                U2[i]=0
            else:
                U2[i] = float(F[i]/K[i][i])
                contador = 0  
                for j in range(n):
                    if i == j:
                        pass
                    else:
                        contador -= float(K[i][j]*U[j]/K[i][i])
                U2[i]-=contador

        for i in range(n):
            if U[i] == 0:
                erro = 0
            else:
                erro = float((U2[i]-U[i])/U[i])
            if erro<max_erro:
                max_erro = erro

        if ((max_erro < tol) and (max_erro != tol)):
            return U2
        
        U = U2

    return U2
     
        
        
K=[[150000, -50000, 0, 0],
   [0, 150000, 0, -100000],
   [0, 0, 150000, 50000],
   [0, 0, 50000, 150000]]

F=[0,0,0,-100]

ite = 500
tol =  0.001
n = 4

print(metodos(ite, tol, K, F, n))