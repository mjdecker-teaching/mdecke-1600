/**
 * @file recursion.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

% base are facts directly
% Could have done this, but not really used in these notes.
%% master(X, Y) :- master(X, Z), master(Z, Y).

% Remember how can have to rules with same head/predicate.
% Remember how Haskell allowed you to have partial functions with
% base and recursive cases.  
% Well, we can use clause(s) as base clause, and another with same 
% head/predicate as recursive case (what we generally need).

% student (transitive property)
master(X, Y) :- student(Y, X).
master(X, Y) :- student(Y, Z), master(X, Z).

student(obi_wan, qui_gon).
student(anakin, obi_wan).
student(ahsoka, anakin). % Clone Wars

% or
%% student(sidious, plagueis).
%% student(vader, sidious).
%% student(starkiller, vader). % Force Unleashed


% Rule order generally only changes solution order (swap master rules)
% In non-terminating programs (which may be a problem in itself) it may find extra solutions.
% In other means, rule order does not matter much.

% If p is true, so is p.  Makes sense...
p :- p. % try trace
% INFINITE RECURSION!!!

% ask for list of friends (one-way for simplicity)
friend(ross, rachel).
friend(rachel, joey).
friend(rachel, phoebe).
friend(phoebe, smelly_cat).

% friend of friends
%% infinite recursion: friend(X, Y) :- friend(Y, X).
friend_of_friend(X, Y) :- friend(X, Y).

% Ok, the friend of my friend is my friend.
%% friend_of_friend(X, Y) :- friend(X, Z), friend(Z, Y).

% What about the friend of my friend of my friend?
% Needs another rule
%% friend_of_friend(X, Y) :- friend(X, A), friend(A, B),
%%                         ...
%%                         friend(Z, Y).

% Or recursion
friend_of_friend(X, Y) :- friend(X, Z), friend_of_friend(Z, Y).

% What happens when swap goal order of friend_of_friend
% DANGER DANGER DANGER!!!  left recursion, is the root of all evil when it comes to non-termination
% Here rule order can matter because of which rule is found first will 
% because it to terminate (non-recursive rule unioned) or not


% A recursive structures
int(0).
int(incr(X)) :- int(X).
% It counts. Try it again via trace.  What is it actually doing?
%% int(X).

% What if we swap the order of int rules?... Crash as infinite.

% Prolog tools: Building and binding. Recursion, unification, and proof search.
% Prolog good for handing recursive structures. Like trees and lists.

% addition on our structure?
% Returns are handled as an additional parameter
%% add(incr(0), incr(incr(0)), incr(incr(incr(0)))).
%% lets think about this.

% Lets look at a simple one.  When one of the parameters is one, but is the answer?
%% add(0, incr(incr(0)), incr(incr(0))).
add(0, Y, Y).

% Building on this, what do we need to do to first parameter.
% We need to add each incr to second paremeter or result.
% We have recursion, the rule up there looks suspiciously like a base case...
% Take one incr at a time and add it to result until reach base case.
%% add(incr(incr(incr(0))), incr(incr(0)), incr(incr(incr(0)))).
% First parameter matches one layer of incr, and we call it again without this layer.
% So, why on last parameter too.  This will be called until first parameter is 0.
% The answer (result) of each query will work back up the chain, and adds a ... incr
add(incr(X), Y, incr(Z)) :- add(X, Y, Z).

% Run and trace these
%% add(0, incr(incr(0)), Z).
%% add(incr(incr(incr(0))), incr(incr(0)), Z).
