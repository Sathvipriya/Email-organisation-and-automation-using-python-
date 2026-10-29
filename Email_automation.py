# Email Organization and Automation Using Python

import imaplib

# --- Configuration ---
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # Use a Gmail App Password
IMAP_SERVER = "imap.gmail.com"
FOLDER_TARGET = "promotion"  # Make sure this folder/label exists in Gmail

try:
    # --- Connect to mailbox ---
    print("Connecting to Gmail server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    print("Login successful!")

    # Check if target folder exists
    status, folders = mail.list()
    if FOLDER_TARGET not in str(folders):
        print(f"Error: Folder '{FOLDER_TARGET}' doesn't exist in your Gmail!")
        print("Please create it in Gmail first.")
        mail.logout()
        exit()

    mail.select("inbox")
    print("Inbox selected")

    # --- Search for newsletters/promotions ---
    keywords = ["unsubscribe", "newsletter", "sale", "promotion"]
    moved_count = 0
    processed = set()

    for keyword in keywords:
        print(f"Searching for: {keyword}")
        status, messages = mail.search(None, f'(SUBJECT "{keyword}")')

        if status == "OK" and messages[0]:
            email_ids = messages[0].split()
            print(f"   Found {len(email_ids)} emails with '{keyword}' in subject")

            for email_id in email_ids:
                if email_id in processed:
                    continue
                # Move email: copy to target folder, then mark original deleted
                mail.copy(email_id, FOLDER_TARGET)
                mail.store(email_id, "+FLAGS", "\\Deleted")
                processed.add(email_id)
                moved_count += 1
        else:
            print(f"   No emails found with '{keyword}' in subject")

    # --- Cleanup ---
    mail.expunge()
    mail.logout()
    print(f"Cleanup complete! {moved_count} promotional emails moved to '{FOLDER_TARGET}'.")

except imaplib.IMAP4.error as e:
    print(f"IMAP Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure you generated an APP PASSWORD (not your regular password)")
    print("2. Enable IMAP in Gmail Settings > See all settings > Forwarding and POP/IMAP")
    print("3. Enable 2-Step Verification in Google Account security settings")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Script execution finished")
