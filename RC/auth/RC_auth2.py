from RC_parameter import *
from RC1_parameter_self import *
from server1_rc_parameter2_2 import *
from server2_rc_parameter4 import *
import os
import pickle
import module.ECC
import module.functions
from fuzzy_extractor import FuzzyExtractor
from user_biometric_key_data import R_i

'''
Upon receiving the message {Z_j}, 
RC computes ECDH shared secret key G_r^*=sG_j=((G_r^* )_x,(G_r^* )_y )∈E_P, 
ECDH shared secret keyC_r^*=sC_i=((C_r^* )_x,(C_r^* )_y )∈E_P, 
ID_Ui=h((C_r^* )_x ||1)⊕NID_i, ID_Sj=h((G_r^* )_x ||3)⊕NID_j. 
RC then computes H_i^'=h(ID_Ui ||s),  F_j^'=h(ID_Sj ||s) , 
M_j^'== h(NID_i ||NID_j ||C_i ||G_j ||G_r^* ||NB_i ||F_j^'), 
L_i^'== h(NID_i ||C_i ||C_r^* ||NB_i ||P_i ||M_j^' ||H_i^'), 
Z_j^'== h(M_j^' ||L_i^' ||δ_j ||F_j^' )  
and checks if Z_j^'?=Z_j holds. 
If it does not hold, RC terminates the process; 
otherwise, RC computes B_i^'=h((C_ri^* )_x ||2)⊕NB_i . 
RC computes  D_r=h((G_r^* )_x ||4)⊕R_i , O_r=h((G_r^* )_x ||5)⊕B_i^' , 
N_r== h(D_r ||O_r ||F_j ||R_i ||G_r^* ||B_i^'), 
L_r== h(ID_Sj ||ID_Ui ||C_i ||C_r^* ||G_j ||H_i^' ||M_j) 
and PID_i=h((G_r^* )_x ||6)⊕ID_Ui. 
RC sends the message {N_r,D_r,O_r,L_r,PID_i} to S_j via an insecure channel.
'''

G_r_share=module.ECC.scalar_mult(s,G_j_pub) 
C_r_share=module.ECC.scalar_mult(s,C_i_pub) 
#print("G_r_share : ",G_r_share)
#print("C_r_share : ",C_r_share)
ID_Ui= module.functions.encrypt_string(str(C_r_share[0])+str(random1))^NID_i 
ID_Sj=module.functions.encrypt_string(str(G_r_share[0])+str(random3))^NID_j
#print("ID_Ui : ",ID_Ui)
#print("ID_Sj : ",ID_Sj)
H_i_= module.functions.encrypt_string(str(ID_Ui)+str(s))
F_j_= module.functions.encrypt_string(str(ID_Sj)+str(s))
#print("H_i_ : ",H_i_)
#print("F_j_ : ",F_j_)
#print("NB_i : ",NB_i)
M_j_= module.functions.encrypt_string(str(NID_i)+str(NID_j)+str(C_i_pub)
+str(G_j_pub)+str(G_r_share)+str(NB_i)+str(F_j_))
#print("M_j_ : ", M_j_)
with open('./auth/helper.pickle', 'rb') as f:
    P_i = pickle.load(f)

Pi_2D_RC= ''.join(str(e) for e in P_i[0][0])
#print("Pi_2D : ",Pi_2D_RC)
L_i_= module.functions.encrypt_string(str(NID_i)+str(C_i_pub)+str(C_r_share)
+str(NB_i)+str(Pi_2D_RC)+str(M_j_)+str(H_i_))
Z_j_=module.functions.encrypt_string(str(M_j_)+str(L_i_)+str(delta_j)
+str(F_j_))
#print("L_i_ : ",L_i_)
#print("Z_j_ : ",Z_j_)
if Z_j_==Z_j :    
    #print("YES, Z_j_ = Z_j :",Z_j_)
    print('Z_j = ',hex(Z_j))
    print('Z_j_ = ',hex(Z_j_))
    print("RC verifies : ok ")
else:
    #print("Z_j_ != Z_j : NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
    print('Z_j = ',hex(Z_j))
    print('Z_j_ = ',hex(Z_j_))
    print("RC verifies fail...")
    exit()
'''
G_r_share :  (27277795148277752070081975622847219230564749777372924037301376772162800462323, 19435017496129124946310422930569376027710364413013798433001896518481058088169)
C_r_share :  (69285565998812565712857647080714626004324804515167533506024841044946667166244, 68351488862331344291853581187185777703677808301096302510293669846887962460305)
ID_Ui :  74372442465237888562585428825218926942370577176913359607894113446211346756504
ID_Sj :  99594609407927317843206528110378694655493681992847333187920745673397204165823
H_i_ :  47758271670838609718814890980207843031779882961895519289075024088788143748735
F_j_ :  14265002496476131235555777951744958751394554191152126752125272167246018263881
M_j_ :  29395113788332622564987093383221262489288967968992449815512541995298760322944
Pi_2D :  24318713417314212226201287812018221824330233152219166115143331150918712516515217091221
L_i_ :  61847046998869577746217087695886097584363578193267537108561780774714478302601
Z_j_ :  43602930389047498962883175116887199570443947776985549859613842673778208454531
YES, Z_j_ = Z_j : 43602930389047498962883175116887199570443947776985549859613842673778208454531
'''

'''
random4=int.from_bytes(os.urandom(32), byteorder="big") 
random5=int.from_bytes(os.urandom(32), byteorder="big")
random6=int.from_bytes(os.urandom(32), byteorder="big")
print("random4 : ",random4)
print("random5 : ",random5)
print("random6 : ",random6)
'''
random4 =  87715611681988517897590045791081321625371164917963034646099350560113330641031
random5 =  20509063491934868987603442815906978114204910626192023373152000071541725312687
random6 =  108117510928581576675068452675811350789955174292611233395361218243576368283609
B_i_RC =module.functions.encrypt_string(str(C_r_share[0])+str(random2))^NB_i
D_r=module.functions.encrypt_string(str(G_r_share[0])+str(random4))^R_i
O_r=module.functions.encrypt_string(str(G_r_share[0])+str(random5))^B_i_RC
'''
print('R_i : ',R_i)

print("B_i_RC : ",B_i_RC)
print("D_r : ",D_r)
print("O_r : ",O_r)
'''
'''
B_i_RC :  29515630589904128245223976570842015727304113738300535931626442982409229123913
D_r :  20491384202947902876892012618229857192268128146303097009960383442601928187995
O_r :  20183964042016017223626491671776108877695979802732917609647789969293956522747
'''
N_r=module.functions.encrypt_string(str(D_r)+str(O_r)+str(F_j_)+str(R_i)+str(G_r_share)+str(B_i_RC))
L_r=module.functions.encrypt_string(str(ID_Sj)+str(ID_Ui)+str(C_i_pub)+str(C_r_share)+str(G_j_pub)+str(H_i_)+str(M_j_))
PID_i=module.functions.encrypt_string(str(G_r_share[0])+str(random6))^ID_Ui
'''
print("N_r : ",N_r)
print("L_r : ",L_r)
print("PID_i : ",PID_i)

N_r :  100255503627370807510708087240015380927897418375245974704600873226624891962494
L_r :  21718818686011294856441694898049676931524042060683850275718453854856831165782
PID_i :  48302553641476123444374078706429232383568025904267017113131854425937685006319
'''
f = open("./auth/RC2_server_parameter5.py", "w")
f.write("N_r = "+str(N_r) +"\n" )
f.write("D_r = "+str(D_r) +"\n" )
f.write("O_r ="+str(O_r) +"\n" )
f.write("L_r ="+str(L_r) +"\n" )
f.write("PID_i ="+str(PID_i) +"\n" )