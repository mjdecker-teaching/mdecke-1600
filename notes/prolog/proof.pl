/**
 * @file proof.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

% How does Prolog search to a knowledge base to satisfy a query

jedi(yoda).
jedi(luke).
master(yoda, luke).
father(vader, luke).
force_is_strong(X) :- jedi(X), master(yoda, X), father(vader, X).


%% force_is_strong(X).
/*
 Draw tree.

 So, what happens?  

 Goals: force_is_strong(X) 

 Prolog reads knowledge base top-down attemptying to unify.
 force_is_strong(X) is unified with the head of the rule.
 (When unify variable in query to variable in fact or rule, new temporary variable is created, left out to simplify)

 Originally query is dependent on jedi, master, and father.
 If can instantiate X to same for each, then query can be satisfied.

    Goals: jedi(X), master(yoda, X), father(vader, X).

    List of goals are satisfied from left to right.

    jedi(X) unifies with jedi(yoda)

        Goals: master(yoda, yoda), father(vader, yoda).

        master(yoda, yoda) does not unify with anything.  So, backtrack.

    jedi(X) unifies with jedi(luke)

        Goals: master(yoda, luke), father(vader, luke).

        master(yoda, luke) unifies with fact.

            Goals: father(vader, luke).

            father(vader, luke) unifies with fact.


                Goals: 

                No more remaining goals, satisfies (proved) query with X = luke
            
If multiple answers, ; backtracts from success.

Proof is a search tree with leaves with goals as failures and leaf with empty goal as success.

trace. (trace stop, turn of with notrace.) - enters trace mode, for debugging commands (or learning Prolog)

*/