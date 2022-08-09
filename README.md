<h1>Bruteforcer - Password Spraying</h1>

<h2>Description</h2>
The project consists of a simple python script that allows the user to brute force the login page of the Damn Vulnerable Web Application (DVWA). The URL to the DVWA application is required. The script performs a password spraying attack thus a valid username and a wordlist of the potential password are required. The user also needs to enter the error message that pops up after a failed login. If the page requires a valid cookie session, the user can provide the cookie value. However, it is not required for the application to run.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Windows 10</b>
- <b>Linux</b>

<h2>Program walk-through:</h2>

<p>
Run the script: python3 .\bruteforce.py <br/>
<img src="https://imgur.com/12EVIj2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the DVWA login page URL:  <br/>
<img src="https://imgur.com/qn1zHma.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the username (default: admin):  <br/>
<img src="https://imgur.com/1iZE43S.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the file path to password wordlist:  <br/>
<img src="https://imgur.com/dQhaL1T.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter error message:  <br/>
<img src="https://imgur.com/ElckVlc.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter cookie if needed or skip<br/>
<img src="https://imgur.com/wXbScnN.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
Wait for proccess to complete:  <br/>
<img src="https://imgur.com/r1JvesX.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
