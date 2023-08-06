import keyboard
import datetime

threshold = 20000
prev = datetime.datetime.now()
leastDiff = 9999999999999
while True:
	now = datetime.datetime.now()
	#print(f"Prev={prev}")
	#print(f"Now={now}")
	diff = now-prev
	print(f"Diff={diff.microseconds}")

	key = keyboard.read_key()
	#print(f"Key {key} pressed")
	if (diff.microseconds <= threshold):
		print(f"Key {key} needs replacement")
	if (diff.microseconds < leastDiff):
		leaseDiff = diff
	prev = now
