a_file := File with("a_file_name.txt")
rows := list("1, Cat, Smol", "1, Animal, size")

File appendNewLine := method(seq,
  self appendToContents("\n#{seq}" interpolate)
)

File writeRows := method(rows,
  rows foreach(row, self appendNewLine(row))
)
a_file writeRows(rows)