### Test Data:
```
test_user =User{
	  email = 'test_frontend@test.com',
	  name = 'test_frontend',
	  password = generate_password_hash('test_frontend')
	  balance =100
}

test_newTicket = NewTicket{
	  owner_email = "ticket_owner@email.com",
	  quantity = 100,
	  price = 10,
	  expiration_date = '20201203'
}


test_ticket = Ticket{
	    name = "validtickename",
	    quantity = 10,
	    price=10,
	    date = '20201212'
	    require_balance = (10*10)*(1+0.35+0.05) //140
}
```

#### Test Case R3.1: if the user is not logged in, redirect to login page 

Mocking: 
 - Mock backend.get.user to return a test_user instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open / 
 - Open /logout 
 - Open / 
 - Validate that current that contains `#login_reminder` element 
 - Open /logout (clean up)

#### Test Case R3.2: This page shows a header "Hi {}", format (user.name)

Mocking: 
 - Mock backend.get_user to return a test_user instance

Action: 
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login
 - Enter test_user's email into element `#email`
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains '#welcome-header' 
 - Validate test_user's name in the format()
 - Open /logout (clean up)

#### Test Case R3.3: This page shows user balance.

Mocking: 
 - Mock backend.get.user to return a test_user instance

Action:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains test_user's balance 
 - Open /logout (clean up)

#### Test Case R3.4 This page shows a logout link, pointing to /logout

Mocking: 
 - Mock backend.get.user to return a test_user instance

Action:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains element `input[type="logout"]`  
 - Click Click element `input[type="logout"]`
 - Open /logout 
 - Validate URL of the current page contains `base+/logout` 
 - Open /logout (clean up)

#### Test Case R3.5: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired

Mocking: 
 - Mock backend.get.user to return a test_user instance
 - Mock backend.get.ticket to return a test_newTicket instance

Action:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains test_newTicket's quantity 
 - Validate current page contains test_newTicket's owner email
 - Validate current page contains test_newTicket's price
 - Open /logout (clean up)

#### Test Case R3.6: This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date

Mocking: 
 - Mock backend.get.user to return a test_user instance

Actions: 
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email`
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains element `#sell_name`
 - Validate current page contains element `#sell_quantity`
 - Validate current page contains element `#sell_price`
 - Validate current page contains element `#sell_expiration_data`
 - Open /logout (clean up)

#### Test Case R3.7: This page contains a form that a user can buy new tickets. Fields: name, quantity

Mocking: 
 - Mock backend.get.user to return a test_user instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Validate current page contains element `#buy_name`
 - Validate current page contains element `#buy_quantity`
 - Open /logout (clean up)

#### Test Case R3.8: The ticket-selling form can be posted to /sell

Mocking: 
 - Mock backend.get.user to return a test_user instance
 - Mock backend.get.ticket to return a test_newTicket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type='submit']`
 - Open /
 - Enter test_newTicket's name to`#sell_name`
 - Enter test_newTicket's quantity to `#sell_quantity`
 - Enter test_newTicket's price to `#sell_price`
 - Enter test_newTicket's expiration_date to `#sell_expiration_data`
 - Validate element `input[type="selling post"]`
 - Click element `input[type="selling post"]`
 - Open /sell
 - Validate current page contains element `#sell_name`
 - Validate current page contains element `#sell_quantity`
 - Validate current page contains element `#sell_price`
 - Validate current page contains element `#sell_expiration_data`
 - Open /logout (clean up)

#### Test Case R3.9: The ticket-buying form can be posted to /buy

Mocking: 
 - Mock backend.get.user to return a test_user instance
 - Mock backend.get.ticket to return a test_newTicket instance 

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_newTicket's name to `#buy_name`
 - Enter test_newTicket's quantity to `#buy_quantity`
 - Validate element['type=buying post']
 - Click element `input[type="buying post"]`
 - Open /buy
 - Validate current page contains element `#buy_name`
 - Validate current page contains element `#buy_quantity`
 - Open /logout (clean up) 

#### Test Case R3.10: The ticket-update form can be posted to /update

Mocking: 
 - Mock backend.get.user to return a test_user instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `intput[type="submit"]`
 - Open /
 - Enter test_newTicket's name to`#sell_name`
 - Enter test_newTicket's quantity to `#sell_quantity`
 - Enter test_newTicket's price to `#sell_price`
 - Enter test_newTicket's expiration_date to `#sell_expiration_data`
 - Validate element `input[type="selling update post"]`
 - Click element `input[type="selling update post"]`
 - Open /update 
 - Validate current page contains element `#sell_update_name`
 - Validate current page contains element `#sell_update_quantity`
 - Validate current page contains element `#sell_update_price`
 - Validate current page contains element `#sell_update_ expiration_data`
 - Open /
 - Enter test_newTicket's name to `#buy_name`
 - Enter test_newTicket's quantity to `#buy_quantity`
 - Validate element `input[type="buying update post"]`
 - Click element `input[type="buying update post"]`
 - Open /update
 - Validate current page contains element `#buy_update_name`
 - Validate current page contains element `#buy_update_quantity`
 - Open /logout (clean up)


#### Test Case R6.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character - positive  

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input['type=submit']`
 - Open /
 - Enter  test_ticket's name into element `#buy_name` 
 - Enter  test_ticket's quantity in to the element `#buy_quantity`
 - Click element #buy_submit
 - Validate the `#buy_message` element shows 'successful'
 - Open /logout (clean up)

#### Test Case R6.1: The name of the ticket has  be alphanumeric-only, and space allowed only if it is not the first or the last character - negative

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter 'this_is_invalid_name()' into element `#buy_name` 
 - Enter  test_ticket's quantity in to the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'the ticket name is not valid'
 - Open /
 - Enter ' spaceAtFirst' into element `#buy_name`
 - Enter  test_ticket's quantity in to the element #buy_quantity
 - Validate the `#buy_message` element shows 'the ticket name is not valid'
 - Open /
 - Enter 'spaceAtLast ' into element `#buy_name`
 - Enter  test_ticket's quantity in to the element #buy_quantity
 - Validate the `#buy_message` element shows 'the ticket name is not valid'
 - Open /logout (clean up)


#### Test Case R6.2: The name of the ticket is no longer than 60 characters -positive 

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element['type=submit']
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter test_user's quantity in to the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'successful'
 - Open /logout (clean up)

#### Test Case R6.2: The name of the ticket is longer than 60 characters -negative 

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter the name of the ticket that has 61 characters into element `#buy_name`
 - Enter test_ticket's quantity in to the element `#buy_quantity`
 - Validate the `#buy_message` element shows 'the ticket name is not valid'
 - Open /logout (clean up)

#### Test Case R6.3: The quantity of the tickets has to be more than 0, and less than or equal to 100 -positve 

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element['type=submit']
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter test_user's quantity in to the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'successful'
 - Open /logout (clean up)

#### Test Case R6.3: The quantity of the tickets has to be more than 0, and less than or equal to 100 -negative

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter '-1' into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'this is invalid ticket quantity'
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter '101' into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'this is invalid ticket quantity'
 - Open /logout (clean up)


#### Test Case R6.4: The ticket name exists in the database and the quantity is more than the quantity requested to buy - positive 

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter test_user's quantity into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'successful'
 - Open /logout (clean up)

#### Test Case R6.4: The ticket name exists in the database and the quantity is more than the quantity requested to buy - negative

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_user_name_not_exists into element `#buy_name` 
 - Enter test_user_quantity_less_than_requested into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element shows 'the ticket quantity cannot be satisfied'
 - Open /logout


#### Test Case R6.5: The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) -positve

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_user's name into element `#buy_name` 
 - Enter test_user's quantity into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the test_ticket's require_balance is more than test_user's balance
 - Validate the `#buy_message` element shows 'successful'
 - Open /logout (clean up)

#### Test Case R6.5: The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) -negative

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter test_user's name into element #`buy_name` 
 - Enter test_user's quantity into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the test_ticket's require_balance is less than 139
 - Validate the `#buy_message` element show 'you have no enough money to purchase the ticket"
 - Open /logout

#### Test Case R6.6: For any errors, redirect back to / and show an error message

Mocking: 
 - Mock backend.get.user to return a test_user instance

Actions:
 - Open /logout (to invalidate any logged-in session may exist)
 - Open /login 
 - Enter test_user's email  into element `#email` 
 - Enter test_user's password into element `#password`
 - Click element `input[type="submit"]`
 - Open /
 - Enter invalid name into element `#buy_name` 
 - Enter test_user's quantity into the element `#buy_quantity`
 - Click element `#buy_submit`
 - Validate the `#buy_message` element show error message 
 - Open /
 - Enter test_user's name into element `#buy_name`
 - Enter invalid quantity into the element `#buy_quantity` 
 - Click element `#buy_submit`
 - Validate the `#buy_message` element show error message 
 - Open /
 - Enter invalid name into element `#buy_name`
 - Enter invalid quantity into the element `#buy_quantity` 
 - Click element `#buy_submit`
 - Validate the `#buy_message` element show error message 
 - Open /logout



