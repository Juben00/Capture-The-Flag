* Download the file
  wget https://artifacts.picoctf.net/c\_titan/111/enc\_flag
  
* use cat "file\_name" to view the content of the file
  
* YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
* upon observation we can see that it uses base64 encryption
* use cyberchef to decrypt the text
* b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='
* take d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ== and decrypt it again in base64
* and we get wpjvJAM{jhlzhy\_k3jy9wa3k\_890k2379}
* the text is now encrypted with CAESAR CIPHER



&nbsp;	picoCTF{caesar\_d3cr9pt3d\_890d2379}

