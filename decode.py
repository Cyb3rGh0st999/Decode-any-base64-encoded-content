import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import email
import base64
from email import policy
from email.parser import BytesParser

def open_file():
    # Let the user choose between .eml or .txt files
    file_path = filedialog.askopenfilename(filetypes=[("EML and Text files", "*.eml *.txt")])
    if not file_path:
        return
    try:
        # Check if it's an .eml or .txt file
        if file_path.endswith('.eml'):
            with open(file_path, 'rb') as f:
                msg = BytesParser(policy=policy.default).parse(f)
                output = parse_eml(msg)
        else:
            with open(file_path, 'r') as f:
                content = f.read()
                output = f"Original Text File Content:\n\n{content}"
        
        # Display the output in the GUI
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, output)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {str(e)}")

def parse_eml(msg):
    output = ""
    for part in msg.walk():
        content_type = part.get_content_type()
        original_content = part.get_payload(decode=False)
        
        if part.get_filename() and (content_type == 'application/xml' or content_type == 'text/xml'):
            filename = part.get_filename()
            output += f"\nFound XML file: {filename}\n"
            
            if part.get_content_transfer_encoding() == 'base64':
                # Decode the base64 content
                decoded_content = base64.b64decode(part.get_payload()).decode('utf-8')
                output += f"\nOriginal Content (Base64 Encoded):\n\n{original_content}\n"
                output += f"\nDecoded XML Content:\n\n{decoded_content}\n"
            else:
                # No need to decode, print the content directly
                output += f"\nOriginal XML Content:\n\n{part.get_payload(decode=True).decode('utf-8')}\n"
        else:
            if part.get_content_maintype() == 'text':  # Handles other text content in the email
                output += f"\nOriginal Email Body Content:\n\n{part.get_payload(decode=True).decode('utf-8')}\n"

    return output

def export_to_file():
    output = output_text.get(1.0, tk.END)
    if not output.strip():
        messagebox.showwarning("Warning", "No output to export!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as f:
                f.write(output)
            messagebox.showinfo("Success", f"Output exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export file: {str(e)}")

def create_gui():
    root = tk.Tk()
    root.title("EML and Text File Parser")

    tk.Label(root, text="Select an EML or Text file to parse:").pack(pady=10)
    tk.Button(root, text="Open File", command=open_file).pack(pady=5)

    global output_text
    output_text = scrolledtext.ScrolledText(root, width=80, height=25)
    output_text.pack(pady=10)

    tk.Button(root, text="Export Output to File", command=export_to_file).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
