import bcrypt

def hash_pw(plaintext_password):
    return bcrypt.hashpw(bytes(plaintext_password, 'utf-8'), bcrypt.gensalt())

def check_pw(plaintext_password, db_password):
    print('Plaintext password: ', plaintext_password)
    print('Is string?: ', isinstance(plaintext_password, str))
    print('DB password', db_password)
    return bcrypt.checkpw(bytes(plaintext_password, 'utf-8'), db_password)