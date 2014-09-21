def grabAESOffset(file):
   s = ConstBitStream(file)
   found = s.find('6165735f68775f63727970746f5f636d645f74', bytealigned=False) 
   print "aes_hw_crypto_cmd_t location found at %d" %found

def main():
   file = sys.argv[0]
   grabKernelKBAG(file)
