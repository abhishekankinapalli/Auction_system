import unittest
from Clients import*
from Auctioneer import*

# Registration testcases
class TestClientRegisterEmail(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        # Clean up the clients.json file after each test
        with open('clients.json', 'w') as file:
            initial_data = {'clients': []}
            json.dump(initial_data, file, indent=4)


    def test_register_successful(self):
        username = 'dayakar'
        email = 'dayakar@example.com'
        password = 'dayakar#123'

        response1 = self.client.register(username, email, password)

        self.assertEqual(response1['message'], 'Registration successful.')


    def test_register_existing_email(self):
        username='dayakar'
        email = 'dayakar@example.com'
        password='dayakar#123'
        # First registration with the same email
        response2_1 = self.client.register(username, email, password)

        response2_2 = self.client.register(username, email, password)

        self.assertEqual(response2_1['message'], 'Registration successful.')
        self.assertEqual(response2_2['message'], 'Email already registered. Please use a different email.')

    def test_register_Invalid_email_format(self):
        username = 'dayakar'
        # Email should not end with "@gmail.com"
        email = 'dayakar@gmail'
        password = 'dayakar#123'

        response3 = self.client.register(username, email, password)
        self.assertEqual(response3['message'], 'Invalid email format')


# Login testcases
class TestLoginValidation(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        username = 'Dayakar'
        email = 'dayakar@gmail.com'
        password = 'dayakar#123'
        self.client.register(username, email, password)


    def test_client_Invalid_eamil(self):
        # Not Registered email
        email = 'example@gmail.com'
        password = 'dayakar#123'

        response1 = self.client.validate_login(email, password)
        self.assertEqual(response1['message'], 'Email not found.')


    def test_client_Invalid_password(self):
        email='dayakar@gmail.com'
        # worng password
        password='jndjknsd'

        response2 = self.client.validate_login(email, password)
        self.assertEqual(response2['message'], 'Invalid password.')

    def test_client_valid_email_password(self):
        email = 'dayakar@gmail.com'
        password = 'dayakar#123'
        response3=self.client.validate_login(email, password)
        self.assertEqual(response3['message'],'Login successful.')



#Submit Bid testcases
class TestClientsubmitbid(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.auctioneer = Auctioneer()
        self.client = Client()
        username = 'Dayakar'
        email = 'dayakar@gmail.com'
        password = 'dayakar#123'
        self.client.register(username, email, password)

    def test_email(self):
        test_email='testexample@gmail.com'
        test_port=8001

        response1=self.auctioneer.submit_bid(test_email, slots=50, bid_price=2000, port=test_port)
        self.assertEqual(response1, {'message': 'Email not found.'})

    def test_port_number(self):
        test_email = 'dayakar@gmail.com'
        test_port = 1421

        response2 = self.auctioneer.submit_bid(test_email, slots=50, bid_price=500, port=test_port)
        self.assertEqual(response2, {'message': 'Invalid port number.'})


    def test_slots(self):
        test_email = 'dayakar@gmail.com'
        test_port = 8001

        response3 = self.auctioneer.submit_bid(test_email, slots=110, bid_price=8000, port=test_port)
        self.assertEqual(response3, {'message': 'Dear client, you can bid slots between 1 to 100.'})


    def test_bidprice(self):
        test_email = 'dayakar@gmail.com'
        test_port = 8001

        response4 = self.auctioneer.submit_bid(test_email, slots=50, bid_price=10, port=test_port)
        self.assertEqual(response4, {'message': 'Please increase the bid price you are lower than the base price.'})

    def test_bidsubmit(self):
        test_email='dayakar@gmail.com'
        test_port=8001

        response5 = self.auctioneer.submit_bid(test_email, slots=50, bid_price=5000, port=test_port)
        self.assertEqual(response5, {'message': 'Bid submitted successfully'})


if __name__ == '__main__':
    unittest.main()