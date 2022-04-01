class Employee(override val name: String, val number: Int) extends Person(name) {
  override def talk(message: String) {
    println(name + " with number " + number + " says " + message)
  }
  override def id():String = number.toString
}

val flanders = new Character("Ned") flanders.greet
