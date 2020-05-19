from subprocess import call
import sys
import os
import ddos as dd
import skanowanie as sk
import spoofing as sp
# from PythonScripts import ddos as dd
# from PythonScripts import skanowanie as sk
# from PythonScripts import spoofing as sp
# from PythonScripts import fuzzing as fuz
import fuzzing as fuz
#choice=int(sys.argv[1]) # wywołanie <nazwa skryptu> numer opcji
# number_of_arguments=len(sys.argv) # 1 element to nazwa skryptu
# # .. tutaj będą wczytywane różne opcje pakietu
# arguments=[]
# for i in range(1,number_of_arguments): # wczytywanie argumentów
#      arguments.append(sys.argv[i])
# każdy indeks argumentów będzie miał jakąś funkcję( np. 1 argument to będzie wybór scenariusza, nastepny to np protokoły, następny ttl itd..
targetIP='192.168.1.144'
gatewayIP='192.168.1.1'

# fuz.main_function(targetIP,1000)
#dd.main_function(targetIP,80)
r=[78,81]
print(sk.main_function(targetIP,r))
#print(sp.main_function(targetIP,gatewayIP))
#out = dd.main_function(targetIP, 21)
def choose(choice, targetIP, gatewayIP, port, portRange):

    if choice == "1":
        out = sk.main_function(targetIP, portRange)
    elif choice == "2":
        out = dd.main_function(targetIP, port)
    elif choice == "3":
        out = sp.main_function(targetIP, gatewayIP)
    elif choice == "4":
        out=fuz.main_function(targetIP,10)
    else:
        out = "Zły wybór"

    return out
