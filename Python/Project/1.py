import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(data,pdf_filename = "candidate_registration.pdf"):
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    c.drawString(100, 750, "Candidate Registration Details")
    y = 720
    for key, value in data.items():
        text = f"{key}: {value}"
        c.drawString(100, y, text)
        y -= 20
    c.save()
    messagebox.showinfo("Success", "PDF generated successfully!")

def validate_data(data):
    for key, value in data.items():
        if not value:
            messagebox.showerror("Error", f"Please fill in {key} field.")
            return False
    if "@gmail.com" not in data['Email Id']:
        messagebox.showerror("Error","Please fill correct Email id.")
        return False
    if data['Phone NO'].isalpha():
        messagebox.showerror("Error","Please fill correct Phone no.")
        return False
    if len(data['Phone NO'])!= 10:
        messagebox.showerror("Error","Please fill 10 digit Phone no.")
        return False
    return True

def submit_form():
    candidate_data = {
        "Name": Name_entry.get(),
        "AICTE Id": AicteId_entry.get(),
        "Email Id": Email_entry.get(),
        "Phone NO": PhoneNo_entry.get(),
        "College Name": CollegeName_entry.get()
    }

    if validate_data(candidate_data):
        generate_pdf(candidate_data)
        

root = tk.Tk()
root.title("Candidate Registration Form")

Name_label = tk.Label(root, text="Name:")
Name_label.grid(row=0, column=0, padx=10, pady=5)
Name_entry = tk.Entry(root)
Name_entry.grid(row=0, column=1, padx=10, pady=5)


AicteId_label = tk.Label(root, text="AICTE ID:")
AicteId_label.grid(row=1, column=0, padx=10, pady=5)
AicteId_entry = tk.Entry(root)
AicteId_entry.grid(row=1, column=1, padx=10, pady=5)

Email_label = tk.Label(root, text="Email:")
Email_label.grid(row=2, column=0, padx=10, pady=5)
Email_entry = tk.Entry(root)
Email_entry.grid(row=2, column=1, padx=10, pady=5)

PhoneNo_label = tk.Label(root, text="Phone No:")
PhoneNo_label.grid(row=3, column=0, padx=10, pady=5)
PhoneNo_entry = tk.Entry(root)
PhoneNo_entry.grid(row=3, column=1, padx=10, pady=5)

CollegeName_label = tk.Label(root, text="College Name:")
CollegeName_label.grid(row=4, column=0, padx=10, pady=5)
CollegeName_entry = tk.Entry(root)
CollegeName_entry.grid(row=4, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()