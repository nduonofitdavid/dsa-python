from arrayadt import ArrayStack

def is_matched(expr):
    """Return True if all delimiters are properly matched; false otherwise."""
    lefty = '({['
    righty = ']})'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


print(is_matched('(({]))'))


# if it is a character you use with the in operator on a string object it takes constant time.

raw_html = """
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
"""
# to cover self closing tags, we create a hash of all the self closing tags, and index them, we can store them in a set
# for constant time indexing.
# this is not necessary, we can just check if it ends with / that is when we ignore the <>, and if it does, we skip that iteration.
# so this does not work for all tags, bearing in mind that some self closing tags dont end in /, / only happens mostly in react code.
# so we have consider the hashing option.
# this algorithm does not also consider instances of where a > could be included in the content of an html tag.

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; false otherwise"""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

print(is_matched_html(raw_html))