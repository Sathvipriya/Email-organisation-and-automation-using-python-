# Email Organization and Automation Using Python

A Python automation script that cleans up a Gmail inbox. It finds promotional and newsletter emails by subject keywords and moves them into a separate folder.

## Features
- Connects securely to Gmail using IMAP over SSL
- Checks that the target folder exists before running
- Searches email subjects for the keywords: `unsubscribe`, `newsletter`, `sale`, `promotion`
- Moves matching emails to the `promotion` folder and removes them from the inbox
- Avoids duplicates: an email matching more than one keyword is moved only once
- Prints progress and the total number of emails moved
- Handles IMAP and general errors with troubleshooting tips

## Technologies Used
- Python
- imaplib (Python standard library)
- IMAP protocol

## How It Works
1. Connects to Gmail's IMAP server and logs in
2. Checks that the `promotion` folder exists
3. Selects the inbox
4. Searches subjects for each keyword
5. Copies each matching email to the `promotion` folder, then marks the original as deleted
6. Clears the marked originals, logs out, and prints the total moved

## Setup
1. Enable IMAP in Gmail: Settings > See all settings > Forwarding and POP/IMAP
2. Turn on 2-Step Verification in your Google Account
3. Generate an App Password in your Google Account security settings
4. Create a label named `promotion` in Gmail
5. Open `Email_automation.py` and replace `EMAIL` and `PASSWORD` with your email address and app password
6. Run the script:

   python Email_automation.py




OUTPUT :
## Example Output
Connecting to Gmail server...
Login successful!
Inbox selected
Searching for: unsubscribe
   Found 12 emails with 'unsubscribe' in subject
Searching for: newsletter
   Found 8 emails with 'newsletter' in subject
Cleanup complete! 20 promotional emails moved to 'promotion'.
Script execution finished
