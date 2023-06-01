import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


class JsonDB:
    def __init__(self):
        self.data = {}

    def open(self, filename, password):
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = self._decrypt(encrypted_data, password)
            self.data = json.loads(decrypted_data)

    def save(self, filename, password):
        serialized_data = json.dumps(self.data).encode('utf-8')
        encrypted_data = self._encrypt(serialized_data, password)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def _encrypt(self, data, password):
        salt = get_random_bytes(16)
        key = PBKDF2(password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
        return salt + cipher.iv + encrypted_data

    def _decrypt(self, data, password):
        salt = data[:16]
        data = data[16:]
        key = PBKDF2(password, salt, dkLen=32)
        iv = data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
        return decrypted_data.decode('utf-8')

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def concept(self, data):
        result = []
        for key, value in self.data.items():
            if data in key:
                result.append(value)
        return result

    def keyconcept(self, data):
        result = []
        for key in self.data.keys():
            if data in key:
                result.append(key)
        return result

    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def items(self):
        return list(self.data.items())

    def clear(self):
        self.data.clear()

    def count(self):
        return len(self.data)

    def delete_by_value(self, data):
        keys_to_delete = []
        for key, value in self.data.items():
            if isinstance(value, str) and data in value:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del self.data[key]

    def delete_by_key(self, key):
        keys_to_delete = []
        for k in self.data.keys():
            if key in k:
                keys_to_delete.append(k)
        for k in keys_to_delete:
            del self.data[k]
