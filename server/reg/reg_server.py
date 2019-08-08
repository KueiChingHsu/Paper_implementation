import os

'''
SERVER REGISTRATION PHASE (STEP 1)

S_j sends the message of its identity {ID_Sj} to RC via a secure channel.
 ''' 
ID_Sj= 99594609407927317843206528110378694655493681992847333187920745673397204165823
#int.from_bytes(os.urandom(32), byteorder="big") 
#print("ID_Sj : ",ID_Sj)
f = open("reg/module/parameter/reg_server_parameter.py", "w")
f.write("ID_Sj ="+str(ID_Sj) +"\n" )

