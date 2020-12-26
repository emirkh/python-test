column=input("est ce que l animal a une colone vertébrale \n")
if column=="oui":
    skin=input("est ce que sa peau porte des poils\n")
    if skin=="oui":
        print("c'est un mammi("")ere\n")
    else:
        skin=input("est ce que sa peau porte des plumes\n")
        if skin=="oui":
            print("est un oiseau")
        else :
            skin=input("est ce que sa peau porte des écac'les soudées\n")
            if skin=="oui":
                print("c'est un sauropsides\n")
            else:
                skin=input("est ce que sa peau est nue\n")
                if skin=="oui":
                    print("c'est un amphibien\n")
                else:
                    skin=input("est ce que sa peau a des ecaille non soudé\n")
                    if skin=="oui":
                        print("c'est un poisson\n") 
else:
    member=input("est ce que il posede des membre articulés\n")  
    if member=="oui":
        pairStr=input("combien de de paires de pattes il a\n")
        pair=int(pairStr)
        if pair==3:
            print("c'est un insecte")
        elif pair==4:
            print("c'est un arachnide")
        elif 5<= pair<=7:
            print("c'est un crustacé")
        elif 12<=pair:
            print("c'est un myriapode")
    else:
        body=input("est ce que son corps est recouvert d'une coquille\n")
        if body=="oui":
            print("c'est un molusque")
        else:
            body=input("est ce que son corpsest re couver de piquant\n")
            if body=="oui":
                print("c'est un echinoderme")
            else:
                body=input("est ce que son corps est nu\n")
                if body=="oui":
                    print("c'est un ver")  
                else:
                    print("ce n'est pas un animal")  
                   

              


                                


        

