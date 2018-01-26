/**
 * @file main.cpp
 *
 * This is a generic C++ main file.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

//global variable;

int unique_id() {
    static int id = 0;
    return id++;
}

int main() {

    std::cout << "id: " << unique_id() << '\n';
    std::cout << "id: " << unique_id() << '\n';
    std::cout << "id: " << unique_id() << '\n';

    return 0;
}
