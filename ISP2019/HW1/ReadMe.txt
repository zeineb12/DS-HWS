STEPS TAKEN TO FIND THE TOKENS:

Exercise 1:
-I inspected the source code of the web page.
-I noticed the "superencryption" function and noticed that the correct password is the username encrypted with this function and "mySecureOneTimePad".
-I used the function to encrypt my epfl email address and got the correct password.

Exercise 2:
-Using the hint given, I noticed there was a cookie which is saved on my browser when I open the webpage.
-I installed the "EditThisCookie" extension on Chrome.
-I used decryption base64 to decrypt the content.
-The last word was "user", I changed that to "administrator", encrypt again.
-After modifying the cookie and loading the page again, the token appeared.

Exercise3:
-I followed the installation steps.
-Connect to the attacker docker container.
-Following the examples of the documentation provided of NetfilterQueue and the instructions to using Scapy, I was able to write the interceptor.py so that it intercepts all packets which have destination port 80 and with layer Raw and display those packets.
-I noticed a packet corresponding to "shipping" and copied the product description.
-I used the Requests library as suggested to create a packet with the right payload and headers and send it to the website -> I received a packet with the token in the payload.

-The script can be run using:
docker exec -it attacker python3 shared/interceptor_ex3.py

Exercise4:
-I kept the same interceptor script but this time I looked at the "transaction" packets to find the secrets.
-Using the Requests library again, I sent a packet with the secrets in the payload -> I received a packet with the token in the payload.

-The script can be run using:
docker exec -it attacker python3 shared/interceptor_ex4.py
