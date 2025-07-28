View the metadata of the png file using exiftool
Strings clue was given:
Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.x
->
CHECKLSB = Least significant bit
also hint was given saying: Red?Ged?Bed?Aed? (a color pattern to extract lsb RGBA)

Solution go to cyberchef and extract the lsb from the image:

it will give repeating: cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==

which is a base64 text

convert the text from base64.

picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

