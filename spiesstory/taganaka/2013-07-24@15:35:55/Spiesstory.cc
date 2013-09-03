#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
using namespace std;

static void rot_x(string &orig, const int shift) {
	int n = shift % 26;

	if (n == 0) {
		return;
	}

	if (orig.empty()) {
		return;
	}

	for (int i = 0, l = orig.length(); i < l; i++) {
		int c = (int) orig[i];

		if (c >= 97 && c <= 122) {
			orig[i] = (char) (((c - 71 + n) % 26) + 97);
		} else if (c >= 65 && c <= 90) {
			orig[i] = (char) (((c - 39 + n) % 26) + 65);
		}
	}
}
int main(int argc, char **argv) {

	ifstream ifs(argv[1], ifstream::in);

	if (!ifs.good()) {
		cerr << "Unable to open file\n";
		return 1;
	}

	int rot;
	string d;
	ifs >> rot;
	std::getline(ifs, d);

	rot = rot * -1;
	char *buffer;
	int len = 1024;
	buffer = new char[len+1];
	while (ifs.good()) {

		ifs.read(buffer, len);

		string line(buffer);
		rot_x(line, rot);
		cout << line;

		memset(buffer,0,len+1);
	}

	ifs.close();
	delete[] buffer;
	return 0;
}
