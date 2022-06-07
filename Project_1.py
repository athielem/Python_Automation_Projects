import re
import smtplib
from datetime import date, datetime
from email.message import EmailMessage
from urllib.request import urlopen

<<<<<<< HEAD
while True:
=======
status_variable = True
while status_variable:
>>>>>>> 7a781f8088dfc039fa37c27c62c5ba2bf382c3fa

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    if (current_time == '08:00:00') and (date.today().weekday() in [0, 1, 2, 3, 4]):

        str_date = str(date.today())
        str_regex = r'(?<={}/).*?/'.format(str_date)

        day = str_date[-2:]
        month = str_date[-5:-3]
        year = str_date[:4]
        str_date_eu = '{}.{}.{}'.format(day, month, year)

        with urlopen('https://versicherungswirtschaft-heute.de/') as response:
            body = response.read()

        decoded_body = body.decode("utf-8")

        result = re.findall(str_regex, decoded_body)
        result = set(result)

        dict_result = {}
        for count, article in enumerate(result):
            dict_result['Article {}'.format(count + 1)] = ' '.join(article.split('-')).upper().strip('/') + '.'

        article_string = ''
        for article in dict_result:
            article_string = article_string + '<p>{}</p>'.format(dict_result[article])

        html_str = '''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="padding:20px 0px">
                    <div style="height: 1000px;width:600px">
                        <div style="text-align:center;">
                            <h3>www.versicherungswirtschaft-heute.de</h3>
                            {}
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''.format(article_string)

        EMAIL_ADDRESS = ''
        EMAIL_PASSWORD = ''

        msg = EmailMessage()
        msg['Subject'] = 'Artikel vom {}'.format(str_date_eu)
<<<<<<< HEAD
        msg['To'] = '' 
        msg.set_content(html_str, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
=======
        msg['To'] = 'andreas.thiele@outlook.com' 
        msg.set_content(html_str, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
>>>>>>> 7a781f8088dfc039fa37c27c62c5ba2bf382c3fa
            smtp.send_message(msg)

    else:
        pass