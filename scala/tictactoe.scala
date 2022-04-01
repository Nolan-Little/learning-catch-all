val BLANK = "-"
val X = "x"
val O = "o"

class Board {
  val squares = List(
    List(EMPTY, EMPTY, EMPTY),
    List(EMPTY, EMPTY, EMPTY),
    List(EMPTY, EMPTY, EMPTY),
  )
  var isFull = checkFullState()

  def checkFullState():Boolean = {
    var fillState = true
    squares.foreach { row =>
      if(row.contains(BLANK)) {
        fillState = false
      }
    }
    return fillState
  }
}

val board = new Board()
println(board.isFull)
