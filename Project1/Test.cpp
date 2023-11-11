#include "test.h"

using namespace cv;
using namespace std;

void test(const string& imagePath)
{
    // Read the image from the specified path
    Mat image = imread(imagePath);

    // Check if the image was successfully loaded
    if (image.empty())
    {
        cout << "Error: Could not read the image." << endl;
        return;
    }

    // Display the image
    imshow("Image", image);

    // Wait for a key press and then close the window
    waitKey(0);
}