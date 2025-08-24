# w5hc_bot_cli.py
# W5HC Framework™ Interactive Bot
# © 2025 Biswajit Satapathy. W5HC Framework™ – Developed at CySec Guardians™. All rights reserved.

from fpdf import FPDF

def ask_question(prompt, follow_up=None):
    answer = input(prompt + " ")
    if follow_up and answer.strip().lower() in ['yes', 'y']:
        follow_answer = input(follow_up + " ")
        return answer, follow_answer
    return answer, None

def generate_pdf(responses, filename="W5HC_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "W5HC Framework™ Report", ln=True, align="C")
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)

    for key, value in responses.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, f"{key}:", ln=True)
        pdf.set_font("Arial", '', 12)
        if isinstance(value, tuple) and value[1]:
            pdf.multi_cell(0, 8, f"{value[0]} \nFollow-up: {value[1]}")
        else:
            pdf.multi_cell(0, 8, str(value))
        pdf.ln(2)

    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 6, "© 2025 Biswajit Satapathy. W5HC Framework™ – Developed at CySec Guardians™. All rights reserved.")
    pdf.output(filename)
    print(f"\nPDF report generated: {filename}")

def main():
    print("Welcome to the W5HC Framework™ Interactive Bot")
    print("Please answer the following questions:\n")
    
    responses = {}
    
    responses['What'] = ask_question("What is the issue?")
    responses['When'] = ask_question(
        "When did this issue occur?", 
        follow_up="Is this a new issue or has it occurred previously?"
    )
    responses['Change'] = ask_question(
        "Were there any recent changes, updates, or deployments?",
        follow_up="Please describe the changes made before the issue started."
    )
    responses['Who'] = ask_question(
        "Who is affected?",
        follow_up="Is it a single person, a group, or the entire organization?"
    )
    responses['Which'] = ask_question(
        "Which feature(s) or modules are affected?",
        follow_up="Is it isolated to one feature, multiple features, or the entire product?"
    )
    responses['How'] = ask_question("How should the feature(s) or product work?")
    responses['Why'] = ask_question("Why is the product/feature not working as expected?")

    generate_pdf(responses)

if __name__ == "__main__":
    main()

