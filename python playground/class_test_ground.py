# 7amp

import cgi

given_string = "I think %s, and despite your opinion, %s, are perfectly normal things to do in public."

def sub1(s, d):
	return given_string % (s, d)	


# # print sub1("running", "shitting") 
# # # => "I think running is a perfectly normal thing to do in public."    
# # print sub1("sleeping", "drinking") 
# # # => "I think sleeping is a perfectly normal thing to do in public."




given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."

def sub_m(name, nickname):
    # sub_d = {'name': name,
    # 		 'nickname': nickname}
    return given_string2 % {"name": name,
    					   "nickname": nickname}


# # print sub_m("Mike", "Goose")


# User Instructions
# 
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
	# return s.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;').replace('"', '&quot;')
	return cgi.escape(s, quote = True)


print escape_html('>')
print escape_html('This is the <true> Test ">')
# print escape_html('<')
# print escape_html('"')
# print escape_html("&")
