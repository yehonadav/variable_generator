Variable Generator
![logo](https://www.qaviton.com/wp-content/uploads/logo-svg.svg)  
[![version](https://img.shields.io/pypi/v/variable_generator.svg)](https://pypi.python.org/pypi)
[![open issues](https://img.shields.io/github/issues/yehonadav/variable_generator)](https://github/issues-raw/yehonadav/variable_generator)
[![downloads](https://img.shields.io/pypi/dm/variable_generator.svg)](https://pypi.python.org/pypi)
![code size](https://img.shields.io/github/languages/code-size/yehonadav/variable_generator)  

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
