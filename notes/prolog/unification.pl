/**
 * @file unification.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

% Unification is a fundamental mechanism for programming in Prolog.
% Prolog takes care of the process, but it is important to understand
% how it goes about this so we can use it correctly.

jedi(yoda).
jedi(luke).
midi_chlorians(anakin, 20001).
father(vader, luke).

% Basic Unification Idea
% Two terms unify if they are the same term or if they contain variables that can be uniformly instantiated
% with terms in such a way that the resulting terms are equal.

% same term unify
% luke unifies with luke as same atom
% 20001 unifies with 20001 as same number
% X unifies with X as same variables
% jedi(yoda) unifies with jedi(yoda) as same complex term

% jedi(yoda) does not unify with jedi(luke) as not same and no variable that can be instatiated the same

% yoda & X can because X can be instatiated with yoda
%% jedi(X). 

% Will this unify?
%% father(X, luke) with father(vader, X) 
% If X is vader then gives us father(vader, luke) and father(vader, vader)
% which are not the same.  Same for X as luke
% This what can be instatiated to X to make true is what we are really
% interested in and this is done by Prolog itself.

/* Unification Details
1) If constants, unify if same atom or same number
2) If one is a variable and other is any term (including variable),
   they unify and variable is instatiated to other term
   (variables instatiate to each other and we say share values).
3) If complex terms, unify if all are true:
    a) Same functor and arity
    b) All corresponding arguments unify
    c) Variable instantiations are compatable
       (e.g., same variables, must be instatiated to same term)
4) No other type of unification possible

*/

% Does unification sound like a complicated name for something else..
% equality (sort of)

% =/2 predicate (not unify is \=)
%% =(yoda,yoda).
%% yoda = yoda.

% What does rules say about these?

%% yoda = luke
%% 'yoda' = yoda.
%% '2' = 2.
%% yoda = X.
%% X = yoda.
%% X = Y.

% X is instantiated with luke by time gets to X = yoda and so fails
%% X = luke, X = yoda.
%% father(X, luke) = father(vader, Y).
%% father(X, X) = father(vader, luke).
% Standard unification algorithms say no, old implementation crash, as recursively expand X to father(vader, X)
% swipl is robust and says yes
% Reason standard unification says no is the occurs check. If variable is unified to term with that variable, then no.
%% father(vader, X) = X. 
%% X = father(vader, X), Y = father(vader, Y), X = Y.
% Standard unify in Prolog: unify_with_occurs_check/2
% unify_with_occurs_check(X, father(vader, X)).

% Facts which test if a line of points is horizontal or vertical
vertical(line(point(X, Y), point(X, Z))).
horizontal(line(point(X, Y), point(Z, Y))).

%% horizontal(line(point(1,3), point(42, 3))).
%% horizontal(line(point(1,3), point(42, 2))).
%% What x-cooredinate will make a vertical line?
%% vertical(line(point(3, 1), point(X, 42))).

%% What point will make a vertical line?
%% vertical(line(point(3, 1), Point)). - Random generated variable to say any point with x-coordinate 3
