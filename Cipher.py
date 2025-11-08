import os
import time

class CipherVault:
    def __init__(self):
        self.tool_name = "CipherVault Pro"
        self.version = "1.0"
        self.author = "CyberSec Tools"
        
    def display_banner(self):
        banner = f"""
        ╔══════════════════════════════════════════════════════════════════╗
        ║                                                                  ║
        ║    ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ ██╗   ██╗██████╗    ║
        ║   ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗██║   ██║██╔══██╗   ║
        ║   ██║     ██║██████╔╝███████║█████╗  ██████╔╝██║   ██║██████╔╝   ║
        ║   ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔═══╝    ║
        ║   ╚██████╗██║██║     ██║  ██║███████╗██║  ██║╚██████╔╝██║        ║
        ║    ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝        ║
        ║                                                                  ║
        ║                    🏰 CAESAR CIPHER TOOL 🏰                     ║
        ║                    Version {self.version} | {self.author}        ║
        ║                    Developed by Talha Baig                       ║
        ╚══════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def caesar_cipher(self, text, shift, mode='encrypt'):
        """
        Encrypt or decrypt text using Caesar Cipher algorithm
        """
        result = ""
        
        for char in text:
            if char.isalpha():
                # Determine the base (A for uppercase, a for lowercase)
                base = ord('A') if char.isupper() else ord('a')
                
                if mode == 'encrypt':
                    # Encryption: shift forward
                    shifted_char = chr((ord(char) - base + shift) % 26 + base)
                else:
                    # Decryption: shift backward
                    shifted_char = chr((ord(char) - base - shift) % 26 + base)
                
                result += shifted_char
            else:
                # Keep non-alphabetic characters as they are
                result += char
        
        return result
    
    def get_valid_shift(self):
        """
        Get a valid shift value from user
        """
        while True:
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    return shift
                else:
                    print("❌ Please enter a shift value between 0 and 25.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def encrypt_message(self):
        """
        Encrypt a message using Caesar Cipher
        """
        print("\n" + "═" * 60)
        print("🔒 ENCRYPTION MODE")
        print("═" * 60)
        
        message = input("Enter message to encrypt: ")
        shift = self.get_valid_shift()
        
        encrypted = self.caesar_cipher(message, shift, 'encrypt')
        
        print("\n" + "🎯 RESULTS:")
        print(f"Original Message: {message}")
        print(f"Shift Value: {shift}")
        print(f"Encrypted Text: {encrypted}")
        
        return encrypted
    
    def decrypt_message(self):
        """
        Decrypt a message using Caesar Cipher
        """
        print("\n" + "═" * 60)
        print("🔓 DECRYPTION MODE")
        print("═" * 60)
        
        message = input("Enter message to decrypt: ")
        shift = self.get_valid_shift()
        
        decrypted = self.caesar_cipher(message, shift, 'decrypt')
        
        print("\n" + "🎯 RESULTS:")
        print(f"Encrypted Message: {message}")
        print(f"Shift Value: {shift}")
        print(f"Decrypted Text: {decrypted}")
        
        return decrypted
    
    def brute_force_decrypt(self):
        """
        Try all possible shift values to decrypt a message
        """
        print("\n" + "═" * 60)
        print("🔍 BRUTE FORCE DECRYPTION")
        print("═" * 60)
        
        message = input("Enter encrypted message: ")
        
        print(f"\nTrying all possible shifts for: {message}")
        print("\n" + "─" * 50)
        
        results = []
        for shift in range(26):
            decrypted = self.caesar_cipher(message, shift, 'decrypt')
            results.append((shift, decrypted))
            print(f"Shift {shift:2d}: {decrypted}")
        
        print("─" * 50)
        print("✨ All possible decryptions displayed above.")
        
        return results
    
    def display_help(self):
        """
        Display help information about Caesar Cipher
        """
        print("\n" + "═" * 60)
        print("📖 HELP - CAESAR CIPHER")
        print("═" * 60)
        
        help_text = """
        What is Caesar Cipher?
        • A substitution cipher where each letter is shifted by a fixed number
        • Named after Julius Caesar who used it for military communications
        • One of the simplest and most widely known encryption techniques
        
        How it works:
        • Encryption: Each letter is shifted FORWARD in the alphabet
        • Decryption: Each letter is shifted BACKWARD in the alphabet
        • Only alphabetic characters are modified
        • Non-alphabetic characters remain unchanged
        
        Example:
        • Message: "HELLO" with shift 3
        • Encryption: "KHOOR" (H→K, E→H, L→O, L→O, O→R)
        • Decryption: "KHOOR" with shift 3 gives "HELLO"
        
        Security:
        • Very weak encryption - easily broken by brute force
        • Only 25 possible keys (shifts 1-25)
        • Mainly used for educational purposes
        """
        print(help_text)
    
    def main_menu(self):
        """
        Display main menu and handle user choices
        """
        while True:
            self.clear_screen()
            self.display_banner()
            
            print("\n" + "═" * 60)
            print("🎮 MAIN MENU")
            print("═" * 60)
            print("1. 🔒 Encrypt Message")
            print("2. 🔓 Decrypt Message")
            print("3. 🔍 Brute Force Decryption (Try all shifts)")
            print("4. 📖 Help & Information")
            print("5. 🚪 Exit")
            print("═" * 60)
            
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == '1':
                self.clear_screen()
                self.display_banner()
                self.encrypt_message()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                self.clear_screen()
                self.display_banner()
                self.decrypt_message()
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                self.clear_screen()
                self.display_banner()
                self.brute_force_decrypt()
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                self.clear_screen()
                self.display_banner()
                self.display_help()
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                print("\n" + "═" * 60)
                print("👋 Thank you for using CipherVault Pro!")
                print("🔒 Stay Secure! 🔒")
                print("═" * 60)
                time.sleep(2)
                break
            
            else:
                print("❌ Invalid choice! Please select 1-5.")
                time.sleep(1)

def main():
    """
    Main function to run the CipherVault Pro tool
    """
    try:
        tool = CipherVault()
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()