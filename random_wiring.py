import random;
import sys;

print('This program will output a randomly wired whirlenig Enigma(tm)-like machine');
print('"Pick a random passphrase to generate your unique wiring.');
print('Running it again with the same passphrase will generate the same wiring.');
print();
passphrase = input('Enter a passphrase: ');
random.seed(passphrase,version=2);

rotor1=list(range(0,72));
random.shuffle(rotor1);
rotor2=list(range(0,72));
random.shuffle(rotor2);
rotor3=list(range(0,72));
random.shuffle(rotor3);

out = open('custom_wiring.ps','w')
f = open('standard_wiring.ps')
for line in f:
	if line.startswith('/ring1'):
		out.write('/ring1 [');
		for i in rotor1:
			out.write('{0:d} '.format(i));
		out.write('] def\n');
	elif line.startswith('/ring2'):
		out.write('/ring2 [');
		for i in rotor2:
			out.write('{0:d} '.format(i));
		out.write('] def\n');
	elif line.startswith('/ring3'):
		out.write('/ring3 [');
		for i in rotor3:
			out.write('{0:d} '.format(i));
		out.write('] def\n');
	else:
		out.write(line);
out.close();
f.close();

print('Custom wiring has been written to custom_wiring.ps.');
