from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI (access_token ="MTNlYjg1MDgtNTUyOS00NTlhLWE3M2MtM2Q1Njc0NTFiYmQwOGJjYzJmN2MtOTJm_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b")


room_name = input("Enter the room name:")
welcome_message = input("Enter the welcome message: ")


room = api.rooms.create(room_name)
print(f"Room '{room.title}' created with ID: {room.id}")


api message.create(room.id, text=welcome_message)
print("Welcome message sent!")