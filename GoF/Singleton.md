## Singleton

|item|Desc|
|:---------|:----------|
|Objective|assure an object of uniqueness|
|Simplicity|★★★★★|
|Frequency|★★★★★|
|Participants|Singleton,CLient|
|Embodiment||
|Refs|1. [wiki](https://en.wikipedia.org/wiki/Singleton_pattern)<br>2. [sourceMaking](https://sourcemaking.com/design_patterns/singleton)<br>3. [defactory](http://www.dofactory.com/javascript/singleton-design-pattern)|

>  [*Learning JavaScript Design Patterns*]
The idea of the singleton pattern is to have only one instance of a specific class. This means that the second time you use the same class to create a new object, you should get the same object that was created the first time.

### Pros and Cons in OOAD

|Factor|Pros|Cons|
|:--------|:--------|:--------|
|Maintainability|(+) Easy to manage resource allocation such as [Singletons and lazy loading](http://archive.oreilly.com/pub/post/singletons_and_lazy_loading.html)<br>(+) Easy to assure client class of thread safety after implementation.|(－) If a singleton class have a reference to another singleton class, be careful not to access to the singleton instance which have not been initialized yet. (See [this](http://marupeke296.com/DP_Singleton.html) article)
|Efficiency|N/A|N/A|
|Reusability|N/A|N/A|

### Implementation
*  C++
Singleton class commonly provide only the public interface which can access its own static instance by forbidding the other constructing interfaces ( constructor, copy constructor, assignment operator ) to be called from client code. In the development language support Generics syntax, you can leverage it in order to write code in simple way. It is worth noting that singleton is created at the same timing of global variables.
```cpp
template<class T>
class Singleton
{
public:
    static inline T& GetInstance()
    {
        static T instance;
        return instance;
    }

protected:
    // Forbid clients from creating singleton class
    // by using constructor
    Singleton() {}
    virtual ~Singleton() {}
private:
    // Forbid other class from creating singleton class
    // by assignment operator and copy constructor
    void operator=(const Singleton& obj) {}
    Singleton(const Singleton &obj) {}
};
```

```cpp
class FileManager : public Singleton<FileManager>
{
public:
    //
    friend class Singleton<FileManager>;

public:
    bool FileExists(const char* strName) const;
    File* OpenFile(const char* strName, eFileOpenMode mode);
    bool CloseFile(File* pFile);

protected:
    FileManager();
    virtual ~FileManager();
};
```

* python
Implementation sample with Python is [here](https://sourcemaking.com/design_patterns/bridge/python/1)

*  Javascript
>  Technically all objects in JavaScript are singletons. And also sometimes developers would say “singleton,” meaning objects created with the module pattern.
