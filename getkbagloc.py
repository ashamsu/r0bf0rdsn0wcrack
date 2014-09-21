def grabKernelKBAG(file):
   s = ConstBitStream(file)
   found = s.find('00004741424B', bytealigned=False)
   print "KBAG location found at %d" %found

def main():
   file = sys.argv[0]
   grabKernelKBAG(file)
