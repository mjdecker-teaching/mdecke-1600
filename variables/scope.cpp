/**
 * @file main.cpp
 *
 * Scope example
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

int main(int argc, char * argv[]) {

    int var = 0;
    {
        std::cout << var << '\n';
        int var = 1;
        std::cout << var << '\n';
    }
    std::cout << var << '\n';

    return 0;
}
