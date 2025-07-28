Connect to: ssh -p 63197 ctf-player@rhea.picoctf.net
Use the password: 6dd28e9b

view the content of the checksum.txt: cat checksum.txt
create a SHA checksum of file and grep for the value of the checksum.txt

Command: cat checksum.txt VALUE: 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
Command: sha256sum files/* -> creates a SHA checksum for all the files in the files directory
Command: grep 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8

OR basically: sha256sum files/* | grep 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
RESPOND: 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8  files/00011a60

user the given decryption script in the root:

Command: ./decrypt.sh files/00011a60

FLAG: picoCTF{trust_but_verify_00011a60}
