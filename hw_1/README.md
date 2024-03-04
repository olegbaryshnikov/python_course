The file `.\artifacts\test.txt` is copy of this README.md

### Task 1.1
**Reference commands:**
```
# For file:
root@a3f1a3fa11bd:/# nl -b a python_course/hw_1/test_file.txt
     1  line1
     2  line2
     3  line3
     4
     5  line4
     6  line5
     7  line6
     8  line7
     9     
    10  line8
    11  line9
    12  line10
    13  line11
    14  line12
    15  line13
    16
    17  line14
    18  line15
    19  line16
    20
    21  line17
    22  line18
    23  line19
    24  line20
    25  line21
    26  line22
    27  line23
    28  line24
    29  line25

```
```
# For user inputs:
root@a3f1a3fa11bd:/# nl -b a
123
     1  123
abc
     2  abc
1
     3  1
2
     4  2
3
     5  3
eee
     6  eee
qqq
     7  qqq
aaa
     8  aaa
   
     9     

    10
sss
    11  sss
ddd
    12  ddd
fff
    13  fff

```
  
**Test for file:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 nl python_course/hw_1/test_file.txt
     1  line1
     2  line2
     3  line3
     4  
     5  line4
     6  line5
     7  line6
     8  line7
     9     
    10  line8
    11  line9
    12  line10
    13  line11
    14  line12
    15  line13
    16  
    17  line14
    18  line15
    19  line16
    20  
    21  line17
    22  line18
    23  line19
    24  line20
    25  line21
    26  line22
    27  line23
    28  line24
    29  line25

```
  
**Test for user inputs:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 nl                                 
123
     1  123
abc
     2  abc
1
     3  1
2
     4  2
3
     5  3
eee
     6  eee
qqq
     7  qqq
aaa
     8  aaa
   
     9     

    10  
sss
    11  sss
ddd
    12  ddd
fff
    13  fff

```

-----

### Task 1.2
**Reference commands:**
```
# For single file:
root@a3f1a3fa11bd:/# tail python_course/hw_1/test_file.txt

line17
line18
line19
line20
line21
line22
line23
line24
line25
```
```
# For multiple files:
root@a3f1a3fa11bd:/# tail python_course/hw_1/test_file.txt python_course/hw_1/another_test_file.txt                         
==> python_course/hw_1/test_file.txt <==

line17
line18
line19
line20
line21
line22
line23
line24
line25
==> python_course/hw_1/another_test_file.txt <==
wtq
tqtqtq
q
q
tailqwt
qwt
qqqtqt
gagaage
userth
gaagedhdh
```
```
# For user inputs:
root@a3f1a3fa11bd:/# tail
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
11
12
13
14
15
16
17
18
19
20

```
  
**Test with file:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 tail python_course/hw_1/test_file.txt

line17
line18
line19
line20
line21
line22
line23
line24
line25
```

**Test with multiple files:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 tail python_course/hw_1/test_file.txt python_course/hw_1/another_test_file.txt          
==> python_course/hw_1/test_file.txt <==

line17
line18
line19
line20
line21
line22
line23
line24
line25
==> python_course/hw_1/another_test_file.txt <==
wtq
tqtqtq
q
q
tailqwt
qwt
qqqtqt
gagaage
userth
gaagedhdh
```
  
**Test with user inputs:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 tail
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
11
12
13
14
15
16
17
18
19
20

```


### Task 1.3

**Reference commands:**
```
# For single file:
root@a3f1a3fa11bd:/# wc python_course/hw_1/test_file.txt                                         
 28  25 200 python_course/hw_1/test_file.txt
```
```
# For multiple files:
root@a3f1a3fa11bd:/# wc python_course/hw_1/test_file.txt python_course/hw_1/another_test_file.txt
 28  25 200 python_course/hw_1/test_file.txt
 21  22 159 python_course/hw_1/another_test_file.txt
 49  47 359 total
```
```
# For user inputs:
root@a3f1a3fa11bd:/# wc
1
2
3
      3       3       6
root@a3f1a3fa11bd:/# wc
1
2
3      2       3       5
root@a3f1a3fa11bd:/# wc
1 1         
222    22
33333 3
      3       6      22
```

**Test with file:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 wc python_course/hw_1/test_file.txt                                         
 28  25 200 python_course/hw_1/test_file.txt
```

**Test with multiple files:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 wc python_course/hw_1/test_file.txt python_course/hw_1/another_test_file.txt
 28  25 200 python_course/hw_1/test_file.txt
 21  22 159 python_course/hw_1/another_test_file.txt
 49  47 359 total
```
  
**Test with user inputs:**
```
root@a3f1a3fa11bd:/# python3 python_course/hw_1 wc
1
2
3
      3       3       6
root@a3f1a3fa11bd:/# python3 python_course/hw_1 wc
1
2
3      2       3       5
root@a3f1a3fa11bd:/# python3 python_course/hw_1 wc
1 1
222    22
33333 3
      3       6      22
```