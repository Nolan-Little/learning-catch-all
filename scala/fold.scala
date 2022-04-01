val strings = List("seven", "five", "Four", "AAA")

var sum_string_sizes = strings.foldLeft(0)((sum, string) => sum + string.length)
println(sum_string_sizes)