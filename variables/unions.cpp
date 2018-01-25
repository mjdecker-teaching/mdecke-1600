/**
 * @file main.cpp
 *
 * Union example.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

union foo {

    int d;
    char ch;

};

void print_union(const foo & bar) {
    std::cout << "size: " << sizeof(bar) << '\n';
    std::cout << bar.d << '\n';
    std::cout << bar.ch << '\n';

}

int main(int argc, char * argv[]) {
    std::cout << "sizeof(int): " << sizeof(int) << '\n';
    std::cout << "sizeof(char): " << sizeof(char) << '\n';

    foo bar;
    bar.d = 0;
    print_union(bar);

    foo baz;
    baz.ch = 'a';
    print_union(baz);

    return 0;
}
