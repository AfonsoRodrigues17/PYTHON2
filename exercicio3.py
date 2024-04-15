faturamento = int(input ("Faturamento - "))
custo = int (input ( "Custo - "))
lucro = faturamento - custo



print ("O lucro foi de:", lucro )

if lucro >= custo:
    print("O lucro foi Bom")

else:
    print ("o lucro nao foi bom")