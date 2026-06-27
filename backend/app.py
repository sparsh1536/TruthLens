from search import search_web

claim = input("Enter a claim: ")

result = search_web(claim)

print("\n====================")
print("WEB SEARCH EVIDENCE")
print("====================\n")

print(result)