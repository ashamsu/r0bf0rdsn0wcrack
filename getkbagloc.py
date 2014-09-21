def grabKernelKBAG(file):
   s = ConstBitStream(file)
   found = s.find('/x00/x00/x47/x41/x42/x4B', bytealigned=False)
   print "KBAG location found at %d" %found

def main():
   file = sys.argv[0]
   grabKernelKBAG(file)
