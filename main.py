from code import encode, decode

print('Choose:')
print('1. Encode')
print('2. Decode')
choice = input()
if choice == '1':
    str_to_encode = input('Enter a tring to encode: ')
    encoded_str = encode(str_to_encode)
    print('Encoded string: ' + encoded_str)
elif choice == '2':
    str_to_decode = input('Enter a tring to decode: ')
    decoded_str = decode(str_to_decode)
    print('Decoded string: ' + decoded_str)


