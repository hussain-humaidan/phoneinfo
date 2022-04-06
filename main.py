import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from termcolor import colored
import os


def main():
    def logo():
        print(colored(
            """
    @@@@@@@@@@@@@@@@@@@@@@@@@@**********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@*****************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@**************************************@@@@@@@@@@@@
    @@@@@@**************@@@@@@@@@@@@@@@@@@@@@@@**************@@@@@
    @@@***    *****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*****    ***@@
    @@***      **@@@@@@@@@@*****************@@@@@@@@@@**      **@@
    @@@****  ***@@@@@@***************************@@@@@@***  ***@@@
    @@@@@@@@@@@@*************@@@@@@@@@@@@@*************@@@@@@@@@@@
    @@@@@@@@@@***    ***@@@@@@@@@@@@@@@@@@@@@@@***    **@@@@@@@@@@
    @@@@@@@@@@@***  ***@@@@@@@***********@@@@@@@**   ***@@@@@@@@@@
    @@@@@@@@@@@@@@*@@@@@***********************@@@@*@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@**    *****@@@@@*****    **@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@***  ***@@@@@@@@@@@***  **@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@********@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    **@@@**@@@@@@@@@@@@@@@@@@**@@@@@@*@@@@@*@@@@@@@@@@@@@@@@@*@@@@
    **@@@**@*@@@*@*****@@******@@*****@@@@****@*****@@*****@@*****
    **@@@**@@*@*@@*@@@**@*@@@**@**@@@*@@@@@**@@*@***@@*@@@@@@*@@@*
    **@@@**@@@**@@*@***@@*@@@**@****@*@@@@@***@*****@@*****@@*@@@*
    @@@@@@@@**@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    Created by Hussain Humaidan
    Uploaded by Hyprid tech
    We are not responsible of any illegal action
    """, 'blue'))

    logo()

    numbercon = input("Enter the country code: ")
    number = input("Enter the number: ")

    whole_num = numbercon + number
    pars_number = phonenumbers.parse(whole_num)

    valid_number = phonenumbers.is_valid_number(pars_number)

    if valid_number is True:
        print(f"The number {whole_num} is vaild")

        print(timezone.time_zones_for_number(pars_number))

        print(carrier.name_for_valid_number(pars_number, "en"))

        print(geocoder.country_name_for_number(pars_number, "en"))

        time.sleep(7)
        
        os.system("clear")

        return main()

    elif valid_number is False:
        quit(f"The number {whole_num} is not valid")


try:
    main()
except Exception:
    quit("Please enter the details correctly")
