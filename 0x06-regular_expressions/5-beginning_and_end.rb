#!/usr/bin/env ruby
"""The regular expression must be exactly matching a string that starts with h ends with n"""


puts AGRV[0].scan(/^h\wn$/).join
