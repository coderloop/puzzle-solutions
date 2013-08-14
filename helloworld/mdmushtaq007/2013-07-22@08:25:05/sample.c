#include<stdio.h>
int main(int argc,char *argv[])
{
 FILE *fr;
 fr = fopen(argv[0],"r");
 printf("Hello World!\n");
 return 0;
}