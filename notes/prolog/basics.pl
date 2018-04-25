/**
 * @file basics.pl
 *
 * @author Michael John Decker, PH.D.
 *
 * Based off of:
 *  * https://en.wikipedia.org/wiki/Prolog
 *  * http://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-html
 *
 */

 /*
    Prolog - Programming with Logic

    In a nut shell: "To get the ultimate answer, you must first ask the ultimate question"

    Background
    * Alain Colmerauer
    * 1972
    * Declarative Programming Language
        * Logic Programming Language (Functional Programming is also declarative)
    * Dynamically typed but with single data type (with several sub-types)
    * extensions: .pl, .pro, .P (swipl expects pl but is also Perl. .P is Pascal)
    * Rooted in first order logic https://en.wikipedia.org/wiki/First-order_logic and formal logic
    * Programming logic is expressed in forms of relations represented as facts and rules, computation initiated by querying over the relations
    * Prolog community may be more down to earth: "Prolog is not a perfect language, and it's not suitable for everything". "Prolog is, was, and always will be, a niche language. But the niche it occupies is fascinating".
    * Used for: NLP, expert systems, artificial intelligence, molecular biology, semantic web, theorem proving, type inference, etc.
    * Best used when structure and knowledge needs described/represented.
 
    Download: 
    * Windows, Linux, Mac: http://www.swi-prolog.org/Download.html
    * Mac: Homebrew
    * Linux: May require additional work.  Ubuntu has PPA available.

 */

 %% Can edit using anything, but make sure plain text.

 % comment
 /* block-comment */


% Prolog program is composed of facts and rules called a knowledge base (or database) and then querying
% Knowledge Base 1 (KB1):
beatle(john).
beatle(paul).
beatle(george).
beatle(ringo).
guitarist(george).
liverpool.

% Queries on KB1 (read in with with swipl as rules and facts (swipl -c (compile), -l (load) file, or query [file].), those entered at top level are queries)
% list clauses with listing.
% direct facts, . is full stop, tells interpretter now to evaluate
% loader does not find errors, compile does

%% beatle(paul). 
%% guitarist(george).
%% guitarist(ringo).
%% guitarist(paul).
%% drummer(ringo). - (depends on implementation) predicate does not exit or no.
%% liverpool.
%% england. - (depends on implementation) predicate does not exit or no.
%% exit with control-d or halt.

% KB2 - rules
% head :- body
% read :- as if or is implied by
% if body is true, so is head
% fundamental deduction is modus ponens p -> q, if p true therefore q is true
% ironically, was playing when wrote this
% fact
playing(lucy_in_the_sky_with_diamonds).
% rule
make_discovery(missing_link) :- playing(lucy_in_the_sky_with_diamonds).
name_discovery(lucy) :- make_discovery(missing_link).
name_discovery(kite) :- playing(being_for_the_benefit_of_mr_kite).

%% make_discovery(missing_link).
% will modus ponens in chains
%% name_discovery(lucy).
% another beatles song
%% name_discovery(kite).

% fact + rule = clauses
% equivalent, has 3 predicates: playing, make_discovery, name_discovery
% predicates are concepts, and clauses define what they mean and how they are related

% next we look at that

% KB3 - and/or

%% all predicates need to exist
name(picard).
holiday(easter).
hot(earl_grey).
%% hot(jasmine).
% whitespace is irrelevant
% , means and
drink(earl_grey) :- name(picard), hot(earl_grey).
% or, separate rules or separated with ;.  ; is faster, separate rules can be more readable
%% wearing(lobster_costume) :- name(picard).
%% wearing(lobster_costume) :- holiday(halloween).
wearing(lobster_costume) :- name(picard); holiday(halloween).

%% drink(earl_grey).
%% wearing(lobster_costume).

% technically the playing and make_discovery should be an and relationship
% note does not like when same name clauses are discontinuous.
%% playing(lucy_in_the_sky_with_diamonds).
%% make_discovery(missing_link).
%% name_discovery(lucy) :- make_discovery(missing_link), playing(lucy_in_the_sky_with_diamonds).

%% name_discover(lucy).

% KB4 - Query Variables

% capital letters are variables
% searches knowledge base top to bottom matching (initiates or binds to) first
%% beatle(X)
%% type ; after to get others
human(picard).
human(riker).
klingon(worf).
rank(captain, picard).
rank(officer, riker).
rank(officer, worf).

%% rank(captain, X).
%% rank(officer, X).
% Unification: find all officer all klingon and find intersection
%% rank(officer, X), klingon(X).

% KB5 - Knowledge Base Variables: how interesting programs are written.
peers(X, Y) :- rank(Z, X), rank(Z, Y). %, X \= Y.

% Syntax Details
% Fact, rules, and queries are built of terms
% 4 types of terms: atoms, numbers, variables, and complex terms (stuctures)
% atoms + numbers == constants
% constants + variables == simple terms

% atom - general-purpose name
%   - sequence of following characters: [a-z][_A-Za-z0-9]+
%   - single quotes containing any characters
%   - sequence of special characters

% numbers - integer and float (not as important)
% variable - [_A-Z][_A-Za-z0-9]+, (_ - is anonymous variable)

% complex terms (structure) = built from atom, numbers, and variables
% Comprised of: atom (called functor) followed by argument list of terms
% What is each of these terms?  No space between functor atom and (
% functor(term_1, term_2, term_3)
% name(arg1, Arg2, 42)

% What comlex term examples have we seen?
% By definitions, what haven't we seen? complex terms as arguments?
beatles(beatle(john), beatle(paul), guitarist(beatle(george)), beatle(ringo)).
% beatles(W, X, Y, Z).
% beatles(W, X, guitarist(beatle(Y)), Z).

% number of arguments == arity (Not Prolog specific term)
% predicate == functor/arity
% peers/2
% predicate can be overloaded on arity

% list info on predicates
% listing(predicate).
% listing(beatle)
% listing(beatles).
