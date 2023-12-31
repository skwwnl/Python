alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(direction, start_text, shift_amount):
  end_text = ""
  for letter in start_text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift_amount
      if new_position > 25:
        new_position -= 26
    elif direction == "decode":
      new_position = position - shift_amount
      if new_position < 0:
        new_position += 26
    end_text += alphabet[new_position]
  print(f"The {direction} text is {end_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction, text, shift)