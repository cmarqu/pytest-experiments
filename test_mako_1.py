#! /usr/bin/env python3

from mako.template import Template 

with open("some_template.mako", "w") as f: 
    f.write("hello world") 

t = Template(filename="some_template.mako", module_directory='data') 

print(t.render()) 
