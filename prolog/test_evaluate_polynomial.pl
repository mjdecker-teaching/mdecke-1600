/**
 * @file test_evaluate_polynomial.pl
 *
 * @author Michael John Decker, Ph.D.
 */
:- initialization(main, main).
:- [function].

test_evaluate_polynomial(Polynomial, X, Expected) :-
    evaluate_polynomial(Polynomial, X, Result),
    assertion(nonvar(Result)),
    assertion(Result = Expected).

main(Argv) :-
        test_evaluate_polynomial([], 3, 0),
        test_evaluate_polynomial([42], 3, 42),       
        test_evaluate_polynomial([1, -2, 1], 3, 4),
        test_evaluate_polynomial([-1, 2, 4, -8], 5, -891).
