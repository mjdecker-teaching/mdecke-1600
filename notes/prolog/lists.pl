/**
 * @file lists.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

% lists use the array like syntax
% empty list
%% [].

% list of atoms
%% [butch, cassidy].

% mixed (52 is meowth), can contain different items like Python
%% ['Team Rocket', member(jessie), member(james), 52].

% can union element in list
% must be same number
%% [A, B, C, D] = ['Team Rocket', member(jessie), member(james), 52].

% Lists (except empty) consist of head/tail like Haskell
% The operator | splits them
%% [Head|Tail] = ['Team Rocket', member(jessie), member(james), 52].
%% [H|T] = [].
%% [H|T] = [foobar].

% | can be used in combination with ,
%% [A, B, C | T] = ['Team Rocket', member(jessie), member(james), 52].
% Anonymous variable can be used to ignore (do not have to union to same, each considered independent)
%% [_, J, _ | _] = ['Team Rocket', member(jessie), member(james), 52].

% Can have list of lists
%% [[butch, cassidy], [jessie, james]].

% get cassidy
%% [[_, C | _] | _] = [[butch, cassidy], [jessie, james]].

% contains
% Lets simplify how would I check if it is the head?
contains(Head, [Head|_]).
% Lets extend that, how then can we recursively check head?
contains(X, [_|Tail]) :- contains(X, Tail).

% Walk though each of these (trace.)
%% contains(waldo, [waldo, carmen, sandiego]).
%% contains(sandiego, [waldo, carmen, sandiego]).
% Why does this report false?
%% contains(blue, [waldo, carmen, sandiego]).

% What does this do?  Huh, a traversal as well.
%% contains(X, [waldo, carmen, sandiego]).

% Lets check if a list of foo has the same number as a list of bar
foo2bar([], []).
foo2bar([foo|Tfoo], [bar|Tbar]) :- foo2bar(Tfoo, Tbar).

%% foo2bar([foo, foo], [bar, bar]).
%% foo2bar([foo, foo], [bar]).
%% foo2bar([foo, foo], [bar, foo]). 
%% foo2bar([foo, foo], Y).
%% foo2bar(X, Y).


%% if time combine, interleave first two into third.
combine([], [], []).
combine([H1|T1], [H2|T2], [H1,H2|T3]) :- combine(T1, T2, T3).

% Another form of combine that may be more natural (note, not assignment at end)
%% combine([], [], []).
%% combine([H1|T1], [H2|T2], Lists]) :-
%%  combine(T1, T2, SubList),
%%  Lists = [H1, H2 | SubList].

% Helps when they struggle with combine: copy(X, Y). copy List X to List Y
copy([], []).
copy([H1 | T1], [H1 | T2]) :- copy(T1, T2).

% combine([1,2,3], [a,b,c], [pair(1,a), pair(2,b), pair(3,c)]).
combine_pair([], [], []).
combine_pair([H1|T1], [H2|T2], [pair(H1,H2)|T3]) :- combine_pair(T1, T2, T3).


