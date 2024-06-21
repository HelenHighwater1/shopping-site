"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name,last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

#Add a __repr()__ method like you have for the Melon class so that when you print a customer, you can see some useful information about them. This is very handy for debugging.
    def __repr__(self):
        """Convenience method to show information about user in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )

#Add a function to read the customers.txt and populate a dictionary with the format:
# {email: Customer(...),
#  email: Customer(...)}
def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: customer object}
    """
    customers = {}

    with open(filepath) as file:
        for line in file: 
            [
                first_name, 
                last_name, 
                email, 
                password
            ] = line.strip().split('|')

            customers[email] = Customer(
                first_name,
                last_name,
                email,
                password
            )

    return customers

customer_list = read_customers_from_file("customers.txt")

def get_customer_by_email(email):
    """Return a customer, given their email."""

    return customer_list.get(email)


