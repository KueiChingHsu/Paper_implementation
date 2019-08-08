import os
import hashlib
import module.functions
from module.parameter.biometric_parameter import *

'''                      
USER REGISTRATION PHASE (STEP 1)

Select N_i , ID_Ui , PW_i , B_i
Compute W_i = h(ID_Ui||PW_i||N_i)
U_i sends the message {ID_Ui,W_i,B_i} to RC via a secure channel.
'''

# N_i = int.from_bytes(os.urandom(32), byteorder="big") #random number
N_i = 103504206770729901746293463820310101514315542340171696605791945893185967585009
ID_Ui = 74372442465237888562585428825218926942370577176913359607894113446211346756504
PW_i = 1234567890

W_i = module.functions.encrypt_string(str(ID_Ui)+str(PW_i)+str(N_i))
# W_i = 77867863593594565774418103378694790184774001763612048520207063084519711784813

f = open("reg/module/parameter/reg_user_parameter.py", "w")
f.write("ID_Ui ="+str(ID_Ui) + "\n")
f.write("W_i = "+str(W_i)+"\n")
f.write("B_i = " + "'" + str(B_i)+"'" + "\n")
#f = open("auth/password_update.py", "w")
#f.write("W_i = "+str(W_i)+"\n")
    
#print("ID_Ui =",ID_Ui)
#print("W_i = ",W_i)
print("PW_i = ",PW_i)
print("B_i = ",B_i)
