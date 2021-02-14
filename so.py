import sys
import random
print ("Wywolany skrypt:", sys.argv[0])
print ("Liczba argumentow:", len(sys.argv))
print ("Przekazane argumenty:", sys.argv[1:])
int_arr=[]
if len(sys.argv)!=3:
    print("Wywołano za mało argumentów, lub za dużo argumentów")
    exit()
for i in sys.argv[1:]:
    try:
        int_arr.append(int(i))
    except:
        print(f"Dana wartosc {i} nie jest liczba")
        exit()


while True:
    first = random.randint(1, int_arr[0])
    second = random.randint(1, int_arr[1])
    answer=input(f"Podaj wynik mnozenia {first}*{second}:")
    if int(answer)==(first*second):
        print("Dobra odpowiedz")
    else:
        print(first*second)
        print("Niestety to zla odpowiedz")

