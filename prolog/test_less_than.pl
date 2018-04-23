/**
 * @file test_less_than.pl
 *
 * @author Michael John Decker, Ph.D.
 */
:- initialization(main, main).
:- [function].

main(Argv) :-
        assertion(less_than(0, incr(0))),
        assertion(less_than(0, incr(incr(0)))),
        assertion(less_than(incr(0), incr(incr(0)))),
        assertion(less_than(incr(incr(0)), incr(incr(incr(0))))),
        assertion(\+ less_than(incr(0), incr(0))),
        assertion(\+ less_than(incr(incr(0)), incr(0))).
