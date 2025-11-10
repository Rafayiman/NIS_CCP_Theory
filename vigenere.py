"""
Vigenere Cipher Implementation
"""


class VigenereCipher:
    """Implements the Vigenere polyalphabetic cipher"""
    
    def __init__(self, key):
        """Initialize with a key"""
        self.key = ''.join(c.upper() for c in key if c.isalpha())
    
    def _extend_key(self, text):
        """Extend key to match text length"""
        extended_key = ''
        j = 0
        for c in text:
            if c.isalpha():
                extended_key += self.key[j % len(self.key)]
                j += 1
            else:
                extended_key += c
        return extended_key
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher"""
        ciphertext = ''
        ext_key = self._extend_key(plaintext)
        
        for i, c in enumerate(plaintext):
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                encrypted = chr((ord(c.upper()) - ord('A') + ord(ext_key[i]) - ord('A')) % 26 + base)
                ciphertext += encrypted
            else:
                ciphertext += c
        
        return ciphertext
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Vigenere cipher"""
        plaintext = ''
        ext_key = self._extend_key(ciphertext)
        
        for i, c in enumerate(ciphertext):
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                decrypted = chr((ord(c.upper()) - ord('A') - ord(ext_key[i]) + ord('A') + 26) % 26 + base)
                plaintext += decrypted
            else:
                plaintext += c
        
        return plaintext
    
    def get_key(self):
        """Return the current key"""
        return self.key
