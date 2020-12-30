# httpdogs [![Badge](https://img.shields.io/pypi/v/httpdogs?color=3776AB&logo=python&style=for-the-badge)](https://pypi.org/project/httpdogs/) [![Badge 2](https://img.shields.io/pypi/dm/httpdogs?color=3776AB&logo=python&style=for-the-badge)](https://pypi.org/project/httpdogs/)
Getting URLs to your favourite HTTP dogs made easy!


### Installation

Installing `httpdogs` is easy, just run `pip install httpdogs`!

### Usage

I've developed `httpdogs` to make using HTTP dogs simple and fun.

Currently, you can get your dogs using one of two functions - `dog_by_name` and `dog_by_code`

`dog_by_name(name: str)` takes in a sole parameter - `name`, which is the status code name to get a dog for.
Upon finding a dog matching the name, it returns an `HTTPDog` object. Here's an example -

```py
from httpdogs import dog_by_name

my_dog = dog_by_name("Success")

print(f"My dog has a code of {my_dog.code} and means {my_dog.name}! The URL is {my_dog.url}")
# Prints - 
# My dog has a code of 200 and means Success! The URL is https://http.dog/200
```

`dog_by_code(code: int)` is extremely similar to `dog_by_name`, just using a status code value.
Upon finding a dog matching the code, it returns an `HTTPDog` object. Here's an example -

```py
from httpdogs import dog_by_code

my_dog = dog_by_code(404)

print(f"My dog has a code of {my_dog.code} and means {my_dog.name} :( The URL is {my_dog.url}")
# Prints - 
# My dog has a code of 404 and means Not Found :( The URL is https://http.dog/404
```

##### The HTTPDog object also has an `image` attribute

You can use this attribute to get the image bytes associated with the dog.
You can then save it or view it, like in the example below -

```py
from httpdogs import dog_by_code
from PIL import Image
from io import BytesIO

my_dog = dog_by_code(302)

dog_image = Image.open(BytesIO(my_dog.image))
dog_image.show()

# Output below -
```

<img src="https://httpstatusdogs.com/img/302.jpg" alt="dog" width="300"/>

### Contributing 

This package is opensource so anyone with adequate python experience can contribute to this project!

### Report Issues
If you find any errors/bugs/mistakes with the package or in the code feel free to create an issue and report it [here.](https://github.com/itsmewulf/httpdogs/issues)

### Fix/Edit Content
If you want to contribute to this package, fork the repository, make your changes and then simply create a Pull Request!

### Contact
If you want to contact me -  
**Mail -** ```wulf.developer@gmail.com```<br>
**Discord -** ```wulf#9716```
