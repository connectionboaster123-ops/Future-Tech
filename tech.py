import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("Phone number Validation")

def track():
    try:
        user = input("Enter your name to use the tool: ")
        number = input(f"Hello {user}, Enter number to validate (e.g., +256700000000): ")

        parsed_number = phonenumbers.parse(number, None)
        status = phonenumbers.is_valid_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "en")
        phone_carrier = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)

        print(f"\nHello {user}, this is the result of the phone number:")
        print(f"Valid: {status}")
        print(f"Region: {region}")
        print(f"Time Zones: {time_zones}")
        print(f"Carrier: {phone_carrier}")

    except Exception as e:
        print("Error occurred:", e)
    else:
        print(f"Successfully validated the phone number {number}")

def main():
    print("Welcome on board")
    choice = input("Do you want to track a number (yes/no): ").strip().lower()
    if choice == "yes":
        track()
    elif choice == "no":
        print("Program stopped")
    else:
        print("Invalid choice")

main()
