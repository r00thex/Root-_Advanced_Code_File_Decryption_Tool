import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import base64
import re
import html
import urllib.parse
import binascii
import os
import zlib
import codecs
import webbrowser

class AdvancedDecryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Root_hex- Advanced Code & File Decryption Tool")
        self.root.geometry("1100x750")
        self.root.configure(bg='#0a0a0a')
        
        # Set hacker theme colors
        self.bg_color = '#0a0a0a'
        self.fg_color = '#00ff00'
        self.accent_color = '#00ffff'
        self.warning_color = '#ff0000'
        self.text_bg = '#111111'
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header with branding
        header_frame = tk.Frame(main_container, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(
            header_frame, 
            text="ChowdhuryVai", 
            font=("Courier", 20, "bold"),
            fg=self.fg_color,
            bg=self.bg_color
        )
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Advanced Code & File Decryption Tool", 
            font=("Courier", 10),
            fg=self.accent_color,
            bg=self.bg_color
        )
        subtitle_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Contact information
        contact_frame = tk.Frame(main_container, bg=self.bg_color)
        contact_frame.pack(fill=tk.X, pady=(0, 10))
        
        telegram_info = [
            ("Telegram ID: @roothexh", "https://t.me/roothexh"),
            ("Telegram Channel: @TEAM_BD_DARK_FOREF","https://t.me/TEAM_BD_DARK_FOREF")
             ]
        
        for text, url in telegram_info:
            link_label = tk.Label(
                contact_frame,
                text=text,
                font=("Courier", 9),
                fg=self.accent_color,
                bg=self.bg_color,
                cursor="hand2"
            )
            link_label.pack(side=tk.LEFT, padx=(0, 20))
            link_label.bind("<Button-1>", lambda e, u=url: self.open_url(u))
        
        # Input section
        input_frame = tk.LabelFrame(main_container, text="Input Encrypted Code/File", 
                                   font=("Courier", 11, "bold"),
                                   fg=self.fg_color, bg=self.bg_color,
                                   bd=1, relief=tk.GROOVE)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # File selection frame
        file_frame = tk.Frame(input_frame, bg=self.bg_color)
        file_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.file_path = tk.StringVar()
        file_entry = tk.Entry(
            file_frame,
            textvariable=self.file_path,
            font=("Courier", 9),
            bg=self.text_bg,
            fg=self.fg_color,
            width=60
        )
        file_entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        
        browse_btn = tk.Button(
            file_frame,
            text="BROWSE",
            font=("Courier", 8),
            bg='#003300',
            fg=self.fg_color,
            command=self.browse_file,
            cursor="hand2"
        )
        browse_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        load_btn = tk.Button(
            file_frame,
            text="LOAD FILE",
            font=("Courier", 8),
            bg='#003300',
            fg=self.fg_color,
            command=self.load_file,
            cursor="hand2"
        )
        load_btn.pack(side=tk.LEFT)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame, 
            height=8,
            font=("Courier", 10),
            bg=self.text_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            wrap=tk.WORD
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Control panel
        control_frame = tk.Frame(main_container, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=10)
        
        # Left side - Code type selection
        left_control = tk.Frame(control_frame, bg=self.bg_color)
        left_control.pack(side=tk.LEFT)
        
        type_label = tk.Label(
            left_control,
            text="Decryption Type:",
            font=("Courier", 9),
            fg=self.fg_color,
            bg=self.bg_color
        )
        type_label.pack(side=tk.LEFT)
        
        self.code_type = tk.StringVar(value="Auto Detect")
        type_combo = ttk.Combobox(
            left_control,
            textvariable=self.code_type,
            values=[
                "Auto Detect", "Base64", "Base64 File", "URL Encoded", 
                "Hex Encoded", "HTML Entities", "ROT13", "Binary"
            ],
            state="readonly",
            width=15,
            height=10
        )
        type_combo.pack(side=tk.LEFT, padx=5)
        
        # Right side - Buttons
        right_control = tk.Frame(control_frame, bg=self.bg_color)
        right_control.pack(side=tk.RIGHT)
        
        decrypt_btn = tk.Button(
            right_control,
            text="DECRYPT CODE",
            font=("Courier", 10, "bold"),
            bg='#003300',
            fg=self.fg_color,
            command=self.decrypt_code,
            cursor="hand2"
        )
        decrypt_btn.pack(side=tk.LEFT, padx=5)
        
        decrypt_file_btn = tk.Button(
            right_control,
            text="DECRYPT FILE",
            font=("Courier", 10, "bold"),
            bg='#330033',
            fg=self.accent_color,
            command=self.decrypt_file,
            cursor="hand2"
        )
        decrypt_file_btn.pack(side=tk.LEFT, padx=5)
        
        save_btn = tk.Button(
            right_control,
            text="SAVE OUTPUT",
            font=("Courier", 9),
            bg='#003333',
            fg=self.accent_color,
            command=self.save_output,
            cursor="hand2"
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            right_control,
            text="CLEAR ALL",
            font=("Courier", 9),
            bg='#330000',
            fg=self.warning_color,
            command=self.clear_all,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Output section
        output_frame = tk.LabelFrame(main_container, text="Decrypted Output", 
                                    font=("Courier", 11, "bold"),
                                    fg=self.fg_color, bg=self.bg_color,
                                    bd=1, relief=tk.GROOVE)
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame, 
            height=10,
            font=("Courier", 10),
            bg=self.text_bg,
            fg=self.accent_color,
            insertbackground=self.accent_color,
            wrap=tk.WORD
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter encrypted code or select file to decrypt")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Courier", 8),
            fg=self.fg_color,
            bg=self.bg_color,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def open_url(self, url):
        webbrowser.open_new(url)
        
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select file to decrypt",
            filetypes=[
                ("All files", "*.*"),
                ("Text files", "*.txt"),
                ("Web files", "*.html;*.htm;*.css;*.js;*.php"),
                ("Encoded files", "*.enc;*.base64;*.hex")
            ]
        )
        if filename:
            self.file_path.set(filename)
            
    def load_file(self):
        filename = self.file_path.get()
        if not filename or not os.path.exists(filename):
            messagebox.showerror("File Error", "Please select a valid file")
            return
            
        try:
            # Try to read as text first
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(1.0, content)
                self.status_var.set(f"File loaded: {os.path.basename(filename)}")
        except:
            # If text reading fails, try binary
            try:
                with open(filename, 'rb') as file:
                    content = file.read()
                    # Try to decode as text
                    try:
                        text_content = content.decode('utf-8', errors='replace')
                        self.input_text.delete(1.0, tk.END)
                        self.input_text.insert(1.0, text_content)
                    except:
                        # Display as hex
                        hex_content = content.hex()
                        self.input_text.delete(1.0, tk.END)
                        self.input_text.insert(1.0, hex_content)
                self.status_var.set(f"Binary file loaded: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("File Error", f"Could not read file: {str(e)}")
        
    def clear_all(self):
        self.input_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.file_path.set("")
        self.status_var.set("Cleared - Ready for new input")
        
    def detect_code_type(self, code):
        if not code or not code.strip():
            return "Auto Detect"
            
        code = code.strip()
        
        # Check for Base64
        base64_pattern = code.replace('\n', '').replace(' ', '').replace('\r', '')
        if (len(base64_pattern) % 4 == 0 and 
            re.match(r'^[A-Za-z0-9+/]*={0,2}$', base64_pattern)):
            try:
                base64.b64decode(base64_pattern)
                return "Base64"
            except:
                pass
            
        # Check for URL encoding
        if '%' in code and len(code) > 3:
            url_pattern = re.findall(r'%[0-9A-Fa-f]{2}', code)
            if len(url_pattern) > len(code) * 0.1:  # At least 10% URL encoded chars
                return "URL Encoded"
            
        # Check for Hex encoding
        hex_pattern = code.replace(' ', '').replace('\n', '').replace('\r', '').replace(':', '')
        if (re.match(r'^[0-9A-Fa-f]+$', hex_pattern) and 
            len(hex_pattern) % 2 == 0 and len(hex_pattern) >= 4):
            return "Hex Encoded"
            
        # Check for HTML entities
        if '&' in code and any(entity in code for entity in ['&amp;', '&lt;', '&gt;', '&quot;', '&#']):
            return "HTML Entities"
            
        # Check for ROT13
        if re.match(r'^[A-Za-z\s]+$', code) and len(code) > 10:
            return "ROT13"
            
        # Check for Binary
        binary_pattern = code.replace(' ', '').replace('\n', '').replace('\r', '')
        if (re.match(r'^[01]+$', binary_pattern) and 
            len(binary_pattern) % 8 == 0 and len(binary_pattern) >= 8):
            return "Binary"
            
        return "Auto Detect"
        
    def decrypt_code(self):
        input_code = self.input_text.get(1.0, tk.END).strip()
        if not input_code:
            messagebox.showwarning("Input Error", "Please enter code to decrypt or load a file")
            return
            
        code_type = self.code_type.get()
        if code_type == "Auto Detect":
            detected_type = self.detect_code_type(input_code)
            if detected_type != "Auto Detect":
                code_type = detected_type
            else:
                code_type = "Base64"  # Default fallback
        
        self.status_var.set(f"Decrypting {code_type}...")
        self.root.update_idletasks()
        
        try:
            result = self.perform_decryption(input_code, code_type)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            self.status_var.set(f"Successfully decrypted {code_type} code")
            
        except Exception as e:
            error_msg = f"Error during decryption: {str(e)}"
            self.status_var.set(error_msg)
            messagebox.showerror("Decryption Error", error_msg)
            
    def perform_decryption(self, code, code_type):
        if code_type == "Base64":
            return self.decode_base64(code)
        elif code_type == "Base64 File":
            return self.decode_base64_file(code)
        elif code_type == "URL Encoded":
            return self.decode_url(code)
        elif code_type == "Hex Encoded":
            return self.decode_hex(code)
        elif code_type == "HTML Entities":
            return self.decode_html_entities(code)
        elif code_type == "ROT13":
            return self.decode_rot13(code)
        elif code_type == "Binary":
            return self.decode_binary(code)
        else:
            return self.auto_decode(code)
                
    def decode_base64(self, code):
        try:
            # Clean the code
            clean_code = code.replace('\n', '').replace(' ', '').replace('\r', '')
            # Add padding if needed
            padding = 4 - (len(clean_code) % 4)
            if padding != 4:
                clean_code += '=' * padding
                
            decoded = base64.b64decode(clean_code)
            return decoded.decode('utf-8', errors='replace')
        except Exception as e:
            raise Exception(f"Base64 decoding failed: {str(e)}")
                
    def decode_base64_file(self, code):
        try:
            decoded = base64.b64decode(code)
            return f"Binary file decoded successfully!\nSize: {len(decoded)} bytes\n\nFirst 500 bytes as text:\n{decoded[:500].decode('utf-8', errors='replace')}"
        except Exception as e:
            raise Exception(f"Base64 file decoding failed: {str(e)}")
                
    def decode_url(self, code):
        try:
            return urllib.parse.unquote(code)
        except Exception as e:
            raise Exception(f"URL decoding failed: {str(e)}")
            
    def decode_hex(self, code):
        try:
            hex_string = code.replace(' ', '').replace('\n', '').replace('\r', '').replace(':', '')
            if len(hex_string) % 2 != 0:
                hex_string = '0' + hex_string  # Add leading zero if odd length
            decoded = binascii.unhexlify(hex_string)
            return decoded.decode('utf-8', errors='replace')
        except Exception as e:
            raise Exception(f"Hex decoding failed: {str(e)}")
            
    def decode_html_entities(self, code):
        try:
            return html.unescape(code)
        except Exception as e:
            raise Exception(f"HTML entities decoding failed: {str(e)}")
            
    def decode_rot13(self, code):
        try:
            return code.translate(str.maketrans(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
            ))
        except Exception as e:
            raise Exception(f"ROT13 decoding failed: {str(e)}")
            
    def decode_binary(self, code):
        try:
            binary_string = code.replace(' ', '').replace('\n', '')
            # Ensure binary string length is multiple of 8
            if len(binary_string) % 8 != 0:
                binary_string = binary_string[:-(len(binary_string) % 8)]
            
            text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
            return text
        except Exception as e:
            raise Exception(f"Binary decoding failed: {str(e)}")
            
    def auto_decode(self, code):
        # Try multiple decoding methods
        methods = [
            ("HTML Entities", self.decode_html_entities),
            ("URL Encoded", self.decode_url),
            ("Base64", self.decode_base64)
        ]
        
        for name, method in methods:
            try:
                result = method(code)
                if result != code and len(result) > 0:
                    return f"Auto-detected as {name}:\n\n{result}"
            except:
                continue
                
        return "Could not auto-detect encoding type. Please select manually."
            
    def decrypt_file(self):
        filename = self.file_path.get()
        if not filename or not os.path.exists(filename):
            messagebox.showerror("File Error", "Please select a valid file to decrypt")
            return
            
        code_type = self.code_type.get()
        if code_type == "Auto Detect":
            # Read file content to detect type
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(1000)  # Read first 1000 chars for detection
                detected_type = self.detect_code_type(content)
                code_type = detected_type if detected_type != "Auto Detect" else "Base64"
            except:
                code_type = "Base64"
        
        self.status_var.set(f"Decrypting file as {code_type}...")
        self.root.update_idletasks()
        
        try:
            with open(filename, 'rb') as file:
                file_content = file.read()
                
            if code_type == "Base64":
                decoded = base64.b64decode(file_content)
                result = decoded.decode('utf-8', errors='replace')
            elif code_type == "Hex Encoded":
                hex_string = file_content.decode('utf-8', errors='ignore').strip()
                decoded = binascii.unhexlify(hex_string.replace(' ', '').replace('\n', ''))
                result = decoded.decode('utf-8', errors='replace')
            else:
                # Try to decode as text
                try:
                    text_content = file_content.decode('utf-8')
                    result = self.perform_decryption(text_content, code_type)
                except:
                    result = f"Binary file - {len(file_content)} bytes\nUse Base64 or Hex decoding for binary files."
            
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            
            # Ask to save
            if messagebox.askyesno("Save File", "Do you want to save the decrypted output?"):
                self.save_output()
            else:
                self.status_var.set(f"File successfully decrypted as {code_type}")
                
        except Exception as e:
            error_msg = f"Error during file decryption: {str(e)}"
            self.status_var.set(error_msg)
            messagebox.showerror("File Decryption Error", error_msg)
        
    def save_output(self):
        output_content = self.output_text.get(1.0, tk.END).strip()
        if not output_content:
            messagebox.showwarning("Output Error", "No output to save")
            return
            
        filename = filedialog.asksaveasfilename(
            title="Save decrypted output",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
      if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(output_content)
                self.status_var.set(f"Output saved: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file: {str(e)}")

def main():
    try:
        root = tk.Tk()
        app = AdvancedDecryptionTool(root)
        root.mainloop()
    except Exception as e:
        print(f"Application error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
