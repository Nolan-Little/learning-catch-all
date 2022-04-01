count(0, []).
count(Count, [Head|Tail]) :- count(TailCount, Tail), Count is TailCount + 1.


count(Len, [a,b,c])
% Len = 0
% Head = a
% Tail = [b, c]

% Len = 1
% Head = b
% Tail = [c]

% Len = 2

% Head = c
% Tail = []
% Len 3

sum(0, []).
sum(Total, [Head|Tail]) :- sum(Sum, Tail), Total is Head + Sum.
average(Average, List) :- sum(Sum, List), count(Count, List), Average is Sum/Count.

plus(A, B, C) :- C is A + B