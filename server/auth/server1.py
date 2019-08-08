from user1_parameter import *
from server_parameter import*
import module.ECC
import module.functions
import os
'''
Upon receiving the message {NID_i,C_i,NB_i,P_i},
S_j computes ECDH public key G_j=tP, 
ECDH shared secret key G_j^*=tP_pub=((G_j^* )_x,(G_j^* )_y)∈E_P,
server anonymity NID_j=h((G_j^* )_x ||3)⊕ID_Sj and
M_j== h(NID_i ||NID_j ||C_i ||G_j ||G_j^* ||NB_i ||F_j). 
S_j sends the message {M_j} to U_i and 
sends the message {NID_i,NID_j,C_i,G_j,NB_i,P_i} to  RC via an insecure channel.
'''
print("authentication start ...")
G_j_pub = serverPublicKey
G_j_share =module.ECC.scalar_mult(serverSecretKey,rcPublicKey) 
#print('G_j_share : ',G_j_share)
#random3 = int.from_bytes(os.urandom(32), byteorder="big") #random number
#print("random3 : ",random3)
random3 = 33990035699478331966720052233532364826397441537667423093933549186520996932429
NID_j=module.functions.encrypt_string(str(G_j_share[0])+str(random3))^ID_Sj
#print("NID_j : ",str(NID_j))
M_j=module.functions.encrypt_string(str(NID_i)+str(NID_j)+str(C_i_pub)
+str(G_j_pub)+str(G_j_share)+str(NB_i)+str(F_j))
#print("M_j : ",M_j )
f = open("auth/server1_user_parameter2_1.py", "w")
f.write("M_j ="+str(M_j) +"\n" )
f = open("auth/server1_rc_parameter2_2.py", "w")
f.write("NID_i = "+str(NID_i) +"\n" )
f.write("NID_j = "+str(NID_j) +"\n" )
f.write("C_i_pub = "+str(C_i_pub) +"\n" )
f.write("G_j_pub = "+str(G_j_pub) +"\n" )
f.write("NB_i = "+str(NB_i) +"\n" )
f = open("auth/server1_parameter_self.py", "w")
f.write("NID_j = "+str(NID_j) +"\n" )
f.write("M_j ="+str(M_j) +"\n" )
f.write("G_j_pub = "+str(G_j_pub) +"\n" )
f.write("G_j_share = "+str(G_j_share) +"\n" )
'''
NID_j :  13560404515982220131953035038843833528227123159732075177537618811226931716612
M_j :  29395113788332622564987093383221262489288967968992449815512541995298760322944
'''



