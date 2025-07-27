Download the python script to review the code.

as we can see the input wasnt sanitize in this part:

elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])


therefore we have to utilize this and bypass by entering ";" followed by RETURNING a line in the song_flag_hunters

song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN
....


we can see that the flag was imported and stored in the scret_intro 

to display this we have to return the index of the secret_intro


the final command is ;RETURN 0

flag: picoCTF{70637h3r_f0r3v3r_509142d4}
