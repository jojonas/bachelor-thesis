#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	string line;
	int counter = 0;
	
	cout << "READY" << endl;
	while (1) {
		cin >> line; 
		if (line == "QUIT") {
			break;
		} else if (line == "REQ") {
			cout << counter << endl;
		} else if (line == "INC") {
			counter++;
		}
	}
	return 0;
}