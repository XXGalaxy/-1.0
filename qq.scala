package main

/**
  * Created by X on 2018/7/20.
  */
object qq1 {
  def main(args: Array[String]) {
    var temp=List(35,36,37,38,32,30)
    for(i<-Range(0,6)){
      if (i!=3) {
        println(temp(i))
      }
      else{
        println("周三的温度为："+temp(i))
      }
    }
  }
}

object qq2 {
    def main(args: Array[String]): Unit = {
      println("....")
      def sum(a: Int, b: Int): Int = {
        a + b
      }
      println(sum(1, 2))
    }
  }


object qq3{
  def main(args: Array[String]) {
    val add=(a:Int,b:Int)=>a+b
    println("1+2等于：")
    def ride(a:String,b:String):String=a+b
    println("?????:"+ride("朱一龙","邱邱"))
    println("!!!!默认值:")
    def abc(a:Int,b:Int,c:Int,opt:String="朱一龙"):Int={
      println(opt)
      a+b+c
    }
    abc(1,2,3)
  }

}

object qq4{
  def main(args: Array[String]) {

  }
}



