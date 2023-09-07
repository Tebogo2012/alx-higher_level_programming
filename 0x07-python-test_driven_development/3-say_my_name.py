 ago
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 #!/usr/bin/python3
 """Defines a name-printing function."""


 def say_my_name(first_name, last_name=""):
         """Print a name.

             Args:
                     first_name (str): The first name to print.
                             last_name (str): The last name to print.
                                 Raises:
                                         TypeError: If either of first_name or last_name are not strings.
                                             """
                                                 if not isinstance(first_name, str):
                                                             raise TypeError("first_name must be a string")
                                                             if not isinstance(last_name, str):
                                                                         raise TypeError("last_name must be a string")
                                                                         print("My name is {} {}".format(first_name, last_name))
