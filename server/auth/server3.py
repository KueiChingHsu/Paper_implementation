import module.functions
import pickle
import time
from RC1_server_parameter3_2 import *
from RC2_server_parameter5 import *
from server1_parameter_self import *
from server_parameter import *
from user1_parameter import *
from user2_server_parameter3_1 import *
from fuzzy_extractor import FuzzyExtractor
import module.ECC

'''
Upon receiving the message {N_r,D_r,O_r,L_r,PID_i}, 
S_j computes ID_Ui=PID_i⊕h((G_jr^* )_x ||6), 
an secret key data R_i=h((G_j^* )_x ||4)⊕D_r, 
biometric information B_i^'=h((G_j^* )_x ||5)⊕O_r 
and N_r^'== h(D_r ||O_r ||F_j ||R_i ||G_j^* ||B_i^' ). 
S_j checks if  N_r^'?=N_r holds. 
If it does not hold, S_j terminates the process; 
otherwise, S_j computes fuzzy extractor R_i^'=Rep(B_i^',P_i ).  
S_j checks if an secret key data R_i^' is correct or not. 
If not,  S_j terminates the process; 
otherwise, S_j computes session key sk_su=h(C_i ||G_j ||tC_i ||NID_i ||NID_j) 
and  S_su= h(sk_su ||L_i ||L_r) 
sends the message {G_j,NID_j,S_su} to U_i via an insecure channel.
'''


ID_Ui=module.functions.encrypt_string(str(G_j_share[0])+str(random6))^PID_i
R_i=module.functions.encrypt_string(str(G_j_share[0])+str(random4))^D_r
#print('R_i : ',R_i)
B_i_server=module.functions.encrypt_string(str(G_j_share[0])+str(random5))^O_r
#print("ID_Ui : ",ID_Ui)
#print("R_i : ",R_i)
#print("B_i_server : ",B_i_server)
N_r_=module.functions.encrypt_string(str(D_r)+str(O_r)+str(F_j)
+str(R_i)+str(G_j_share)+str(B_i_server))
if N_r_==N_r :    
    #print("YES, N_r_ = N_r :",N_r_)
    
    print('N_r_ = ',hex(N_r_))
    print('N_r = ',hex(N_r))
    print("Server recieves message : ok")
else:
    print("N_r_ != N_r : NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
    #print("Server recieves message : ok")
    print('N_r_ = ',hex(N_r_))
    print('N_r = ',hex(N_r))
    exit()
start_fuzzy_server = time.time()
with open('./auth/helper.pickle', 'rb') as f:
    helper_server = pickle.load(f)
with open('./auth/extractor.pickle', 'rb') as f:
    extractor_server = pickle.load(f)
B_i_ascii_byte= B_i_server.to_bytes((B_i_server.bit_length()+7) // 8, byteorder='big')
#print("B_i_ascii_byte : ",B_i_ascii_byte)
#   SS=46213386383469074264372642516125468765049240515817850823816272673921625651273
#   SSS= SS.to_bytes((SS.bit_length()+7) // 8, byteorder='big')
#   print('SSS',SSS)
B_i_ascii= B_i_ascii_byte.decode()
print("B_i_ascii : ",B_i_ascii)
R_i_server_byte=extractor_server.reproduce(B_i_ascii, helper_server)
#print("R_i_server_byte : ",R_i_server_byte)
R_i_server=int.from_bytes(R_i_server_byte, byteorder='big')
#print("R_i_server : ",R_i_server)
end_fuzzy_server = time.time()
print ("Server side fuzzy extractor computation cost : ",end_fuzzy_server-start_fuzzy_server," seconds")
'''
R_i_server :  72395800100906082882372659910109285186011116955846183153377521326795930277851
'''
if R_i_server==R_i :    
    #print("YES, R_i_server = R_i :",R_i_server)
    print('R_i_server = ',hex(R_i_server))
    print('R_i = ',hex(R_i))
    print("Biometric verifies : ok")
else:
    #print("R_i_server != R_i : NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
    print("Biometric verifies : fail")
    exit()
tC_i=module.ECC.scalar_mult(serverSecretKey,C_i_pub) 
sk_su=module.functions.encrypt_string(str(C_i_pub)+str(G_j_pub)+str(tC_i)
+str(NID_i)+str(NID_j))
S_su=module.functions.encrypt_string(str(sk_su)+str(L_i)+str(L_r))
#print("tC_i : ",tC_i)
#print("sk_su : ",sk_su)
#print("S_su : ",S_su)
'''
tC_i :  (41596040621878323751681958119212698940610738295038647762295056985634424971232, 112841413483737280705031023042458026677531174067066267988100629748170898630416)
sk_su :  112546697679053448126100528779452395291606141395749302926864101819679527514903
S_su :  42165408054789839321955270518446419180209090048128037517149586987198629465032
'''
f = open("./auth/server3_user_parameter6.py", "w")
f.write("G_j_pub ="+str(G_j_pub) +"\n" )
f.write("NID_j ="+str(NID_j) +"\n" )
f.write("S_su ="+str(S_su) +"\n" )
f.write("ID_Sj ="+str(ID_Sj) +"\n" )

