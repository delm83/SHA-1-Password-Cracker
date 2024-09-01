import hashlib
passwordlist = [line.rstrip() for line in open('top-10000-passwords.txt', 'r')]
saltlist = [line.rstrip() for line in open('known-salts.txt', 'r')]
def crack_sha1_hash(hash, use_salts = False):
    for password in passwordlist:
        if use_salts:
            for salt in saltlist:
                saltedpassword = salt+password
                if hash == hashlib.sha1(saltedpassword.encode()).hexdigest():
                    return password
                saltedpassword = password+salt
                if hash == hashlib.sha1(saltedpassword.encode()).hexdigest():
                    return password
        else:
            if hash == hashlib.sha1(password.encode()).hexdigest():
                return password

    return "PASSWORD NOT IN DATABASE"