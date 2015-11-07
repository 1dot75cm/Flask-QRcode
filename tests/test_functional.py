# coding=utf-8
import unittest
from flask_qrcode import qrcode


class BasicTestCase(unittest.TestCase):


    def test_create_qrcode(self):

        new_qr = qrcode('Test Data')
        self.assertIn('data:image/png;base64,', new_qr)


    def test_qrcode_encodes_string_right(self):

        new_qr = qrcode('Test Data')
        self.assertEqual('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANIAAADSAQAAAAAX4qPvAAABLUlEQVR4nOWYQW7EIAxFnwtSlxxhjkKu3BskR5kDVCLLkYh+F0DaTbfBmngRkbzNk2WCDfQIIhdojxYf/B/vziBLkkqQVKCvJPnynMB2M1sAs0dtH80sznFxyoJs8eLih+VymFYfLrNZhCRgB20Glr9Ac1w8sTOCyGUcSnNcPLGocyl4WS8fgM2T55x6kUoY6UgSEO5+TkslyOxRkcpkF0cMraPV1Qr05k51gosnRk9J2z1nSlJFqyfP6+tF0jiFkkbl3D4vEQCBMDii2EM1Epgrz4n9S2t1s+p49eR5PevzNEBSS45WDvPmeTkb8zTsEVv2SOt8vXleyuLv0kjfNv4vL5Mrz7ms3zNIz8+b18uf+zpyCdKapN7OePK8fh9tBkAA0rivy89Ydeu58Qd0j6Vi20PbhwAAAABJRU5ErkJggg==', new_qr)


    def test_qrcode_changes_with_diff_data(self):

        qr1 = qrcode('Test Data')
        qr2 = qrcode('Test Data 2')
        self.assertNotEqual(qr1, qr2)


    def test_qrcode_encodes_integer_right(self):

        int_qr = qrcode(1)
        self.assertEqual('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANIAAADSAQAAAAAX4qPvAAABMUlEQVR4nO2YMW7EIBBF3yz0RMoBchR85dwAHyU3gHIlVj8F2NkmbRitM4WFeM2TNXj8gVlB5ArjMerG7/XqDLIkqQZJFeZKki/PBayZ2QaYffSxaWZxjYtTFmSbFxc/LNeHqfhwWc0iJAENtBtY/gStcfHEzgoi12MorXHxxKLOpeBus30Adk+ea/pFquF4HUkCwsXnNCoEkaWzcYJUkqTiyXMFexg0M5XUkdSBFrHNm+dfMiB1VFIfEUCqwGgaT55Lvruy/BUBQrdcehTtfYGLJ4bOGp2jGjRO1KX75WazIiotYlu62yoXRyySCzAOTqpjcx4rT54L2JGngTNKJ+na8yj+LA0M0d5gN9Cl/3efWZbGPcP/vRRP93XMX91+xAJPnmvyEWeeVkkaseDac/ob5Tmlv4TEYpYAAAAASUVORK5CYII=', int_qr)

if __name__ == '__main__':
    unittest.main()
