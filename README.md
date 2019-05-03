# python-mailsearch
Check gmail (or other POP3) using python, and scan it for patterns.

<p>The username and password are read from .nosec</p>

<p>You may execute "./gmail.py test" to examine the regex patterns. It reads a plain text file called 'samplemail' which is supposed to be in CWD</p>

<p>Here is the expected test output:</p>
<pre>
Admins-MacBook-Pro:~ partapk$ ./script/gmail.py test
A: some value

B: KEY(key) = VALUE(another kind of value)

kv pair: Key = value

basic paren enclosure: (value x$323a0jwfaoia32!@#$wit ha ji456 )

matches:

[False, ['Key', 'value'], ['code', 'value x$323a0jwfaoia32!@#$wit ha ji456 '], False, False]
</pre>

<p>This is my output from the gmail server:</p>
<pre>
*cmd* 'STAT'
*stat* ['+OK', '117', '5602278']
(117, 5602278)
*cmd* 'LIST'
*cmd* 'RETR 113'
*cmd* 'RETR 114'
*cmd* 'RETR 115'
*cmd* 'RETR 116'
*cmd* 'RETR 117'
[False, ['Key', 'value'], ['value with things', 'value with things'], False, False]
</pre>
