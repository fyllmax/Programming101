import smtplib


def send_email(email, random_hash):

    TO = email
    SUBJECT = 'bank acc password change code'
    MSG = 'You have asked to reset pass for your bank acc.\n You can do that by using the code bewlow. \nCode: {}'.format(
        random_hash)

    sender = 'xxxx'
    sender_pass = 'xxxx$'

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
        print('Sending email in process')

    except:
        print('error occured')

    server.quit()


def send_tan(email, tan_code):

    TO = email
    SUBJECT = 'Tan codes for bank transactions'
    MSG = 'Here are list of tan codes:\n {}'.format(
        '\n'.join(tan_code))

    sender = 'xxxx'
    sender_pass = 'xxxx'

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
        print('Sending email in process')

    except:
        print('error occured')

    server.quit()
