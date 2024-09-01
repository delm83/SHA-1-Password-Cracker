import hashlib
passwordlist = [line.rstrip('\n') for line in open('top-10000-passwords.txt', 'r')]
saltlist = [line.rstrip('\n') for line in open('known-salts.txt', 'r')]
def crack_sha1_hash(hash, use_salts = False):
    for password in passwordlist:
        if hash == hashlib.sha1(password.encode()).hexdigest():
            return password

    return "PASSWORD NOT IN DATABASE"