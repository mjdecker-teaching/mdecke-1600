#include <iostream>
#include <string>


std::string question = "What is the answer to the life, universe, and everything?";
int answer = 42;

int main() {

    int answer = 0;
    std::cout << "question: " << question << '\n';
    std::cout << "local : " << answer << '\n';
    std::cout << "global: " << ::answer << '\n';

    return 0;
}
