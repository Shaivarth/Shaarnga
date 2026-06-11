"""
Śārṅga (शार्ङ्ग) — Binary Cipher 
Custom encoding schema: each character is mapped to a
type-prefix + binary payload.

  00 + 5 bits  →  lowercase a–z  (offset 96)
  11 + 5 bits  →  uppercase A–Z  (offset 64)
  01 + 4 bits  →  digits 0–9
  10 + 8 bits  →  any other character (full ASCII ordinal)
"""


def encrypt(text: str) -> str:
    bits = []
    for ch in text:
        if ch.islower():
            bits.append("00" + format(ord(ch) - 96, "05b"))
        elif ch.isupper():
            bits.append("11" + format(ord(ch) - 64, "05b"))
        elif ch.isdigit():
            bits.append("01" + format(int(ch), "04b"))
        else:
            bits.append("10" + format(ord(ch), "08b"))
    return "".join(bits)


def decrypt(binary: str) -> str:
    i, out = 0, []
    while i < len(binary):
        tag = binary[i:i + 2]
        i += 2
        if tag == "00":
            out.append(chr(96 + int(binary[i:i + 5], 2))); i += 5
        elif tag == "11":
            out.append(chr(64 + int(binary[i:i + 5], 2))); i += 5
        elif tag == "01":
            out.append(str(int(binary[i:i + 4], 2))); i += 4
        elif tag == "10":
            out.append(chr(int(binary[i:i + 8], 2))); i += 8
        else:
            raise ValueError(f"Unknown type tag '{tag}' at position {i - 2}")
    return "".join(out)


def main():
    print("\n  Śārṅga  |  Binary Cipher\n")
    choice = input("  [E]ncrypt  /  [D]ecrypt  → ").strip().lower()

    if choice == "e":
        plaintext = input("  Enter text : ")
        print("\n  " + encrypt(plaintext) + "\n")
    elif choice == "d":
        binary = input("  Enter binary : ").strip()
        try:
            print("\n  " + decrypt(binary) + "\n")
        except ValueError as err:
            print(f"\n  Error: {err}\n")
    else:
        print("\n  Invalid choice. Use E or D.\n")


if __name__ == "__main__":
    main()