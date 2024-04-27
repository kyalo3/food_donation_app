# MongoDB Database Schema

This document describes the schema of our MongoDB database. These collections will support the main functionalities of our food donation platform, including user management, donation management, request management, communication management, data analytics, and system settings.

## Users Collection

Stores personal information and history of users.

**Fields:**

- `_id`: Unique identifier for the user
- `username`: Username of the user
- `password`: Password of the user
- `email`: Email of the user
- `role`: Role of the user, possible values include "donor", "recipient", and "administrator"
- `profile`: Contains additional information such as contact details, preferences
- `history`: List of past donations or requests made by the user

## Donations Collection

Stores information about donations.

**Fields:**

- `_id`: Unique identifier for the donation
- `donorId`: ID of the donor
- `itemDescription`: Description of the donated item
- `quantity`: Quantity of the donated item
- `expiryDate`: Expiry date of the donated item
- `pickupAvailability`: Availability for pickup of the donated item
- `location`: Location of the donation
- `status`: Status of the donation, possible values include "pending", "approved", and "rejected"

## Requests Collection

Stores information about donation requests.

**Fields:**

- `_id`: Unique identifier for the request
- `recipientId`: ID of the recipient
- `donationId`: ID of the donation
- `requestMessage`: Message of the request
- `status`: Status of the request, possible values include "pending", "approved", and "rejected"

## Communications Collection

Stores communication messages between users or administrators.

**Fields:**

- `_id`: Unique identifier for the message
- `senderId`: ID of the sender
- `recipientId`: ID of the recipient
- `message`: Content of the message
- `timestamp`: Time of sending the message

## Analytics Collection

Stores analytics and reporting data.

**Fields:**

- `_id`: Unique identifier for the data
- `date`: Date of the data
- `donationCount`: Number of donations
- `userCount`: Number of users
- `participationRate`: Rate of participation

## Settings Collection

Stores system settings and configurations.

**Fields:**

- `_id`: Unique identifier for the setting
- `settingName`: Name of the setting
- `settingValue`: Value of the setting