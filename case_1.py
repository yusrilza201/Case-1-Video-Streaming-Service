from tabulate import tabulate  # Import tabulate module for creating tables
import random
import string

class User:
    """
    User class represents a video streaming service user.

    Attributes:
    - username (str): User's name
    - duration_plan (int): Subscription duration in months
    - current_plan (str): Current subscription plan
    - data (dict): Existing user data
    - plan_list (dict): List of subscription plans with their details

    Methods:
    - cek_benefit(): Displays a comparison of benefits for all plans
    - cek_plan(username): Displays plan details for a specific user
    - upgrade_plan(username, current_plan, new_plan): Calculates the price for a plan upgrade
    """

    def __init__(self, username, duration_plan, current_plan):
        """
        Initialize a User object.

        Parameters:
        - username (str): User's name
        - duration_plan (int): Subscription duration in months
        - current_plan (str): Current subscription plan
        """
        self.username = username  # Store the username
        self.duration_plan = duration_plan  # Store the subscription duration
        self.current_plan = current_plan  # Store the current subscription plan
        
        self.data = {  # Store existing user data
            "Shandy": ["Basic Plan", 12, "shandy-2134"],
            "Cahya": ["Standard Plan", 24, "cahya-abcd"],
            "Ana": ["Premium Plan", 5, "ana-2f9g"],
            "Bagus": ["Basic Plan", 11, "bagus-9f92"]
        }

        self.plan_list = {  # Store the list of subscription plans with their details
            'basic plan': {
                'Can Stream': True,
                'Can Download': True,
                'SD Quality': True,
                'HD Quality': False,
                'UHD Quality': False,
                'Number of Devices': 1,
                'Content Type': '3rd Party Movie only',
                'Price': 120_000
            },
            'standard plan': {
                'Can Stream': True,
                'Can Download': True,
                'SD Quality': True,
                'HD Quality': True,
                'UHD Quality': False,
                'Number of Devices': 2,
                'Content Type': 'Basic Plan Content + Sport',
                'Price': 160_000
            },
            'premium plan': {
                'Can Stream': True,
                'Can Download': True,
                'SD Quality': True,
                'HD Quality': True,
                'UHD Quality': True,
                'Number of Devices': 4,
                'Content Type': 'Basic Plan + Standard Plan + PacFlix Original Series',
                'Price': 200_000
            },
        }

    def cek_benefit(self):
        """
        Display a comparison of benefits for all plans in a table format.

        Returns:
        str: Table of plan benefit comparisons
        """
        headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']  # Define table headers
        table = []  # Initialize empty table

        services = list(self.plan_list['basic plan'].keys())  # Get list of services

        for service in services:  # Iterate through each service
            row = [  # Create a row for each service
                self.plan_list['basic plan'][service],
                self.plan_list['standard plan'][service],
                self.plan_list['premium plan'][service],
                service
            ]
            
            table.append(row)  # Add row to the table
        
        all_benefit = tabulate(table, headers, tablefmt='github')  # Create table with GitHub format
        
        print('PacFlix Plan List\n')  # Print plan list title
        return all_benefit  # Return the benefits table
    
    def cek_plan(self, username):
        """
        Display plan details for a specific user.

        Parameters:
        - username (str): User's name

        Returns:
        None
        """
        plan_name = self.data[username][0].title()  # Get user's plan name
        duration = self.data[username][1]  # Get user's subscription duration
        
        plan_details = self.plan_list[plan_name.lower()]  # Get plan details

        headers = [plan_name, 'Services']  # Define table headers
        table = [[value, key] for key, value in plan_details.items()]  # Create plan details table
        
        plan_table = tabulate(table, headers, tablefmt='github')  # Create table with GitHub format
        
        print(f"{plan_name}\n{duration}\n")  # Print plan name and duration
        print(f"{plan_name} PacFlix Benefit List\n")  # Print benefit list title
        print(plan_table)  # Print benefits table
            
    def upgrade_plan(self, username, current_plan, new_plan):
        """
        Calculate the price for upgrading a plan, considering applicable discounts.
        Users can only upgrade, not downgrade.

        Parameters:
        - username (str): User's name
        - current_plan (str): Current subscription plan
        - new_plan (str): New subscription plan

        Returns:
        str: Price to be paid for the upgrade, or an error message if downgrading
        """
        current_plan = current_plan.lower()  # Convert current plan to lowercase
        new_plan = new_plan.lower()  # Convert new plan to lowercase
        
        plan_order = ['basic plan', 'standard plan', 'premium plan']
        if plan_order.index(current_plan) >= plan_order.index(new_plan):
            return "Error: Anda hanya dapat melakukan upgrade paket, bukan downgrade."
        
        discount = 0.05 if self.data[username][1] > 12 else 0  # Determine discount based on subscription duration
            
        plan_price = self.plan_list[new_plan]['Price']  # Get the price of the new plan
        price_to_pay = plan_price - (plan_price * discount)  # Calculate the price to pay after discount
        return f"Rp. {price_to_pay}"  # Return the price to pay

class NewUser(User):
    """
    NewUser class represents a new user of the video streaming service.
    Inherits from the User class.

    Methods:
    - cek_benefit(): Displays a comparison of benefits for all plans
    - pick_plan(new_plan, referral_code): Calculates the price of a plan for a new user
    """

    def __init__(self, username):
        """
        Initialize a NewUser object.

        Parameters:
        - username (str): New user's name
        """
        super().__init__(username, None, None)  # Call parent class constructor
        
    def cek_benefit(self):
        """
        Display a comparison of benefits for all plans.

        Returns:
        str: Table of plan benefit comparisons
        """
        return super().cek_benefit()  # Call parent class cek_benefit method
    
    def pick_plan(self, new_plan, referral_code=None):
        """
        Calculate the price of a plan for a new user, considering any referral code.

        Parameters:
        - new_plan (str): Chosen subscription plan
        - referral_code (str, optional): Referral code

        Returns:
        str: Price to be paid for the chosen plan

        Raises:
        TypeError: If the referral code is invalid
        """
        new_plan = new_plan.lower()  # Convert new plan to lowercase
        
        discount = 0  # Initialize discount
        
        if referral_code:  # If referral code is provided
            if referral_code not in [v[2] for v in self.data.values()]:  # Check if referral code exists
                raise TypeError("Referral Code doesn't exist")  # Raise exception if code is invalid
            else:
                print("Referral code exists")  # Print message if code is valid
                discount = 0.04  # Set referral discount
        
        plan_price = self.plan_list[new_plan]['Price']  # Get plan price
        price_to_pay = plan_price - (plan_price * discount)  # Calculate price to pay after discount
        
        
        # Generate random referral code
        ref_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        # Add new user data
        self.data[self.username] = [new_plan, 1, f"{self.username.lower()}-{ref_code}"]
        
        return f"Rp. {price_to_pay}"  # Return price to pay

if __name__ == "__main__":
    # Creating a new user instance
    pengguna_baru = NewUser("Yusril")
    
    # Displaying comparison of benefits for all packages
    print("Perbandingan Manfaat Paket:")
    print(pengguna_baru.cek_benefit())
    
    # Choosing a package with referral code
    try:
        harga = pengguna_baru.pick_plan("Premium Plan", "cahya-abcd")
        print(f"Harga paket Premium dengan kode referral: {harga}")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Choosing a package without referral code
    harga = pengguna_baru.pick_plan("Standard Plan")
    print(f"Harga paket Standard tanpa kode referral: {harga}")
    
    # Creating an instance of an existing user
    pengguna_lama = User("Cahya", 24, "Standard Plan")
    
    # Checking another user's package
    print("Paket Cahya:", pengguna_lama.cek_plan("Cahya"))
    
    # Attempting to upgrade the package
    hasil_upgrade = pengguna_lama.upgrade_plan("Cahya", "Standard Plan", "Premium Plan")
    print("Hasil upgrade:", hasil_upgrade)
