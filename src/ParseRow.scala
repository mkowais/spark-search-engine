import scala.io.Source

class Post(val toBeParsed: String) {
   private var postMap = transformIntoMap()

   private def transformIntoMap() : Map[String, String] = {
     var preParsedRow = toBeParsed.split('"').map(_.replace("<row","")).map(_.replace("/>","")).map(_.trim).filterNot(_.isEmpty)
     var postHeader = preParsedRow.filter(_.endsWith("=")).map(_.replace("=", ""))
     var postContent = preParsedRow.filterNot(_.endsWith("="))
     return (postHeader zip postContent).toMap
   }

   def getPost() :Map[String,String] = {
      return postMap
   }
}

def readXMLFile() : Array[String] = {
   val xmlSource = Source.fromFile("data/Posts.xml")
   val posts = xmlSource.getLines.toArray
   xmlSource.close
   return posts
}