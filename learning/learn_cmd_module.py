#!/usr/bin/python3

import sys
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(MyHbnb)'
    def do_create(self, line):
        print("i have created", line)
    def precmd(self, line):
        if not sys.stdin.isatty():
            print()
        #line = 'create iliass'
        #print(f'{line} is the command line ')
        #command, other = line.split(" ")
        #print(command)
        #print(other)
        #line = command+' shoes'
        if "." in line:
            line = line.replace(".", " ").replace("()", "")
            line = line.split(" ")
            line = line[1]+" "+line[0]
        print(line)
        return cmd.Cmd.precmd(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
