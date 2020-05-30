from subprocess import call
import sys
import os

from PythonScripts import ddos as dd
from PythonScripts import skanowanie as sk
from PythonScripts import spoofing as sp
from PythonScripts import fuzzing as fuz


def choose(choice, targetIP, gatewayIP, port, portRange, numberOfPackets):
    print('Target IP', targetIP , ' port range: ', portRange)
    if choice == "1":
        out = sk.main_function(targetIP, portRange)
    elif choice == "2":
        out = dd.main_function(targetIP, port)
    elif choice == "3":
        out = sp.main_function(targetIP, gatewayIP)
    elif choice == "4":
        out=fuz.main_function(targetIP, numberOfPackets)
    else:
        out = "Zły wybór"

    return out
