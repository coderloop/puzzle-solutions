#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	int n = -1;
	int np = 0;
	int numok = 0;
	int numko = 0;
	int* nl = NULL; 
	ifstream ifs(argv[1]);
	
	while( !ifs.eof() )
	{
		if( n == -1 )
		{
			ifs >> n;
			nl = new int[2*n+1];
			int i;
			for( i=0; i<2*n+1; i++ )
				nl[i] = -1;
			np = n;
		}
		else
		{
			string c;
			int n1, n2;
			
			ifs >> c >> n1 >> n2;
			
			if ( c == "c" )
			{
				int next1 = nl[n1];
				int next2 = nl[n2];
				while(true)
				{
					if (next1 == -1)
					{
						if (next2 == -1)
						{
							nl[n1] = np;
							nl[n2] = np;
							np = np + 1;
							break;
						}
						else
						{
							nl[n1] = next2;
							break;
						}
					}	
					else
					{
						if (next2 == -1)
						{
							nl[n2] = next1;
							break;
						}
						else if (next1 != next2)
						{
							n1 = next1;
							n2 = next2;
							next1 = nl[n1];
							next2 = nl[n2];
						}
						else
							break;
					}		
				}
			}
			else if ( c == "q" )
			{
				int next1 = nl[n1];
				int next2 = nl[n2];
				while (true)
				{
					if( (next1 == -1) || (next2 == -1) )
					{
						numko = numko + 1;
						break;
					}
					else
					{
						if (next1 == next2)
						{
							numok = numok + 1;
							break;
						}
						else
						{
							n1 = next1;
							n2 = next2;
							next1 = nl[n1];
							next2 = nl[n2];
						}
					}
				}
			}
		}
	}
	ifs.close();
	cout << numok << "," << numko << endl;
}
