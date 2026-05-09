% family.pl

male(john).
male(peter).

female(mary).
female(susan).

parent(john, peter).
parent(mary, peter).
parent(john, susan).
parent(mary, susan).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).