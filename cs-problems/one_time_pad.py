from secrets import token_bytes
from typing import Tuple

def generate_key(length: int) -> int:
    token = token_bytes(length)
    return int.from_bytes(token, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = generate_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == '__main__':
    key1, key2 = encrypt("My One Time Pad!" * 10)
    print(key1)
    print(key2)
    result: str = decrypt(key1, key2)
    print(result)
