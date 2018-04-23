/**
 * @file test_tower_of_hanoi.pl
 *
 * @author Michael John Decker, Ph.D.
 */
:- initialization(main, main).
:- [function].


test_tower_of_hanoi(Number, Expected) :-
    tower_of_hanoi(Number, Result),
    assertion(nonvar(Result)),
    assertion(Result = Expected).

main(Argv) :-
        test_tower_of_hanoi(0, []),
        test_tower_of_hanoi(1, [move(1,right)]),
        test_tower_of_hanoi(3, [move(1,right), move(2,middle), move(1,middle),
                                     move(3,right), move(1,left), move(2,right),
                                     move(1,right)]),
        test_tower_of_hanoi(5, [move(1,right), move(2,middle), move(1,middle),
                                     move(3,right), move(1,left), move(2,right),
                                     move(1,right), move(4,middle), move(1,middle),
                                     move(2,left), move(1,left), move(3,middle),
                                     move(1,right), move(2,middle), move(1,middle),
                                     move(5,right), move(1,left), move(2,right),
                                     move(1,right), move(3,left), move(1,middle),
                                     move(2,left), move(1,left), move(4,right),
                                     move(1,right), move(2,middle), move(1,middle),
                                     move(3,right), move(1,left), move(2,right),
                                     move(1,right)]).
