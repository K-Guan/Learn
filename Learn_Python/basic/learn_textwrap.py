#!/usr/bin/env python3
import textwrap

# textwrap.shorten
print(textwrap.shorten("Hello  world!", width=11))
print(textwrap.shorten("Hello  world! This is a test", width=25))
print('\n')

# textwrap.dedent
print(textwrap.dedent("""\
                      Proper indentation
                      with multiline strings"""))
print('\n')

# textwrap.fill and textwrap.dedent
print(textwrap.fill(textwrap.dedent("""\
        The Zen of Python, by Tim Peters

        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
        """), 40))
print('\n')

# textwrap.wrap
print(textwrap.wrap("This function can split string"
                    "to a list by width like this", 20))

print(textwrap.wrap("This function can split string"
                    "to a list by width like this", 20)[0])
print('\n')
