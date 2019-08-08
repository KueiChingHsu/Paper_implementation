import os
import time
import hashlib
import module.functions 
from module.parameter.reg_user_parameter import *
from fuzzy_extractor import FuzzyExtractor
import pickle
import binascii
'''
USER REGISTRATION PHASE (STEP 2)
Upon receiving the message {ID_Ui,W_i,B_i}, 
RC computes fuzzy extractor Gen(B_i)=(R_i,P_i), 
H_i=h(ID_Ui ||s) and I_i=W_i⊕R_i⊕H_i, 
RC stores the master secret key s. 
RC sends the parameters {h(.),Rep,P_i,P_i,P,P_pub,W_i,I_i} 
to U_i via a secure channel.

'''
rcSecretKey = 57821339089684328170078643393297452417348490406290096822816616169117693678235
s=rcSecretKey
rcPublicKey = (16321396343898609237058457459634586976814428690654624591817221787745052778620, 110853329480792751580624951942149634954474272806761480481621057182840458402147)
'''
extractor = FuzzyExtractor(32, 8)
key, helper = extractor.generate(B_i)


print(extractor)
print(key)
print(B_i)
R_i:''

print("R_i : ",'0x'+key.hex())
print(type(key.hex()))
R_i_string='0x'+key.hex()

R_i_test=hex(int(R_i, 16))
print(R_i_test)
print(type(R_i_test))


with open('reg/user/helper.pickle', 'wb') as f:
    pickle.dump(helper, f)
with open('reg/user/extractor.pickle', 'wb') as f:
    pickle.dump(extractor, f)
'''


with open('reg/user/helper.pickle', 'rb') as f:
    helper = pickle.load(f)
with open('reg/user/extractor.pickle', 'rb') as f:
    extractor = pickle.load(f)
'''
R_i_string='0x'+key.hex()

R_i_test=hex(int(R_i_string, 16))
print(R_i_test)
'''
R_i_bytes = extractor.reproduce(B_i, helper)
#print ("r_key : ",int.from_bytes(r_key, byteorder='big'))
H_i= module.functions.encrypt_string(str(ID_Ui)+str(s))

#print("H_i : ",H_i)
#H_i :  47758271670838609718814890980207843031779882961895519289075024088788143748735
R_i=int(R_i_bytes.hex(),16)
#print(R_i)
I_i= W_i ^ R_i ^ H_i
#print(extractor)
print("W_i = ", hex(W_i))
print("I_i = ", hex(I_i))

print("R_i = ", hex(R_i))
#print("R_i = ", R_i)
'''
print("W_i = ", W_i)
print("I_i = ", I_i)
'''
#print("ID_Ui registration success !")

f = open("reg/user/password_update_RC.py", "w")
f.write("W_i = "+str(W_i)+"\n")
f.write("I_i = "+str(I_i)+"\n")
f = open("auth/user_biometric_key_data.py", "w")
f.write("R_i = "+str(R_i)+"\n")

'''
R_i =  85121441368677895659409983127243673931343870524226690515439041004684878351940
W_i =  0xac27a621d28f6cb6e9b26e6748441d5a608a12a51aee47070046b4f9731b3f6d
I_i =  0x7980982559565d5e42a772b842364b457d7eb261cef9dfacfdc442fd8dfe8756
R_i =  0xbc31074acd006bbb46e807baaeb36692f1f3712535f854e1726c7455d6a90e44
W_i =  77867863593594565774418103378694790184774001763612048520207063084519711784813
I_i =  54957061175237927381032276342263271019728876765729280635829942461610030171990
'''