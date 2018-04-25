/**
 * @file main.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *  * http://www.swi-prolog.org/pldoc/doc/_SWI_/library/main.pl
 */

% For unix
#!/usr/bin/env swipl


% initialize(:Goal, +When)
% When program starts execute goal main as main goal
% When of main makes act like executable.
:- initialization(main, main).

% nl writes new line
main(Argv) :-
        echo(Argv),
        factorial_tail(10, Result),
        write(Result), nl.

echo([]).

% ! is cut and means if reached here, don't backtrack
% so does not do next rule on fail or ; (or).
echo([Last]) :- !,
        write(Last), nl.
echo([Head|Tail]) :-
        write(Head), write(' '),
        echo(Tail).

factorial_tail_helper(0, Accumulator, Accumulator).
factorial_tail_helper(Num, Accumulator, Result) :-
    Num >= 1,
    NextNum is Num - 1,
    NextAccumulator is Accumulator * Num,
    factorial_tail_helper(NextNum, NextAccumulator, Result).

factorial_tail(Num, Result) :- factorial_tail_helper(Num, 1, Result).
