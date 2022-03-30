#include "Bag.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>

using namespace std;

int main() {

	testAll();
	cout << "Short tests over" << endl;
	try {
		testAllExtended();
	}
	catch (exception e) {
		cerr << e.what() << endl;
	}

	cout << "All test over" << endl;
}