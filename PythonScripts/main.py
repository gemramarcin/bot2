from subprocess import call
import sys
import os
#import ddos as dd
#import skanowanie as sk
#import spoofing as sp
from PythonScripts import ddos as dd
from PythonScripts import skanowanie as sk
from PythonScripts import spoofing as sp


#choice=int(sys.argv[1]) # wywołanie <nazwa skryptu> numer opcji
#number_of_arguments=len(sys.argv)-2 # 1 element to nazwa skryptu
# .. tutaj będą wczytywane różne opcje pakietu
#arguments=[]
# for i in range(1,number_of_arguments): # wczytywanie argumentów
#     arguments.append(sys.argv[i])
# każdy indeks argumentów będzie miał jakąś funkcję( np. 1 argument to będzie wybór scenariusza, nastepny to np protokoły, następny ttl itd..


def choose(choice, targetIP, gatewayIP = "0.0.0.0"):


    if choice == "1":
        out = sk.main_function(targetIP) # print() jeżeli chcesz rezultat funkcji
    elif choice == "2":
        out = dd.main_function(targetIP)
    elif choice == "3":
        out = sp.main_function(targetIP, gatewayIP)
    elif choice == "4":
        pass # tutaj bedzie 4 skrpy
    else:
        out = "Zły wybór"
    
    return out

