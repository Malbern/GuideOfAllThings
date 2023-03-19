# About
A cheat sheet to make Markdown and writing on GitHub easier.

***
<details open><summary><h1>Headers</h1></summary>
A way to have the section folded and unfolded, then just normal headers.

    <details id=0 open> <summary><h1>Header</h1></summary>
    Spam.
    </details>

<details id=0 open> <summary><h1>Header</h1></summary>
Spam.
</details>

    # Header 1
    ## Header 2
    ### Header 3
    #### Header 4
    ##### Header 5
    ###### Header 6

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
</details>

***
<details open><summary><h1>Text Formatting</h1></summary>
Change the way text looks and how it displays.

    *Italize* **Bold** ***Both***
    
    _Italize_ __Bold__ ___Both___

*Italize* **Bold** ***Both***

_Italize_ __Bold__ ___Both___
</details>

***
<details open><summary><h2>Links</h2></summary>
Linking to a URL or image.

    [Link](https://www.github.com)
    
    <p>This is an <a href=“http://example.com/“>example link</a>.</p>
    
    This is an [example link](http://example.com/ “With a Title”).
    
    ![The Sun](/Development/Web/Templates/Sun Face.png)
    
    [Reference Link][1] is the same link as [Reference Link][2]

    [1]: https://example.com
    [2]: https://example.com

[Link](https://www.github.com)

<p>This is an <a href=“https://example.com/“>example link</a>.</p>

This is an [example link](https://example.com/ “With a Title”).

![The Sun](/Development/Web/Templates/Sun Face.png)

[Reference Link][1] is the same link as [Reference Link][2]

[1]: https://example.com
[2]: https://example.com
</details>

<img src=“/Development/Web/Templates/Sun Face.png” alt=“alt text” title=“Title” />

***
<details open><summary><h1>Organization</h1></summary>
Get the info all in order.

## Lists
Different types and layouts of lists.

### Ordered List
Numbers the list, what comes after 1 doesn’t matter.

    1.
    *
    -
    +
 
1. 1
* 2
- 3
+ 4

***
### Unordered List
Just have dots making up the list.

    *
    - -
    +
    * [x]
    - [ ]
    + [ ] 
    
* 1
- - Outer
* [x] Checked
- [ ] Unchecked
+ [ ] Unchecked

***
### Ordered & Unordered List
A combined type of list that has numbers and dots.

<ol>
<li>Candy.</li>
<ul>
<li>Gum.</li>
<li>Booze.</li>
</ul></ol>

***
## Tables

First Header  | Second Header | Third Header |
 ———— | :————: | ————: |
Cell	  |   *Cell*	  |	  Cell	|
Cell  |   **Cell**	|	  Cell	|

| Rank | THING-TO-RANK |
|——:   |—————|
|     1|               |
|     2|               |
|     3|               |

***
## Spacers

    ***
*** 

    - - - -
- - - -
</details>

***
<details open><summary><h1>Code Blocks</h1></summary>
A way to present code so that it’s a lot more visible.

* An indentation is 4 spaces, it makes a code block.

	Code
	block.

* Use >For code blocks. Only lines with text need >before the code.

>Other code block.

>Skipped line.

> Or a quote.

* ‘ Does not work. It must be a `, a word(s) with a backtick on each side would identify 1 word or multiple.

`<code>` spans are delimited
by backticks.
  
* ``` before and and after the text would identify the whole thing.

```
You can include literal backticks
like this.
```

<blockquote>
<p>Yes</p>
    <p>Test.</p>
</blockquote> 
</details>

***
<details open><summary><h1>References</h1></summary>

Reference this. [^1]

Testing [^2]

[^1]: Always goes to bottom.

[^2]: Second.

</details>

***
details open><summary><h1>Extra</h1></summary>

Experiment with lists.

- A
- - B
- * + C
 - D
 - 1. E
  * F

~~~
Code Fence
~~~

```
<
 >.   Yeah 
  -
```
Test

<table><tr><td>
<pre>
**Hello**,

_world_.
</pre>
</td></tr></table>

|test|
|:———|