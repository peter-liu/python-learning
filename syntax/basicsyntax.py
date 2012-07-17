'''
Created on 2012-7-17

@author: Administrator
'''

'''
Notation
'''
# variable name
# letter (letter | "_")* ; letter = "a"..."z"

'''
Lexical Analysis

1. python program is read by a "parser",lexical analyzer breaks a file into "tokens", and then "parser" read it
2. character set:
    2.1 python uses the 7-bit ASCII character set for program text
    2.2 an "encoding declaration" can be used to indicate that string literals and comments use a different one(since python 2.3)
        it will warm you if it finds 8-bit characters. those warm should be corrected by declaring explicit encoding or escape them
        
3*.Line structure (program is divided into a number of logic lines)
    3.1 logic lines:
            logical line is represented by a token named 'NEWLINE'
            logical line is constructed from one or more physical lines by following the explicit or implicit line joining rules
    3.2 physical lines
            is a sequence of characters terminated by an end-of-line sequence(different by os), but all of those forms can used equally, regardless of platform. because source code passed to pythons APIs using the standard C conventions for new line(\n | ASCII LF)
    3.3 comment
            starts with a hash character(#), end of physical line
            if a comment signifies the end of the logical line unless the implicit line joining rules are invoked, comments are ignored(they are not tokens)
            
            3.3.1 encoding declarations
                first line or second line, match the regular expression "coding[=]\s*[-\w.]+"
                e.g.  # -*- coding: encoding-name -*-
                if the first bytes of the file is the UTF-8 form mark.the declared file encoding is UTF-8
                string literals are converted to unicode for syntactical analysis, then converted back to their own encoding before interpretation? starts
    3.4 line join
            3.4.1    explicit line join
                        two or more physical line may be joined into logical lines using backslash(\)
                        a line ending in a backslash does not continue a comment, a token except  but can continue a string literals.
            3.4.2    implicit line join
                        expression in () or [] or {} can split a logic line to two or more physical lines.
                        implicitly continued lines can carry comments
                        the indentation of implicitly joined lines is not important
                        implicitly continued line can occur within triple-quoted string without any comment
    3.5 blank lines
            constructed by spaces, tabs,formfeeds and possibly a comment( no NEWLINE taken generated)
            in the standard implementation, an entirely blank logical line terminates a multi-line statement. 
            
    3.6* Indentation
            leading white space ( spaces and tabs) at the beginning of a logical line is used to compute the indentation level(determine the grouping of statements).
            it's not unwise to use mixture of spaces and tabs for the indentation in a single source file, because tabs will be converted to different length on different platform.
            formfeed characters at the start of line will be ignored for the indentation calculations( formfeed occurring elsewhere in the leading whitespace have an undefined effect, eg. clear the indentation )
            the indentation levels of consecutive lines are used to generate INDENT and DEDENT tokens
    3.7 Whitespace between tokens
            except leading the logic line, white spaces are used interchangeable to separate tokens
            e.g., ab is one token, a b are two tokens
    3.8 Other tokens
            beside NEWLINE,INDENT and  DEDENT, the following categories of tokens exist: identifiers,keywords,literals,operators and delimiters
            whitespace are not tokens,but serve to delimit tokens

4 identifiers and keywords
        identifiers : a.k.a names 
                identifier ::=  (letter|"_") (letter | digit | "_")*
                letter     ::=  lowercase | uppercase
                lowercase  ::=  "a"..."z"
                uppercase  ::=  "A"..."Z"
                    digit      ::=  "0"..."9"
        keywords:
                and       del       from      not       while
                as        elif      global    or        with
                assert    else      if        pass      yield
                break     except    import    print
                class     exec      in        raise
                continue  finally   is        return
                def       for       lambda    try
    
    4.1 reserved classed of identifiers
        classes are identified by the patterns of leading and trailing underscore
        
            _* 
                not imported by [from module import *.], 
                the special identifier _ is used in the interactive interpreter to store the result of the last evaluation, it is stored in the __builtin__ module
                when not in interactive mode? _ has no special meaning and it's not defined. see section[http://docs.python.org/reference/simple_stmts.html#import]
                often used in conjuncation with i18n,refer to the gettext[http://docs.python.org/library/gettext.html#module-gettext] module 
            
            __*__
                system-defined names, are defined by the interpreter and its implementation(current system names are discussed in the Special method names[http://docs.python.org/reference/datamodel.html#specialnames])
                in any context, using __*__ names does not follow explicitly documented use( it's a standard , not compulsive)
            
            __*
                class-private names, re-written to use a mangled form to avoid name clashes between "private" attributes of base and derived class, see section Identifiers(Name)[http://docs.python.org/reference/expressions.html#atom-identifiers]
                it act on attributes or classes??

5.Literals
    literals are notations for constant values of some ?built-in? types
    
    5.1 string literals
            stringliteral   ::=  [stringprefix](shortstring | longstring)
            stringprefix    ::=  "r" | "u" | "ur" | "R" | "U" | "UR" | "Ur" | "uR"
                                 | "b" | "B" | "br" | "Br" | "bR" | "BR"
            shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
            longstring      ::=  "'''" longstringitem* "'''"
                                 | '"""' longstringitem* '"""'
            shortstringitem ::=  shortstringchar | escapeseq
            longstringitem  ::=  longstringchar | escapeseq
            shortstringchar ::=  <any source character except "\" or newline or the quote>
            longstringchar  ::=  <any source character except "\">
            escapeseq       ::=  "\" <any ASCII character>
        
        string prefix:
            R|r : raw strings , the value is what it look like.
            U|u : unicode strings, there are some escaped character in literalu
            B|b : ignored in python 2.x, it indicates that the literal should become a bytes literal in python 3(e.g. when code is automatically cnverted with 2to3??)
            
            A 'U|u' or 'B|b' prefixe may be followed by an "R|r" prefix??
        
        triple-quoted strings
            unescaped newlines and quotes are allowed(except three unescaped quotes )
        
    5.2 string literal concatenation
        multiple adjacent string literals(terminate by whitespace and possibly using different quoting form.) are allowed
    
    5.3 Numeric literals
        four types: plain integers,long integers,floating integers,imaginary numbers.
            they are no complex literals(complex numbers can be formed by adding a real number and an imaginary number?)
        note that literals don't include a sign, -1 is actually a expression composed of the operator "-" and the literal "1" 
        
        5.3.1 integer and long integer
            longinteger    ::=  integer ("l" | "L")
            integer        ::=  decimalinteger | octinteger | hexinteger | bininteger
            decimalinteger ::=  nonzerodigit digit* | "0"
            octinteger     ::=  "0" ("o" | "O") octdigit+ | "0" octdigit+
            hexinteger     ::=  "0" ("x" | "X") hexdigit+
            bininteger     ::=  "0" ("b" | "B") bindigit+
            nonzerodigit   ::=  "1"..."9"
            octdigit       ::=  "0"..."7"
            bindigit       ::=  "0" | "1"
            hexdigit       ::=  digit | "a"..."f" | "A"..."F"
        5.3.2 imaginary literals ???
6 Operators
    +       -       *       **      /       //      %
    <<      >>      &       |       ^       ~
    <       >       <=      >=      ==      !=      <>
    <> and != are alternate spellings.!= is preferred

7 Delimiters
        (       )       [       ]       {       }      @
        ,       :       .       `       =       ;
        +=      -=      *=      /=      //=     %=
        &=      |=      ^=      >>=     <<=     **=
    the delimiters at 3rd and 4th line, serve lexically as delimiters but also perform an operation
    
        ' " # \
    describe on above
        
        $ ?
    not allowed in in python. only can occur in a literal.
    
'''

