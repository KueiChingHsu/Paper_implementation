import hashlib
import os
import pickle

import module.ECC
import module.functions
from fuzzy_extractor import FuzzyExtractor
from user_parameter import *
from password_update_RC import *


with open('auth/extractor.pickle', 'rb') as f:
    extractor = pickle.load(f)
with open('auth/helper.pickle', 'rb') as f:
    helper = pickle.load(f)

print("extractor",extractor)
print("helper = ",helper)
