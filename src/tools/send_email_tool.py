import os
import resend
from dotenv import load_dotenv
from agents import function_tool

load_dotenv()
resend_api_key = os.getenv("RESEND_API_KEY")
from_email = os.getenv("RESEND_FROM_EMAIL", "onboarding@resend.dev")
to_email = os.getenv("RESEND_TO_EMAIL")

if not resend_api_key:
    raise ValueError("RESEND_API_KEY not found in environment variables.")
elif not to_email:
    raise ValueError("TO_EMAIL not found in environment variables.")


@function_tool
def send_email(subject: str, html_body: str) -> dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    resend.api_key = resend_api_key

    r = resend.Emails.send({
        "from": from_email,
        "to": to_email,
        "subject": subject,
        "html": html_body
    })
    return {"status": "success"}