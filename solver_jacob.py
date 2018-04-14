def metodos (ite, tol, K, F, n):
    U = [1,1,1,1,1,1]
    U2 = [0,0,0,0,0,0]
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
                U2[i]+=contador


        for i in range(n):
            if U[i] == 0:
                erro = 0
            else:
                erro = abs(float((U2[i]-U[i])/U[i]))
                print("U2", U2[i])
                print("U", U[i])
            if erro < max_erro:
                max_erro = erro

            

        if ((max_erro < tol) and (max_erro != 0)):
            
            return U2
        U = U2
   
    return U2
     
        
        
K=[[192600, 38400, -141400, 0, -51200, -38400],
   [38400, 28800, 0, 0, -38400, -28800],
   [-141400, 0, 141400, 0, 0, 0],
   [0, 0, 0, 188533, 0, -188533],
   [-15200, -38400, 0, 0, 51200, 38400],
   [-38400, -28800, 0, -188533, 38400, 217333]]

F=[1500,-1000,0, 0, 0, 0]

ite = 500
tol =  0.0001
n = 6

print(metodos(ite, tol, K, F, n))