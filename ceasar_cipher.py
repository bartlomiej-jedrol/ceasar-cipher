alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']

run_again = True
while run_again == True:
    direction = input("Provide direction - (encrypt) or (decrypt): ")
    text = input("Provide text: ")
    shift = int(input("Provide shift: "))

    def ceasar(input_direction, input_text, shift_amount):
        print(shift_amount)
        encrypted_text = ""

        if input_direction == "decrypt":
            shift_amount *= -1

        for char in input_text:
            if char not in alphabet:
                encrypted_text += char
            else:
                # Get current letter's index.
                index = alphabet.index(char)
                # Set a new index.
                new_index = index + shift_amount
                # Check if exceeds he alphabet list.
                nr_exceeds_alpha = int((abs(new_index) + shift) / len(alphabet)-1)
                # Extend the alphabet list if range is excedeed.
                if nr_exceeds_alpha > 0:
                    for _ in range(nr_exceeds_alpha): 
                        alphabet.extend(alphabet)
                # Set a new letter.
                new_char = alphabet[new_index]
                # Add the letter to encrypted text.
                encrypted_text += new_char
        print(encrypted_text)

    ceasar(direction, text, shift)

    run_again_input = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if run_again_input == "no":
        run_again = False