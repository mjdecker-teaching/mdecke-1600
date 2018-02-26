/**
 * @file main.cpp
 *
 * This is a generic C++ main file.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

int main(int argc, char * argv[]) {

    for(int i = 0; i < argc; ++i) {
	std::cout << argv[i] << '\n';
    }

    return 0;
}
