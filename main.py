import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Load data from JSON file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create PDF with zero margins
pdf_file = "output.pdf"
pdf = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
elements = []

# Get the default style
styles = getSampleStyleSheet()
normal_style = styles["BodyText"]

# Extract relevant information and add it to the PDF
for vault_id, vault_content in data["vaults"].items():
    for item in vault_content["items"]:
        service_name = item["data"]["metadata"].get("name", "N/A")
        email = item["data"]["content"].get("itemEmail", "N/A")
        password = item["data"]["content"].get("password", "N/A")
        url = item["data"]["content"].get("urls", ["N/A"])[0] if item["data"]["content"].get("urls") else "N/A"

        # Create a formatted text string for each account without line breaks
        account_info = (
            f"Service: {service_name}\n"
            f"Username/Email: {email}\n"
            f"Password: {password}\n"
            f"URL: {url}\n"
        )
        
        # Add the account info as a single Paragraph
        elements.append(Paragraph(account_info.replace('\n', '<br/>'), normal_style))
        # Add a small space after each account using a blank line
        elements.append(Paragraph("<br/>", normal_style))  # This creates a line break

# Build the PDF
pdf.build(elements)

print(f"PDF generated successfully as '{pdf_file}'")

