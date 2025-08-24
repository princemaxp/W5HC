# w5hc_bot_gui.py
# W5HC Framework™ GUI Bot – Fully Updated
# © 2025 Biswajit Satapathy. W5HC Framework™ – Developed at CySec Guardians™. All rights reserved.

import tkinter as tk
from tkinter import messagebox, filedialog
from fpdf import FPDF

class W5HCBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("W5HC Framework™ Interactive Bot")
        self.responses = {}
        self.current_question = 0

        self.questions = [
            ("What", "What is the issue?"),
            ("When", "When did this issue occur?", "Is this a new issue or has it occurred previously?"),
            ("Change", "Were there any recent changes, updates, or deployments?", "Please describe the changes made before the issue started."),
            ("Who", "Who is affected?", "Is it a single person, a group, or the entire organization?"),
            ("Which", "Which feature(s) or modules are affected?", "Is it isolated to one feature, multiple features, or the entire product?"),
            ("How", "How should the feature(s) or product work?"),
            ("Why", "Why is the product/feature not working as expected?")
        ]

        self.label = tk.Label(root, text="", wraplength=500, font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.followup_label = None
        self.followup_entry = None

        self.show_question()

    def show_question(self):
        key, question = self.questions[self.current_question][:2]
        self.label.config(text=question)
        self.entry.delete(0, tk.END)

        # Remove previous follow-up widgets if exist
        if self.followup_label:
            self.followup_label.destroy()
            self.followup_entry.destroy()
            self.followup_label = None
            self.followup_entry = None

    def next_question(self):
        key, question = self.questions[self.current_question][:2]
        followup = self.questions[self.current_question][2] if len(self.questions[self.current_question]) > 2 else None
        answer = self.entry.get().strip()
        if not answer:
            messagebox.showwarning("Input Required", "Please enter a response before proceeding.")
            return

        # Handle conditional follow-up
        if followup and answer.lower() in ['yes', 'y']:
            if not self.followup_label:
                self.followup_label = tk.Label(self.root, text=followup, wraplength=500, font=("Arial", 12))
                self.followup_label.pack(pady=5)
                self.followup_entry = tk.Entry(self.root, width=60)
                self.followup_entry.pack(pady=5)
                self.entry.delete(0, tk.END)
                return
            else:
                follow_answer = self.followup_entry.get().strip()
                self.responses[key] = (answer, follow_answer)
        else:
            self.responses[key] = (answer, None)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.generate_pdf()

    def generate_pdf(self):
        # Ask user where to save the PDF
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save your W5HC Report"
        )
        if not file_path:
            messagebox.showinfo("Cancelled", "PDF generation cancelled.")
            self.root.destroy()
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "W5HC Framework™ Report", ln=True, align="C")
        pdf.set_font("Arial", '', 12)
        pdf.ln(10)

        for key, value in self.responses.items():
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, f"{key}:", ln=True)
            pdf.set_font("Arial", '', 12)
            if value[1]:
                pdf.multi_cell(0, 8, f"{value[0]} \nFollow-up: {value[1]}")
            else:
                pdf.multi_cell(0, 8, str(value[0]))
            pdf.ln(2)

        pdf.ln(10)
        pdf.set_font("Arial", 'I', 10)
        pdf.multi_cell(0, 6, "© 2025 Biswajit Satapathy. W5HC Framework™ – Developed at CySec Guardians™. All rights reserved.")

        try:
            pdf.output(str(file_path))
            messagebox.showinfo("Completed", f"PDF report successfully saved:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF:\n{e}")

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = W5HCBotGUI(root)
    root.mainloop()
