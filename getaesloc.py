def grabAESOffset(file):
   s = ConstBitStream(file)
   found = s.find('/x61/x65/x73/x5f/x68/x77/x5f/x63/x72/x79/x70/x74/x6f/x5f/x63/x6d/x64/x5f/x74', bytealigned=False)
   print "aes_hw_crypto_cmd_t location found at %d" %found

def main():
   file = sys.argv[0]
   grabKernelKBAG(file)
