class FileName:
    """
    A class for manipulating and renaming file names based on a given format.
    """

    def __init__(
        self, init_format=["MM", "DD", "YYYY"], delimiter="-", custom_base=None
    ):
        """
        Initializes a FileName object.

        Args:
            init_format (list): The initial format of the file name. Defaults to ['MM', 'DD', 'YYYY'].
            delimiter (str): The delimiter used to separate the parts of the file name. Defaults to '-'.
        """
        self.init_format = init_format
        self.delimiter = delimiter

        if custom_base:
            self.base = custom_base
        else:
            self.base = {"MM": None, "DD": None, "YYYY": None}

        self.name = None

    def read_file_name(self, name):
        """
        Reads a file name and extracts the parts based on the initial format.

        Args:
            name (str): The file name to be processed.

        Returns:
            dict: A dictionary containing the extracted parts of the file name.
        """
        self.name = name
        parts = name.split(self.delimiter)
        for i in range(len(parts)):
            self.base[self.init_format[i]] = parts[i]
        return self.base

    def rename_file(self, new_format=["YYYY", "MM", "DD"], new_delimiter="-"):
        """
        Renames the file based on a new format and delimiter.

        Args:
            new_format (list): The new format of the file name. Defaults to ['YYYY', 'MM', 'DD'].
            new_delimiter (str): The new delimiter used to separate the parts of the file name. Defaults to '-'.

        Returns:
            str: The renamed file name.
        """
        new_name = []
        for i in range(len(new_format)):
            new_name.append(self.base[new_format[i]])
        return new_delimiter.join(new_name)
