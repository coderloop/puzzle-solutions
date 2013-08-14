#include <stdio.h>

int main( int argc, char *argv[] ) {
  if( argc < 2 ) {
    return 1;
  }

  FILE *in = fopen( argv[1], "rb" );

  printf("Hello World!\n");

  fclose(in);
  return 0;
}

