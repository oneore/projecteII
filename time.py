from progressbar import *               # just a simple progress bar

widgets = ['Test: ', Percentage(), ' ', Bar(marker='0',left='[',right=']'),
           ' ', ETA(), ' ', FileTransferSpeed()] #see docs for other options

pbar = ProgressBar(widgets=widgets, maxval=500)
pbar.start()

for i in range(100,500+1,50):
    # here do something long at each iteration
    pbar.update(i) #this adds a little symbol at each iteration
pbar.finish()
print
