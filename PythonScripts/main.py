from subprocess import call
import sys
import os

choice=int(sys.argv[1]) # wywołanie <nazwa skryptu> numer opcji
number_of_arguments=len(sys.argv)-2 # 1 element to nazwa skryptu
# .. tutaj będą wczytywane różne opcje pakietu
arguments=[]
# for i in range(1,number_of_arguments): # wczytywanie argumentów
#     arguments.append(sys.argv[i])
# każdy indeks argumentów będzie miał jakąś funkcję( np. 1 argument to będzie wybór scenariusza, nastepny to np protokoły, następny ttl itd..

if choice==1:
    call(["python", "skanowanie.py"])
elif choice == 2:
    call(["python","ddos.py"])
elif choice ==3:
    call(["python","spoofing.py"])
elif choice == 4:
    pass # tutaj bedzie 4 skrpy
else:
    print("Zly wybor")

