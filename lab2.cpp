#include <iostream>
#include <string>
using namespace std;

int main() {
    int ihatethiscourse;
    string input;

    while (true) {
        cout << "Please enter a number: ";
        cin >> input;

        if (isdigit(input[0]) && input.length() == 1 && input[0] >= '3' && input[0] <= '9') {
            ihatethiscourse = input[0] - '0';
            break;
        } else {
            cout << "Input is not a valid number. Please try again." << endl;
        }
    }

    for (int i = 1; i <= ihatethiscourse; i++) {
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    for (int i = ihatethiscourse - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}