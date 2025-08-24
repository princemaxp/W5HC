W5HC Framework™

A structured approach for Support Teams to analyze, document, and resolve issues effectively.

📌 About

The W5HC Framework™ is designed by Biswajit Satapathy to bring clarity and consistency in technical support and incident analysis.
It uses the W5HC method (What, When, Change, Who, Which, How, Why) to structure information, ensuring:

Faster root cause analysis (RCA)

Better Jira/issue ticket documentation

A reusable format for reports

This repository hosts an open-source bot-style tool that guides users through the W5HC framework interactively.
The tool asks only the necessary questions, generates a structured summary, and exports it as a PDF RCA report.

🎯 Features

Interactive GUI-based bot

Step-by-step questioning using W5HC

Follow-up questions only when required

Automatic PDF report generation

Can be used for RCA reports, Jira tickets, or case documentation

🗂️ Structure

/docs → Diagrams, framework explanation, articles

/src → Source code (Python GUI bot)
- CLI-based interactive bot (w5hc_bot_cli.py)
- GUI-based interactive bot (w5hc_bot_gui.py)

Requirements

Python 3.x installed
Required Python packages: pip install -r requirements.txt


📜 License

W5HC Framework™ is proprietary software.  

- ✅ Free for internal organizational use.  
- ❌ Redistribution, resale, or sublicensing is **not permitted** without prior written consent.  
- ✅ Organizations may modify the software internally for their own use.  
- ❌ Modified versions may not be shared or published externally.  

For commercial licensing or redistribution rights, please contact:  
**Biswajit Satapathy** – [your email/contact link here]

See the [LICENSE](./LICENSE.txt) file for full details.
