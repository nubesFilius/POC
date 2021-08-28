fun main(args: Array<String>) {
    class Dog {

        var name: String
        var age: Int
        var furColor: String

        // constructor(name: String, age: Int, furColor: String) {
        //     this.name = name
        //     this.age = age
        //     this.furColor = furColor
        // }

        constructor() {
            name = ""
            age = 0
            furColor = ""
        }

        // func dogInfo() {
        //     println("$name is $age years old, he has a beatiful $furColor fur.")
        // }
        
    }

    var myDog = Dog(name: "Lila", age: 2, furColor: "Golden")
    println(myDog)

}