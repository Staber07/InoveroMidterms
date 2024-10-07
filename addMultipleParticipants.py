from webexteamssdk import WebexTeamsAPI

def add_participants_to_room(api, room_id, participants):
    for email in participants:
        try:
            api.memberships.create(roomId=room_id, personEmail=email)
            print(f"Added {email} to the room.")
        except Exception as e:
            print(f"Failed to add {email}: {e}")

def main():
    # Assuming you've already created the room and have its ID
    access_token = "MTNlYjg1MDgtNTUyOS00NTlhLWE3M2MtM2Q1Njc0NTFiYmQwOGJjYzJmN2MtOTJm_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"
    api = WebexTeamsAPI(access_token=access_token)

    room_id = "YOUR_ROOM_ID"  # Replace with your room ID
    participants = [
        "allandavemarcoso@baliuagu.edu.ph",
        "dennissegailfrancisco@baliuagu.edu.ph",
        "karlorobertwagan@baliuagu.edu.ph"
    ]

    add_participants_to_room(api, room_id, participants)

if __name__ == "__main__":
    main()