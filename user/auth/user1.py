import hashlib
import os
import pickle

import time
import module.ECC
import module.functions
from fuzzy_extractor import FuzzyExtractor
from user_parameter import *
from password_update_RC import *

'''
LOGIN PHASE AND AUTHENTICATION PHASE (STEP 1)
In this phase, when a registered user U_i wants to access to services from S_j, 
he inserts his smart card SC_i into a terminal device 
and input his identity ID_Ui',password PW_i' and biometric B_i'. 
Then SC_i performs the following steps:
SC_i checks if W_i W=h(ID_Ui^' ||PW_i^' ||N_i) holds. 
If it does not hold, SC_i terminates the process; 
otherwise, SC_i computes  fuzzy extractor R_i'=Rep(B_i',P_i ) 
and picks a public reproduction parameter P_i.  
SC_i  computes H_i=I_i⊕W_i⊕R_i,
C_i=dP(ECDH public key), 
C_i*=dP_pub=((C_i* )_x,(C_i* )_y )∈E_P(ECDH shared secret key value, where  P_pub=sP), 
user anonymity NID_i=h((C_i* )_x ||1)⊕ID_Ui 
and biometric information  anonymity NB_i=h((C_i* )_x ||2)⊕B_i'.
U_i sends the message {NID_i,C_i,NB_i,P_i} to S_j via an insecure channel.
'''

PW_i = 1234567890
print('PW_i = ',PW_i)
print('B_i =',B_i)
print("login phase ...")
ID_Uii = ID_Ui
PW_ii = PW_i
W_ii = module.functions.encrypt_string(str(ID_Uii)+str(PW_ii)+str(N_i))

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
 

with open('auth/extractor.pickle', 'rb') as f:
    extractor_user = pickle.load(f)
with open('auth/helper.pickle', 'rb') as f:
    helper_user = pickle.load(f)

R_i_byte = extractor_user.reproduce(B_i, helper_user)
R_i = int.from_bytes(R_i_byte, byteorder='big')
print ("R_i : ",hex(R_i))

H_i = I_i ^ W_ii ^ R_i
#print("H_i : ",H_i)
#print("I_i : ",I_i)

C_i_pub = userPublicKey
C_i_share = module.ECC.scalar_mult(userSecretKey, rcPublicKey)
#print("C_i_share : ",C_i_share[0])
# random1 = int.from_bytes(os.urandom(32), byteorder="big") #random number
#print("random1 : ",random1)
random1 = 5007788644736981932531528517127578712502545913257300873308777699879150468499
# random2 = int.from_bytes(os.urandom(32), byteorder="big") #random number
#print("random2 : ",random2)
random2 = 24831301395142545992326481884931277697072200052066173939556833115116220163654
#B_i_ = int.from_bytes(b'f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"xI', byteorder='big')
#noisy_biometric='f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"xI'

B_i_ = int.from_bytes(bytes(B_i, 'utf-8'), byteorder='big')
#print("Biometrc user imput (int) : ",B_i_)
NID_i = module.functions.encrypt_string(str(C_i_share[0])+str(random1)) ^ ID_Ui
#print("NID_i : ",NID_i)
NB_i = module.functions.encrypt_string(str(C_i_share[0])+str(random2)) ^ B_i_
#print("NB_i : ",NB_i)

f = open("./auth/user1_parameter.py", "w")
f.write("NID_i ="+str(NID_i) + "\n")
f.write("C_i_pub ="+str(C_i_pub) + "\n")
f.write("NB_i ="+str(NB_i) + "\n")

f = open("./auth/user1_parameter_self.py", "w")
f.write("NID_i ="+str(NID_i) + "\n")
f.write("C_i_pub ="+str(C_i_pub) + "\n")
f.write("C_i_share ="+str(C_i_share) + "\n")
f.write("NB_i ="+str(NB_i) + "\n")
f.write("H_i ="+str(H_i) + "\n")
'''
login phase ...
YES, W_ii = Wi : 77867863593594565774418103378694790184774001763612048520207063084519711784813
login verifies : ok 
R_i :  5477252666279777205944259937506748438677686670498821103431486625141337284313
H_i :  89340019238769221374091918354231078801768000530046002087000695688493345767293
I_i :  46021158285148116846527490676213512086313685844417887791720342046889358827209
C_i_share :  69285565998812565712857647080714626004324804515167533506024841044946667166244
Biometrc user imput (int) :  46213386383469074264372642516125468765049240515817850823816272673921625651273
NID_i :  103105860784411137979052453000834924803834664734762204184628726740193178176275
NB_i :  103017628012458516620268304286932052936156576771239814003647129079025714258452
'''
