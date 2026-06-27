from pipeline import run_pipeline

print("=" * 70)
print("🔍 TruthLens AI")
print("=" * 70)

url = input("\n📺 Paste YouTube URL: ")

result = run_pipeline(url)

print("\n")
print("=" * 70)
print("ANALYSIS REPORT")
print("=" * 70)

for i, item in enumerate(result["results"], start=1):

    print("\n" + "=" * 70)
    print(f"CLAIM {i}")
    print("=" * 70)

    print("\n📝 Claim:")
    print(item["sentence"])

    print("\n🏷 Category:")
    print(item["category"])

    if item["verification"]:

        lines = item["verification"].split("\n")

        verdict = ""
        confidence = ""
        explanation = ""

        for line in lines:
            if line.startswith("Verdict"):
                verdict = line.replace("Verdict:", "").strip()

            elif line.startswith("Confidence"):
                confidence = line.replace("Confidence:", "").strip()

            elif line.startswith("Explanation"):
                explanation = line.replace("Explanation:", "").strip()

        print("\n✅ Verdict:")
        print(verdict)

        print("\n📊 Confidence:")
        print(confidence + "%")

        print("\n💡 Explanation:")
        print(explanation)

    if item["evidence"]:

        best_result = item["evidence"][0]

        print("\n📚 Source:")
        print(best_result["title"])

        print("\n📖 Evidence:")
        print(best_result["content"][:600] + "...")

        print("\n🔗 URL:")
        print(best_result["url"])

print("\n")
print("=" * 70)
print("✅ Analysis Complete")
print("=" * 70)