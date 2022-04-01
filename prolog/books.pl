book(dune, frank_herbert).
book(dune_messiah, frank_herbert).
book(children_of_dune, frank_herbert).
book(hyperion, dan_simmons).
book(endymion, dan_simmons).
book(starship_troopers, robert_heinlein).
book(farnhams_freehold, robert_heinlein).
book(farnhams_freehold, robert_heinlein).
book(farnhams_freehold, robert_heinlein).
book(calvin_and_hobbes, bill_watterson).
book(the_far_side, gary_larsen).
book(lord_of_the_rings, jrr_tolkein).
book(drizzt, ra_salvatore).
book(foundation, isaac_aasimov).
book(foundation_and_empire, isaac_aasimov).
book(forward_the_foundation, isaac_aasimov).

author(isaac_aasimov, science_fiction).
author(bill_watterson, cartoon).
author(gary_larsen, cartoon).
author(robert_heinlein, science_fiction).
author(dan_simmons, science_fiction).
author(frank_herbert, science_fiction).
author(jrr_tolkein, fantasy).
author(ra_salvatore, fantasy).

what_genre(Title, Genre) :- book(Title, Author), author(Author, Genre).
written_by(Author, Title) :- book(Title, Author).