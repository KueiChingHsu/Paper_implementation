import pickle
from fuzzy_extractor import FuzzyExtractor
face_result=496216505212515211525214534218554218563214573211582212590216535265540266545267550266555264545230545239545249545258565278557283550285545286540286533284525279529279541279545279550279562279509229516227523228528232522233515232482223484239486254489269495283505294518302531309545311559309572301584293593282598268600253602239603224560232565227572227578230573232566233525279534277541275545276550275557276565278562279550280545280541280529279
face_binary="{0:b}".format(face_result)
face_128 = face_binary[0:128]

#print (face_128)
face_hex_128=hex(int(face_128, 2))
#print(face_hex_128)
result=face_hex_128[2:]
print("Biometric = ",result)
print("Biometric Type = ",type(result))
'''
face_binary="{0:b}".format(face_result)
face_1024 = face_binary[0:1024]
#print (face_1024)
face_int=int(str(face_1024),2)

face_byte= face_int.to_bytes((face_int.bit_length()+7) // 8, byteorder='big')
face_ascii= face_byte.decode(encoding="utf8", errors='ignore')
face_input=face_ascii[0:32]
print("face_input=",face_input)
'''
with open('biometric/parameter.py', 'w') as f:
    f.write("B_i = '"+ result +"'" )
with open('reg/module/parameter/biometric_parameter.py', 'w') as f:
    f.write("B_i = '"+result +"'" )

'''
extractor = FuzzyExtractor(32, 8)

key, helper = extractor.generate('f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"x6')
print("extractor",extractor)

with open('helper.pickle', 'wb') as f:
    pickle.dump(helper, f)
with open('extractor.pickle', 'wb') as f:
    pickle.dump(extractor, f)

result:
face_input= f+ي-4:b~^RIlm?{e#hFmP{?<XDЫ"x6
extractor <fuzzy_extractor.FuzzyExtractor object at 0x7f18b0bfb588>
'''
'''
新增 user/reg fuzzy extractor 檔案
with open('helper.pickle', 'rb') as f:
    helper = pickle.load(f)
with open('../reg/helper.pickle', 'wb') as f:
    pickle.dump(helper, f)
with open('extractor.pickle', 'rb') as f:
    extractor = pickle.load(f)
with open('../reg/extractor.pickle', 'wb') as f:
    pickle.dump(extractor, f)
'''
'''
10000101100111100110011000101011100101111010010111011001100010100010110100110100100100100011101010001110011000101111101110100011
0x859e662b97a5d98a2d34923a8e62fba3
859e662b97a5d98a2d34923a8e62fba3
<class 'str'>
'''
