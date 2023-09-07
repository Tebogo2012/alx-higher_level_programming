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
 19
 20
 21
 #!/usr/bin/python3
 """Defines a square-printing function."""


 def print_square(size):
         """Print a square with the # character.

             Args:
                     size (int): The height/width of the square.
                         Raises:
                                 TypeError: If size is not an integer.
                                         ValueError: If size is < 0
                                             """
                                                 if not isinstance(size, int):
                                                             raise TypeError("size must be an integer")
                                                             if size < 0:
                                                                         raise ValueError("size must be >= 0")

                                                                         for i in range(size):
                                                                                     [print("#", end="") for j in range(size)]
                                                                                             print("")
