/**
  * Created by X on 2018/7/25.
  */
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
object Book {
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
  .map(line=>{
    val view_price = line.getString("view_price").toFloat
    var price_name = ""
    if(view_price>=200){
      price_name ="200元以上"
    }else if(view_price>=100){
      price_name ="100元~200元"
    }else if (view_price>=50){
      price_name ="50元~100元"
    }else if (view_price>=30){
      price_name="30元~50元"
    }else if (view_price>=10){
      price_name ="10元~30元"
    }else{
      price_name ="1元~10元 "
    }
    var view_sales = 0
    try{
      //println(line)
      view_sales = line.getString("view_sales").replace("人付款","").toInt
    }catch{
      case e:Exception=>{println(" 付款为零 ")}
    }
    (price_name,view_sales)
  })
      .reduceByKey(_+_)
      .take(6)
    for(i<-resultlist){
      println(i)
    }
    sc.stop()
  }
}
