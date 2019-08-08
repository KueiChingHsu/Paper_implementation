import module.functions
from module.parameter.reg_server_parameter import *   #import all objects and methods in reg_server.py
'''
SERVER REGISTRATION PHASE (STEP 2)

Upon receiving the message ID_Sj,
RC computes F_j=h(ID_Sj ||s) and 
sends the message {F_j } to S_j via a secure channel.
'''
rcSecretKey = 57821339089684328170078643393297452417348490406290096822816616169117693678235
rcPublicKey = (16321396343898609237058457459634586976814428690654624591817221787745052778620, 110853329480792751580624951942149634954474272806761480481621057182840458402147)
s=rcSecretKey

F_j = module.functions.encrypt_string(str(ID_Sj)+str(s))
print("F_j = ", hex(F_j))
#print("ID_Sj registration success !")
#F_j :  14265002496476131235555777951744958751394554191152126752125272167246018263881
f = open("reg/server/module/parameter/reg_server_RC_parameter.py","w")
f.write("F_j ="+str(F_j) +"\n" )