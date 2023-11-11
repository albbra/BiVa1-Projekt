// Project1.cpp: Definiert den Einstiegspunkt für die Anwendung.
//
#include "Project1.h"
#include "Test.h"

using namespace std;
using namespace cv;

int main()
{
	// Call the test function to read and display the image
	test("TestBild/Katze.jpg");

	cout << "Hello CMake." << endl;
	return 0;
}
