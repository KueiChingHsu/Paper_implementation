from server1_user_parameter2_1 import *
from user1_parameter_self import *
from user_parameter import *
from password_update_RC import *
import pickle
import module.functions
'''
Upon receiving the message {M_j} , 
U_i computes L_i=h(NID_i ||C_i ||C_i^* ||NB_i ||P_i ||M_j ||H_i). 
U_i sends the message {L_i} to S_j via an insecure channel. 
'''
with open('auth/helper.pickle', 'rb') as f:
    P_i = pickle.load(f)

Pi_2D= ''.join(str(e) for e in P_i[0][0])
#print("Pi_2D : ",Pi_2D)
L_i=module.functions.encrypt_string(str(NID_i)+str(C_i_pub)+str(C_i_share)+str(NB_i)
+str(Pi_2D)+str(M_j)+str(H_i))
'''
print("L_i : ",L_i)
print("NB_i : ",NB_i)
print("M_j : ", M_j)
print("H_i : ",H_i)
'''
f = open("auth/user2_server_parameter3_1.py", "w")
f.write("L_i ="+str(L_i) +"\n" )
f = open("auth/user2_parameter_self.py", "w")
f.write("L_i ="+str(L_i) +"\n" )
'''
'''