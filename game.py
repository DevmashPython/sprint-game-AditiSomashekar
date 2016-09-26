import msvcrt
import time 
import sys

finish=30
count=0

print "Press the enter key to start! :D"
raw_input()
print "press d"
stime=time.time()

while(count<int(finish-20)):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		sys.stdout.write('-->')
	else:
		print "You have lost the game.... :("
		break
if count==int(finish-20):
	print 'press s'	

	while(count<int(finish-10)):
		key=msvcrt.getch()
		if key=='s':
			count=count+1
			print '                             |'
			print "                             V"
		else: 
			print '\nYou have lost the game.... :('
			break
if count==int(finish-10):
	print "                       press a" ,

	while(count<int(finish)):
		key=msvcrt.getch()
		if key=='a':
			count=count+1  
			sys.stdout.write("-->")
		else:
			print '\nYou have lost the game.... :('
			break
if count==finish:
	time_e=time.time()-stime
	print '\nCongrats!!!'
	print "\nYou finished the game in "+str(time_e)	

raw_input("Press enter to exit. :)")
