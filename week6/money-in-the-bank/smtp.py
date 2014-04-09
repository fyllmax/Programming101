import smtplib


def send_email(email, random_hash):

    TO = email
    SUBJECT = 'bank acc password change code'
    MSG = 'You have asked to reset pass for your bank acc.\n You can do that by using the code bewlow. \nCode: {}'.format(
        random_hash)

    sender = 'xxx'
    sender_pass = 'xxx'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, sender_pass)

    BODY = '\r\n'.join([
        'To: {}'.format(TO),
        'From: {}'.format(sender),
        'Subject: {}'.format(SUBJECT),
        '',
        MSG])

    try:
        server.sendmail(sender, [TO], BODY)
        print('email sent')

    except:
        print('error occured')

    server.quit()
