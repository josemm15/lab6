def password_encoder(password):

    if len(password) != 8 or not password.isdigit():
        return "Error: Input must be an 8-digit string."

    encoded_string = "".join([str((int(char) + 3) % 10) for char in password])

    return encoded_string
def password_decoder(encoded_password):
    # Ensure the input is exactly 8 digits long
    if len(encoded_password) != 8 or not encoded_password.isdigit():
        return "Error: Input must be an 8-digit string."
    decoded_string = "".join([str((int(char) - 3) % 10) for char in encoded_password])
    return decoded_string

def print_menu():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_option = int(input("\nPlease enter an option: "))
        if menu_option == 1:
            #
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded_password = password_encoder(password)
        elif menu_option == 2:
            # Decoding option
            if encoded_password:
                # Decode the encoded password by reversing the shift
                original_password = password_decoder(encoded_password)  # Applying encode twice reverses the shift
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet.")


        elif menu_option == 3:
            break
# Print menu
def main():
    print_menu()

if __name__ == '__main__':
    main()