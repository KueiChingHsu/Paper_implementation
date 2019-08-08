import hashlib
import os
import pickle

import module.ECC
import module.functions
from fuzzy_extractor import FuzzyExtractor
from user_parameter import *
from password_update_RC import *

PW_i =  input("old password : ")
print("login phase ...")
ID_Uii = ID_Ui
PW_ii = PW_i
W_ii = module.functions.encrypt_string(str(ID_Uii)+str(PW_ii)+str(N_i))
#print('old password : ',PW_i)
if W_i == W_ii:
    #print("YES, W_ii = Wi :",W_i)
    print('W_i = ',hex(W_i))
    print('W_ii = ',hex(W_ii))
    print("login verifies : ok ")
else:
    print('W_i = ',hex(W_i))
    print('W_ii = ',hex(W_ii))
    print("login fail ...")
    exit()
PW_i_new = input("new password : ")
#start = time.time()
W_i_new = module.functions.encrypt_string(str(ID_Uii)+str(PW_i_new)+str(N_i))
f = open("auth/new_password.py", "w")
f.write("W_i_new ="+str(W_i_new) +"\n" )