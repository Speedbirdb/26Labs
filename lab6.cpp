#include <iostream>
#include <string>

using namespace std;

int call_count = 0;
double sum = 0.0;


void func(int n) {
    call_count += 1;
    
    sum += 1.0 / n;
    
    // Base case
    if (n == 1) {
        std::cout << "Summation : " << sum << std::endl;
        return;
    }
    
    func(n - 1);
}

void func(){
    call_count = 0;
    sum = 0.0;

    int n;
    std::cout << "Enter a positive integer: ";
    std::cin >> n;
    
    if (n <= 0) {
        std::cout << "Please enter a positive integer!" << std::endl;
        return;
    }
    
    func(n);
    
    std::cout << "Number of calls: " << call_count << std::endl;

}

int main() {
    func(5);
    
    std::cout << "Number of calls: " << call_count << std::endl;
    
    return 0;
}

int main() {return 0;}