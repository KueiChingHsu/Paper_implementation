import collections
import hashlib
import random
import binascii
EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')
curve = EllipticCurve(
    'secp256k1',
    # Field characteristic.
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    # Curve coefficients.
    a=0,
    b=7,
    # Base point.
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    # Subgroup order.
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    # Subgroup cofactor.
    h=1,
)
# Modular arithmetic ##########################################################
def inverse_mod(k, p):
    """Returns the inverse of k modulo p.
    This function returns the only integer x such that (x * k) % p == 1.
    k must be non-zero and p must be a prime.
    """
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)
    # Extended Euclidean algorithm.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    gcd, x, y = old_r, old_s, old_t
    assert gcd == 1
    assert (k * x) % p == 1
    return x % p
# Functions that work on curve points #########################################
def is_on_curve(point):
    """Returns True if the given point lies on the elliptic curve."""
    if point is None:
        # None represents the point at infinity.
        return True
    x, y = point
    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0
def point_add(point1, point2):
    """Returns the result of point1 + point2 according to the group law."""
    assert is_on_curve(point1)
    assert is_on_curve(point2)
    if point1 is None:
        # 0 + point2 = point2
        return point2
    if point2 is None:
        # point1 + 0 = point1
        return point1
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and y1 != y2:
        # point1 + (-point1) = 0
        return None
    if x1 == x2:
        # This is the case point1 == point2.
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        # This is the case point1 != point2.
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)
    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)
    assert is_on_curve(result)
    return result
def scalar_mult(k, point):
    """Returns k * point computed using the double and point_add algorithm."""
    assert is_on_curve(point)
    if k % curve.n == 0 or point is None:
        return None
    if k < 0:
        # k * point = -k * (-point)
        return scalar_mult(-k, point_neg(point))
    result = None
    addend = point
    while k:
        if k & 1:
            # Add.
            result = point_add(result, addend)
        # Double.
        addend = point_add(addend, addend)
        k >>= 1
    assert is_on_curve(result)
    return result


# Keypair generation and ECDSA ################################################

def make_keypair():
    """Generates a random private-public key pair."""
    private_key = random.randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)
    return private_key, public_key

'''
print ("Basepoint:\t",curve.g)
rcSecretKey = 57821339089684328170078643393297452417348490406290096822816616169117693678235
rcPublicKey = (16321396343898609237058457459634586976814428690654624591817221787745052778620, 110853329480792751580624951942149634954474272806761480481621057182840458402147)

userSecretKey = 18389312126672388558932582546480038667228499401742387498714331289885270368100
userPublicKey = (104794922284476211188539510874574520439368955857631400794825825280406668743622, 76955737309824395470986576820650110587227188240129111379703754475155357103655)
 
serverSecretKey = 109595195285931551302123380388891451684880829339665071061898110788443083113443
serverPublicKey = (86162140726858981498335099083713831683300879107620687399830264644432057851960, 19052722683819249944236338398234184693862153921902986251199800499740938817011)
 
print ("RC\'s secret key:\t", rcSecretKey)
print ("RC\'s public key:\t", rcPublicKey)
print ("User\'s secret key:\t", userSecretKey)
print ("User\'s public key:\t", userPublicKey)
print ("Server\'s secret key:\t", serverSecretKey)
print ("Server\'s public key:\t", serverPublicKey)

#print ("==========================")


User_RC_sharedSecret = scalar_mult(userSecretKey,rcPublicKey)
RC_User_sharedSecret = scalar_mult(rcSecretKey,userPublicKey)

Server_RC_sharedSecret = scalar_mult(serverSecretKey,rcPublicKey)
RC_Server_sharedSecret = scalar_mult(rcSecretKey,serverPublicKey)

print ("=======================================================================================================================")
print ("User_RC_sharedSecret\'s shared key:\t",hex(User_RC_sharedSecret[0]))
print ("RC_User_sharedSecret\'s shared key:\t",hex(RC_User_sharedSecret[0]))
print ("Server_RC_sharedSecret\'s shared key:\t",hex(Server_RC_sharedSecret[0]))
print ("RC_Server_sharedSecret\'s shared key:\t",hex(RC_Server_sharedSecret[0]))

'''