

# Easy Donate API Requirements

## Donations/Request => GET/POST API.

Category - String
isDonation - boolean
Description - String
Donor Address - String
Donor Name - String
Location - String
Posted Time - DateTime
Quantity - String
Time - DateTime
Title - String
User - String
ID - String
Image - String 

Note: 
*ID is a unique random String assigned by the Server in POST.
Image parameter will be sent only for Donation.
GET API should return the List of All Donations/Requests.*

## Categories => GET/POST API

Name - String
Icon - String
User => GET/POST API
Address - String
Email - String
Location - String
Mobile - String
Name - String
UID - String

## FAQ => GET/POST API

Question - String
Answer - String
