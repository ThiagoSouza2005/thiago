from conversor import*

tenis_pe=int(input("Digite tamanho do seu calcado: "))
europa=europeu(tenis_pe)
print("o seu calcado " +str(tenis_pe)+ " corresponde " +str(europa)+ " no tamanho europeu\n")

file = open('resultados da conversão.txt', 'a')
file.write("o seu calcado " +str(tenis_pe)+ " corresponde " +str(europa)+ " no tamanho europeu\n")
file.close()