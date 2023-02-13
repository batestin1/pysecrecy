
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=Pysecrecy%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center"> Pysecrecy </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> A python project for encrypting messages. can be used as a basis for creating a simple cryptographic system for encrypting passwords and tokens, for example.
In short it is an implementation of a text encoding/decoding class, where the original text is transformed into asterisks * and can be decoded back to the original text. </p>

>> <h3> How install </h3>

```
pip install pysecrecy

```
>> <h3> How Works </h3>

```
from pysecrecy import *

secret = Pysecrecy("Batatinha")

print(secret.encode()) # "***** *****"

secret.text = secret.decode()
print(secret.text) # "Batatinha"

```
    