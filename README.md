

# Easy Donate API Requirements

### Existing API
To check the installation, open the Installation folder.

## Donations/Request => GET/POST API.

Category - String <br>
isDonation - boolean<br>
Description - String<br>
Donor Address - String<br>
Donor Name - String<br>
Location - String<br>
Posted Time - DateTime<br>
Quantity - String<br>
Time - DateTime<br>
Title - String<br>
User - String<br>
ID - String<br>
Image - String <br><br>

Note: 
*ID is a unique random String assigned by the Server in POST.<br>
Image parameter will be sent only for Donation.<br>
GET API should return the List of All Donations/Requests.*<br>

## Categories => GET/POST API

Name - String<br>
Icon - String<br>

## User => GET/POST API<br>

Address - String<br>
Email - String<br>
Location - String<br>
Mobile - String<br>
Name - String<br>
UID - String<br>

## FAQ => GET/POST API

Question - String<br>
Answer - String<br>
