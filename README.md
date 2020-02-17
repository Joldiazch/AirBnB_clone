---
<h1 align="center">0x00. AirBnB clone</h1>
<p align="center">The console</p>

![N|Solid](https://www.tecnofem.com/wp-content/uploads/2020/02/airbnb-logo.png)


---
## Description Project Command Interprete
Project Command Iterpreter HolbertonBnB is a complete web application, integrating database storage from Back-End in a clone of AirBnB.

The project currently only implements the back-end console.

![N|Solid](https://www.tecnofem.com/wp-content/uploads/2020/02/airbnb-map.png)


## Classes
---
   |BaseModel|FileStorage|User|State|City|Amenity|Place|Review|
---|---|---|---|---|---|---|---|---|---
**Private class attributes**|  |__file_path, __objects|
**Public instance attributes**|id: string, created_at: datetime, updated_at: datetime|
**Public instance methods**|save(self), to_dict(self)|all(self), new(self, obj), save(self), reload(self)|

### General
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

## How to use it

## Examples

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


## Author

- Jose Luis Diaz C. [@joldiazch](https://twitter.com/joldiazch)
- Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)

![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
