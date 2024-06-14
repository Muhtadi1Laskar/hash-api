import hashlib

def hash_data(value, hash):
    hash_func = hashlib.new(hash)
    
    encoded_str = bytes(value, encoding='utf-8')
    hash_func.update(encoded_str)

    if hash == 'shake_256' or hash == 'shake_128':
        return hash_func.hexdigest(20)

    return hash_func.hexdigest()

data = "example text"

print(hash_data(data, 'blake2b'))
