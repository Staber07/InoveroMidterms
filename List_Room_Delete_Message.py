from webexteamssdk import WebexTeamsAPI

def list_messages(api, room_id):
    messages = api.messages.list(roomId=room_id)
    message_list = {message.id: message.text for message in messages}
    return message_list

def delete_message(api, message_id):
    try:
        api.messages.delete(message_id)
        print(f"Message {message_id} deleted successfully.")
    except Exception as e:
        print(f"Failed to delete message {message_id}: {e}")

def main():
    access_token = "MTNlYjg1MDgtNTUyOS00NTlhLWE3M2MtM2Q1Njc0NTFiYmQwOGJjYzJmN2MtOTJm_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"
    api = WebexTeamsAPI(access_token=access_token)

    room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vODdiZmYxNjAtODQ3OC0xMWVmLTlkMzMtNGIxNWFiNmUwZjQ4"  # Replace with your room ID

    # List messages
    messages = list_messages(api, room_id)
    for msg_id, msg_text in messages.items():
        print(f"ID: {msg_id} | Message: {msg_text}")

    # Prompt user to delete a message
    message_id_to_delete = input("Enter the message ID to delete: ")
    delete_message(api, message_id_to_delete)

if __name__ == "__main__":
    main()