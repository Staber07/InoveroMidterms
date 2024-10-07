from faker import Faker

def generate_fake_profiles(n=10):
    faker = Faker()
    profiles = []
    
    for _ in range(n):
        profile = {
            "full_name": faker.name(),
            "email": faker.email(),
            "job_title": faker.job(),
            "company": faker.company()
        }
        profiles.append(profile)
    
    return profiles

def main():
    profiles = generate_fake_profiles()
    for profile in profiles:
        print(f"Name: {profile['full_name']}, Email: {profile['email']}, Job Title: {profile['job_title']}, Company: {profile['company']}")

if __name__ == "__main__":
    main()
