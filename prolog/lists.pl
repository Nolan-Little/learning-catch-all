concat([], List, List).
concat([Head|Tail1], List, [Head|Tail2]) :-
  concat(Tail1, List, Tail2).


swap([], ResultList, ResultList).
swap([Head|Tail], ResultList, PartialList) :-
  swap(Tail, ResultList, [Head|PartialList]).

list_min([Head|Tail], Min) :- list_min(Tail, Head, Min).
list_min([], Min, Min).
list_min([Head|Tail], CurrentMin, Min) :-
  NewMin is min(CurrentMin, Head),
  list_min(Tail, NewMin, Min).

sort([], List, List).
sort([Head|Tail]).

% When the min in a list is found it is appended to a new list