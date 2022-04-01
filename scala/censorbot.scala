implicit class Censor (s: String){
  var string = s
  val keywords = Map("Fuck" -> "F-BOMB", "Shit" -> "SHITE")
  def censor (s: String) {
    println(s)
  }
}


var a = new Censor("a")
a.censor