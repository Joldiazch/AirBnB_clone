---
<h1 align="center">0x00. AirBnB clone</h1>
<p align="center">The console</p>

![N|Solid](https://www.tecnofem.com/wp-content/uploads/2020/02/airbnb-logo.png)


---
## Description Project Command Interprete
Project Command Iterpreter HolbertonBnB is a complete web application, integrating database storage from Back-End in a clone of AirBnB.

The project currently only implements the back-end console.

![N|Solid](https://www.tecnofem.com/wp-content/uploads/2020/02/airbnb-map.png)

---
## Classes
|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

---
## General
Concepts to learn in this project:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## How to start it

### Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HolbertonBnB instantiates an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from 
any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the `storage` object is used to register corresponding changes in the `file.json`.

### Console :computer:

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the `storage` object defined above).

## How to use it

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

## Examples
Starting with no objects, we will create a BaseModel instance, update it with the key-value pair `first_name: "Juan_Jose"`, and then prove our instance has changed.
```
(hbnb) all
[]
(hbnb) create BaseModel
bafb7c4f-6415-4e93-801e-50bf68a18f3c
(hbnb) show BaseModel bafb7c4f-6415-4e93-801e-50bf68a18f3c
[BaseModel] (bafb7c4f-6415-4e93-801e-50bf68a18f3c) {'id': 'bafb7c4f-6415-4e93-801e-50bf68a18f3c', 'created_at': datetime.datetime(2020, 2, 19, 19, 8, 9, 799299), 'updated_at': datetime.datetime(2020, 2, 19, 19, 8, 9, 799299)}
(hbnb) update BaseModel bafb7c4f-6415-4e93-801e-50bf68a18f3c first_name "Juan_Jose"
(hbnb) show BaseModel bafb7c4f-6415-4e93-801e-50bf68a18f3c
[BaseModel] (bafb7c4f-6415-4e93-801e-50bf68a18f3c) {'id': 'bafb7c4f-6415-4e93-801e-50bf68a18f3c', 'created_at': datetime.datetime(2020, 2, 19, 19, 8, 9, 799299), 'updated_at': datetime.datetime(2020, 2, 19, 19, 8, 9, 799299), 'first_name': 'Juan_Jose'}
(hbnb)
```
* Now let's create a few more objects to demonstrate how all, count, and destroy work.
```
(hbnb) create BaseModel
d98de563-89c7-4dc3-9f46-e087911813f6
(hbnb) create User
a83cba86-f7ce-470f-89f8-85af656bc6df
(hbnb) count BaseModel
2
(hbnb) count User
1
(hbnb) count City
0
(hbnb) all BaseModel
["[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'first_name': 'Betty'}", "[BaseModel] (d98de563-89c7-4dc3-9f46-e087911813f6) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668384), 'id': 'd98de563-89c7-4dc3-9f46-e087911813f6', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668408)}"]
(hbnb) all
["[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'first_name': 'Betty'}", "[BaseModel] (d98de563-89c7-4dc3-9f46-e087911813f6) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668384), 'id': 'd98de563-89c7-4dc3-9f46-e087911813f6', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668408)}", "[User] (a83cba86-f7ce-470f-89f8-85af656bc6df) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112270), 'id': 'a83cba86-f7ce-470f-89f8-85af656bc6df', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112295)}"]
(hbnb) destroy BaseModel d98de563-89c7-4dc3-9f46-e087911813f6
(hbnb) count BaseModel
1
(hbnb)
```
* In addition, all of our commands (except for create) work with Object method notation as such:
```
(hbnb) BaseModel.count()
1
(hbnb) User.all()
["[User] (cbde29bc-7dbb-45d5-b6b3-54afaf953cb3) {'created_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362051), 'updated_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362076), 'id': 'cbde29bc-7dbb-45d5-b6b3-54afaf953cb3', "[User] (a83cba86-f7ce-470f-89f8-85af656bc6df) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112270), 'id': 'a83cba86-f7ce-470f-89f8-85af656bc6df', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112295)}"]
(hbnb) User.update("cbde29bc-7dbb-45d5-b6b3-54afaf953cb3", "gender", "Male")
(hbnb) User.show("cbde29bc-7dbb-45d5-b6b3-54afaf953cb3")
[User] (cbde29bc-7dbb-45d5-b6b3-54afaf953cb3) {'created_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362051), 'updated_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362076), 'id': 'cbde29bc-7dbb-45d5-b6b3-54afaf953cb3', 'gender': 'Male'}
(hbnb) User.count()
2
(hbnb) User.destroy("cbde29bc-7dbb-45d5-b6b3-54afaf953cb3")
(hbnb) User.count()
1
```
* Update from dictionary: to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
```
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
```


## Task Project
---
File Name|Task Name|Task Description
---|---|---
README.md and AUTHORS|0. README, AUTHORS|Description Project and Authors github
AirBnB_clone|1. Be PEP8 compliant!|Check all files with PEP8
tests/|2. Unittests|All files, classes, functions must be tested with unit tests
models/base_model.py, models/__init__.py, tests/|3. BaseModel|Start with BaseModel: Write a class BaseModel that defines all common attributes/methods for other classes
models/base_model.py, tests/|4. Create BaseModel from dictionary|Now it’s time to re-create an instance with this dictionary representation.
models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/|5. Store first object|recreate a BaseModel from another one by using a dictionary representation
console.py|6. Console 0.0.1|contains the entry point of the command interpreter cmd
console.py|7. Console 0.1|Update your command interpreter with someone commands: create, show, destroy, all and update
models/user.py, models/engine/file_storage.py, console.py, tests/|8. First User|Write a class User that inherits from BaseModel
models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/|9. More classes!|Write all those classes that inherit from BaseModel: State, City, Amenity, Place, Review
console.py, models/engine/file_storage.py, tests/|10. Console 1.0|Update FileStorage to manage correctly serialization and deserialization and Update your command interpreter (console.py)
console.py|11. All instances by class name|Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().
console.py|12. Count instances|Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
console.py|13. Show|Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>)
console.py|14. Destroy|Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>)
console.py|15. Update|Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>)
console.py|16. Update from dictionary|Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).


## Author

- Jose Luis Diaz C. [@joldiazch](https://twitter.com/joldiazch)
- Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)

![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
