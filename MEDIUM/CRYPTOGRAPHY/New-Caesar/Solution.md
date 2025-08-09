Download the file.

I edited the file and comment the original code. Here is the modified code:

def b16_decode(enc):
	plain = ""
	for i in range(0, len(enc), 2):
		binary = "{0:04b}{1:04b}".format(ALPHABET.index(enc[i]), ALPHABET.index(enc[i + 1]))
		plain += chr(int(binary, 2))
	return plain

enc_flag = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
for KEY in ALPHABET:
	dec = ''
	for c in enc_flag:
		dec += shift(c, KEY)
	decoded = b16_decode(dec)
	
	print(decoded)


FLAG: picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}