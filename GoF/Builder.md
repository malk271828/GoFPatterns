
## Builder

### Summary

|item|Desc|
|:---------|:----------|
|Objective|1. Abstraction of creational process. <br>2. provide sophisticated chained interface on constructing  objects. |
|Simplicity|★★★|
|Frequency|★★★|
|Components|Product,AbstructBuilder,ConcreteBuilder,Director|
|Embodiment|.NET StringBuilder<br>JQuery|
|Ref|1. [wiki](https://en.wikipedia.org/wiki/Builder_pattern)<br> 2. [sourceMaking](https://sourcemaking.com/design_patterns/builder)|

Using Builder pattern help us to create Test fixtures, which setup a certain [SUT](http://xunitpatterns.com/SUT.html). (See [This article](https://www.javacodegeeks.com/2013/06/builder-pattern-good-for-code-great-for-tests.html))

### Advantages
Advantages of using Builder are presented in [this slide](https://www.classes.cs.uchicago.edu/archive/2010/winter/51023-1/presentations/ricetj_builder.pdf) [[“will be …” vs. “are presented in section …” (tenses in scientific writing)](https://english.stackexchange.com/questions/268414/will-be-vs-are-presented-in-section-tenses-in-scientific-writing)]

>*  Allows you to vary a product’s internal representation.
>*  Encapsulates code for construction and representation.
>*  Provides control over steps of construction process.

### Relation
*  Telescoping Constructor Anti-pattern
Telescoping constructor is disreputable creative interface which requires a lot of arguments. In the consequence, client code have to obey with the order of these parameters or Telescoping constructor have to provide all the variations of constructors which can take a permutation of parameters as input.
[Telescoping Constructor Pattern Java](http://codethataint.com/blog/telescoping-constructor-pattern-java/) explain the benefit of introducing builder pattern and fluent chain interface in stead of using Telescoping constructor.

*  Template Method
As a derived class of template method class requires implementation of each template method, constructing interfaces of a concrete builder have to be implemented to be used by director class. Both patterns differ in which class is responsible for controlling processes executed in sub-classes. While a super template method class control sub class by calling template methods, it is a director class (not a abstract builder class) that calls constructing interfaces and decides which product you want to create.

* Abstract Factory
[sourceMaking](https://sourcemaking.com/design_patterns/builder) describe difference between Builder and Abstract Factory.
>  Builder focuses on constructing a complex object step by step. Abstract Factory emphasizes a family of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.

*  Facade
Director class handle complex construction process and provide simple interface to a client class. This relationship is similar to that of Facade pattern.

### Embodiments

*  [Mocking support in CppUTest](https://blog.odd-e.com/basvodde/2010/08/mocking-support-in-cpputest.html)
CppUTest test harness provides a mock class which have fluent chained interfaces for invoking a function/method with a configurable arguments like this:

```cpp
MockSupport mock;

// In your procedure, next function call expect
// can be parametrized with chained interfaces.
mock.expectOneCall("functionName").withParameter("parameterName", 10);
```
As discussed in [CppUTest: how to pass more data to a specific mock call?](https://stackoverflow.com/questions/15243838/cpputest-how-to-pass-more-data-to-a-specific-mock-call), the test suites can also specify a returning value:

```cpp
size_t CMockSocket::recv(void* buf, size_t len)
{
  return (size_t) mock().actualCall("recv")
      .withParameter("len", (int) len)
      .returnValue().getIntValue();
}
```
In a chain of methods calling, output arguments can be passed and verified:
```cpp
char buffer[] = "blabla";

mock().expectOneCall("recv")
    .withOutputParameterReturning("buf", buffer, sizeof(buffer))
    .withParameter("len", sizeof(buffer))
    .andReturnValue(sizeof(buffer));
```

*  jQuery (Javascript)
In jQuery, client code can switch a context by using $(selector) to access to jQuery. From a point of view in client side, ```AbstructBuilder``` class provides interfaces switching a context without creating explicitly objects. (see [This page](https://code.tutsplus.com/tutorials/understanding-design-patterns-in-javascript--net-25930))
```js
var myDiv = $('<div id="myDiv">This is a div.</div>');
//myDiv now represents a jQuery object referencing a DOM node.

var someText = $('<p/>');
//someText is a jQuery object referencing an HTMLParagraphElement

var input = $('<input />');
```
*  Tensorflow
[TensorBoard: Visualizing Learning ](https://www.tensorflow.org/get_started/summaries_and_tensorboard)
The following code show how do we build graph in TensorBoard by ```with``` keyword which switch a context.
```python
def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
  """Reusable code for making a simple neural net layer.

  It does a matrix multiply, bias add, and then uses relu to nonlinearize.
  It also sets up name scoping so that the resultant graph is easy to read,
  and adds a number of summary ops.
  """
  # Adding a name scope ensures logical grouping of the layers in the graph.
  with tf.name_scope(layer_name):
    # This Variable will hold the state of the weights for the layer
    with tf.name_scope('weights'):
      weights = weight_variable([input_dim, output_dim])
      variable_summaries(weights)
    with tf.name_scope('biases'):
      biases = bias_variable([output_dim])
      variable_summaries(biases)
    with tf.name_scope('Wx_plus_b'):
      preactivate = tf.matmul(input_tensor, weights) + biases
      tf.summary.histogram('pre_activations', preactivate)
    activations = act(preactivate, name='activation')
    tf.summary.histogram('activations', activations)
    return activations
```
