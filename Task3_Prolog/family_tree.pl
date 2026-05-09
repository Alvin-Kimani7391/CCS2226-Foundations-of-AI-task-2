% FAMILY FACTS

male(john).
male(paul).
male(mark).

female(mary).
female(susan).
female(linda).

parent(john, paul).
parent(mary, paul).

parent(john, susan).
parent(mary, susan).

parent(paul, mark).
parent(linda, mark).

% RULES

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

uncle(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    male(X).

aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    female(X).