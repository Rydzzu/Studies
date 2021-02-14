address="192.168.0.0"
maska=25
if_possible=True
how_much=input("Ile chcesz zaadresować komputerów(1-254)?:")
if int(how_much)<3:
    maska=30
elif int(how_much)<7:
    maska=29
elif int(how_much)<15:
    maska=28
elif int(how_much)<31:
    maska=27
elif int(how_much)<63:
    maska=26
elif int(how_much)<127:
    maska=25
elif int(how_much)<255:
    maska=24
else:
    if_possible=False
    print("Nie da sie zaadresować takiej ilości komputerów")
if if_possible:
    octets=maska//8
    bits=maska%8
    bits_b=(8-bits)*"1"
    octets_addres=address.split(".")
    is_correct=True
    add_tab=[]
    for j in range(256//(int(bits_b,2)+1)):
        first=j*(int(bits_b,2)+1)
        add_tab.append(str(first))
    if octets_addres[3] in add_tab:
        is_correct=True
    else:
        is_correct=False

    if is_correct:
        for i in range(256//(int(bits_b,2)+1)):
            first=i*(int(bits_b,2)+1)
            second=first+(int(bits_b,2)+1) -1
            first_add=octets_addres[0]+"."+octets_addres[1]+"."+octets_addres[2]+"."+str(first)
            last_add=octets_addres[0]+"."+octets_addres[1]+"."+octets_addres[2]+"."+str(second)
            print(f"Adresy podsieci to {first_add}-{last_add} adres podsieci: {first_add}, adres rozgloszeniowy: {last_add}")
        computer=str(int(bits_b,2)-1)
        maska=octets*"255."
        bits_to_mask=bits*"1"+(8-bits)*"0"
        print(f"Maska to {maska}{int(bits_to_mask,2)}")
        print(f"W takich podsieciach można adresować po {computer} komputerów")
    else:
        print(f"Adres {address} nie jest prawidłowym adresem sieci dla tej maski")