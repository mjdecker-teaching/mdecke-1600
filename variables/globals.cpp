/**
 * @file main.cpp
 *
 * This is a generic C++ main file.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

//global variable;

void unique_id() {
    static int id = 0;
    std::cout << "id: " << id << '\n';
    ++id;

}

int main(int argc, char * argv[]) {

    unique_id();
    unique_id();
    unique_id();

    return 0;
}
