"""
Display functions for algorithms and security analysis reports
"""


def display_algorithms():
    """Display encryption/decryption algorithms"""
    print("\n+================================================================+")
    print("|                    ENCRYPTION ALGORITHM                        |")
    print("+================================================================+")
    print("\nSTEP 1: Playfair Encryption")
    print("1. Create 5x5 matrix using Playfair key (merge I/J)")
    print("2. Prepare plaintext: remove non-letters, insert X between doubles")
    print("3. Split into digraphs (pairs)")
    print("4. For each pair (a,b):")
    print("   - Same row: shift right → (c,d)")
    print("   - Same column: shift down → (c,d)")
    print("   - Rectangle: swap columns → (c,d)")
    print("5. Output: Playfair ciphertext")
    
    print("\nSTEP 2: Vigenere Encryption")
    print("1. Take Playfair output as input")
    print("2. Extend Vigenere key to match text length")
    print("3. For each letter i:")
    print("   Ci = (Pi + Ki) mod 26")
    print("4. Output: Final hybrid ciphertext")
    
    print("\n+================================================================+")
    print("|                    DECRYPTION ALGORITHM                        |")
    print("+================================================================+")
    print("\nSTEP 1: Vigenere Decryption")
    print("1. Extend Vigenere key to match ciphertext length")
    print("2. For each letter i:")
    print("   Pi = (Ci - Ki + 26) mod 26")
    print("3. Output: Playfair ciphertext")
    
    print("\nSTEP 2: Playfair Decryption")
    print("1. Use same 5x5 matrix from encryption")
    print("2. For each digraph pair (a,b):")
    print("   - Same row: shift left → (c,d)")
    print("   - Same column: shift up → (c,d)")
    print("   - Rectangle: swap columns → (c,d)")
    print("3. Output: Original plaintext")


def display_security_analysis():
    """Display security analysis report"""
    print("\n+================================================================+")
    print("|                    SECURITY ANALYSIS REPORT                    |")
    print("+================================================================+")
    
    print("\n1. CIPHER COMBINATION STRATEGY:")
    print("   [+] Playfair (digraph substitution) + Vigenere (polyalphabetic)")
    print("   [+] Two-layer encryption provides defense in depth")
    print("   [+] Playfair obscures letter patterns and digraph frequencies")
    print("   [+] Vigenere adds key-based shift variation")
    
    print("\n2. STRENGTHS:")
    print("   [+] Resistant to simple frequency analysis")
    print("   [+] Digraph encryption breaks single-letter patterns")
    print("   [+] Polyalphabetic layer adds complexity")
    print("   [+] Large combined keyspace (~=10^25 x 26^n)")
    print("   [+] No electronic computer needed for encryption")
    
    print("\n3. WEAKNESSES:")
    print("   [-] Vulnerable to known-plaintext with sufficient data")
    print("   [-] Vigenere component susceptible to Kasiski examination")
    print("   [-] Playfair limited to 25 letters (I/J merged)")
    print("   [-] Pattern 'X' insertion may leak information")
    print("   [-] Not secure against modern cryptanalysis")
    
    print("\n4. ATTACK RESISTANCE:")
    print("   o Frequency Analysis: HIGH resistance")
    print("   o Brute Force: VERY HIGH resistance")
    print("   o Known-Plaintext: MODERATE resistance")
    print("   o Chosen-Plaintext: LOW resistance")
    
    print("\n5. RECOMMENDED USE:")
    print("   -> Educational purposes and historical study")
    print("   -> Basic message obfuscation")
    print("   -> NOT recommended for sensitive data")
    print("   -> Use modern encryption (AES, RSA) for real security")
    
    print("\n6. COMPARISON TO MODERN STANDARDS:")
    print("   o AES-256 keyspace: 2^256 ~= 10^77 keys")
    print("   o This hybrid: ~= 10^25 x 26^n keys")
    print("   o Modern ciphers use mathematical complexity")
    print("   o Classical ciphers rely on pattern obscuration")
