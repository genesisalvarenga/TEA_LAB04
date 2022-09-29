try:
    #defino programas
    def mostrarmínimo(m):
        print('\nEl numero mínimo es: ',m)

    def mostrarmáximo(M):
        print('\nEl numero máximo es: ',M)
        
    def pedirdato():
        mínimo=None
        máximo=None
        while True:
            n=input('Ingrese un numero: ')
            if n=='fin':
                break
            if máximo is None or n>máximo:
                máximo=n
            if mínimo is None or n<mínimo:
                mínimo=n
        mostrarmáximo(máximo)
        mostrarmínimo(mínimo)
#Comienza Programa
    pedirdato()
#Fin del programa
except:
    print('\nError!! Ingrese un numero o la palabra "fin".\nEl programa ha finalizado')
