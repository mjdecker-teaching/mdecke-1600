/**
 * @file test_tower_of_hanoi_output.pl
 *
 * @author Michael John Decker, Ph.D.
 */
:- initialization(main, main).
:- [function].

main(Argv) :-
        tower_of_hanoi(3), nl, nl,
        tower_of_hanoi(5).
