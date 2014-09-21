typedef int (*aes_crypto_cmd_t)(unsigned int op, void* src, void* dst, int size, unsigned int hwKey, void* iv, void* key); 

int main() {
  aes_crypto_cmd_t mahAESThing = (aes_crypto_cmd_t) = aes_hw_offset;
  memcpy((void*) someAddy, (void*) KBAGloc, 0x30); // Copy the KBAG to someAddy... 
  mahAESThing(0x11,(void*) someAddy,(void*)someAddy,0x30,0x20000200,0,0); // (0x10 == ENCRYPT & 0x11 == DECRYPT) 
  // Hexdump the area of someAddy to grab the result :) 
  return 0;
}