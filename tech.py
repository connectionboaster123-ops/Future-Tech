import phonenumbers                                                                                   from phonenumbers import geocoder, carrier, timezone

print("Phone number Validation")

def track():
    try:
        user = input("Enter your name to use the tool: ")
        number = input(f"Hello {user}, Enter number to validate (e.g., +2567000000): ")

        parsed_number = phonenumbers.parse(number, None)
        status = phonenumbers.is_valid_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "en")                                         time_zones = timezone.time_zones_for_number(parsed_number)
        phone_carrier = carrier.name_for_number(parsed_number, "en")

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
      choice = str(input("Do u want to track a number (yes /no )..."))
      if choice in ["Yes","YES","yes"]:
          track()
      elif choice in ["No","no","NO"]:
          print("program stopped")
      else:
          print("Invalid choice")
main()
