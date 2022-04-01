OperatorTable addAssignOperator(":", "atPutPair")

Builder := Object clone
Builder depth ::= 0;

curlyBrackets := method(
    attr := list

    call message arguments foreach(pair,
        attr append(self doString(pair asString))
    )
    return(attr)
)

atPutPair := method(name, value,
    attr := Map clone

    attr atPut("name", name)
    attr atPut("value", value)

    return(attr)
)

Builder isAttr := method(message,
    return((message asString findSeq("curlyBrackets")) == 0)
)

Builder forward := method(
    indent := ("    " repeated(self depth))
    argList := call message arguments

    if(self isAttr(argList at(0)),
        attr := argList removeFirst
        attrList := self doMessage(attr)

        // This part is nasty, but it gets the job done. Probably much better ways of doing this
        writeln(indent, "<", call message name, " ", attrList at(0) at("name") exSlice(1, ((attrList at(0) at("name") size)) - 1), "=\"", attrList at(0) at("value"), "\">"),

    //else
        writeln(indent, "<", call message name, ">")
    )
    self setDepth(self depth + 1)

    argList foreach(args,
        content := self doMessage(args)
        if(content type == "Sequence",
            writeln(indent, "    ", content)
        )
    )
    self setDepth(self depth - 1)

    writeln(indent, "</", call message name, ">")
)

Builder  languages(
        language({"good": "false"}, name("Io")),
        language({"good": "true"}, name("Lua")),
        language({"good": "false"}, name("JavaScript"))
