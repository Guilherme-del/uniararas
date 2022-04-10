print ("="*32)
print ("        DESCRUBA SE VOCE IRA PASSAR DE ANO NA FHO")
print ("="*32)



A1=float(input("Qual a nota da sua A1? "))
A2=float(input("Qual a nota da sua A2? "))
Media=(A1+2*A2)/3
if(Media>=5):
    print("Voce passou de ano")
else:
    if(Media<5):
        print("Não passou")
    else:
        print("None")