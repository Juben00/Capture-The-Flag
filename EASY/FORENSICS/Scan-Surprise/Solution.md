Download the file or connect to the ssh -p 57102 ctf-player@atlas.picoctf.net  6dd28e9b

In my case I downloaded the file challenge.zip

Extract the zip file using unzip challenge.zip > challenge

home/ctf-players/drop-in has been created where flag.png was stored

navigate to the file cd home/ctf-players/drop-in 

then get the value of the barcode image using zbar-tool

Command: zbarimg 'filename'

picoCTF{p33k_@_b00_a81f0a35}
