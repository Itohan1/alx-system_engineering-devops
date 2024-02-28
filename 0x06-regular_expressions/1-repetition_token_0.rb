#!/usr/bin/env ruby
"""Find the regular expression that will match these cases"""


puts ARGV[0].scan(/hbttn|hbtttn|hbttttn|hbtttttn/).join
