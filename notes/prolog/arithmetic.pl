/**
 * @file arithmetic.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

% Math is a little different than we are used to.

% Assignment is done with is operator
%% 3 is 1 + 2.
%% 10 is 9 - -1.
%% 42 is 6 * 7.
%% 2.5 is 5 / 2.
%% 2 is 5 // 2.
%% 1 is 5 mod 2.

% Can assign to variable
%% Answer is 6 * 7.

% Normal precedence. Or (10 ** 3).  Can use parenthesis to force precedence.
% http://www.swi-prolog.org/pldoc/man?section=operators
%% Level is 9 * 10 ^ 3 + 1.
%% Level is ((9 * (10 ^ 3)) + 1).

% So, why not
%% Answer = 6 * 7.

% = is union and 6 * 7 is really *(6, 7). That is, a complex term.
% So, they union.  is operator means evaluate.

% BTW, is is a term
%%  is(3, 2 + 1).

% Arithmetic is outside the normal Prolog behavior, attached on
% because useful/required.

% So, while we Can
%% 6 * 7 = Answer.

% We can not
%% 6 * 7 is Answer.

% Lets define a function
% Variables can exist on right-hand side
% but they must have already been instantiated with a number.
line_equation(M, X, B, Result) :- Result is M * X + B.



%% line_equation(3, 2, 1, Result).
% Fails, lets look why?
% This is asking: 7 is 3 * 2 + B
% Can it evaluate: 3 * 2 + B?  No
%% line_equation(3, 2, B, 7).

% Not a number
%% line_equation(3, 2, '1', Result).

% Now some interesting things.

% len (cause length taken) of list
len([], 0).
len([Head|Tail], Size) :- len(Tail, Result),
    Size is Result + 1.

% trace has to go back (and do addition) to give final answer.
%% len([1,2,3], Size).

% tail recursive: does not have to go back up.
% Uses accumulator variable.  This common thing for tail recursion
% insertion_sort (Haskell assignment) used this concept.
% This is generally considered more efficient as less bookkeeping overhead
% as does not need to go back.
length_tail_helper([], Accumulator, Accumulator).
length_tail_helper([Head|Tail], Accumulator, Size) :-
    % Gives fail, must have different variable name
    %% Accumulator is Accumulator + 1,
    AccumulatorNew is Accumulator + 1,
    length_tail_helper(Tail, AccumulatorNew, Size).

% add later
length_tail(List, Size) :- length_tail_helper(List, 0, Size).

%% length_tail([1,2,3], Size)
%% length_tail_helper([1,2,3], Size)


%% factorial
factorial(0, 1).
factorial(Num, Result) :- 
    %% Num >= 0,
    NextNum is Num -1,
    factorial(NextNum, NextResult),
    Result is Num * NextResult.

%% tail recursive factorial (start as 1, can add helper like did before)
factorial_tail_helper(0, Accumulator, Accumulator).
factorial_tail_helper(Num, Accumulator, Result) :-
    %% Num >= 0,
    NextNum is Num - 1,
    NextAccumulator is Accumulator * Num,
    factorial_tail_helper(NextNum, NextAccumulator, Result).

factorial_tail(Num, Result) :- factorial_tail_helper(Num, 1, Result).


% Comparison
% Normal except, =:= is == and =\= is !=.
% Force both sides to be evaluated
%% 1 + 3 =:= 2 + 2.
% Compare to:
%% 1 + 3 = 2 + 2.

% Like is, they variables need instantiated
%% X = 1, X < 2.
%% X < 2.

% How you do selection? A bit awkward.
% list min
min_helper([], Accumulator, Accumulator).
min_helper([Head|Tail], Accumulator, Min) :-
    Head < Accumulator,
    NextAccumulator is Head,
    min_helper(Tail, NextAccumulator, Min).

min_helper([Head|Tail], Accumulator, Min) :-
    Head >= Accumulator,
    min_helper(Tail, Accumulator, Min).

% How to initialize to start?
min(List, Min) :-
    % Must have element
    [Head|Tail] = List,
    min_helper(Tail, Head, Min).

% Fix factorial with condition, show how breaks without.
