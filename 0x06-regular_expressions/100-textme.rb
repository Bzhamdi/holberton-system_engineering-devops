#!/usr/bin/env ruby
#find_and_print_word
#\:print special character
#.*? : anything > 1
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
