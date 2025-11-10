"""
Attack Simulation and Cryptanalysis Tools
"""

import time
from collections import Counter
from constants import ENGLISH_FREQ
from playfair import PlayfairCipher


class AttackSimulator:
    """Simulates various cryptographic attacks on the hybrid cipher"""
    
    def _calculate_frequency(self, text):
        """Calculate letter frequency in text"""
        freq = Counter()
        for c in text:
            if c.isalpha():
                freq[c.upper()] += 1
        return freq
    
    def _calculate_chi_squared(self, observed, total):
        """Calculate chi-squared statistic"""
        chi_squared = 0.0
        
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            expected = (ENGLISH_FREQ[c] / 100.0) * total
            obs = observed.get(c, 0)
            if expected > 0:
                chi_squared += (obs - expected) ** 2 / expected
        
        return chi_squared
    
    def frequency_analysis(self, ciphertext):
        """Perform frequency analysis attack"""
        print("\n+========================================+")
        print("|     FREQUENCY ANALYSIS ATTACK          |")
        print("+========================================+")
        
        start = time.time()
        
        freq = self._calculate_frequency(ciphertext)
        total = sum(freq.values())
        
        print(f"\nCiphertext Statistics:")
        print(f"Total Letters: {total}")
        print(f"Unique Letters: {len(freq)}\n")
        
        print("Letter Frequency Distribution:")
        print("--------------------------------")
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        for char, count in sorted_freq:
            percentage = (count * 100.0) / total
            bars = '#' * int(percentage * 2)
            print(f"{char}: {count:4d} ({percentage:5.2f}%) {bars}")
        
        chi_squared = self._calculate_chi_squared(freq, total)
        print(f"\nChi-Squared Value: {chi_squared:.2f}")
        print("(Lower values indicate closer match to English)")
        print("Expected range for English: 20-40")
        
        duration = (time.time() - start) * 1000
        print(f"\nComputational Effort: {duration:.0f} ms")
        
        print("\nAnalysis Result:")
        if chi_squared > 100:
            print("[+] Cipher appears HIGHLY RESISTANT to simple frequency analysis")
            print("[+] The hybrid approach successfully obscures letter patterns")
        elif chi_squared > 50:
            print("[~] Cipher shows MODERATE RESISTANCE to frequency analysis")
        else:
            print("[-] Cipher may be VULNERABLE to frequency analysis")
    
    def known_plaintext_attack(self, plaintext, ciphertext, playfair_key, vigenere_key):
        """Simulate known-plaintext attack"""
        print("\n+========================================+")
        print("|    KNOWN-PLAINTEXT ATTACK              |")
        print("+========================================+")
        
        start = time.time()
        
        print(f"\nKnown Plaintext: {plaintext}")
        print(f"Known Ciphertext: {ciphertext}\n")
        
        attempts = 0
        vigenere_cracked = False
        
        # Attempt to deduce Vigenere key
        print("Attempting to deduce Vigenere key...")
        deduced_vig_key = ''
        
        pf = PlayfairCipher(playfair_key)
        after_playfair = pf.encrypt(plaintext)
        
        for i in range(min(len(after_playfair), len(ciphertext))):
            if after_playfair[i].isalpha() and ciphertext[i].isalpha():
                key_char = chr(((ord(ciphertext[i].upper()) - ord(after_playfair[i].upper()) + 26) % 26) + ord('A'))
                deduced_vig_key += key_char
                attempts += 1
        
        print(f"Deduced Vigenere Key Pattern: {deduced_vig_key}")
        
        # Check if pattern matches actual key
        if len(deduced_vig_key) >= len(vigenere_key):
            detected_key = deduced_vig_key[:len(vigenere_key)]
            if detected_key == vigenere_key.upper():
                vigenere_cracked = True
                print(f"[+] Vigenere Key SUCCESSFULLY CRACKED: {detected_key}")
        
        duration = (time.time() - start) * 1000000
        
        print(f"\nAttack Statistics:")
        print(f"Attempts Made: {attempts}")
        print(f"Computational Time: {duration:.0f} us")
        print(f"Key Space Explored: {attempts} / {26**len(vigenere_key):.0f}")
        
        print("\nAttack Result:")
        if vigenere_cracked:
            print("[!] PARTIALLY SUCCESSFUL: Vigenere component vulnerable to known-plaintext")
            print("  However, Playfair key remains secure")
            print("  Attacker still needs to break the Playfair cipher")
        else:
            print("[+] ATTACK FAILED: Insufficient known plaintext")
            print("[+] Hybrid cipher provides additional security layer")
        
        print(f"\nRequired known plaintext length: {len(vigenere_key)} characters minimum")
