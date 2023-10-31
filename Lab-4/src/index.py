def calculate_parity_bits(key):
    key_binary = ''.join(format(ord(symbol), '08b') for symbol in key)
    key_with_parity = ''
    for i in range(0, len(key_binary), 7):
        byte = key_binary[i:i + 7]
        parity_count = byte.count('1')
        if parity_count % 2 == 0:
            byte += '1'  # Odd parity bit
        else:
            byte += '0'  # Even parity bit
        key_with_parity += byte
    return key_with_parity


# Example usage
key = "abcdefgh"  # Replace with your 8-symbol DES key
k_plus = calculate_parity_bits(key)
print(f"The 64-bit key K+ is: {k_plus}")
