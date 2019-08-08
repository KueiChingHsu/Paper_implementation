import module.functions 
from user2_server_parameter3_1 import *
from RC1_server_parameter3_2 import *
from server1_parameter_self import *
from server_parameter import *
from user1_parameter import *
'''
Upon receiving the message {L_i} and {δ_j}. 
S_j computes Z_j=h(M_j ||L_i ||δ_j ||F_j) and 
sends the message {Z_j} to RC via an insecure channel.
'''
Z_j=module.functions.encrypt_string(str(M_j)+str(L_i)+
str(delta_j)+str(F_j))
#print("Z_j : ",Z_j)
f = open("./auth/server2_rc_parameter4.py", "w")
f.write("Z_j = "+str(Z_j) +"\n" )
f = open("./auth/server2_parameter_self.py", "w")
f.write("Z_j = "+str(Z_j) +"\n" )
'''
Z_j :  35163114698380681977973594506810966323769620458708853307642265142183138631323
'''