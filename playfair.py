"""
Playfair Cipher Implementation
"""

from constants import PLAYFAIR_ALPHABET


class PlayfairCipher:
    """Implements the Playfair digraph substitution cipher"""
    
    def __init__(self, key):
        """Initialize with a key and create the 5x5 matrix"""
        self.matrix = self._create_matrix(key)
    
    def _create_matrix(self, key):
        """Create 5x5 Playfair matrix from key"""
        matrix = []
        used = set()
        used.add('J')  # J is merged with I
        
        # Add key characters
        for c in key.upper():
            if c.isalpha() and c not in used:
                matrix.append(c)
                used.add(c)
        
        # Add remaining alphabet
        for c in PLAYFAIR_ALPHABET:
            if c not in used:
                matrix.append(c)
        
        # Convert to 5x5 grid
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def _find_position(self, c):
        """Find row and column of character in matrix"""
        if c == 'J':
            c = 'I'
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == c:
                    return i, j
        return 0, 0
    
    def _prepare_text(self, text):
        """Prepare text for Playfair encryption"""
        # Remove non-letters and convert to uppercase
        result = ''.join(c.upper() if c != 'J' else 'I' for c in text if c.isalpha())
        
        # Insert X between duplicate letters
        processed = ''
        i = 0
        while i < len(result):
            processed += result[i]
            if i + 1 < len(result) and result[i] == result[i + 1]:
                processed += 'X'
            i += 1
        
        # Add X if odd length
        if len(processed) % 2 != 0:
            processed += 'X'
        
        return processed
    
    def display_matrix(self):
        """Display the Playfair matrix"""
        print("\n+=======================+")
        print("|  Playfair Matrix 5x5  |")
        print("+=======================+")
        for row in self.matrix:
            print(f"|   {' '.join(row)}  |")
        print("+=======================+")
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using Playfair cipher"""
        text = self._prepare_text(plaintext)
        ciphertext = ''
        
        for i in range(0, len(text), 2):
            r1, c1 = self._find_position(text[i])
            r2, c2 = self._find_position(text[i + 1])
            
            if r1 == r2:  # Same row
                ciphertext += self.matrix[r1][(c1 + 1) % 5]
                ciphertext += self.matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:  # Same column
                ciphertext += self.matrix[(r1 + 1) % 5][c1]
                ciphertext += self.matrix[(r2 + 1) % 5][c2]
            else:  # Rectangle
                ciphertext += self.matrix[r1][c2]
                ciphertext += self.matrix[r2][c1]
        
        return ciphertext
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Playfair cipher"""
        plaintext = ''
        
        for i in range(0, len(ciphertext), 2):
            r1, c1 = self._find_position(ciphertext[i])
            r2, c2 = self._find_position(ciphertext[i + 1])
            
            if r1 == r2:  # Same row
                plaintext += self.matrix[r1][(c1 - 1) % 5]
                plaintext += self.matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:  # Same column
                plaintext += self.matrix[(r1 - 1) % 5][c1]
                plaintext += self.matrix[(r2 - 1) % 5][c2]
            else:  # Rectangle
                plaintext += self.matrix[r1][c2]
                plaintext += self.matrix[r2][c1]
        
        return plaintext
