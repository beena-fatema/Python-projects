import pyqrcode
from pyqrcode import QRCode
s=input("Enter the link")
url=pyqrcode.create(s)
url.svg("My QRcode.svg",scale=10)