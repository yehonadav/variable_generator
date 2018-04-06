Variable_Generator


variable_generator is a small module to support automation

of generating valid python variable names from external data.

It is designed as a service to be used by other programs

that would parse through data and need to translate that data to usable python code.


Installing

Install and update using pip:

pip install -U variable_generator

A Simple Example


from variable_generator.name_generator import generate_valid_variable_name

raw_data = "123_ $%^ ששthis_is_var1   "

var1 = generate_valid_variable_name(self.testing_data['string1'])


> num123_dollar_percent_circumflex_15131513this_is_var1
