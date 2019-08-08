from server1_user_parameter2_1 import *
from user1_parameter_self import *
from user_parameter import *
from user2_parameter_self import *
from server3_user_parameter6 import *
import pickle
import module.functions
import module.ECC
from password_update_RC import *
'''
Upon receiving the message {G_j,NID_j,S_su}. 
U_i  computes session key sk_us=h(C_i ||G_j ||dG_j ||NID_i ||NID_j), 
L_r^'== h(ID_Sj ||ID_Ui ||C_i ||C_i^* ||G_j ||H_i ||M_j) and 
S_us== h(sk_us ||L_i ||L_r^'), 
and then checks if S_us  ?=S_su . 
If it does not hold,  U_i terminates the process; 
otherwise, U_i is authenticated by S_j and shares a session key sk_us with S_j.
'''

dG_j=module.ECC.scalar_mult(userSecretKey,G_j_pub) 
sk_us=module.functions.encrypt_string(str(C_i_pub)+str(G_j_pub)+str(dG_j)+str(NID_i)
+str(NID_j))
L_r_=module.functions.encrypt_string(str(ID_Sj)+str(ID_Ui)+str(C_i_pub)+str(C_i_share)
+str(G_j_pub)+str(H_i)+str(M_j))
S_us=module.functions.encrypt_string(str(sk_us)+str(L_i)+str(L_r_))
#print('S_us = ',S_us)
if S_us==S_su :  
    print('S_us = ',hex(S_us))
    print('S_su = ',hex(S_su)) 
    print("Authentication!!")
else:
    print("QQ")
    exit()