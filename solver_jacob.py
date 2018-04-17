def metodos (ite, tol, K, F, n):
    U = []
    U2 = []

    for v in range(n):
        U.append(0)
        U2.append(0)

    max_erro = 1
    
    for k in range(ite):
        for i in range(n):
            if K[i][i] == 0:
                U2[i]=0
            else:
                U2[i] = float(F[i])/float(K[i][i])
                contador = 0  
                for j in range(n):
                    if i == j:
                        pass
                    else:
                        
                        contador -= float(K[i][j]*U[j])/float(K[i][i])
                U2[i]+=contador

        
        for a in range(n):
            if U2[a] == 0:
                erro = 1
            else:
                erro = abs(float((U2[a])-float(U[a]))/float(U2[a]))
                print(erro)
            if (erro < max_erro) and (erro>0):
                max_erro = erro

        U=U2[:]

        if ((max_erro < tol) and (max_erro > 0)):
            return U2, max_erro, k
   
    return U2, max_erro, k
     

K = [[150000, -50000, 0, 0], 
     [-50000, 150000, 0, -100000],
     [0, 0, 150000, 50000],
     [0, -100000, 50000, 150000]]  

F=[0, 0, 0, -100]

ite = 600
tol =  0.000000001
n = 4

print(metodos (ite, tol, K, F, n))