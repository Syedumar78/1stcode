import string  # Import string module
import random  # Import random module
def generate_name(length=50):
    _Nawaz_ = string.ascii_uppercase + string.punctuation # Combine letters and digits
    name = ''.join(random.choice(_Nawaz_) for _ in range(length))  # Generate random name
    return name  # Return the generated name
name = generate_name(50)
print("Generated name",(name))
print(len(name))
 
import random
import string 
def generate_random(length=30):
    _Imran = string.ascii_letters + string.digits + string.punctuation
    _random =''.join(random.choice(_Imran)for _ in range(length))
    return _random
_random = generate_random(30)
print("generated random:", (_random))
print(len(_random))

