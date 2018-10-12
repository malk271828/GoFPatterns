
## FactoryMethod

|item|Desc|
|:---------|:----------|
|Objective|delegation of creation process to derived sub-classes|
|Simplicity|★★★★|
|Frequency|★★★
|Components|Product,ConcreteProduct,Factory,ConcreteFactory|
|Embodiment||
|Ref|1. [wiki](https://en.wikipedia.org/wiki/Factory_method_pattern)<br> 2. [sourceMaking](https://sourcemaking.com/design_patterns/factory_method)<br>3. [TechScore](http://www.techscore.com/tech/DesignPattern/FactoryMethod.html/)|

When your client code need to create instances of various classes, the client class will have a lot of dependency on other creating classes.  Delegating instance creation to a class dedicated to the creating process enable us to lower interclass dependency. The most simple factory class identify requested products by means of class-identifier (constant value/enumerations) and create a single or several classes. On the other hand, a factory class in FactoryMethod pattern discern the product by class type (see [This page](http://www.nulab.co.jp/designPatterns/designPatterns2/designPatterns2-2.html)).

### Relation

*  Mock Object
Mock object act as a non-test target object in Test driven development. There are the several reasons to introduce mock object: a tester want to exclude all the other objects except test target or difficulty in executing the function provided by the object (e.g. from hardware restrictions) under a test circumstance. [Advanced Unit Test, Part V - Unit Test Patterns](https://www.codeproject.com/Articles/5772/Advanced-Unit-Test-Part-V-Unit-Test-Patterns) and [TheMockObjectPattern](http://www.netobjectives.com/PatternRepository/index.php?title=TheMockObjectPattern) mentioned that factory method pattern should be used in mock object.

### Embodiment

* FactoryMethod in Tensorflow
Calling ```tf.get_variable``` function with several specifying parameters easily create Variables classes as factory products. See [official pages](https://www.tensorflow.org/programmers_guide/variables) to get more detailed information.

```python
my_variable = tf.get_variable("my_variable", [1, 2, 3])

my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3], dtype=tf.int32,
                                  initializer=tf.zeros_initializer)
```
