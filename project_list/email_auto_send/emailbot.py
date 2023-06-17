import win32com.client as win32
from jinja2 import Template
import project1.customer_list as customer_list

for cus in customer_list.list():
    # Define the email subject and recipient
    subject = "Test Email"
    to = cus["email"]

    # Load the HTML template and render it with Jinja2
    template = Template(open("email_content.html").read())
    html_content = template.render(name=cus['name'])

    # Create a new Outlook email item
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject

    # Use the HTML body and send the email
    mail.HTMLBody = html_content
    mail.Send()