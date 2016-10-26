
import sys

from PyQt5.QtWidgets import QApplication, QLabel

import cryptography.fernet


def main():

    app = QApplication([])

    if len(sys.argv) >= 2:
        status_file_path = sys.argv[1]
    else:
        status_file_path = 'spafit_status.txt'

    m = b'does this work?'
    s = 'original message:\n' + str(m) + '\n\n'

    k = cryptography.fernet.Fernet.generate_key()
    fernet = cryptography.fernet.Fernet(k)
    t = fernet.encrypt(m)
    d = fernet.decrypt(t)
    s += 'key:\n' + str(k) + '\n\n'
    s += 'token:\n' + str(t) + '\n\n'
    s += 'decoded message:\n' + str(d)

    window = QLabel(s)
    window.show()

    app.exec_()

    with open(status_file_path, 'w') as f:
        f.write('PASS\n')

if __name__ == '__main__':

    main()
