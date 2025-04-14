import tkinter as tk
from tkinter import ttk, messagebox

class CaesarCipherApp:
    def __init__(self, root):
        """Initialize the Caesar Cipher application with GUI components"""
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.root.configure(padx=20, pady=20)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface"""
        # Title
        title_label = ttk.Label(self.root, text="Caesar Cipher Encryption/Decryption", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input")
        input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Input text
        ttk.Label(input_frame, text="Enter Text:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.input_text = tk.Text(input_frame, width=50, height=5)
        self.input_text.grid(row=0, column=1, padx=5, pady=5)
        
        # Shift value
        ttk.Label(input_frame, text="Shift Value:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.shift_value = ttk.Spinbox(input_frame, from_=1, to=25, width=5)
        self.shift_value.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.shift_value.set(3)  # Default shift value
        
        # Buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Encrypt button
        self.encrypt_button = ttk.Button(button_frame, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=0, column=0, padx=5)
        
        # Decrypt button
        self.decrypt_button = ttk.Button(button_frame, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=0, column=1, padx=5)
        
        # Clear button
        self.clear_button = ttk.Button(button_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=2, padx=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(self.root, text="Output")
        output_frame.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Output text
        self.output_text = tk.Text(output_frame, width=50, height=5, state="disabled")
        self.output_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Status label
        self.status_label = ttk.Label(self.root, text="Status: Ready", font=("Arial", 10))
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5, sticky="w")
        
    def encrypt(self):
        """Encrypt the input text using Caesar cipher"""
        try:
            # Get input text and shift value
            text = self.input_text.get("1.0", "end-1c")
            if not text.strip():
                messagebox.showwarning("Warning", "Please enter text to encrypt")
                return
                
            try:
                shift = int(self.shift_value.get())
                if shift < 1 or shift > 25:
                    raise ValueError("Shift value must be between 1 and 25")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid shift value: {str(e)}")
                return
                
            # Perform encryption
            result = self.caesar_cipher(text, shift)
            
            # Display result
            self.set_output_text(result)
            self.set_status("Text encrypted successfully!")
            
        except Exception as e:
            self.set_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def decrypt(self):
        """Decrypt the input text using Caesar cipher"""
        try:
            # Get input text and shift value
            text = self.input_text.get("1.0", "end-1c")
            if not text.strip():
                messagebox.showwarning("Warning", "Please enter text to decrypt")
                return
                
            try:
                shift = int(self.shift_value.get())
                if shift < 1 or shift > 25:
                    raise ValueError("Shift value must be between 1 and 25")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid shift value: {str(e)}")
                return
                
            # Perform decryption (encrypt with negative shift)
            result = self.caesar_cipher(text, -shift)
            
            # Display result
            self.set_output_text(result)
            self.set_status("Text decrypted successfully!")
            
        except Exception as e:
            self.set_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def caesar_cipher(self, text, shift):
        """
        Apply Caesar cipher to the given text with the specified shift
        
        Args:
            text (str): The text to encrypt/decrypt
            shift (int): The shift value (positive for encryption, negative for decryption)
            
        Returns:
            str: The encrypted/decrypted text
        """
        result = ""
        
        for char in text:
            # Process alphabetic characters
            if char.isalpha():
                # Determine ASCII offset based on case
                ascii_offset = ord('A') if char.isupper() else ord('a')
                
                # Apply shift and wrap around the alphabet (26 letters)
                # (char_code - ascii_offset + shift) % 26 + ascii_offset
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                
                result += shifted_char
            else:
                # Preserve non-alphabetic characters
                result += char
                
        return result
            
    def clear(self):
        """Clear input and output fields"""
        self.input_text.delete("1.0", tk.END)
        self.shift_value.set(3)
        self.set_output_text("")
        self.set_status("Status: Ready")
        
    def set_output_text(self, text):
        """Set the output text field with the given text"""
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.configure(state="disabled")
        
    def set_status(self, status):
        """Set the status label with the given status"""
        self.status_label.configure(text=f"Status: {status}")


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

