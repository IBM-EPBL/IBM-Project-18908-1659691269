import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(
    from_email="sit19cs023@sairamtap.edu.in",
    to_emails="receiver@gmail.com",
    subject="test",
    html_content="<p>hi</hi>"
)

try:
    sg = SendGridAPIClient("XXXX API key XXXXXX")
    response = sg.send(message)
except Exception as e:
    print(e)
