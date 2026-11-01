messages = [
    "hello",
    "good morning",
    "how are you"
]

sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print("original messages:")
print(messages)
print("\nsent messages:")
print(sent_messages)