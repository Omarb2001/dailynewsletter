import smtplib
from email.message import EmailMessage
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Make the newsletter into a good template
def messenger(content: list, email_address='email'):
    email = MIMEMultipart()
    email['from'] = 'admin'
    email['to'] = email_address
    email['subject'] = f'Daily Newsletter! - {date.today()}'

    html = format_email(content)

    email.attach(MIMEText(html, 'html'))

    with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('email', 'pass')
        smtp.send_message(from_addr='email', msg=email)


def format_email(hn: list):
    html = """\
        <html>
          <body>
          """

    html_end = """</body>
        </html>
        """

    for story in hn:
        html += f'''
        <h1><b>{story['title']}</b></h1>
        <p>{story['summary']}</p>
        <small><i>Source: <a href={story['link']}>{story['link']}</a></i></small>
        '''

    return html + html_end