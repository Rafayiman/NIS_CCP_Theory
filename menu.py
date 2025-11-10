"""
User interface and menu system
"""

import time
from playfair import PlayfairCipher
from vigenere import VigenereCipher
from attack_simulator import AttackSimulator


class Menu:
    """Handles the interactive menu system"""
    
    def __init__(self):
        """Initialize menu with cipher instances"""
        self.playfair = None
        self.vigenere = None
        self.attacker = AttackSimulator()
        self.plaintext = ''
        self.ciphertext = ''
        self.encryption_done = False
        self.decryption_done = False
    
    def setup(self):
        """Setup keys and initialize ciphers"""
        print("+===============================================================+")
        print("|      HYBRID CIPHER: Playfair + Vigenere Implementation        |")
        print("|              With Attack Simulation & Analysis                |")
        print("+===============================================================+")
        
        playfair_key = input("\nEnter Playfair Key: ")
        vigenere_key = input("Enter Vigenere Key: ")
        
        self.playfair = PlayfairCipher(playfair_key)
        self.vigenere = VigenereCipher(vigenere_key)
        self.playfair_key = playfair_key
        self.vigenere_key = vigenere_key
    
    def display_menu(self):
        """Display main menu options"""
        print("\n+======================================+")
        print("|           MAIN MENU                  |")
        print("+======================================+")
        print("| 1. Display Playfair Matrix           |")
        print("| 2. Encrypt Message                   |")
        print("| 3. Decrypt Message                   |")
        print("| 4. Frequency Analysis Attack         |")
        print("| 5. Known-Plaintext Attack            |")
        print("| 6. Exit                              |")
        print("+======================================+")
    
    def handle_display_matrix(self):
        """Option 1: Display Playfair matrix"""
        self.playfair.display_matrix()
    
    def handle_encrypt(self):
        """Option 2: Encrypt message"""
        self.plaintext = input("\nEnter plaintext: ")
        
        print("\n+========================================+")
        print("|         ENCRYPTION PROCESS             |")
        print("+========================================+")
        
        start = time.time()
        
        after_playfair = self.playfair.encrypt(self.plaintext)
        print(f"\nStep 1 - After Playfair: {after_playfair}")
        
        self.ciphertext = self.vigenere.encrypt(after_playfair)
        print(f"Step 2 - After Vigenere: {self.ciphertext}")
        
        duration = (time.time() - start) * 1000000
        
        print(f"\n[+] Encryption completed in {duration:.0f} us")
        print(f"Original length: {len(self.plaintext)} -> Cipher length: {len(self.ciphertext)}")
        
        self.encryption_done = True
    
    def handle_decrypt(self):
        """Option 3: Decrypt message"""
        self.ciphertext = input("\nEnter ciphertext: ")
        
        print("\n+========================================+")
        print("|         DECRYPTION PROCESS             |")
        print("+========================================+")
        
        start = time.time()
        
        after_vigenere = self.vigenere.decrypt(self.ciphertext)
        print(f"\nStep 1 - After Vigenere Decrypt: {after_vigenere}")
        
        final_plain = self.playfair.decrypt(after_vigenere)
        print(f"Step 2 - After Playfair Decrypt: {final_plain}")
        
        duration = (time.time() - start) * 1000000
        
        print(f"\n[+] Decryption completed in {duration:.0f} us")
        
        self.decryption_done = True
    
    def handle_frequency_analysis(self):
        """Option 6: Frequency analysis attack"""
        if not self.ciphertext:
            print("\n[!] Please encrypt a message first (Option 2)")
        else:
            self.attacker.frequency_analysis(self.ciphertext)
    
    def handle_known_plaintext_attack(self):
        """Option 5: Known-plaintext attack"""
        if not self.encryption_done:
            print("\n[!] Please perform encryption first (Option 2)")
        else:
            self.attacker.known_plaintext_attack(
                self.plaintext, 
                self.ciphertext,
                self.playfair_key, 
                self.vigenere_key
            )
    
    def handle_exit(self):
        """Option 6: Exit program"""
        if not self.encryption_done or not self.decryption_done:
            print("\n[!] You must perform at least one encryption AND one decryption before exiting!")
            print(f"Encryption done: {'[+]' if self.encryption_done else '[-]'}")
            print(f"Decryption done: {'[+]' if self.decryption_done else '[-]'}")
            return False
        else:
            print("\n[+] Thank you for using the Hybrid Cipher System!")
            return True
    
    def run(self):
        """Main program loop"""
        self.setup()
        
        while True:
            self.display_menu()
            
            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("\n[-] Invalid choice! Please try again.")
                continue
            
            if choice == 1:
                self.handle_display_matrix()
            elif choice == 2:
                self.handle_encrypt()
            elif choice == 3:
                self.handle_decrypt()
            elif choice == 4:
                self.handle_frequency_analysis()
            elif choice == 5:
                self.handle_known_plaintext_attack()
            elif choice == 6:
                if self.handle_exit():
                    break
            else:
                print("\n[-] Invalid choice! Please try again.")
