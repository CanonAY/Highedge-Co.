
#### Tested Method: backend.login_user 
#####Approach: Condition Coverage

| Conditon                                                                                                    | Input                                               | Test | Output                       | 
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|------|------------------------------|
| (not user): True; (not check_password_hash(user.password, password)): True; (not email == user.email): True | email = 'boxwhite';          password = 'white_BOX' | T1   | None            - [expected] |
| (not user): False;(not check_password_hash(user.password, password)): True; (not email == user.email): True | email = 'whitebox';          password = 'white_BOX' | T2   | None            - [expected] |
| (not user): True; (not check_password_hash(user.password, password)): False;(not email == user.email): True | email = 'boxwhite';          password = 'WHITE_box' | T3   | None            - [expected] |
| (not user): True; (not check_password_hash(user.password, password)): True; (not email == user.email): False| email = 'boxwhite@test.com'; password = 'white_BOX' | T4   | None            - [expected] |
| (not user): False;(not check_password_hash(user.password, password)): False;(not email == user.email): True | email = 'whitebox';          password = 'WHITE_box' | T5   | None            - [expected] |
| (not user): True; (not check_password_hash(user.password, password)): False;(not email == user.email): False| email = 'boxwhite@test.com'; password = 'WHITE_box' | T6   | None            - [expected] |
| (not user): False;(not check_password_hash(user.password, password)): True; (not email == user.email): False| email = 'whitebox@test.com'; password = 'white_BOX' | T7   | None            - [expected] |
| (not user): False;(not check_password_hash(user.password, password)): False;(not email == user.email): False| email = 'whitebox@test.com'; password = 'WHITE_box' | T8   | get_user(email) - [expected] |