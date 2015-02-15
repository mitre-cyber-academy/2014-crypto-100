Name: SHA-1 extraction

Description: The user is presented with four different files. A jpeg, a bin, txt, and a file with no extension. All of these files contain incorrect SHA-1 keys. However, one of these files contains one correct key.

To solve: The simplest way to solve this challenge is type the following into terminal: grep -Eo [0-9a-f]{40} *