import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import json
import smtplib
from email.mime.text import MIMEText


class Dcmr():
    def __init__(self, file_path, host_address):
        self.parts = []
        data = open(file_path, 'r')
        self.cmr_file = json.load(data)
        self.host = open(host_address).read()

    def get_keys(self):
        keys = []
        for i in self.parts:
            key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 512)
            uid = pgpy.PGPUID.new(i[0], comment=i[1], email=i[2])
            key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                        hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
                        ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
                        compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP,
                                     CompressionAlgorithm.Uncompressed])
            keys.append(key)
        self.parts = list(zip(self.parts, keys))

    def keys_out(self):
        for i in self.parts:
            print(i)
            if not i == self.parts[0]:
                mail = MIMEText(str(i[1]))
                mail['Subject'] = 'Your private key to CMR waybill no. %s' % self.cmr_file[0]
                mail['From'] = self.parts[0][0]
                mail['To'] = i[0]
                s = smtplib.SMTP(self.host)
                s.starttls()
                s.login(self.parts[0][0], '57tiGEr175')
                s.send_message(mail)
                s.quit()

    def signing(self, signer, file_path):
        message = pgpy.PGPMessage.new(file_path, file=True)
        message |= signer.sign(message)
        return message

    def export_pgp_msg(self, msg):
        output = open("sender_pgp_msg.txt", "w")
        output.write(str(msg))

    def update_block(self):
        #by ChainSign
        pass

    def let_send(self):
        self.load_data()
        self.get_keys()
        signed_msg = self.signing(self.parts[0][1], "ecmr.json")
        self.keys_out()
        self.export_pgp_msg(signed_msg)
        self.update_block()

    def load_data(self):
        adresses = [1, 2, 16]
        for i in adresses:
            self.parts.append(self.cmr_file[i][2])


c = Dcmr('ecmr.json', 'smtp.txt')
c.let_send()
