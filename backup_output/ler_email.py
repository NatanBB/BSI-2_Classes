import imaplib
import email

#E-mail de teste

FROM_EMAIL = "joaosilvapires3@gmail.com"
PWD = "SenhaGmail_5@"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORTA = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, PWD)
mail.select('inbox')
assunto = 'backup efeutado com sucesso'
type_mail, data = mail.search(None, 'SUBJECT {}'.format(assunto))
print(type_mail, data)