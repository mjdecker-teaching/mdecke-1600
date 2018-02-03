/**
 * @file raw_strings.cpp
 *
 * Raw strings in C++.
 *
 * @author Michael John Decker, Ph.D. <mdecke@bsgu.edu>
 */

#include <iostream>

const char * help_str = "program arg [optional_arg]\n"
                        "  * arg - an argument\n"
                        "  * optional_arg - an optional argument";


int main() {


    const char * raw_str_one 
	= R"("It's just a flesh wound." Black Knight)";
    std::cout << raw_str_one << '\n';


    const char * raw_str_two = R"(C:\WINDOWS\system32)";
    std::cout << raw_str_two << '\n';

    //const char * raw_str_three = R"("(*ptr).func()")";


    const char * raw_str_three = R"delimiter("(*ptr).func()")delimiter";
    std::cout << raw_str_three << '\n';
    std::cout << '\n';

    std::cout << help_str << '\n';

    return 0;
}
