Animal := Object clone

Animal walk := method("I am walking" println)

"Tell the animal what to do" println
input := File standardInput readLine
Animal getSlot(input) call
"These are the others things I can do" println
Animal slotNames println