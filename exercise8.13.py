def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    "priskila",
    "arum",
    university="uns",
    major="industrial engineering"
    hobby="reading"
)

print(my_profile)