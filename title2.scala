import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by X on 2018/7/25.
  */
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
object title2 {
  def main(args: Array[String]) {
    import org.json.JSONObject
    import scala.collection.mutable.ListBuffer
    val conf = new SparkConf().setMaster("local").setAppName("shu")
    val sc = new SparkContext(conf)
    val resultlist = sc.textFile("书-淘宝数据.txt")
      .filter(line=>{
        val isJson = line.startsWith("{\"")&&line.endsWith("}")
        var isShow = false
        if (isJson){
          val json = new JSONObject(line)
          val status=json.getJSONObject("mods").getJSONObject("itemlist").getString("status")
          isShow = status.equals("show")
        }
        isJson&isShow
      })
      .flatMap(line=>{
        val json = new JSONObject(line)
        val goods= json.getJSONObject("mods").getJSONObject("itemlist").getJSONObject("data").getJSONArray("auctions")
        var list = ListBuffer[JSONObject]()
        for (i<-0 to goods.length()-1){
          list.append(goods.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("category"),line.getString("view_sales").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))
  }
}
