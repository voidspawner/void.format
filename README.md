# V O I D format

## Description

**⌜ V O I D format ⌟** is the data format that inherits the best features of **JSON**, **YAML**, **CSV** formats. Makes it easier to write and read data, both by human and by program.

**The project is in the process of development. Code and description are subject to change and inconsistency.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

## MIME Type

```application/void```

## File Extension

- ```.void``` (preferred)
- ```.txt```

## Value Types

- Text
- Number
- Boolean
- List
- Dictionary
- Null
- Binary

## Data Separator

- Space ```" "```

## Data Indent

- Spaces ```" "```
- Tabs ```"\t"``` (preferred)

## Example

<table>
<tr>
<th>V O I D format</th>
<th>JSON</th>
</tr>
</tr>
  
<tr>
<td>

```
text
```

</td>
<td>

```json
"text"
```

</td>
</tr>

<tr>
<td>

```
text\ with\ space
```

</td>
<td>

```json
"text with space"
```

</td>
</tr>

<tr>
<td>

```
"text with space"
```

</td>
<td>

```json
"text with space"
```

</td>
</tr>

<tr>
<td>

```
text with space
```

</td>
<td>

```json
"text with space"
```

</td>
</tr>

<tr>
<td>

```
'
very 
very 
very long text
```

</td>
<td>

```json
"very very very long text"
```

</td>
</tr>

<tr>
<td>

```
"
multiline
text
```

</td>
<td>

```json
"multiline\ntext"
```

</td>
</tr>

<tr>
<td>

```
c:\Users\name\Desktop
```

</td>
<td>

```json
"c:\\Users\\name\\Desktop"
```

</td>
</tr>

<tr>
<td>

```
"text\r\n\t\u1234\"\\"
```

</td>
<td>

```json
"text\r\n\t\u1234\"\\"
```

</td>
</tr>

<tr>
<td>

```
123
```

</td>
<td>

```json
123
```

</td>
</tr>

<tr>
<td>

```
-123
```

</td>
<td>

```json
-123
```

</td>
</tr>

<tr>
<td>

```
0.123
```

</td>
<td>

```json
0.123
```

</td>
</tr>

<tr>
<td>

```
100_000_000
```

</td>
<td>

```json
100000000
```

</td>
</tr>

<tr>
<td>

```
100 000 000
```

</td>
<td>

```json
100000000
```

</td>
</tr>

<tr>
<td>

```
0.1e2
```

</td>
<td>

```json
0.1e2
```

</td>
</tr>

<tr>
<td>

```
h0A
```

</td>
<td>

```json
10
```

</td>
</tr>

<tr>
<td>

```
b1001
```

</td>
<td>

```json
9
```

</td>
</tr>

<tr>
<td>

```
true
```

</td>
<td>

```json
true
```

</td>
</tr>

<tr>
<td>

```
false
```

</td>
<td>

```json
false
```

</td>
</tr>

<tr>
<td>

```
null
```

</td>
<td>

```json
null
```

</td>
</tr>

<tr>
<td>

```
1
text
true
false
null
```

</td>
<td>

```json
[1, "text", true, false, null]
```

</td>
</tr>

<tr>
<td>

```
:
1 12.34 Name
2 56.78 Other\ name
```

</td>
<td>

```json
[
  [1, 12.34, "Name"],
  [2, 56.78, "Other name"]
]
```

</td>
</tr>

<tr>
<td>

```
:,
1,12.34,Comma separator
2,56.78,Other name
```

</td>
<td>

```json
[
  [1, 12.34, "Comma separator"],
  [2, 56.78, "Other name"]
]
```

</td>
</tr>

<tr>
<td>

```
name
  text
other name
  123
```

</td>
<td>

```json
{
  "name": "text",
  "other name": 123
}
```

</td>
</tr>

<tr>
<td>

```
name
  text
multiline text "
  text
  next
  line
text in line '
  text
  in
  line
bool
  true
empty list:
with empty value
  |""|
list
  1
  2
  3
table:
  1 12.34 Name
  2 56.78 Other\ name
dictionary
  name
    value
  other name
    other value
code:
  . Hi\ World
  = expr 1 + 1 * 2 * |cos 0.5|
  request
    url
      https://site.com
    header
      User
        12345
      Key
        12345
    param
      id
        12345
    done:
      . {text}
      . {code}
```

</td>
<td>

```json
{
  "name": "text",
  "multiline text": "text\nnext\nline",
  "text in line": "textinline",
  "bool": true,
  "empty list": [],
  "with empty value": [""],
  "list": [1, 2, 3],
  "table": [
    [1, 12.34, "Name"]
    [2, 56.78, "Other name"]
  ],
  "dictionary": {
    "name": "value",
    "other name": "other value"
  },
  "code": [
    [".", "Hi World"],
    ["=", "expr", 1, "+", 1, "*", 2, "*", ["cos", 0.5]],
    ["request", {
      "url": "https://site.com",
      "header": {
        "User": 12345,
        "Key": 12345
      },
      "param": {
        "id": 12345
      },
      "done": [
        [".", "{text}"],
        [".", "{code}"]
      ]
    }]
  ]
}
```

</td>
</tr>

</tr>

<tr>
<td>

```
binary data length 10
  :10 
```

</td>
<td>

```json
{
  "binary data length 10": "\u0003..."
}
```

</td>
</tr>

<tr>
<td>

```
gzip + base64
  :eNoDAAAAAAE=
```

</td>
<td>

```json
{
  "gzip + base64": "text text text ..."
}
```

</td>
</tr>

<tr>
<td>

```
base64
  :dGV4dCB0ZXh0IHRle...
```

</td>
<td>

```json
{
  "base64": "text text text text ..."
}
```

</td>
</tr>

<tr>
<td>

```
reference
  :{dictionary.other name}
```

</td>
<td>

```json
{
  "reference": "other value"
}
```

</td>
</tr>

<tr>
<td>

```
|short\ form 1 2 3|name:value||
```

</td>
<td>

```json
["short form",1,2,3,{"name":"value"}]
```

</td>
</tr>

</table>

## V O I D lang
**[⌜ V O I D lang ⌟](https://github.com/voidspawner/void.lang)** is the language for rapidly creating applications in the **JSON format**. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

## V O I D engine
**[⌜ V O I D engine ⌟](https://github.com/voidspawner/void.lang#game-engine)** is a pre-compiled **V O I D spawner** game for rapidly creating games, apps and animation in **V O I D lang**.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D ai
Generate **images・videos・texts・assets**. A limited number of uses are available for free. To use extra **V O I D ai** you can **pay** with **⦵ voids** digital currency.

## V O I D voids
Digital currency used in the **V O I D ecosystem**.

- Name ```voids```
- Symbol ```⦵```
- Exchange rate ```⦵ 1``` = ```$ 1``` = ```USD₮ 1```

The currency is also a **spawner**. Every month the profit is distributed among the **voids** holders. The number of voids increases proportionally and can be withdrawn to other digital currencies.

## V O I D social
**[⌜ V O I D social ⌟](https://voidsp.com)** is a **social network** for messaging, sharing apps, games, images, videos and other content. Buy and sell, find job, crypto exchange, transfer **V O I D voids** and more other.
