
import hashlib
import module.functions 
from module.parameter.reg_user_parameter import *
from fuzzy_extractor import FuzzyExtractor
import pickle
from module.parameter.new_password import *
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.user_biometric_key_data import R_i
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
print(B_i)
key, helper = extractor.generate('f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"x6')

R_i = int.from_bytes(key, byteorder='big')
print("R_i : ",R_i)
R_i :  5477252666279777205944259937506748438677686670498821103431486625141337284313


with open('reg/user/helper.pickle', 'wb') as f:
    pickle.dump(helper, f)
with open('reg/user/extractor.pickle', 'wb') as f:
    pickle.dump(extractor, f)

'''
'''
with open('reg/user/helper.pickle', 'rb') as f:
    helper = pickle.load(f)
with open('reg/user/extractor.pickle', 'rb') as f:
    extractor = pickle.load(f)

R_i =  5477252666279777205944259937506748438677686670498821103431486625141337284313

r_key = extractor.reproduce('f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"xI', helper)
'''
#R_i =  85121441368677895659409983127243673931343870524226690515439041004684878351940
#print ("r_key : ",int.from_bytes(r_key, byteorder='big'))
H_i= module.functions.encrypt_string(str(ID_Ui)+str(s))
#print("H_i : ",H_i)
#H_i :  47758271670838609718814890980207843031779882961895519289075024088788143748735
I_i= W_i_new ^ R_i ^ H_i
print("W_i_new = ", hex(W_i_new))

print("I_i_new = ", hex(I_i))
print("    R_i = ", hex(R_i))
#I_i :  91221627644951107714942069145346708250565789035861815100671757907404856842187
#print("ID_Ui registration success !")

f = open("reg/user/password_update_RC.py", "w")
f.write("W_i = "+str(W_i_new)+"\n")
f.write("I_i = "+str(I_i)+"\n")


