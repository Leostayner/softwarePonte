def metodos (ite, tol, K, F, n):
    U = []
    U2 = []

    for v in range(n):
        U.append(1)
        U2.append(1)

    max_erro = 1.0
    
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
                U2[i]+=contador

        
        for a in range(n):
            if U[a] == 0:
                erro = 0
            else:
                erro = abs(float((U2[a]-U[a])/U2[a]))
            if erro < max_erro:
                max_erro = erro

        U=U2[:]

        if ((max_erro < tol) and (max_erro > 0)):
            return U2, max_erro
   
    return U2, max_erro
     

K = [[192600.0, 38400.0], 
     [38400.0, 28800.0]]  

F=[1500,-1000]

ite = 30
tol =  0.00001
n = 2