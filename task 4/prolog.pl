parent(X, Y).
male(X).
female(X).
married(X, Y).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).
grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(X).
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).
grandson(X, Y) :- parent(Y, Z), parent(Z, X), male(X).
granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
uncle_by_marriage(X, Y) :- married(X, W), sibling(W, Z), parent(Z, Y), male(X).
cousin(X, Y) :- parent(Z, X), sibling(Z, W), parent(W, Y), male(X).
brother_in_law(X, Y) :- married(X, Z), sibling(Z, Y), male(X).
niece(X, Y) :- parent(Z, X), sibling(Z, Y), female(X).
second_cousin(X, Y) :- parent(A, X), parent(B, Y), cousin(A, B).

reverse([], []).
reverse([H|T], R) :- reverse(T, RT), append(RT, [H], R).

member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

palindrome(L) :- reverse(L, L).

sorted([]).
sorted([_]).
sorted([A,B|T]) :- A =< B, sorted([B|T]).

permutation([], []).
permutation(L, [H|T]) :- select(H, L, R), permutation(R, T).

scum(1, 1).
scum(N, Res) :- N > 1, N1 is N-1, scum(N1, R1), Res is R1 + N.

sumDigits(0, 0).
sumDigits(Num, Sum) :- Num > 0, Digit is Num mod 10, Rest is Num // 10, sumDigits(Rest, SRest), Sum is SRest + Digit.

split(0, []).
split(N, L) :- N > 0, split(N // 10, L1), Digit is N mod 10, append(L1, [Digit], L).

create([], 0).
create([H|T], N) :- create(T, N1), length(T, L), Pow is 10^L, N is H*Pow + N1.

intersection([], _, []).
intersection([H|T], L2, [H|Z]) :- member(H, L2), intersection(T, L2, Z).
intersection([H|T], L2, Z) :- \+ member(H, L2), intersection(T, L2, Z).

minus([], _, []).
minus([H|T], L2, Z) :- member(H, L2), minus(T, L2, Z).
minus([H|T], L2, [H|Z]) :- \+ member(H, L2), minus(T, L2, Z).