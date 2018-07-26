import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by X on 2018/7/25.
  */
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
object title {
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
        var category = 0
        try{
          category=line.getString("category").toInt
        }catch{
          case err:Exception=>{println("category问题")}
        }
        var cate = ""
        var view_sales = 0
        if(category==333002){
          cate ="励志:"
        }else if(category==50000052){
          cate ="口才演讲:"
        }else if (category==50003137){
          cate ="心理学"
        }else if (category==50000050){
          cate ="成功"
        }else if (category==50000147){
          cate ="现代文学"
        }else if (category==50004676){
          cate ="世界名著"
        }else if (category==50004684){
          cate ="当代随笔"
        }else if (category==50000150){
          cate ="外国小说"
        }else if (category==50000051){
          cate ="心灵修养"
        }else if(category==51234007){
          cate="漫画"
        }else if (category==51218006){
          cate="青春小说"
        }else if (category==51220030){
          cate="中国通识"
        }else if (category==50005701){
          cate="其他小说"
        }else if (category==51118019){
          cate="菜谱"
        }else if (category==50000068){
          cate="广告营销"
        }else if (category==50004681){
          cate="中国古诗词"
        } else if (category==51228037){
          cate="大学教材"
        }else if (category==50010485){
          cate="期刊杂志"
        }else if (category==50004675){
          cate="作品集"
        }else if (category==56766004){
          cate="儿童读物"
        }else if (category==50000142){
          cate="都市情感小说"
        }else if (category==56828001){
          cate="孕期读物"
        }else if (category==56830001){
          cate="胎教读物"
        }else if (category==50004862){
          cate="儿童绘本"
        }else if (category==56826001){
          cate="育儿读物"
        } else {
          cate ="其他"
        }
        try{
         // println(line)
          view_sales = line.getString("view_sales").replace("人付款","").toInt
        }catch{
          case e:Exception=>{println("无分类")}
        }
        (cate,view_sales)
      })
      .reduceByKey(_+_)
      .take(26)
    for(i<-resultlist){
      println(i)
    }
    sc.stop()
  }
}
