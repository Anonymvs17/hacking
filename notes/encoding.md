# encoding in base64
`echo https://www.hackthebox.eu/ | base64`

# decoding base64
`echo N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz | base64 -d`

# hex
16 characters only: 0-9 and a-f.

## hexencode
echo https://www.hackthebox.eu/ | xxd -p

## hexdecode
echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r

## detect with encoding
https://www.boxentriq.com/code-breaking/cipher-identifier
