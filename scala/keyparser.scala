import scala.xml.XML

val xml = XML.loadFile("sso.xml")
//  how tf do you get elements by attribute. Xpath is lying to me.
// val certNodes = xml \\ "KeyDescriptor@use=signing" \ "KeyInfo" \ "X509Data" \ "X509Certificate"
val keyDescriptors = xml \\ "KeyDescriptor"

var signingNodes = List[scala.xml.Node]()

keyDescriptors.foreach { node =>
  if ((node \ "@use").text == "signing") {
    signingNodes ::= node
  }
}

println((signingNodes.last \ "KeyInfo" \ "X509Data" \ "X509Certificate").text)