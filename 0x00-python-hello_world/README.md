<h1 class="gap">0x00. Python - Hello, World</h1><div class="gap" id="project-description">
<p><img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg" style=""/></p>
<h2>Author’s disclaimer</h2>
<pre><code>Welcome to the Python world!

After 3 months of C, you will start Python today.
The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume, CTO at Holberton
</code></pre>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="/rltoken/fX5geNeDFcCtootbB_MqCQ" target="_blank" title="The Python tutorial">The Python tutorial</a> (<em>only the first three chapters below</em>)

<ul>
<li><a href="/rltoken/JnsZOCXrWDkZn6iMo1uuFg" target="_blank" title="Whetting Your Appetite">Whetting Your Appetite</a> </li>
<li><a href="/rltoken/AejXr_G-d8CSITEtpvwpRg" target="_blank" title="Using the Python Interpreter">Using the Python Interpreter</a> </li>
<li><a href="/rltoken/lUBuPMNcox9EqJ1Q3oVesQ" target="_blank" title="An Informal Introduction to Python">An Informal Introduction to Python</a> (<em>Read up until “3.1.2. Strings” included</em>)</li>
</ul></li>
<li><a href="/rltoken/z6mk3Yep2tJVSF6KsBAYrg" target="_blank" title="How To Use String Formatters in Python 3">How To Use String Formatters in Python 3</a> </li>
<li><a href="/rltoken/gYgGXOth8N16KjUpXgO1uQ" target="_blank" title="Learn to Program">Learn to Program</a> </li>
<li><a href="/rltoken/BMIjFOY7HvWHSjHfNrkzPg" target="_blank" title="PEP 8 -- Style Guide for Python Code">PEP 8 – Style Guide for Python Code</a> </li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="/rltoken/gcf9f4p0O8LJk9lrruE0bg" target="_blank" title="explain to anyone">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>Who created Python</li>
<li>Who is Guido van Rossum</li>
<li>Where does the name ‘Python’ come from</li>
<li>What is the Zen of Python</li>
<li>How to use the Python interpreter</li>
<li>How to print text and variables using <code>print</code></li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Holberton Python coding style and how to check your code with <code>PEP 8</code></li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file at the root of the <code>holbertonschool-higher_level_programming</code> repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version <code>1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>
<h3>Shell Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 14.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>wc -l file</code> should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>All your files must be executable</li>
</ul>
<h3>C Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code></li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" target="_blank" title="betty-style.pl">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" target="_blank" title="betty-doc.pl">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don’t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>
<h2>More Info</h2>
<h3>Zen</h3>
<pre><code>The Zen of Python, by Tim Peters

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
</code></pre>
<h3>Install PEP8</h3>
<p><code>Pycodestyle</code> is now the <a href="/rltoken/D67mmHg2X9ZI7QHlQxayyw" target="_blank" title="new standard of Python style code">new standard of Python style code</a>, but at school we will use <code>PEP8</code>, <code>version 1.7.*</code>
Don’t worry, <code>pycodestyle</code> is based on <code>pep8</code>.
The hardest part now is to install it for Python 3:</p>
<h4>Using Pip3</h4>
<h5>Install Pip3</h5>
<pre><code>$ sudo apt-get install python3-pip
</code></pre>
<h4>Install Pep8</h4>
<pre><code>$ sudo apt-get install python3-pep8
$ sudo apt-get install python3-pip
$ sudo pip3 install -Iv pep8==1.7.0
</code></pre>
<p>-&gt; Make sure you have the right version</p>
<pre><code>$ pep8 --version
1.7.0
$
</code></pre>
<p>Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.</p>
<p><br/>
<br/>
<img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg" style=""/></p>
</div>actualization