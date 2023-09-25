# V O I D format

## Description

**⌜ V O I D format ⌟** is the data format that inherits the best features of **JSON**, **YAML**, **CSV** formats. Makes it easier to write and read data, both by humans and by programs.

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
- Array
- Dictionary
- Null

## Data Separator

- Spaces ```" "```
- Tabs ```"\t"```
- Newlines ```"\r\n"```
  
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
'very 
 very
 very long text'
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
"multiline
text"
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
1 text true false null
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
[1 2 3]
```

</td>
<td>

```json
[1, 2, 3]
```

</td>
</tr>

<tr>
<td>

```
1 12.34 Name
2 56.78 "Other name"
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
[name: text "another name": 123]
```

</td>
<td>

```json
{"name": "text", "another name": 123}
```

</td>
</tr>

<tr>
<td>

```
name: text
other name: 123
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
multiline text
  "text
  next
  line"
bool
  true
empty array: []
value array: [null]
array
  1
  2
  3
dict
  name
    value
  other name
    other value
mixed: [1 [2 3]
  name
    value
]
```

</td>
<td>

```json
{
  "name": "text",
  "multiline text": "text\nnext\nline",
  "bool": true,
  "empty array": [],
  "value array": [null],
  "array": [
    1,
    2,
    3
  ],
  "dict": {
    "name": "value",
    "another name": "other value"
  },
  "mixed": [1, [2, 3], {
    "name": "value"
  }]
}
```

</td>
</tr>
</table>

## V O I D lang
**[⌜ V O I D lang ⌟](https://github.com/voidspawner/void.lang)** is the language for rapidly creating applications in the **JSON format**. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.
