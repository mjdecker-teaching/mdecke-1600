/**
 * @file main.cpp
 *
 * Unsafe pointer examples.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>
#include <string>

int main(int argc, char * argv[]) {

    char number[] = { "123"};
    char * number_plus_one = number + 1;
    std::cout << number_plus_one << '\n';

    int integers[5] = { 0x65666768, 92, 4, 5, 0x2A };
    for(int integer : integers) {
        std::cout << integer << ' ';
    }
    std::cout << '\n';

    char * characters = (char *)integers;
    for(int i = 0; i < 5; ++i) {
        std::cout << characters[i] << ' ';
    }
    std::cout << '\n';

    std::string * str = (std::string *)integers;
    std::cout << str->size() << '\n';
    std::cout << '\'' << str->c_str() << "'\n";


    return 0;
}
