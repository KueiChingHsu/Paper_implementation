import hashlib
import module.functions 
from module.parameter.reg_user_parameter import *
from fuzzy_extractor import FuzzyExtractor
import pickle
import binascii

with open('reg/user/helper.pickle', 'rb') as f:
    helper = pickle.load(f)
with open('reg/user/extractor.pickle', 'rb') as f:
    extractor = pickle.load(f)

R_i_before  = extractor.reproduce('859e662b97a5d98a2d34923a8e62fba3', helper)
R_i_after = extractor.reproduce('859e662b97a5d98a2dL492La8e62fbas', helper)
if (R_i_before == R_i_after):
    print("Y")
else :
    print("N")




