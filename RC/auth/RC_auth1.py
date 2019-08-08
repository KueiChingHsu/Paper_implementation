import os

'''
LOGIN PHASE AND AUTHENTICATION PHASE
Upon receiving the message {NID_i,NID_j,C_i,G_j,NB_i,P_i} , 
RC selects a random number δ_j 
and sends the message {δ_j} to S_j via an insecure channel.
'''

delta_j = int.from_bytes(os.urandom(32), byteorder="big")
print('delta_j = ',hex(delta_j))
#delta_j = 49916506474320652705657053577569393293619656572310681519752695363994418109978
#print('delta_j = ',delta_j)
#print("delta_j : ",delta_j)
#select a random number
f = open("./auth/RC1_server_parameter3_2.py", "w")
f.write("delta_j ="+str(delta_j) +"\n" )
f = open("./auth/RC1_parameter_self.py", "w")
f.write("delta_j ="+str(delta_j) +"\n" )
'''
delta_j :  49916506474320652705657053577569393293619656572310681519752695363994418109978
'''