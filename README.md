# MAC address in Hardware -- only NIC have that MAC address 

<img src="mac.png">

### Uderstanding function 

<img src="func.png">

### TYpe of function in any programming lang 

<img src="typef.png">

## Best case calling and importing tricks for any Modules 

```
>>> 
>>> import  time
>>> del time 
>>> from  time  import ctime
>>> 
>>> ctime()
'Tue Jun 15 20:29:16 2021'
>>> 
>>> 
>>> import  time
>>> 
>>> time.ctime()
'Tue Jun 15 20:29:32 2021'
>>> 
>>> del time 
>>> from  time import sleep,ctime
>>> sleep(2)
>>> ctime()
'Tue Jun 15 20:29:55 2021'

```

