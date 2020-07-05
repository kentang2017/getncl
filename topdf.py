import img2pdf
import os

dirname = "/大六壬銀河棹/"
with open("大六壬銀河棹.pdf","wb") as f:
	imgs = []
	for fname in os.listdir(dirname):
		if not fname.endswith(".jpg"):
			continue
		path = os.path.join(dirname, fname)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	f.write(img2pdf.convert(imgs))